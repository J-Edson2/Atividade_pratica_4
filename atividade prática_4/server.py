import socket
import threading
import datetime

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    if request == 'd':
        response = datetime.date.today().strftime('%Y-%m-%d')
    elif request == 'h':
        response = datetime.datetime.now().strftime('%H:%M:%S')
    elif request == 'dh':
        response = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    else:
        response = "Opção inválida."
    client_socket.send(response.encode('utf-8'))
    client_socket.close()

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Servidor pronto para receber conexões...")

    while True:
        client_socket, addr = server_socket.accept()
        print("Conexão recebida de:", addr)
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    main()