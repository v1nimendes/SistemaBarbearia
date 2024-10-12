from flask import Flask, render_template
from models import db
from database import init_db

app = Flask(__name__)

# Configurando a aplicação com as configurações do banco de dados
app.config.from_object('config.Config')

# Inicializando o banco de dados
db.init_app(app)

# Rotas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/agendamento')
def agendamento():
    return render_template('agendamento.html')

if __name__ == '__main__':
    with app.app_context():
        init_db()  # Cria as tabelas no banco de dados
    app.run(debug=True)
