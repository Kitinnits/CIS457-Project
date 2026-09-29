import socket

host = 'localhost'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

print(f"Server is listening on {host}:{port}")

client_socket, address = server_socket.accept()
print(f"Connected to {address}.")

data = client_socket.recv(1024).decode()
print("Client:", data)
message = input("You: ")
client_socket.send(message.encode())

