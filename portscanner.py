import socket
from IPy import IP

# Function to check if IP or domain is valid
def check_ip(address):
    try:
        IP(address)
        return address
    except ValueError:
        return socket.gethostbyname(address)

# Function to scan a specific port
def scan_port(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)  # Timeout of 0.5 seconds
        connection = sock.connect_ex((target, port))
        if connection == 0:  # If connection is successful, port is open
            print(f"Port {port} is open")
        sock.close()
    except socket.error:
        print(f"Couldn't connect to {target}")
        return

# Function to scan all ports within a given range
def scan(target, start_port, end_port):
    target_ip = check_ip(target)
    print(f"\nStarting scan on {target_ip}...")
    
    for port in range(start_port, end_port + 1):
        scan_port(target_ip, port)

# Main function to interact with the user
def main():
    print("=== Simple Python Port Scanner ===")
    target = input("Enter target IP address or domain: ")
    start_port = int(input("Enter starting port (default 1): ") or 1)
    end_port = int(input("Enter ending port (default 1024): ") or 1024)
    
    scan(target, start_port, end_port)

# Corrected line
if __name__ == "__main__":
    main()
