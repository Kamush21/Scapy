import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)

    print(f"Listening on {HOST}:{PORT}")

    conn, addr = server.accept()

    with conn:
        print(f"Connection from {addr}")
        data = conn.recv(4096)
        print("Received:", data.decode("utf-8"))
