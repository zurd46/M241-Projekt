import os
import requests
from flask import Blueprint, render_template, current_app, request, jsonify
from flask_mail import Message
from . import mail  # Greift auf das Mail-Objekt aus __init__.py zu

main = Blueprint('main', __name__)

@main.route('/')
def index():
    image_folder = os.path.join(current_app.static_folder, 'images')
    valid_exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
    try:
        hero_images = [
            fname for fname in os.listdir(image_folder)
            if fname.lower().endswith(valid_exts)
        ]
    except FileNotFoundError:
        hero_images = []
    hero_images.sort()
    return render_template('index.html', hero_images=hero_images)

@main.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json() or {}
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    message_body = data.get('message', '').strip()
    recaptcha_token = data.get('recaptcha_token', '').strip()

    # Validierung: Alle Felder müssen ausgefüllt sein
    if not name or not email or not message_body or not recaptcha_token:
        return jsonify(success=False, error="Alle Felder inkl. reCAPTCHA sind verpflichtend."), 400

    # --- reCAPTCHA-Prüfung ---
    recaptcha_secret = os.environ.get("RECAPTCHA_SECRET_KEY", "")
    if not recaptcha_secret:
        return jsonify(success=False, error="Server-Fehler: Kein reCAPTCHA Secret konfiguriert."), 500

    try:
        recaptcha_resp = requests.post(
            "https://www.google.com/recaptcha/api/siteverify",
            data={
                'secret': recaptcha_secret,
                'response': recaptcha_token
            },
            timeout=3
        )
        recaptcha_result = recaptcha_resp.json()
        if not recaptcha_result.get("success"):
            return jsonify(success=False, error="reCAPTCHA nicht bestanden."), 400
    except Exception as e:
        return jsonify(success=False, error="reCAPTCHA-Überprüfung fehlgeschlagen."), 500

    # --- Mailversand ---
    try:
        subject = f"Kontaktanfrage von {name}"
        msg = Message(
            subject=subject,
            recipients=['info@it-praktika.ch'],
            body=(
                f"Neue Kontaktanfrage über das Formular:\n\n"
                f"Name: {name}\n"
                f"E-Mail: {email}\n\n"
                f"Nachricht:\n{message_body}\n"
            )
        )
        mail.send(msg)
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=f"E-Mail-Versand fehlgeschlagen: {e}"), 500

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/trainees')
def trainees():
    return render_template('trainees.html')

@main.route('/school')
def school():
    return render_template('school.html')

@main.route('/contact')
def contact():
    recaptcha_site_key = os.environ.get("RECAPTCHA_SITE_KEY", "")
    return render_template('contact.html', recaptcha_site_key=recaptcha_site_key)

@main.route('/impressum')
def impressum():
    return render_template('impressum.html')
