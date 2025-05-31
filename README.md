# IT-Praktika Website

Moderne Webanwendung für Informatik-Praktikanten der Benedict-Schule Luzern

Diese Website stellt die Auszubildenden der Informatikklasse (Applikations- & Plattformentwicklung) der Benedict-Schule Luzern vor, informiert über die Ausbildung, bietet ein Portfolio aller Praktikanten mit Filterfunktion und stellt alle Kontaktmöglichkeiten (inkl. E-Mail-Versand) zur Verfügung. Das Projekt basiert auf Flask und Bootstrap 5 und ist vollständig responsiv gestaltet.

---

## Inhaltsverzeichnis

1. [Features](#features)  
2. [Installation](#installation)  
3. [Umgebungsvariablen / `.env`](#umgebungsvariablen--env)  
4. [Projektstruktur](#projektstruktur)  
5. [Anwendung starten](#anwendung-starten)  
6. [Kontakt](#kontakt)  
7. [Lizenz / Copyright](#lizenz--copyright)

---

## Features

- **Dynamischer Hero-Carousel**  
  - Alle Bilder im Ordner `static/images/` werden automatisch eingelesen und in einem Bootstrap Carousel angezeigt.  
  - Egal wie viele Bilder vorliegen, sie laufen reibungslos durch (inklusive Steuerungspfeilen und Indikatoren).  
  - Fallback-Frontend, falls der `static/images`-Ordner leer ist.

- **Über uns (Klasse & Mission / FAQ-Accordion)**  
  - Infos zur Klasse (aktuell 20 Auszubildende in Applikations- & Plattformentwicklung).  
  - Mission, Ausbildungsgliederung und detaillierte Modulübersicht (Semester 1–4 und 5–8).  
  - FAQ‐Accordion zu den häufigsten Fragen (Was ist IT-Praktika? Wie funktioniert die Suche? etc.).  
  - Zusätzlicher Infokasten mit den wichtigsten Schwerpunkten (Praxisbezug, Innovative Lehre, Starkes Netzwerk).  

- **Praktikanten-Portfolio (Filterbare Grid‐Darstellung)**  
  - Alle Profile der Auszubildenden werden in einem adaptiven Grid (Höhe 200–370 px, 4 Spalten auf großen Bildschirmen) dargestellt.  
  - Zu jedem Praktikanten: Foto (alle Bilder immer exakt 370 px hoch), Name, Fachrichtung, Skills, Kurzbeschreibung und ein E-Mail‐Button.  
  - Oben in der Seite: ein Suchfeld, das clientseitig nach Name oder Skill filtert (JavaScript-Filter).  
  - Profilbilder liegen im Ordner `static/images/` und werden über Jinja2 in `trainees.html` eingebunden.  

- **Schulvorstellung (Benedict-Schule Luzern)**  
  - Infos zur Schule, Klassenfoto, Räumlichkeiten, dozierende Lehrpersonen, Partnerschaften mit regionalen IT-Firmen.  
  - Ausbilder, Module und realisierte Projekte werden strukturiert präsentiert.  
  - Zwei Infokarten: „Profilübersicht“ und „Filterfunktion“ unterhalb, horizontal angeordnet.

- **Kontaktseite mit E-Mail‐Versand über Flask-Mail**  
  - Anzeige aller Kontaktdaten (Adresse, Telefon, Fax, E-Mail).  
  - Eingebettete Google Maps-Ansicht der Adresse `Inseliquai 12B, 6005 Luzern`.  
  - Kontaktformular mit Name, E-Mail und Nachricht (alle Felder Pflicht).  
  - Formular sendet per JavaScript (`fetch()`) eine JSON‐Anfrage an `/send_email`, wo Flask-Mail (SMTP) die Nachricht an `info@it-praktika.ch` verschickt.  
  - Fehler- und Erfolgsmeldung werden im Frontend angezeigt.  

- **Impressum**  
  - Standard‐Pflichtinformationen zum Projekt, Betreiber, Hosting usw.

- **Responsives Design**  
  - Vollständig mobil‐ und tabletfreundlich (Mobile‐First mit Bootstrap 5).  
  - Grid‐Layouts, Flexbox und CSS‐Utilities sorgen für optimale Darstellung auf allen Endgeräten.  
  - Alle Bilder werden mit `object-fit: cover` beschnitten, um stets dieselbe Höhe beizubehalten.

- **Barrierefreiheit**  
  - WCAG 2.1 AA: Semantisches HTML, ausreichende Farbkontraste, Fokus‐Zustände, Tastaturnavigation.  
  - Alt‐Texte für alle Bilder, ARIA‐Attribute für Accordion und Carousel‐Indikatoren.

- **Sicherer Umgang mit sensiblen Daten**  
  - SMTP‐Zugangsdaten werden in einer `.env`‐Datei oder als Umgebungsvariablen gespeichert (nicht im Code).  
  - Python‐Bibliothek `python-dotenv` liest die `.env` automatisch beim Start.  

- **Modulare Flask‐Architektur**  
  - Blueprint‐Struktur (`app/routes.py`, `app/__init__.py`).  
  - `create_app()` in `__init__.py` initialisiert Flask, Flask-Mail, lädt Umgebungsvariablen, registriert das Blueprint und setzt Kontext‐Variable `now`.  

- **Styling & Design**  
  - Farbpalette: Hauptfarben Blau (#1565c0) und Türkis (#2196f3) mit neutralem Hellgrau (#f8f9fa) und Weiß (#ffffff).  
  - Primärschrift: Bootstrap‐Standard; Icons via Bootstrap-Icons.  
  - Card‐ und Button‐Styles exakt auf CI-Farben abgestimmt (`background-color: #1565c0; border-color: #1565c0;`).  

---

## Installation

1. **Repository klonen**  
   ```bash
   git clone https://github.com/zurd46/IT-Praktika.git
   cd IT-Praktika
