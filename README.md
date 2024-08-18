# Serial Port Data Simulator

## Overview

**Serial Port Data Simulator** is a Python-based application designed to simulate data streams through virtual COM ports. This tool is particularly useful for testing applications that need to read from COM ports without requiring physical devices. It allows you to configure a virtual COM port to send simulated data, which can then be read by another application.

## Features

- **Virtual COM Port Support**: Filters and lists only virtual COM ports labeled as "serial port emulator."
- **Configurable Data Stream**: Generates data in the following format: `[current date],[current time],[simulated northing value 1],[simulated northing value 2],[simulated depth value],[simulated 4-digit random value with 4 decimal points],[kilometer pipeline which starts from 0.0]`.
- **Customizable Baud Rate**: Default baud rate is 9600, but it can be configured.
- **Adjustable Data Frequency**: Default frequency is 1 second, adjustable based on user input.
- **Write-Only Mode**: The application only opens the selected virtual COM port for writing, allowing another application to open and read from the paired virtual COM port.

## Requirements

- Python 3.x
- `pyserial` Python package
- **Null-modem emulator (com0com)**: Required to create virtual COM ports.

## Installation

1. **Install the Null-modem emulator (com0com)**:
    - Download and install com0com from the official [source](https://sourceforge.net/projects/com0com/).

2. **Clone the repository**:
    ```bash
    git clone https://github.com/tajulsharby/serialdatasim.git
    cd serialdatasim
    ```

3. **Install the required Python packages**:
    ```bash
    pip install pyserial
    ```

4. **Ensure you have virtual COM ports created by com0com**:
    - The virtual COM ports should be labeled as "serial port emulator" in your Device Manager.

## Usage

1. **Run the simulator**:
    ```bash
    python serial_port_data_simulator.py
    ```

2. **Follow the prompts**:
    - Select the virtual COM port to write to by number.
    - Enter the baud rate (default is 9600).
    - Enter the data frequency in seconds (default is 1 second).

3. **Stop the simulation**:
    - Press `Ctrl + C` to stop the simulation at any time.

## Example Output

```
Available Virtual COM Ports:
1: COM4
2: COM5
Select the virtual COM port to write to by number: 1
Enter baud rate (default is 9600): 9600
Enter data frequency (default is 1 second): 2
Sent to COM4: 2024-08-18,12:34:56,1234.5678,2345.6789,50.5,1234.5678,0.0
...
```

## Contributing

If you have suggestions for improving this project, feel free to submit a pull request or open an issue. Contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Author

- **TJ S**  
  - [GitHub](https://github.com/tajulsharby)  
  - [LinkedIn](https://www.linkedin.com/in/tajulsharby/)

---

You can now replace the content in your `README.md` file with this updated version. Let me know if there’s anything else you need!