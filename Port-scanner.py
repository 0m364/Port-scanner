import socket
import threading

def port_scan(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def scan_range(target, start_port, end_port):
    for port in range(start_port, end_port+1):
        if port_scan(target, port):
            print(f"Port {port}: Open")

def main():
    target = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    threads = []
    for i in range(start_port, end_port+1, 100):
        end = min(i+100, end_port+1)
        thread = threading.Thread(target=scan_range, args=(target, i, end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Scanning complete.")

if __name__ == '__main__':
    main()

