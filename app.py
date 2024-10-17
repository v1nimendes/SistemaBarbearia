from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Usuario
from database import init_db
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = '9c8e02b4f3c16aeb57b74b12eab07ef2'
app.config.from_object('config.Config')

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        user = Usuario.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.senha, senha):
            return redirect(url_for('agendamento'))
        else:
            flash('Usuário inválido')
        
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        senharepeat = request.form['senharepeat']

        if senha != senharepeat:
            flash('As senhas não coincidem.')
            return render_template('index.html')

        if Usuario.query.filter_by(email=email).first():
            flash('Email já cadastrado.')
            return render_template('index.html')

        senha_hash = generate_password_hash(senha)
        new_user = Usuario(nome=nome, email=email, senha=senha_hash)
        
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')

    return render_template('index.html')

@app.route('/agendamento')
def agendamento():
    return render_template('agendamento.html')

@app.route('/logout')
def logout():
    return redirect('/login')

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)
