import socket

# Setup the "Radio Frequency"
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5050))
server_socket.listen(1)

print("[SPACECRAFT] Systems online. Standby for Ground Control...")

# The Outer Loop (Keeps the server running after disconnects)
while True:
    print("\n[SPACECRAFT] Waiting for a new connection...")
    conn, addr = server_socket.accept()
    print(f"[SPACECRAFT] Linked to Ground Control at {addr}")

    # The Command Loop (Handles the current session)
    active_mission = True
    while active_mission:
        try:
            # Receive the command
            data = conn.recv(1024).decode('utf-8')
            
            if not data:
                break # Client crashed or disconnected abruptly
            
            print(f"[SPACECRAFT] Processing: {data}")

            # GNC Command Logic
            if data == "GET_STATUS":
                response = "STATUS: ALL SYSTEMS NOMINAL. FUEL: 85%"
            
            elif data == "READ_LOG":
                try:
                    with open("mission_log.txt", "r") as file:
                        lines = file.readlines()
                        # STRETCH CHALLENGE: Reading from local file
                        response = f"[LOG DATA]: {lines[-1].strip()}"
                except FileNotFoundError:
                    response = "ERROR: MISSION_LOG.TXT NOT FOUND ON SPACECRAFT."
            
            elif data == "THRUST_ON":
                response = "ACTION: MAIN ENGINES IGNITED."
            
            elif data == "EXIT":
                response = "SYSTEM: CLOSING MISSION LINK. GOODBYE."
                active_mission = False # Breaks the Command Loop
            
            else:
                response = "ERROR: UNKNOWN COMMAND."

            # Send the response back
            conn.send(response.encode('utf-8'))
            
        except ConnectionResetError:
            print("[SPACECRAFT] Ground Control lost signal unexpectedly.")
            break

    # Close the specific connection, but the "while True" keeps the server alive!
    conn.close()
    print(f"[SPACECRAFT] Mission with {addr} concluded. Returning to standby.")