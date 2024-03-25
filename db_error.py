import sqlite3
from flask import Flask, request

app = Flask(__name__)

# データベース接続の設定
DATABASE = 'mydatabase.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/search')
def search():
    username = request.args.get('username')
    conn = get_db()
    cursor = conn.cursor()

    # SQLインジェクションの脆弱性を含むクエリ
    query = "SELECT * FROM users WHERE username = '{}'".format(username)
    cursor.execute(query)

    results = cursor.fetchall()
    return '<br>'.join([str(row) for row in results])

if __name__ == '__main__':
    app.run(debug=True)

print(終了)
