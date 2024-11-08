Here is a Python program that performs an aggressive port scan on a target host

This program prompts the user for the target host and port range to scan. 
It creates a queue of ports to scan and spawns 100 threads to perform the port scanning concurrently. 
Each thread takes a port from the queue, tries to connect to it using a timeout of 1 second, and adds the open port to the open_ports list if the connection succeeds. 
Finally, it prints out the list of open ports found.

Please note that port scanning is a form of ethical hacking and should only be done with explicit permission and for educational purposes. 
Scanning ports without permission is illegal and can be considered a crime.
