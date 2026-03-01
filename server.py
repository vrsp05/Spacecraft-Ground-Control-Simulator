import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5050))
server_socket.listen(1)

print("[SPACECRAFT] Systems online. Waiting for Ground Control...")
conn, addr = server_socket.accept()
print(f"[SPACECRAFT] Linked to Ground Control at {addr}")

# The Command Loop
active_mission = True
while active_mission:
    # Receive the command
    data = conn.recv(1024).decode('utf-8')
    
    if not data:
        break # Handle unexpected disconnect
    
    print(f"[SPACECRAFT] Processing: {data}")

    # Simple GNC Command Logic
    if data == "GET_STATUS":
        response = "STATUS: ALL SYSTEMS NOMINAL. FUEL: 85%"
    elif data == "THRUST_ON":
        response = "ACTION: MAIN ENGINES IGNITED."
    elif data == "EXIT":
        response = "SYSTEM: CLOSING MISSION LINK. GOODBYE."
        active_mission = False
    else:
        response = "ERROR: UNKNOWN COMMAND."

    # Send the response back
    conn.send(response.encode('utf-8'))

print("[SPACECRAFT] Mission link closed.")
conn.close()
server_socket.close()