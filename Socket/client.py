import socket

def client():
    print("Please enter a target host and target port")
    target_host = input("Target host: ")

    while True:
        try:
            target_port = int(input("Target port: "))
            if 1 <= target_port <= 65535:
                break
            else:
                print("Please enter a valid port (between 1 and 65535).")
        except ValueError:
            print("Please enter a valid integer for the port.")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((target_host, target_port))

    message = input(">> ")
    while message.lower() != "quit":
        if message == "":
            print("Don't send an empty message.")
        else:
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
            print("Response from target: " + str(data))
        message = input(">> ")

    client_socket.close()

client()
