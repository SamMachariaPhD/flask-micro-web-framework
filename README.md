# flask-micro-web-framework
Basics of Flask micro web framework in Python.

Flask Web Dev Framework

# Miguel Lectures

==*30/09/2023 00:31*==

# 1\. Introduction

## GitHub Repository

- https://github.com/miguelgrinberg/microblog
- 1 commit per chapter

## Miguel Microblog

- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

# 2\. Installing Python and Flask

1.  Install Anaconda https://www.anaconda.com/download
2.  Install Flask
3.  Make a GitHub repository https://github.com/SamMachariaPhD/flask-micro-web-framework
4.  Git clone it to your documents

```bash
git clone https://github.com/SamMachariaPhD/flask-micro-web-framework.git
```

1.  Create a virtual environment

```bash
python3 -m venv venv # the 1st venv is a must, the 2nd is just a name of your environment
source venv/bin/activate 
python3 -m pip install --upgrade pip 
pip install -r requirements.txt
```

- Eliminates/minimises version conflicts
- Uses only the libraries an versions needed
- Makes it easy to determine the exact requirements for your project so you can easily reproduce elsewhere
- Good introduction to Docker

# 3\. 1st Flask App

*==30/09/2023 15:10==*

1.  Make `microblog` folder
2.  Make a `app` folder **inside** the `microblog`
3.  Make `__init__.py` **inside** the `app` folder
4.  Write the following code in `__init__.py` in the following order to avoid common circular dependency in Flask

```python
from flask import Flask # not everything 
app = Flask(__name__) # Flask will now know the locations of our files 
from app import routes # not yet made
```

- Define the logic of the application in `app/routes.py`

```python
# Import app variable defined in the app package 
from app import app # The 1st app is the app package represented by app directory and the 2nd is the app variable defined in __init__.py 

# Decorators enhance functions with additional behaviours 
# Writen above a function and starts with @ sign 
# Here it provides a mapping between a url and a function 
# You can assign more than 1 url to the same function 
@app.route('/')
@app.route('/index')

# Do the following whenever the following function is called. 
def index():
    return "Hello Microblog!"
```

- Make top level script that represents the application `microblog/microblog.py`

```python
from app import app
```

- To tell Flask where the application is located, define an environment variable `export FLASK_APP` to reset to `microblog.py`, which is the module that defines the application

```bash
export FLASK_APP=microblog.py
set FLASK_APP=microblog.py # windows 
flask run # start the application
```

- Go to the http url shown in console

```bash
(venv) (base) ... /microblog$ flask run
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000 # Go to this url to see "Hello Microblog!"
Press CTRL+C to quit
127.0.0.1 - - [30/Sep/2023 15:47:16] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [30/Sep/2023 15:47:16] "GET /favicon.ico HTTP/1.1" 404 -
```

- To forcefully kill the Flask application, you should use `CTRL + C` and not `CTRL + Z`.
- If you confuse and use `CTRL + Z` it will not be possible to use `CTRL + C` and the Flask application will not stop and the next time you do `flask run`, you will get this error:

```bash
* Debug mode: off
Address already in use
Port 5000 is in use by another program. Either identify and stop that program, or start the server with a different port.
```

- To force stop, identify the `PID` of the Flask application running in the background:

```bash
ps aux | grep python
```

- Let us say you identify this output :

```bash
user       279519  0.0  0.1 108460 28072 pts/4    T    17:12   0:00 /home/user/Documents/flask-micro-web-framework/venv/bin/python3 /home/user/Documents/flask-micro-web-framework/venv/bin/flask run
```

- The `PID` is `279519` and you can now force kill it:

```bash
kill -9 279519
```

*==02/10/2023 17:32==*

## 4\. Templates

With the following code, if you navigate to /user url, you will find the following message: "Hello, Sam!"

```python
@app.route('/user')
def user():
    user = {'username':'Sam'}
    return f"Hello, {user['username']}!"
```

Or

```python
@app.route('/user')
def user():
    user = {'username':'Sam'}
    return """
<html>
    <head>
    <title>Microblog</title>
    </head>
    <body>
    <h1> Hello, """ + user['username'] + """ !</h1>
    </body>
</html>
"""
```

- But if your website continues to grow and, say, you have several pages and each page need to have, say, the same navigation bar, you have to keep copying that code across all pages and that is going to be very difficult to maintain.
- It is important to separate the application logic from the presentation. Avoid mixing the code with HTML.
- An easier way to do this is to create a `templates` folder in `microblog/app/templates` and Flask will automatically recognise this folder.
- Then create, say, `index.html` inside `templates` folder:

```html
<html>
    <head>
    <title>{{title}} - Microblog</title>
    </head>
    <body>
    <h1> Hello, {{user.username}} !</h1>
    <h2>Here is h2 line.</h2>
    </body>
</html>
```

- You can then pass those variables in `render_template` in `routes.py`:

```python
@app.route('/user')
def user():
    user = {'username':'Sam'}
    return render_template("index.html", title="User", user=user)
```

==*12/10/2023 17:35*==

## 5\. Conditional Statements

- An example condition: what if the title is not provided?

`microblog/app/routes.py`

```python
@app.route('/user')
def user():
    user = {'username':'Sam'}
    return render_template("index.html", title="", user=user) # title not provided
```

`microblog/app/templates/index.html`

```html
<html>
    <head>
        {% if title %}
        <title>{{title}} - Microblog</title>
        {% else %}
        <title>Welcome to Microblog</title> <!-- Print this if the title is not provided.  -->
        {% endif %}
    </head>
    <body>
    <h1> Hello, {{user.username}} !</h1>
    <h2>Here is h2 line.</h2>
    </body>
</html>
```

- Loops 

```python
posts = [
        {
            'author':{'username':'John'},
            'body':'The Future of AI'
        },
        {
            'author':{'username':'Daniel'},
            'body':'Solid Mechanics'
        },
    ]
```

```html
{% for post in posts %}
    <div><p> <i>{{ post.author.username }}</i> says: <b>{{ post.body }}</b></p></div>
    {% endfor %}
```

## 7\. Template Inheritance

We can use *template inheritance* method to make a `base.html` skeleton which contains the **navigation bar** and all other common features/structure of our page that can be reused in other pages. Every new page will be *extending* the *base.html* and the new part will be inserted in the `block content` space.

- base.html

```html
<html>
    <head>
        {% if title %}
        <title>{{title}} - Microblog</title>
        {% else %}
        <title>Welcome to Microblog</title> <!-- Print this if the title is not provided.  -->
        {% endif %}
    </head>
    <body>
        <div>Microblog: <a href="/index">Home</a></div>
        {% block content %}
        {% endblock %}
    </body>
</html>
```

- index.html

```html
{% extends "base.html" %}

{% block content %}
    <h1> Hello, {{user.username}} !</h1>
    <h2>Here is h2 line.</h2>
    {% for post in posts %}
    <div><p> <i>{{ post.author.username }}</i> says: <b>{{ post.body }}</b></p></div>
    {% endfor %}
{% endblock %}
```
