# NC Spacecraft-Ground Control Link (TCP Simulator)

This project simulates a mission-critical communication link between a Spacecraft (Server) and a Ground Control Station (Client). It uses Python’s socket library to implement a reliable TCP connection. The goal of this software is to demonstrate the fundamentals of networking required for GNC (Guidance, Navigation, and Control) engineering, specifically focusing on command parsing, telemetry retrieval from onboard storage, and robust connection management.

## Instructions for Build and Use

Steps to build and/or run the software:

1. **Clone the Repository:** Download the server.py, client.py, and mission_log.txt files into the same directory on your local machine.
2. **Prepare the Onboard Memory:** Ensure the mission_log.txt file contains at least a few lines of simulated telemetry data (e.g., timestamps, fuel levels, and system status).
3. **Open Two Terminals:** You will need two separate terminal windows or command prompts to simulate the two distinct hardware systems.

Instructions for using the software:

1. **Initialize the Spacecraft:** In the first terminal, run python server.py. The spacecraft computer will enter a "Standby" mode and begin listening for signals.
2. **Establish the Link:** In the second terminal, run python client.py. You should see a "Connection Established" message in both terminals.
3. **Execute Commands:** From the Ground Control (Client) terminal, enter commands such as GET_STATUS, THRUST_ON, or READ_LOG to interact with the spacecraft.
4. **Terminate the Session:** Type EXIT to conclude the current mission. Note that the spacecraft remains in orbit (the server stays running) and will wait for a new connection.

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* **Python 3.10+:** The project utilizes standard libraries including socket and sys.
* **Standard Socket Library:** Used for establishing the TCP/IP stack (AF_INET, SOCK_STREAM).
* **VS Code or similar IDE:** Recommended for side-by-side terminal debugging.
* **OS:** Tested on Windows 11/Linux using the localhost loopback address (127.0.0.1).

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Socket Programming in Python (Guide](https://realpython.com/python-sockets/)
* [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)
* [Python Socket Programming Tutorial](https://www.youtube.com/watch?v=3QiPPX-KeSc)
* [Socket module in python](https://pythontic.com/modules/socket/introduction)
* [Socket Programming in Python](https://www.geeksforgeeks.org/python/socket-programming-python/)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] **UDP Telemetry Stream:** Implement a secondary high-frequency UDP socket for real-time sensor data simulation (to contrast with TCP command reliability).
* [ ] **Data Serialization:** Use the struct or pickle library to send raw binary GNC data packets rather than simple strings.
* [ ] **GUI Dashboard:** Create a graphical interface for the Ground Control client using Tkinter or PyQT to visualize fuel levels and thrust status.
