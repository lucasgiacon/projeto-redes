# request_handler.py

import os
from http_responses import send_response, send_error

def handle_request(client_connection, request_data):
    # Encontra o final dos cabeçalhos (dupla quebra de linha)
    try:
        headers_end = request_data.index(b'\r\n\r\n') + 4
    except ValueError:
        # Se não encontrar o final dos cabeçalhos, assuma que todo o request é cabeçalho
        headers_end = len(request_data)
    
    # Separa os cabeçalhos do corpo
    header_part = request_data[:headers_end].decode('utf-8', 'ignore')
    body_part = request_data[headers_end:]  # Mantém o corpo como bytes
    
    headers = header_part.split("\n")
    method = headers[0].split()[0]
    filename = headers[0].split()[1]

    if filename == "/":
        filename = "/index.html"

    # Passa o corpo como dados binários para os métodos que precisam
    if method == "GET":
        handle_get(client_connection, filename)
    elif method == "PUT":
        handle_put(client_connection, filename, body_part)

def handle_get(client_connection, filename):
    try:
        # Define um tipo de conteúdo genérico para todos os arquivos
        # Isto pode ser ajustado manualmente para tipos de arquivo específicos, se desejado
        content_type = 'application/octet-stream'
        
        # Para arquivos que você sabe serem de texto, você pode ajustar content_type aqui
        if filename.endswith('.html'):
            content_type = 'text/html'
        elif filename.endswith('.css'):
            content_type = 'text/css'
        elif filename.endswith('.js'):
            content_type = 'application/javascript'
        
        with open("htdocs" + filename, "rb") as fin:  # Abre o arquivo em modo binário
            content = fin.read()
            send_response(client_connection, "200 OK", content, content_type)
    except FileNotFoundError:
        send_error(client_connection, "404 NOT FOUND", "<h1>ERROR 404!<br>File Not Found!</h1>")


def handle_put(client_connection, filename, request_data):
    # O caminho onde os arquivos serão armazenados
    file_path = "htdocs" + filename
    
    try:
        # Escreve os dados recebidos no arquivo especificado.
        # Isso abrirá ou criará o arquivo em file_path, substituindo-o se já existir.
        with open(file_path, "wb") as fout:
            print(request_data)
            fout.write(request_data)
        
        # Se o arquivo foi criado ou sobrescrito com sucesso, envia uma resposta 201 (Created) ou 200 (OK).
        send_response(client_connection, "201 Created", "<h1>File Created/Updated Successfully!</h1>")
    except Exception as e:
        # Em caso de erro ao salvar o arquivo, envia uma resposta 500 (Internal Server Error).
        send_error(client_connection, "500 Internal Server Error", f"<h1>ERROR 500!<br>Internal Server Error!</h1>\n<p>{str(e)}</p>")
