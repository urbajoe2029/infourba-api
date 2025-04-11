from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Conexão com Supabase ou Neon (exemplo com Supabase)
conn = psycopg2.connect(
    host="db.tdyqpuprumdynezvieqy.supabase.co",
    port="5432",
    dbname="postgres",
    user="postgres",
    password="Urbajoe26?",
)

cursor = conn.cursor()

@app.route("/")
def home():
    return "API está rodando!"

@app.route("/colaboradores", methods=["GET"])
def listar_colaboradores():
    cursor.execute("SELECT cod, nome, depto FROM colaboradores")
    rows = cursor.fetchall()
    return jsonify([{"cod": r[0], "nome": r[1], "depto": r[2]} for r in rows])

@app.route("/colaboradores", methods=["POST"])
def adicionar_colaborador():
    data = request.get_json()
    nome = data.get("nome")
    depto = data.get("depto")
    cursor.execute("INSERT INTO colaboradores (nome, depto) VALUES (%s, %s)", (nome, depto))
    conn.commit()
    return jsonify({"status": "ok"})

# Para o Render detectar e rodar na porta certa
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
