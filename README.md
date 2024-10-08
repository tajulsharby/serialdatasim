# Serial Port Data Simulator

**Author:** TJ S  
**GitHub:** [https://github.com/tajulsharby](https://github.com/tajulsharby)  
**LinkedIn:** [https://www.linkedin.com/in/tajulsharby/](https://www.linkedin.com/in/tajulsharby/)

## Overview

**Serial Port Data Simulator** is a Python-based application designed to simulate data streams through virtual COM ports. This tool is particularly useful for testing applications that need to read from COM ports without requiring physical devices. It allows you to configure a virtual COM port to send simulated data, which can then be read by another application.

## Features

- **Virtual COM Port Support**: Filters and lists only virtual COM ports labeled as "serial port emulator."
- **Configurable Data Stream**: Generates data in a format based on an underwater inspection data survey:
  ```text
  [current_date],[current_time],[easting],[northing],[depth],[heading],[kp],[altitude],[dcc],[random_data_10],[random_data_11],[random_data_12]
  ```
- **Customizable Baud Rate**: Default baud rate is 9600, but it can be configured.
- **Adjustable Data Frequency**: Default frequency is 1 second, adjustable based on user input.
- **Write-Only Mode**: The application only opens the selected virtual COM port for writing, allowing another application to open and read from the paired virtual COM port.
- **Graceful Shutdown**: Allows the simulation to be stopped gracefully by pressing `Ctrl + C`.

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

## Data Format

The simulated data stream is based on an underwater inspection data survey and will be generated in the following format:

```text
[current_date],[current_time],[easting],[northing],[depth],[heading],[kp],[altitude],[dcc],[random_data_10],[random_data_11],[random_data_12]
```

- **`current_date`**: The current date in the format `YYYY-mm-dd`.
- **`current_time`**: The current time in the format `hh:mm:ss`.
- **`easting`**: A simulated value representing a vertical line movement of an object from top to bottom.
- **`northing`**: A simulated value representing a horizontal line movement of an object running left to right.
- **`depth`**: A simulated value representing an underwater depth movement of an object.
- **`heading`**: A simulated value of a compass point (north, south, east, or west), a number of degrees, and then another compass point.
- **`kp`**: A simulated current position of an object’s movement in kilometers with an average speed of 0.5 km per hour.
- **`altitude`**: A simulated height of an object above the sea or riverbed within the water column, corresponding to the current value of the depth.
- **`dcc`**: A simulated Depth Compensation Control (DCC) value corresponding to the value of depth.
- **`random_data_10`**, **`random_data_11`**, **`random_data_12`**: Simulated 4-digit random values with 4 decimal points (floats between 1000.0000 and 9999.9999).

## Example Output

```
Available Virtual COM Ports:
1: COM4
2: COM5
Select the virtual COM port to write to by number: 1
Enter baud rate (default is 9600): 9600
Enter data frequency (default is 1 second): 2
Sent to COM4: 2024-08-18,12:34:56,2345.6789,9876.5432,55.0,E180°W,0.5,27.5,110.0000,4321.5678,8765.4321,1234.5678
```

### Sample Data Output

Below is an example of the data generated by the simulator:

```
2024-08-18,12:34:56,2345.6789,9876.5432,55.0,E180°W,0.5,27.5,110.0000,4321.5678,8765.4321,1234.5678
2024-08-18,12:34:58,2345.6789,9876.5432,56.0,N90°E,1.0,28.0,112.0000,5432.6789,9876.5432,2345.6789
2024-08-18,12:35:00,3456.7890,8765.4321,60.5,S270°W,1.5,30.25,121.0000,6543.7890,1987.6543,3456.7890
```

## Contributing

If you have suggestions for improving this project, feel free to submit a pull request or open an issue. Contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.