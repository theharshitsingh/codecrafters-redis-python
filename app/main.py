# Uncomment this to pass the first stage
import socket


def main():
    print("Logs from your program will appear here!")
    pong = "+PONG\r\n"

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, addr = server_socket.accept()  # wait for client

    with conn:
        while True:
            data = conn.recv(1024)
            print(f"Received: {data}")  # Debugging: log received data
            if not data:
                print("No data received, closing connection.")
                break  # Exit the loop if no data is received, indicating the client has closed the connection
            data = data.strip()
            if data == b'PING':
                print("Sending PONG")
                conn.send(pong.encode())
            else:
                print(f"Unexpected data received: {data}")

if __name__ == "__main__":
    main()
