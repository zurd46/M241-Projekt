from flask import Flask
from .routes import main
from datetime import datetime

def create_app():
    app = Flask(__name__)

    # --> HIER Blueprint REGISTRIEREN:
    app.register_blueprint(main)

    @app.context_processor
    def inject_now():
        return {'now': datetime.now()}

    return app
