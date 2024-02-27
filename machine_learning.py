def detect_anomaly(packet):
    # Example: Detect anomaly if packet size exceeds a threshold
    if len(packet) > 1500:  # Example threshold: 1500 bytes
        return True
    else:
        return False
