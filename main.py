from scapy.all import sniff
from packet_analysis import analyze_packet
from visualization import visualize_data
from integration import integrate_with_SIEM

def start_sniffing():
    print("Sniffing started...")
    try:
        sniff(prn=analyze_and_visualize_packet, filter="tcp", count=10)
    except KeyboardInterrupt:
        stop_sniffing()

def stop_sniffing():
    print("Sniffing stopped.")

def analyze_and_visualize_packet(packet):
    # Analyze each packet
    analyze_packet(packet)
    
    # Visualize data
    visualize_data(packet)
    
    # Integrate with SIEM
    integrate_with_SIEM(packet)

if __name__ == "__main__":
    start_sniffing()
