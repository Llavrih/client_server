import socket
import time


def receive_file(host, port, default_filename):
    filename = input(
        f"Enter filename to save (or press enter to use '{default_filename}'): "
    )
    if not filename:
        filename = default_filename

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        start_time = time.time()  # Start the timer

        # Receiving data from the server
        received_bytes = 0
        with open(filename, "wb") as file:
            while True:
                data = s.recv(1024)
                if not data:
                    break
                file.write(data)
                received_bytes += len(data)

        end_time = time.time()  # End the timer

        # Calculate the bandwidth
        duration = end_time - start_time
        bandwidth = (received_bytes / duration) / (1024 * 1024)  # Bandwidth in MB/s

        print(f"File {filename} received successfully.")
        print(f"Transfer duration: {duration:.2f} seconds")
        print(f"Bandwidth: {bandwidth:.2f} MB/s")


if __name__ == "__main__":
    host = "192.168.75.165"  # Replace with the server's IP address
    port = 12346
    default_filename = "received_carina_nebula.zip"  # Default name of the file to be saved on the client
    receive_file(host, port, default_filename)
