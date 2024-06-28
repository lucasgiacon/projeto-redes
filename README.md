# Simple HTTP Server

This project is a simple HTTP server implemented in Python using the socket library. It handles basic GET and PUT requests to serve and store files, respectively.

## Features

- **GET Requests:** Serve files from the `htdocs` directory.
- **PUT Requests:** Store files in the `htdocs` directory.
- **Error Handling:** Returns appropriate HTTP error responses for missing files and internal server errors.

## Project Structure

- **http_responses.py:** Contains functions to send HTTP responses and errors.
- **request_handler.py:** Handles incoming HTTP requests, processes GET and PUT methods, and serves appropriate responses.

## Usage

1. **Clone the repository:**

   `
   git clone https://github.com/yourusername/simple-http-server.git
   cd simple-http-server
   `

2. **Run the server:**

   `bash
   python server.py
   `

3. **Access the server:**

   Open your web browser and navigate to `http://localhost:8000`.

## File Descriptions

### http_responses.py

- **send_error(client_connection, status_code, message):** Sends an HTTP error response.
- **send_response(client_connection, status, content, content_type='text/html'):** Sends a general HTTP response.

### request_handler.py

- **handle_request(client_connection, request_data):** Parses HTTP requests and delegates them to the appropriate handler.
- **handle_get(client_connection, filename):** Handles GET requests to serve files.
- **handle_put(client_connection, filename, request_data):** Handles PUT requests to store files.

## Requirements

- Python 3.x

