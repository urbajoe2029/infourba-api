import psycopg2
from flask import Flask

app = Flask(__name__)

# Sua connection string
DATABASE_URL = "postgresql://postgres:Urbajoe26?@db.tdyqpuprumdynezvieqy.supabase.co:5432/postgres"

@app.route('/')
def hello():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("SELECT NOW()")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return f"Conexão com o banco deu certo! Data/hora: {result}"
    except Exception as e:
        return f"Erro: {e}"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
