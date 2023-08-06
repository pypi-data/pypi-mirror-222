import socket
import sys

#HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

def send_message(HOST,PORT,data):
    data = " ".join(sys.argv[1:])
    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        print("Sent:     {}".format(data))
        print("Received: {}".format(received))

#send_message("localhost",9999,data)

# import socket

# def send_message(host, port, message):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#         client_socket.connect((host, port))
#         client_socket.sendall(message.encode())
#         response = client_socket.recv(1024)
#         print(f"Server response: {response.decode()}")

# Now, let's package these modules and upload to PyPI.

# Create a directory for the package and place the server.py and client.py files in it.

# Create a setup.py file in the root directory of your package with the following content: