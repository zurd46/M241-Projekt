# IT-Praktika Website

Moderne Webanwendung für Informatik-Praktikanten der Benedict-Schule Luzern

Diese Website präsentiert die IT-Praktikanten-Klasse, informiert über die Ausbildung, bietet ein Praktikanten-Portfolio und stellt alle Kontaktmöglichkeiten bereit.
Das Projekt basiert auf Flask und Bootstrap 5 und ist vollständig responsiv gestaltet.

Features

* Startseite mit Hero-Bereich und Portfolio-Cards
* Über uns mit FAQ-Accordion (Ausbildung, Ziele, Module etc.)
* Praktikanten-Portfolio: Alle Profile als Carousel (modern, mobilfreundlich)
* Schulvorstellung: Über die Benedict-Schule mit Bildern und Fakten
* Kontaktseite: Kontaktinfos, Google Maps und Kontaktformular
* Impressum

Installation

1. Repository klonen

git clone [https://github.com/zurd46/IT-Praktika.git](https://github.com/zurd46/IT-Praktika.git)
cd IT-Praktika

2. Virtuelle Umgebung erstellen und aktivieren

python -m venv .venv

Für Windows:

.venv\\Scripts\\activate

Für Mac/Linux:

source .venv/bin/activate

3. Abhängigkeiten installieren

pip install -r requirements.txt

4. Anwendung starten

python run.py

Die Seite ist dann erreichbar unter [http://127.0.0.1:5000](http://127.0.0.1:5000)

Projektstruktur

Projekt/
│
├── app/
│   ├── **init**.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── about.html
│   │   ├── trainees.html
│   │   ├── school.html
│   │   ├── contact.html
│   │   └── impressum.html
│   └── static/
│       ├── css/
│       │   └── styles.css
│       └── img/
│           └── ... (eigene Bilder, z. B. Praktikanten)
│
├── config.py
├── requirements.txt
├── run.py
└── README.md

Anpassungen

* Praktikanten-Profile/Bilder:
  Eigene Bilder im Ordner app/static/img/ speichern und den Bildpfad in trainees.html anpassen.
* Kontaktformular:
  Das Backend für E-Mail-Versand kannst du bei Bedarf ergänzen (z.B. Flask-Mail, Formspree, etc.).

Kontakt

Benedict-Schule Luzern AG
Inseliquai 12B, 6005 Luzern, Schweiz
Telefon: 041 227 01 01
E-Mail: [info@it-praktika.ch](mailto:info@it-praktika.ch)

© 2025 IT-Praktika
