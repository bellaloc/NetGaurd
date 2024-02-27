# NetGuard: Network Intrusion Detection System (NIDS)

NetGuard is a simple yet effective Network Intrusion Detection System (NIDS) implemented in Python using the Tkinter GUI toolkit and the Scapy library for packet sniffing. It provides real-time monitoring and analysis of network traffic to detect potential intrusions or anomalies.

## Features

- Start/Stop packet sniffing with the click of a button.
- Real-time analysis of network packets to detect anomalies.
- Basic machine learning-based anomaly detection (packet size threshold).
- Alert notifications for detected anomalies.
- Simple and user-friendly graphical user interface (GUI).

## Prerequisites

- Python 3.x
- Flask
- Scapy
- Additional Python libraries for packet analysis, visualization, and SIEM integration (dependencies specified in requirements.txt)

## Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/bellaloc/netguard.git
    ```

2. cd NetGuard
  - Set up a virtual environment (optional but recommended): 

    python3 -m venv venv

    Activate the virtual environment:

    # For macOS/Linux
        source venv/bin/activate

     # For Windows
        venv\Scripts\activate

# Install the required dependencies:

pip install -r requirements.txt


## Usage

1. Navigate to the project directory:

    cd netguard

    # cli 
    
    Set the FLASK_APP environment variable to main.py:
    ```
    ```

2. Run the main_gui.py script:

    ```
    python main_gui.py
    ```
    # Run the Flask application:

    flask run


1. Open a web browser and navigate to http://127.0.0.1:5000 to access the NetGuard web interface.
2. Click on the "Start Sniffing" button to begin packet sniffing and intrusion detection.
3. Monitor the console output for real-time updates on detected network activities.
4. To stop packet sniffing, click on the "Stop Sniffing" button.


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The Scapy development team for providing the powerful packet manipulation capabilities.
- The Tkinter development team for creating the GUI toolkit used in this project.
- [OpenAI](https://openai.com) for providing guidance and support.

## Contact

For any inquiries or feedback, please contact [your_email@example.com](mailto:your_email@example.com).
