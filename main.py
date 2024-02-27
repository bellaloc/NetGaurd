from scapy.all import sniff
from packet_analysis import analyze_packet
from visualization import visualize_data
from integration import integrate_with_SIEM
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# Route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Function to start packet sniffing
def start_sniffing():
    print("Sniffing started...")
    try:
        sniff(prn=analyze_and_visualize_packet, filter="tcp", count=10)
    except KeyboardInterrupt:
        stop_sniffing()

# Function to analyze and visualize packet, and send updates to client
def analyze_and_visualize_packet(packet):
    # Analyze packet
    analysis_result = analyze_packet(packet)
    
    # Visualize data
    visualization_result = visualize_data(packet)
    
    # Integrate with SIEM
    siem_integration_result = integrate_with_SIEM(packet)
    
    # Send updates to client via WebSocket
    socketio.emit('packet_analysis', {
        'analysis_result': analysis_result,
        'visualization_result': visualization_result,
        'siem_integration_result': siem_integration_result
    })

# WebSocket event handler for starting packet sniffing
@socketio.on('start_sniffing')
def start_sniffing_ws():
    start_sniffing()

if __name__ == '__main__':
    # Run Flask app with SocketIO support
    socketio.run(app, debug=True)
