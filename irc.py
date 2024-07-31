
import socket
import threading
#irssi -c localhost -p 6667
#nc localhost 6667

# Configurações do servidor IRC
HOST = '0.0.0.0'
PORT = 6667
BUFFER_SIZE = 1024

# Lista para manter o controle das conexões dos clientes
clients = []

# Função para lidar com mensagens de clientes
def handle_client(client_socket, client_address):
    client_socket.send(b"Bem-vindo ao servidor IRC!\n")
    
    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE)
            if message:
                broadcast(message, client_socket)
            else:
                remove_client(client_socket)
                break
        except:
            continue

# Função para enviar mensagens para todos os clientes conectados
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                remove_client(client)

# Função para remover um cliente da lista de clientes
def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

# Função principal para iniciar o servidor IRC
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    print(f"Servidor IRC iniciado em {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"Conexão estabelecida com {client_address}")

        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()
print("\x1bc\x1b[47;34m")
if __name__ == "__main__":
    main()
