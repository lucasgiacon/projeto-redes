# http_responses.py

def send_error(client_connection, status_code, message):
    send_response(client_connection, status_code, message)

def send_response(client_connection, status, content, content_type='text/html'):
    response = f'HTTP/1.1 {status}\r\n'
    response += 'Content-Type: ' + content_type + '\r\n'
    response += 'Connection: close\r\n'
    response += f'Content-Length: {len(content)}\r\n'
    response += '\r\n'
    client_connection.sendall(response.encode())
    if isinstance(content, str):
        client_connection.sendall(content.encode())
    else:
        client_connection.sendall(content)
    client_connection.close()

