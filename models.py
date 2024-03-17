from extensions import db

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    population = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Animal {self.name}>'
