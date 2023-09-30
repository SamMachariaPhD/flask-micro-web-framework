
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
    