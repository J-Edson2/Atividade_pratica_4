import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        command = input("Digite 'd' para Data, 'h' para Hora, 'dh' para Data e Hora, ou '/sair' para sair: ")
        if command == '/sair':
            break
        client_socket.send(command.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print("Resposta do servidor:", response)

    client_socket.close()

if __name__ == '__main__':
    main()