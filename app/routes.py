import os
from flask import Blueprint, render_template, current_app

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # 1) Absoluter Pfad zum Ordner static/images
    image_folder = os.path.join(current_app.static_folder, 'images')
    
    # 2) Nur gültige Bilddateien herausfiltern
    valid_exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
    try:
        hero_images = [
            fname for fname in os.listdir(image_folder)
            if fname.lower().endswith(valid_exts)
        ]
    except FileNotFoundError:
        # Sollte der Ordner fehlen, liste eine leere Liste auf
        hero_images = []
    
    # 3) Optional: Alphabetisch sortieren
    hero_images.sort()
    
    # 4) Übergabe an das Template
    return render_template('index.html', hero_images=hero_images)

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
