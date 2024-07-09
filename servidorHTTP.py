#servidor HTTP
import socket
from request_handler import handle_request

SERVER_HOST = ""
SERVER_PORT = 8080

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print(f"Servidor em execução...\nEscutando por conexões na porta {SERVER_PORT}")

    while True:
        client_connection, client_address = server_socket.accept()
        request_data = b''
        while True:
            chunk = client_connection.recv(1024)
            request_data += chunk
            if len(chunk) < 1024:
                break
        request = request_data
        if request:
            print(request)
            handle_request(client_connection, request)

if __name__ == "__main__":
    start_server()
