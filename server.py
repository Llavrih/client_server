import socket


def server():
    host = "192.168.75.165"  # Server's IP address
    port = 12346
    default_filename = "carina_nebula.zip"  # Default file name

    # Prompt for a filename, use default if no input is given
    filename = input(f"Enter filename (or press enter to use '{default_filename}'): ")
    if not filename:
        filename = default_filename

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")

            # Open and read the file
            try:
                with open(filename, "rb") as file:
                    file_data = file.read()

                # Send the file data
                conn.sendall(file_data)
                print(f"File {filename} sent successfully.")
            except FileNotFoundError:
                print(f"Error: File '{filename}' not found.")


if __name__ == "__main__":
    server()
