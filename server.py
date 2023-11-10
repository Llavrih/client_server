import socket


def server():
    host = "192.168.75.165"  # Server's IP address
    port = 12346
    filename = "carina_nebula.zip"  # Name of the file to send

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")

            # Open and read the file
            with open(filename, "rb") as file:
                file_data = file.read()

            # Send the file data
            conn.sendall(file_data)

            print(f"File {filename} sent successfully.")


if __name__ == "__main__":
    server()
