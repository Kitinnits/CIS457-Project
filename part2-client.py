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
                print("\nServer disconnected.")
                break

            print(f"\nServer: {data.decode()}")
            print("You: ", end="", flush=True)

        except OSError:
            break


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(f"Connected to {host}:{port}")

    sender = threading.Thread(
        target=send_messages,
        args=(client_socket,),
        daemon=True
    )

    sender.start()

    receive_messages(client_socket)

    client_socket.close()
    print("Client is closed.")


if __name__ == "__main__":
    main()