import os
from flask import Flask
from flask_mail import Mail
from datetime import datetime
from dotenv import load_dotenv

# 1) Mail-Objekt global (damit es überall importiert werden kann)
mail = Mail()

def create_app():
    # 2) .env-Datei laden (sichert, dass alle Umgebungsvariablen im Code verfügbar sind)
    load_dotenv()

    app = Flask(__name__)

    # 3) SMTP- und E-Mail-Konfiguration per ENV
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.example.com')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True').lower() in ('true', '1', 'yes')
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

    # Default-Sender: Name und Adresse aus ENV (Fallbacks als Default)
    sender_name = os.getenv('MAIL_DEFAULT_SENDER_NAME', 'IT-Praktika Kontakt')
    sender_addr = os.getenv('MAIL_DEFAULT_SENDER_ADDR', 'kontakt@it-praktika.ch')
    app.config['MAIL_DEFAULT_SENDER'] = (sender_name, sender_addr)

    # Optional: Geheimnisse wie reCAPTCHA in ENV, NICHT im Code! (wird im Blueprint benötigt)
    os.getenv('RECAPTCHA_SECRET_KEY')
    os.getenv('RECAPTCHA_SITE_KEY')

    # 4) Flask-Mail initialisieren
    mail.init_app(app)

    # 5) Import und Registration vom Blueprint NACH mail.init_app()
    from .routes import main
    app.register_blueprint(main)

    # 6) Kontext-Processor, damit {{ now.year }} in allen Templates verfügbar ist
    @app.context_processor
    def inject_now():
        return {'now': datetime.now()}

    return app
