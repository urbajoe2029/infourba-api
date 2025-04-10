from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route("/colaboradores")
def get_colaboradores():
    try:
        conn = psycopg2.connect("postgresql://SEU_USUARIO:SEU_TOKEN@ep-XXXXXX-pooler.us-east-2.aws.neon.tech/SEU_BANCO?sslmode=require")
        cur = conn.cursor()
        cur.execute("SELECT id, nome, setor FROM colaboradores")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        return jsonify([
            {"id": r[0], "nome": r[1], "setor": r[2]}
            for r in rows
        ])
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
