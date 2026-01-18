from scapy.all import sniff, IP, TCP, UDP, ICMP
from scapy.config import conf
from datetime import datetime

# ---------------- ETHICAL WARNING ----------------
print("=" * 60)
print("Network Packet Analyzer - Educational Use Only")
print("Use this tool only on authorized networks.")
print("=" * 60)

# ---------------- USER SETTINGS ----------------
PACKET_LIMIT = 20
PROTOCOL_FILTER = "ALL"   # TCP / UDP / ICMP / ALL
SUSPICIOUS_SIZE = 1000    # bytes

log_file = "packet_log.txt"

# Display Interface Name
print(f"Using Interface: {conf.iface}")
print(f"Protocol Filter: {PROTOCOL_FILTER}")
print("=" * 60)

packet_count = 0

def analyze_packet(packet):
    global packet_count
    packet_count += 1

    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "OTHER"
        src_port = "-"
        dst_port = "-"

        # Protocol Detection
        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        elif ICMP in packet:
            protocol = "ICMP"

        # Apply protocol filter
        if PROTOCOL_FILTER != "ALL" and protocol != PROTOCOL_FILTER:
            return

        payload_size = len(packet[IP].payload)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        alert = ""
        if payload_size > SUSPICIOUS_SIZE:
            alert = "⚠ Suspicious Packet Size Detected"

        # ICMP Detection (Ping)
        if protocol == "ICMP":
            alert = "ICMP Packet (Ping Detected)"

        output = (
            f"\nPacket #{packet_count}\n"
            f"Time: {timestamp}\n"
            f"Source IP: {src_ip}\n"
            f"Destination IP: {dst_ip}\n"
            f"Protocol: {protocol}\n"
            f"Source Port: {src_port}\n"
            f"Destination Port: {dst_port}\n"
            f"Payload Size: {payload_size} bytes\n"
            f"{alert}\n"
            + "-" * 55
        )

        print(output)

        with open(log_file, "a") as file:
            file.write(output)

# ---------------- START SNIFFING ----------------
sniff(count=PACKET_LIMIT, prn=analyze_packet)
