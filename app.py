import psycopg2
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# URL de conexão ao banco PostgreSQL (sem colchetes!)
DATABASE_URL = "postgresql://postgres:Urbajoe26?@db.tdyqpuprumdynezvieqy.supabase.co:5432/postgres"

def get_conn():
    return psycopg2.connect(DATABASE_URL)

# Criação da tabela (uma vez só)
@app.route('/criar-tabela')
def criar_tabela():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
        return "Tabela criada com sucesso!"
    except Exception as e:
        return f"Erro ao criar tabela: {e}"

# Inserir usuário
@app.route('/inserir', methods=['POST'])
def inserir():
    data = request.get_json()
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (data['nome'], data['email']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"mensagem": "Usuário inserido com sucesso!"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

# Listar todos os usuários
@app.route('/usuarios')
def listar():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, nome, email FROM usuarios")
        usuarios = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify([{"id": u[0], "nome": u[1], "email": u[2]} for u in usuarios])
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

# Teste simples
@app.route('/')
def home():
    return "API está rodando!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

