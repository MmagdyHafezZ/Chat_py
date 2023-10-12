import socket
import threading
import os

SERVER_ADDRESS = ("10.14.122.21", 12000)
messages = []


def establish_connection():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect(SERVER_ADDRESS)
        return True
    except socket.error:
        print("Server not found. Please ensure the server is running and try again.")
        return False

def send_username():
    username = input("Enter your name: ")
    client_socket.send(username.encode("utf-8"))
    
    try:
        server_res = client_socket.recv(1024).decode("utf-8")
        if server_res == "Duplicated username":
            print("Username already exists. Please choose a different one.")
            client_socket.close()
            return False
        else:
            print(f"Connected to server as {username}.")
            print("You can start typing your messages.")
            return True
    except ConnectionError:
        print("\nConnection Error occurred.")
        return False

def print_messages():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print all buffered messages
    for msg in messages:
        print(msg)
    print("\n You: ", end='', flush=True)  # Show the prompt without waiting for newline

def read_messages():
    global messages
    while True:
        try:
            server_message = client_socket.recv(1024).decode("utf-8")
            if not server_message or server_message.lower() == "server closed":
                messages.append("\nServer has been closed. Exiting chat.")
                break
            messages.append(server_message)
            print_messages()
        except ConnectionError:
            messages.append("\nConnection Error occurred.")
            print_messages()
            break

def write_messages():
    global messages
    while True:
        print_messages()
        client_message = input()
        if not client_message:
            continue
        messages.append("You: " + client_message)
        if client_message.lower() == "bye":
            messages.append("You exited the chat.")
            exit(0)
            break
        try:
            client_socket.send(client_message.encode("utf-8"))

        except ConnectionError:
            messages.append("\nUnable to send message. Connection Error occurred.")

def main():
    print("Type your messages, press enter to send them.")
    print("Type '/list' to see the list of active users.")
    print("Type '/pm <username> <message>' to send a private message to a user.")
    print("Type '/changeusername <newusername>' to change your username.")
    print("Type 'bye' whenever you want to leave the chat.\n")
    
    if not establish_connection():
        return
    
    if not send_username():
        return
    
    read_thread = threading.Thread(target=read_messages, daemon=True)
    write_thread = threading.Thread(target=write_messages, daemon=True)
    
    read_thread.start()
    write_thread.start()
    
    read_thread.join()
    write_thread.join()

    client_socket.close()

if __name__ == "__main__":
    main()
