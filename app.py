from flask import Flask, jsonify, request, send_from_directory, render_template_string
import os

app = Flask(__name__)

# Directory where files are stored
BASE_DIRECTORY = '.'  # Change this to your desired directory if needed

@app.route('/browse', methods=['GET'])
def browse_directory():
    # Get the directory path from the query parameter, default to current directory
    directory_path = request.args.get('path', BASE_DIRECTORY)

    # Ensure the directory exists
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        return jsonify({"error": "Invalid directory path"}), 400

    # Get the list of file extensions from the query parameter, default to .ex4
    extensions = request.args.get('extensions', '.ex4')
    extensions_list = extensions.split(',')

    # List all files in the directory that match the given extensions
    files = [f for f in os.listdir(directory_path) if any(f.endswith(ext) for ext in extensions_list)]

    # Render the files in a simple HTML template
    template = """
    <ul>
        {% for file in files %}
        <li>
            <a href="/{{ file }}">{{ file }}</a> <!-- Modified URL -->
            <a href="/download?path={{ directory }}/{{ file }}">[Download]</a>
        </li>
        {% endfor %}
    </ul>
    """
    return render_template_string(template, files=files, directory=directory_path)

@app.route('/<filename>', methods=['GET'])
def direct_download(filename):
    """
    Serve files directly based on their filename in the base directory.
    """
    file_path = os.path.join(BASE_DIRECTORY, filename)

    # Ensure the file exists
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        return jsonify({"error": "File not found"}), 404

    return send_from_directory(BASE_DIRECTORY, filename, as_attachment=True)

@app.route('/file', methods=['GET'])
def view_file():
    file_path = request.args.get('path')
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        return jsonify({"error": "Invalid file path"}), 400

    # Check for supported file extensions
    allowed_extensions = ['.ex4', '.ex5', '.zip']  # Add more extensions as needed
    if not any(file_path.endswith(ext) for ext in allowed_extensions):
        return jsonify({"error": "Unsupported file type"}), 400

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    return f"<pre>{content}</pre>"

@app.route('/download', methods=['GET'])
def download_file():
    file_path = request.args.get('path')
    directory, filename = os.path.split(file_path)

    # Ensure the file exists
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        return jsonify({"error": "File not found"}), 404

    return send_from_directory(directory, filename, as_attachment=True)

# To run the API
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8282)
