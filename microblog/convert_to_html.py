import subprocess
import os

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
asciidoc_file_path = 'index.adoc'

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
