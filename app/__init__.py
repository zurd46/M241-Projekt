import os
from flask import Flask
from flask_mail import Mail
from datetime import datetime
from dotenv import load_dotenv

# 1) Mail-Objekt erstellen (noch vor dem Import von routes)
mail = Mail()

def create_app():
    # 2) Lade alle Variablen aus der .env-Datei (falls vorhanden)
    load_dotenv()

    app = Flask(__name__)

    # 3) Konfiguriere Flask-Mail rein aus Umgebungsvariablen
    #    Fallbacks dienen nur als Default, falls die entsprechende ENV nicht gesetzt ist.
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.example.com')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
    # MAIL_USE_TLS: True/False. von .env als String, also in bool konvertieren
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True').lower() in ('true', '1', 'yes')

    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

    # Default-Sender aus zwei ENV-Variablen zusammensetzen
    sender_name = os.getenv('MAIL_DEFAULT_SENDER_NAME', 'IT-Praktika Kontakt')
    sender_addr = os.getenv('MAIL_DEFAULT_SENDER_ADDR', 'info@it-praktika.ch')
    app.config['MAIL_DEFAULT_SENDER'] = (sender_name, sender_addr)

    # 4) Initialisiere Flask-Mail
    mail.init_app(app)

    # 5) Importiere und registriere das Blueprint erst jetzt
    from .routes import main
    app.register_blueprint(main)

    # 6) Kontext‐Processor für {{ now.year }}
    @app.context_processor
    def inject_now():
        return { 'now': datetime.now() }

    return app
