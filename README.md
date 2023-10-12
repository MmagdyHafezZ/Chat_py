
# Chat Application

This repository contains the code for a simple chat server and client written in Python. The server can handle multiple client connections concurrently and supports features like private messaging, user listing, and dynamic username handling. A batch file for easy startup of the server and client is also included.

## Features

- Multi-client support via threading
- Real-time communication between server and clients
- Private messaging between users
- Active user listing
- Username changing support
- Connection management to prevent duplicate logins from the same IP

## Prerequisites

- Python 3.x
- Basic knowledge of socket programming

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installation

1. Clone the repository to your local machine:
   ```
   https://github.com/MmagdyHafezZ/Chat_py.git
   ```
2. Navigate to the directory:
   ```
   cd Chat_py
   ```

### Usage

You can start the server and client using the included batch file:

1. Double-click the `start_chat_app.bat` file.
   This will run the server and client scripts automatically. The server script will start in the background, and the client script will run after a short delay.

Alternatively, you can start the server and clients manually:

1. Start the server:
   ```
   python server.py
   ```
   The server will start and listen for incoming connections.

2. Run the client script in a separate terminal:
   ```
   python client.py
   ```
   Follow the prompts to enter your username and connect to the chat server.

3. Repeat step 2 for multiple clients, as needed.

## Commands

- `/list` - Lists all active users.
- `/pm <username> <message>` - Sends a private message to the specified user.
- `/changeusername <newusername>` - Changes your current username if the new one is available.

## Batch File Usage

The repository contains a batch file named `start_chat_app.bat` for Windows users, which simplifies the process of starting the server and client. 

When you run this batch file, it performs the following actions:

1. Starts the server script (`Server_group.py`) in the background.
2. Waits for 2 seconds to ensure the server is up and running.
3. Starts the client script (`Client_Groups.py`).

To use the batch file, simply double-click on it, or open a command prompt in the project's directory and run:
```
start_chat_app.bat
```

## Contributing

```
TheOnlyYoussef
```

## Acknowledgments

- Inspiration from ENSF 461 networking application class at University of Calgary

---

