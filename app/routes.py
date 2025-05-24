from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

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
