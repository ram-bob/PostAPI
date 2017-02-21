from flask import Flask
from flask import json
from flask import jsonify
import sqlite3
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
@app.route("/posts", methods=['GET'])
def posts():
    conn = sqlite3.connect('blog.db')
    cursor = conn.execute("SELECT post_id, title, body from posts")
    list=[]
    for row in cursor:
      list.append({'post_id': row[0] , 'title': row[1], 'body': row[2]})
    conn.close()
    return jsonify(results=list)

if __name__ == "__main__":
    app.run()
