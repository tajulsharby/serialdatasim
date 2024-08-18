import random
import time
import serial
from datetime import datetime
import serial.tools.list_ports

def list_virtual_com_ports():
    ports = serial.tools.list_ports.comports()
    virtual_ports = [port.device for port in ports if "serial port emulator" in port.description.lower()]
    return virtual_ports

def generate_data_line(km_pipeline):
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime('%H:%M:%S')
    northing1 = random.uniform(1000, 9999)
    northing2 = random.uniform(1000, 9999)
    depth = random.uniform(10, 100)
    random_value = round(random.uniform(1000, 9999), 4)
    
    data_line = f"{current_date},{current_time},{northing1},{northing2},{depth},{random_value},{km_pipeline:.1f}"
    return data_line

def start_simulation(write_port, baud_rate, data_frequency):
    ser_write = serial.Serial(write_port, baud_rate)
    km_pipeline = 0.0

    try:
        while True:
            data_line = generate_data_line(km_pipeline)
            ser_write.write(data_line.encode('utf-8') + b'\n')
            print(f"Sent to {write_port}: {data_line}")
            
            km_pipeline += 0.1
            time.sleep(data_frequency)
    except KeyboardInterrupt:
        print("Simulation stopped.")
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
