import os

class Config:
    # Corrigindo o esquema de conexão para PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:12345@localhost:5432/barbearia')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
