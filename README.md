# IT-Praktika Website

**Kurzübersicht:**  
Flask-&-Bootstrap-basiertes Portal der Benedict-Schule Luzern, um Auszubildende (Applikations- & Plattformentwicklung) zu präsentieren, Praktikanten-Profile zu filtern und Kontakt per E-Mail zu ermöglichen.

---

Projektstruktur:
   ```bash
   M241-Projekt/
      ├── .env               # SMTP-& E-Mail-Daten (Demo-Werte)
      ├── requirements.txt
      ├── run.py             # Flask-App-Factory
      └── app/
          ├── __init__.py    # create_app(): Flask, Mail, Blueprint, Kontext
          ├── routes.py      # Routen & E-Mail-Handler
          ├── templates/     # Jinja2-Vorlagen
          │   ├── base.html
          │   ├── index.html
          │   ├── about.html
          │   ├── trainees.html
          │   ├── school.html
          │   ├── contact.html
          │   └── impressum.html
          └── static/
              ├── css/
              │   └── style.css
              ├── favicon.ico
              └── images/    # Alle Hero- und Profilbilder

```

## Installation

1. Repository klonen  
   ```bash
   git clone https://github.com/zurd46/M241-Projekt.git
   cd M241-Projekt

2. Virtuelle Umgebung erstellen & aktivieren
   ```bash
   python -m venv .venv
    # Windows PowerShell:
    .venv\Scripts\activate
    # Linux/macOS:
    source .venv/bin/activate

3. Abhängigkeiten installieren
   ```bash
   pip install -r requirements.txt

4. .env anlegen (Demo-Werte)
   ```bash
   MAIL_SERVER=smtp.example.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=demo@example.com
   MAIL_PASSWORD=demopassword
   MAIL_DEFAULT_SENDER_NAME="IT-Praktika Kontakt"
   MAIL_DEFAULT_SENDER_ADDR=info@it-praktika.ch

   RECAPTCHA_SITE_KEY=................
   RECAPTCHA_SECRET_KEY==................
  
   Hinweis:
   Achte darauf, dass .env in .gitignore steht.
   Alternativ System-Umgebungsvariablen verwenden.

5. Anwendung starten
    ```bash
    python run.py

6. Im Browser öffnen
   ```bash
   http://127.0.0.1:5000
