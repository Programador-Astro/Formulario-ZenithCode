from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    discord = db.Column(db.String(50))
    github = db.Column(db.String(100))
    linkedin = db.Column(db.String(100))
    tecnologias = db.relationship('Tecnologia', backref='usuario', cascade="all, delete")

class Tecnologia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    nivel = db.Column(db.String(20))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
