# Blog Post API Assignment
Language used : Python 2.7.13

Blog Post API Assignment

# API Framework used is flask(http://flask.pocoo.org/docs/0.12/)
install instruction for Flask

`$ pip install Flask`

# Running main Python program
Download the entire repository in one folder.

Set pwd to this repo folder

Command to run the Web Server
``` shell
$ python main.py

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```


# Two Test case
1. An endpoint for POSTing a single blog post
```shell
$ curl -i -H "Content-type: application/json" -X POST -d '{"title":"Blog Title", "body": "Blog Body"}'  http://localhost:5000/post
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 4
Server: Werkzeug/0.11.15 Python/2.7.13
Date: Tue, 21 Feb 2017 13:00:46 UTC

Done

```
2. An endpoint for GETing all blog posts
```shell
$ curl -i -X GET  http://localhost:5000/posts
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 106
Server: Werkzeug/0.11.15 Python/2.7.13
Date: Tue, 21 Feb 2017 12:26:51 UTC

{
  "results": [
    {
      "body": "Blog Body",
      "post_id": "1",
      "title": "Blog Title"
    }
  ]
}
```
