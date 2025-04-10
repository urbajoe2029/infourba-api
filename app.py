from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route("/colaboradores")
def get_colaboradores():
    try:
        conn = psycopg2.connect("postgresql://neondb_owner:npg_XU2VZajNP4oR@ep-weathered-sound-a5q0b2x5-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require")
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
        
if __name__ == "__main__":
    from os import getenv
    port = int(getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)