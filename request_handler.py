# request_handler.py

import os
from http_responses import send_response, send_error

def handle_request(client_connection, request_data):
    try:
        headers_end = request_data.index(b'\r\n\r\n') + 4
    except ValueError:
        headers_end = len(request_data)
    
    header_part = request_data[:headers_end].decode('utf-8', 'ignore')
    body_part = request_data[headers_end:]
    
    headers = header_part.split("\n")
    method = headers[0].split()[0]
    filename = headers[0].split()[1]

    if filename == "/":
        filename = "/index.html"

    if method == "GET":
        handle_get(client_connection, filename)
    elif method == "PUT":
        handle_put(client_connection, filename, body_part)

def handle_get(client_connection, filename):
    try:
        content_type = 'application/octet-stream'
        
        if filename.endswith('.html'):
            content_type = 'text/html'
        elif filename.endswith('.css'):
            content_type = 'text/css'
        elif filename.endswith('.js'):
            content_type = 'application/javascript'
        
        with open("htdocs" + filename, "rb") as fin:
            content = fin.read()
            send_response(client_connection, "200 OK", content, content_type)
    except FileNotFoundError:
        send_error(client_connection, "404 NOT FOUND", "<h1>ERROR 404!<br>File Not Found!</h1>")

def handle_put(client_connection, filename, request_data):
    file_path = "htdocs" + filename
    
    try:
        with open(file_path, "wb") as fout:
            fout.write(request_data)
        
        send_response(client_connection, "201 Created", "<h1>File Created/Updated Successfully!</h1>")
    except Exception as e:
        send_error(client_connection, "500 Internal Server Error", f"<h1>ERROR 500!<br>Internal Server Error!</h1>\n<p>{str(e)}</p>")