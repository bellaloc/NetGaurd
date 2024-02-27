import matplotlib.pyplot as plt
from threading import Thread

def visualize_data(packet):
    """
    Function to visualize packet data.
    
    This is a placeholder function. You can implement actual visualization logic here
    based on the packet data received.
    """
    # Example visualization logic
    print("Visualizing packet data...")
    print("Source IP:", packet.src)
    print("Destination IP:", packet.dst)
    print("Packet Summary:", packet.summary())
    
    # Extracting packet information
    src_ip = packet.src
    dst_ip = packet.dst
    src_port = packet.sport
    dst_port = packet.dport
    protocol = packet.payload.name
    
    # Function to create and show the plot
    def create_plot():
        try:
            # Plotting packet information
            fig, axs = plt.subplots(2, 1, figsize=(8, 8))
            
            # Bar plot for IP addresses
            axs[0].bar(['Source IP', 'Destination IP'], [src_ip, dst_ip], color=['blue', 'green'])
            axs[0].set_ylabel('IP Address')
            axs[0].set_title('IP Address Information')
            
            # Pie chart for port information
            port_labels = ['Source Port', 'Destination Port']
            port_sizes = [src_port, dst_port]
            axs[1].pie(port_sizes, labels=port_labels, autopct='%1.1f%%', startangle=140)
            axs[1].set_title('Port Information')
            
            plt.tight_layout()

            # Display the plot
            plt.show()
        except Exception as e:
            print("Error occurred while plotting:", e)

    # Create and show the plot in a separate thread to avoid blocking the main thread
    plot_thread = Thread(target=create_plot)
    plot_thread.start()
