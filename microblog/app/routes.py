
# Import app variable defined in the app package 
from app import app # The 1st app is the app package represented by app directory and the 2nd is the app variable defined in __init__.py 

from flask import send_from_directory
import os

import subprocess

# # Decorators enhance functions with additional behaviours 
# # Writen above a function and starts with @ sign 
# # Here it provides a mapping between a url and a function 
# # You can assign more than 1 url to the same function 
# @app.route('/')
# @app.route('/index')

# # Do the following whenever the following function is called. 
# def index():
#     return "Hello Microblog!"


def convert_asciidoc_to_html(asciidoc_file_path):
    if os.path.exists(asciidoc_file_path):
        
        # Use the subprocess module to run the AsciiDoctor command
        cmd = ['asciidoctor', '-o', output_html_path, asciidoc_file_path]
        try:
            subprocess.run(cmd, check=True)
            return True
        except subprocess.CalledProcessError:
            return False
    else:
        return False


# current_directory = os.getcwd()
# print("Current directory:", current_directory)

# Specify the path to your AsciiDoc file
asciidoc_file_path = 'static/adoc/index.adoc'

# Get the base name of the AsciiDoc file (without extension)
file_base_name = os.path.splitext(os.path.basename(asciidoc_file_path))[0]

# Generate the output HTML file path
output_html_path = f"static/html/{file_base_name}.html"

# Convert the AsciiDoc content to HTML and save it with the same name as the input file
conversion_successful = convert_asciidoc_to_html(asciidoc_file_path)

if conversion_successful:
    print(f"Conversion successful. HTML saved as '{output_html_path}'")
else:
    print('Error: AsciiDoc file not found or conversion failed.')



@app.route('/')
@app.route('/index')
def serve_index():
    # Get the path to the 'static' directory, which is one level above 'app'
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static')
    
    # Get the path to the 'html' directory within 'static'
    html_dir = os.path.join(static_dir, 'html')
    
    # Use send_from_directory to serve the index.html file
    return send_from_directory(html_dir, 'index.html')


