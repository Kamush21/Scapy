import socket

from scapy.all import Raw, StreamSocket

HOST = "127.0.0.1"
PORT = 12345

MESSAGE = (
    "Dear Steel Cat! This is no attack, "
    "it's my humster Pinkie you should track"
)


def main() -> None:
    try:
        with socket.create_connection((HOST, PORT), timeout=5) as sock:
            stream = StreamSocket(sock, Raw)
            stream.send(Raw(load=MESSAGE.encode("utf-8")))

        print(f"Message sent to {HOST}:{PORT}")
        print(f"Payload: {MESSAGE}")

    except ConnectionRefusedError:
        print(f"Connection refused: is a TCP server listening on {PORT}?")
        raise SystemExit(1)
    except TimeoutError:
        print("Connection timed out.")
        raise SystemExit(1)


if __name__ == "__main__":
    main()

