import socket
import threading
import queue

def scan_ports(host, port_queue, open_ports):
    while not port_queue.empty():
        port = port_queue.get()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is open")
            sock.close()
        except:
            pass

def main():
    host = input("Enter the target host: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    port_queue = queue.Queue()
    for port in range(start_port, end_port + 1):
        port_queue.put(port)

    open_ports = []
    threads = []

    for _ in range(100):
        t = threading.Thread(target=scan_ports, args=(host, port_queue, open_ports))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"\nOpen ports on {host}: {open_ports}")

if __name__ == "__main__":
    main()