from scapy.all import sniff
from packet_analysis import analyze_packet
from visualization import visualize_data
from integration import integrate_with_SIEM
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/start_sniffing')
def start_sniffing_route():
    start_sniffing()
    return "Sniffing started."

if __name__ == '__main__':
    app.run(debug=True)
