from flask import Flask, request
from flask import json
from flask import jsonify
import sqlite3
app = Flask(__name__)

@app.route("/") #default case. Used for testing only
def hello():
    return "Hello World!"
@app.route("/posts", methods=['GET']) #An endpoint for POSTing a single blog post
def posts():
    conn = sqlite3.connect('blog.db')
    cursor = conn.execute("SELECT post_id, title, body from posts")
    list=[]
    for row in cursor:
      list.append({'post_id': row[0] , 'title': row[1], 'body': row[2]})
    conn.close()
    return jsonify(results=list)
@app.route("/post", methods=['POST']) #An endpoint for GETing all blog post
def post():
    conn = sqlite3.connect('blog.db')
    json_dict = request.get_json()
    cursor = conn.execute("SELECT count(*) from posts")
    count_id=0
    for row in cursor:
      count_id=row[0]
    count_id += 1
    conn.execute("INSERT INTO posts (post_id,title,body)  VALUES (?,?,?)",(str(count_id),str(json_dict['title']),str(json_dict['body'])))
    conn.commit()
    conn.close()
    return "Done"

if __name__ == "__main__":
    app.run()
