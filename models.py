from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)

class Profissional(db.Model):
    __tablename__ = 'profissionais'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    profissional_id = db.Column(db.Integer, db.ForeignKey('profissionais.id'), nullable=False)
    tipo_servico = db.Column(db.String(255), nullable=False)
    horario = db.Column(db.DateTime, nullable=False)

    usuario = db.relationship('Usuario', backref='agendamentos')
    profissional = db.relationship('Profissional', backref='agendamentos')

class HorarioDisponivel(db.Model):
    __tablename__ = 'horarios_disponiveis'

    id = db.Column(db.Integer, primary_key=True)
    profissional_id = db.Column(db.Integer, db.ForeignKey('profissionais.id'), nullable=False)
    horario = db.Column(db.DateTime, nullable=False)
    disponivel = db.Column(db.Boolean, default=True)

    profissional = db.relationship('Profissional', backref='horarios_disponiveis')
