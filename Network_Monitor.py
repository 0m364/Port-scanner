import psutil
from scapy.all import ARP, Ether, srp

def print_network_stats():
    # Get network io statistics
    net_io = psutil.net_io_counters()

    print(f"Bytes Sent: {net_io.bytes_sent}")
    print(f"Bytes Received: {net_io.bytes_recv}")

def scan_network():
    # Use the ARP protocol to discover local network devices
    arp = ARP(pdst="192.168.1.0/24")  # Replace with your network
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    # Print out the IP and MAC address of each responding device
    for sent, received in result:
        print(f"Device detected: {received.psrc} ({received.hwsrc})")

# Print network stats and scan the network
print_network_stats()
scan_network()
