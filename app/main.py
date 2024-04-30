# Uncomment this to pass the first stage
import socket


def main():
    print("Logs from your program will appear here!")
    pong = "+PONG\r\n"

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    client_socket, address = server_socket.accept()

    with client_socket:
        while True:
            try:
                data = client_socket.recv(1024)
                if data:
                    client_socket.sendall(b"+PONG\r\n")
            except ConnectionResetError:
                print(f"Connection to {address} lost")

if __name__ == "__main__":
    main()
