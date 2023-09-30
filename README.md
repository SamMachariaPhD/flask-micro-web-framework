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

