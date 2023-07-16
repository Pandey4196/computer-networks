import socket
HOST = '127.0.0.1'
PORT = 12344
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Server listening on {HOST}:{PORT}")
client_socket, client_address = server_socket.accept()
print(f"Client connected from {client_address[0]}:{client_address[1]}")
while True:
    message = client_socket.recv(1024).decode()
    print(f"Client: {message}")
    if message.lower() == "bye" or message.lower() == "exit":
        break
    else:
        response = input("Server: ")
        client_socket.send(response.encode())
client_socket.close()
server_socket.close()
print("Server terminated")