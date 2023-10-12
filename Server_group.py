from socket import *
import threading

serverPort = 80
serverSocket = socket(AF_INET, SOCK_STREAM)
print("Socket created")
serverSocket.bind(("", serverPort))
print("Socket bound to port")
users_dict = {}
connected_ips = []

def handle_client(connectionSocket, addr):
    set_name = True
    name = ""

    while True:
        try:
            data = connectionSocket.recv(1024)
            if not data:
                break

            if set_name:
                name = data.decode()
                users_dict[connectionSocket] = name
                set_name = False
                continue

            message = data.decode()

            if message.startswith('/'):
                command = message.split(" ")[0]

                if command == "/list":
                    active_users = ", ".join(users_dict.values())
                    send_pri(f"active users: {active_users}", connectionSocket)
                    continue

                # Add other commands here
                elif command == "/pm":
                    parts = message.split(" ", 2)
                    if len(parts) < 3:
                        send_pri("Invalid format for private message. Use /pm <username> <message>", connectionSocket)
                        continue

                    target_user, pm_message = parts[1], parts[2]
                    for socket, username in users_dict.items():
                        print(username)
                        if username == target_user:
                            socket.send(f"Private message from {name}: {pm_message}".encode())
                            break
                    else:
                        send_pri("User not found.", connectionSocket)
                        continue

                elif command == "/changeusername":
                    new_name = message.split(" ")[1]
                    if new_name in users_dict.values():
                        send_message(f"{name} tried to change their username to {new_name} but it was already in use.", connectionSocket)
                    else:
                        users_dict[connectionSocket] = new_name
                        send_message(f"{name} changed their username to {new_name}", connectionSocket)

            else:
                print(f"Received message from {name}: {message}")
                send_message(f"{name}: {message}", connectionSocket)

        except Exception as e:
            print(str(e))
            break

    del users_dict[connectionSocket]
    connectionSocket.close()
    print(f"Connection closed with {addr}")



def send_message(message, this_connection):
    for connection in users_dict.keys():
        if connection == this_connection:
            continue
        try:
            connection.send(message.encode())
        except Exception as e:
            print(f"Error sending message to {users_dict[connection]}: {str(e)}")

def send_pri(message, His_connection):
    for connection in users_dict.keys():
        try:
            if connection == His_connection:
                connection.send(message.encode())
        except Exception as e:
            print(f"Error sending message to {users_dict[connection]}: {str(e)}")

            

while True:
    serverSocket.listen(5)
    connectionSocket, addr = serverSocket.accept()
    print("Connection established with: ", addr)

    # # Check if IP already connected
    # if addr[0] in connected_ips:
    #     message = "IP address already connected"
    #     print("Already connected: ", addr[0])
    #     connectionSocket.send(message.encode())
    #     connectionSocket.close()
    #     continue

    # Add the IP to the list
    connected_ips.append(addr[0])

    # Send a preliminary response to the client to expect a username
    connectionSocket.send("200".encode())

    # Create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
    client_thread.start()
