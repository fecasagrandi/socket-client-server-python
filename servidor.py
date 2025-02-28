import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 6969))
server.listen(5)

PASSWORD = "casa1234"

try:
    while True:
        client, address = server.accept()
        data = client.recv(5000).decode()
        print(data)

        lines = data.split("\r\n")
        received_password = lines[0].strip() if len(lines) > 0 else ""

        if received_password == PASSWORD:
            response = "HTTP/1.0 200 OK\r\n\r\n<html><body>Boas vindas! Autenticação realizada!.</body></html>\r\n\r\n"
        else:
            response = "HTTP/1.0 401 Unauthorized\r\n\r\n<html><body>Acesso negado</body></html>\r\n\r\n"

        client.sendall(response.encode())
        client.shutdown(socket.SHUT_WR)
        client.close()
except:
    server.close()
