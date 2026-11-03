import socket
import threading

host = 'localhost'
port = 12345


def send_messages(sock):
    while True:
        message = input("You: ")

        if message.lower() == "quit":
            break

        try:
            sock.sendall(message.encode())
        except OSError:
            break

    try:
        sock.shutdown(socket.SHUT_RDWR)
    except OSError:
        pass


def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)

            if not data:
                print("\nClient disconnected.")
                break

            print(f"\nClient: {data.decode()}")
            print("You: ", end="", flush=True)

        except OSError:
            break


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server is waiting on {host}:{port}")

    client_socket, address = server_socket.accept()
    print(f"Connected to {address}")

    sender = threading.Thread(
        target=send_messages,
        args=(client_socket,),
        daemon=True
    )

    sender.start()

    receive_messages(client_socket)

    client_socket.close()
    server_socket.close()
    print("Server is closed.")


if __name__ == "__main__":
    main()