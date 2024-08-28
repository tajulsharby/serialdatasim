import random
import time
import serial
from datetime import datetime
import serial.tools.list_ports
import signal
import sys

def list_virtual_com_ports():
    ports = serial.tools.list_ports.comports()
    virtual_ports = [port.device for port in ports if "serial port emulator" in port.description.lower()]
    return virtual_ports

def generate_data_line(km_pipeline):
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime('%H:%M:%S')
    easting = round(random.uniform(1000, 9999), 4)
    northing = round(random.uniform(1000, 9999), 4)
    depth = round(random.uniform(10, 100), 4)
    
    # Generate a realistic heading value
    heading = f"{random.choice(['N', 'S', 'E', 'W'])}{random.randint(0, 360)}°{random.choice(['N', 'S', 'E', 'W'])}"

    # Calculate altitude as some fraction of depth (for example, half)
    altitude = round(depth * 0.5, 4)

    # Depth Compensation Control (DCC) as a value related to depth
    dcc = round(depth * random.uniform(1.0, 2.0), 4)

    # Simulated random data
    random_data_10 = round(random.uniform(1000.0000, 9999.9999), 4)
    random_data_11 = round(random.uniform(1000.0000, 9999.9999), 4)
    random_data_12 = round(random.uniform(1000.0000, 9999.9999), 4)

    data_line = f"{current_date},{current_time},{easting},{northing},{depth},{heading},{km_pipeline:.1f},{altitude},{dcc},{random_data_10},{random_data_11},{random_data_12}"
    return data_line

def start_simulation(write_port, baud_rate, data_frequency):
    ser_write = serial.Serial(write_port, baud_rate)
    km_pipeline = 0.0

    def graceful_shutdown(signal, frame):
        print("\nSimulation stopped by user.")
        ser_write.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, graceful_shutdown)

    try:
        while True:
            data_line = generate_data_line(km_pipeline)
            ser_write.write(data_line.encode('utf-8') + b'\n')
            print(f"Sent to {write_port}: {data_line}")
            
            km_pipeline += 0.5 * (data_frequency / 3600.0)  # Assuming 0.5 km per hour, scaled by frequency
            time.sleep(data_frequency)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        ser_write.close()

if __name__ == "__main__":
    virtual_ports = list_virtual_com_ports()
    if not virtual_ports:
        print("No virtual COM ports found.")
    else:
        print("Available Virtual COM Ports:")
        for i, port in enumerate(virtual_ports):
            print(f"{i + 1}: {port}")

        write_port_index = int(input("Select the virtual COM port to write to by number: ")) - 1
        write_port = virtual_ports[write_port_index]

        baud_rate_input = input("Enter baud rate (default is 9600): ")
        baud_rate = int(baud_rate_input) if baud_rate_input else 9600

        data_frequency_input = input("Enter data frequency (default is 1 second): ")
        data_frequency = float(data_frequency_input) if data_frequency_input else 1.0

        start_simulation(write_port, baud_rate, data_frequency)
