# PostAPI
Language used : Python 2.7.13

Blog Post API Assignment

# API Framework used is flask(http://flask.pocoo.org/docs/0.12/)
install instruction

`$ pip install Flask`

# Running main Python program
Command to run
`$ python main.py`
``` python
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [21/Feb/2017 18:32:33] "GET /posts HTTP/1.1" 200 -
```


# Two Test case
1. An endpoint for POSTing a single blog post
```shell
$ curl -i -H "Content-type: application/json" -X POST -d '{"title":"Blog Title", "body": "Blog Body"}'  http://localhost:5000/post
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 4
Server: Werkzeug/0.11.15 Python/2.7.13
Date: Tue, 21 Feb 2017 13:00:46 GMT

Done

```
2. An endpoint for GETing all blog posts
```shell
$ curl -i -X GET  http://localhost:5000/posts
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 106
Server: Werkzeug/0.11.15 Python/2.7.13
Date: Tue, 21 Feb 2017 12:26:51 GMT

{
  "results": [
    {
      "body": "body1",
      "post_id": "1",
      "title": "tille1"
    }
  ]
}
```
