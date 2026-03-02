import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5050))
print("[GROUND CONTROL] Connection established.")

print("Available Commands: GET_STATUS, READ_LOG, THRUST_ON, EXIT")

while True:
    # Get user input
    command = input("Enter Command > ").upper()
    
    # Send the command
    client_socket.send(command.encode('utf-8'))
    
    # Get the spacecraft's reply
    response = client_socket.recv(1024).decode('utf-8')
    print(f"[SPACECRAFT REPLY]: {response}")
    
    # Break the loop if we sent EXIT
    if command == "EXIT":
        break

client_socket.close()
print("[GROUND CONTROL] Terminal offline.")