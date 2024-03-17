from flask import Flask, render_template, request, redirect, url_for
from extensions import db
from models import Animal

app = Flask(__name__)
app.debug = True  # Enable debug mode
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost/animal'
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_animal():
    if request.method == 'POST':
        name = request.form['name']
        species = request.form['species']
        population = request.form['population']

        animal = Animal(name=name, species=species, population=population)
        db.session.add(animal)
        db.session.commit()

        return redirect(url_for('animals'))

    return render_template('add_animal.html')

@app.route('/animals')
def animals():
    all_animals = Animal.query.all()
    return render_template('animals.html', animals=all_animals)
