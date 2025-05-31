import os
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

    if not name or not email or not message_body:
        return jsonify(success=False, error="Alle Felder (Name, E-Mail, Nachricht) sind verpflichtend."), 400

    try:
        subject = f"Kontaktanfrage von {name}"
        msg = Message(
            subject=subject,
            recipients=['info@it-praktika.ch']
        )
        msg.body = f"""
Neue Kontaktanfrage über das Formular:

Name: {name}
E-Mail: {email}

Nachricht:
{message_body}
        """
        mail.send(msg)
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e)), 500

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
    return render_template('contact.html')

@main.route('/impressum')
def impressum():
    return render_template('impressum.html')
