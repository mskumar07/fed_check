# from flask import Flask, request, jsonify, send_from_directory
# import os
# from werkzeug.utils import secure_filename

# app = Flask(__name__)
# upload_folder = "upload/"

# # @app.route('/api', methods=['GET'])
# # def check():
# #     return "Running Correct file"

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if request.method == 'POST':
#         # Check if the POST request has the file part
#         if 'file' not in request.files:
#             return "No file part"

#         file = request.files['file']

#         # If the user does not select a file, the browser submits an empty file without a filename
#         if file.filename == '':
#             return "No selected file"

#         # Save the uploaded file to the upload folder
#         if not os.path.exists(upload_folder):
#             os.makedirs(upload_folder)

#         # Use secure_filename to avoid any filename-related issues
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(upload_folder, filename)
#         file.save(file_path)

#         print(f"File uploaded successfully. Image URL: {request.host_url}upload/{filename}")
#         return f"File uploaded successfully. Image URL: {request.host_url}upload/{filename}"


# @app.route('/upload/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(upload_folder, filename)

from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.utils import secure_filename
from PIL import Image
import os

app = Flask(__name__)

# Define your upload folder
upload_folder = "upload/"

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'file' not in request.files:
            return "No file part"

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return "No selected file"

        # Save the uploaded file to the upload folder
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        # Use secure_filename to avoid any filename-related issues
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, filename)

        # Open the image
        
        image = Image.open(file)

        # Save the image with reduced quality and in JPEG format without resizing
        compressed_file_path = os.path.join(upload_folder, filename)
        image.save(compressed_file_path, format='JPEG', quality=30, optimize=True)

        print(f"File uploaded successfully. Original Image URL: {request.host_url}upload/{filename}")
        print(f"Compressed Image URL: {request.host_url}upload/{filename}")

        return f"File uploaded successfully. Original Image URL: {request.host_url}upload/{filename}" \
               f"\nCompressed Image URL: {request.host_url}upload/{filename}"

    
@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(upload_folder, filename)


if __name__ == '__main__':
    app.run(debug=True)


# from datetime import datetime
# from flask import Flask, request, jsonify
# from psycopg2.extras import RealDictCursor
# import psycopg2
# from flask_cors import CORS


# app = Flask(__name__)

# CORS(app, resources={r"/mypythonapp/*": {"origins": "https://react.singhis.in"}})

# # def mysqlconnect(): 
# #     # To connect PostgreSQL database
# #     db_host = 'localhost'
# #     db_port = '5432'
# #     db_user = "postgres"
# #     db_password = "zealzoft@123"

# #     # Connect to PostgreSQL
# #     connection = psycopg2.connect(
# #         host=db_host,
# #         port=db_port,
# #         user=db_user,
# #         password=db_password,
# #         dbname="checkdb"
# #     )
# #     return connection

# def mysqlconnect():
#     # To connect PostgreSQL database
#     db_host = '66.85.140.26'
#     db_port = '5433'
#     db_user = "postgres"
#     db_password ='pass123'
#     # Connect to PostgreSQL
#     connection = psycopg2.connect(
#         host=db_host,
#         port=db_port,
#         user=db_user,
#         password=db_password,
#         dbname="checkdb"
#     )
#     return connection

# def execute_query(query, qtype):
#     conn = mysqlconnect()
#     cur = conn.cursor(cursor_factory=RealDictCursor)
#     cur.execute(query)
#     if qtype.upper() == "SELECT":
#         return jsonify(cur.fetchall())
#     else:
#         conn.commit()
#         return jsonify({"Success": "{} Successfully.".format(qtype.lower())})

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/insert_data', methods=['POST'])
# def insert_data():
#     data = request.get_json()
#     conn = mysqlconnect()
#     cur = conn.cursor(cursor_factory=RealDictCursor)
#     cur.execute('INSERT INTO users (username, email) VALUES (%s, %s)', (data['username'], data['email']))
#     conn.commit()
#     return "Success"


# @app.route('/get_data', methods=['GET'])
# def get_data():
#     conn = mysqlconnect()
#     cur = conn.cursor(cursor_factory=RealDictCursor)
#     cur.execute('SELECT * from users')
#     get_data = cur.fetchall()
#     return jsonify(get_data)


# @app.route('/delete_data/<int:id>', methods=['delete'])
# def delete_data(id):
#     conn = mysqlconnect()
#     cur = conn.cursor(cursor_factory=RealDictCursor)
#     cur.execute('DELETE  from users WHERE id = %s',(id,))
#     conn.commit()
#     return jsonify('Deleted success') 


