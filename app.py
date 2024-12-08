from flask import Flask, jsonify, Response ,request, send_from_directory, render_template_string
import sqlite3
from math import ceil
# from polygon_forex import get_data
import json
import os
from io import StringIO
import csv


app = Flask(__name__)

DATABASE_NAME = "klines_data.db"

DEFAULT_PAGE_SIZE = 100

# def query_db(query, args=(), one=False):
#     conn = sqlite3.connect(DATABASE_NAME)
#     cur = conn.cursor().execute(query, args)
#     rv = cur.fetchall()
#     conn.close()
#     return (rv[0] if rv else None) if one else rv

@app.route('/browse', methods=['GET'])
def browse_directory():
    # Get the directory path from the query parameter, default to current directory
    directory_path = request.args.get('path', '.')

    # Ensure the directory exists
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        return jsonify({"error": "Invalid directory path"}), 400

    # Get the list of file extensions from the query parameter, default to .json
    extensions = request.args.get('extensions', '.zip')
    extensions_list = extensions.split(',')

    # List all files in the directory that match the given extensions
    files = [f for f in os.listdir(directory_path) if any(f.endswith(ext) for ext in extensions_list)]

    # Render the files in a simple HTML template
    template = """
    <ul>
        {% for file in files %}
        <li>
            <a href="/file?path={{ directory }}/{{ file }}">{{ file }}</a>
            <a href="/download?path={{ directory }}/{{ file }}">[Download]</a>
        </li>
        {% endfor %}
    </ul>
    """
    return render_template_string(template, files=files, directory=directory_path)


@app.route('/file', methods=['GET'])
def view_file():
    file_path = request.args.get('path')
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        return jsonify({"error": "Invalid file path"}), 400

    # Check for supported file extensions
    allowed_extensions = ['.json', '.txt', '.zip']  # Add more extensions as needed
    if not any(file_path.endswith(ext) for ext in allowed_extensions):
        return jsonify({"error": "Unsupported file type"}), 400

    with open(file_path, 'r') as f:
        content = f.read()

    return f"<pre>{content}</pre>"


@app.route('/download', methods=['GET'])
def download_file():
    file_path = request.args.get('path')
    directory, filename = os.path.split(file_path)
    return send_from_directory(directory, filename, as_attachment=True)

# To run the API
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=8282)
