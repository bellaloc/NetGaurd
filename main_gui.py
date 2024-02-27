import tkinter as tk
from tkinter import messagebox
from scapy.all import sniff
from packet_analysis import analyze_packet
from visualization import visualize_data
from integration import integrate_with_SIEM
import platform
import sys

class NetGuardGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NetGuard: Network Intrusion Detection System")
        self.geometry("400x200")

        self.label = tk.Label(self, text="NetGuard: Network Intrusion Detection System", font=("Arial", 14))
        self.label.pack(pady=10)

        self.start_button = tk.Button(self, text="Start Sniffing", command=self.start_sniffing)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(self, text="Stop Sniffing", command=self.stop_sniffing, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

    def start_sniffing(self):
        # Start sniffing packets
        messagebox.showinfo("Info", "Sniffing started...")
        sniff(prn=self.analyze_and_visualize_packet, filter="tcp", count=10)
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_sniffing(self):
        # Stop sniffing packets
        messagebox.showinfo("Info", "Sniffing stopped.")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def analyze_and_visualize_packet(self, packet):
        # Analyze each packet
        analyze_packet(packet)
        
        # Visualize data
        visualize_data(packet)
        
        # Integrate with SIEM
        integrate_with_SIEM(packet)

def check_macos_version():
    # Get macOS version information
    macos_version = platform.mac_ver()[0]

    # Convert macOS version to tuple for comparison
    version_parts = macos_version.split('.')
    version_tuple = tuple(map(int, version_parts))

    # Check if macOS version meets the requirement
    required_version = (12, 1207)  # macOS 12 (1207) or later required
    if version_tuple >= required_version:
        return True
    else:
        print(f"Warning: macOS {macos_version} detected. "
              f"This script requires macOS {required_version[0]} ({required_version[1]}) or later.")
        return False

def sniff_packets():
    if not check_macos_version():
        sys.exit(1)  # Exit if macOS version is not compatible

    # Try to sniff packets
    try:
        sniff(count=10)  # Example: sniffing 10 packets
        print("Packet sniffing completed successfully.")
    except Exception as e:
        print(f"Error occurred while sniffing packets: {e}")

def main():
    sniff_packets()

if __name__ == "__main__":
    app = NetGuardGUI()
    app.mainloop()
