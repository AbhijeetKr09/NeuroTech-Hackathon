
# PyQt5 Real-time Serial Data Visualization

This repository contains the source code for a PyQt5 application that visualizes real-time data from a serial port using pyqtgraph and applies digital filters using SciPy's signal processing module. The application is designed to read data from a serial port, apply bandpass and notch filters to the incoming data, and display the filtered results in real-time.

## Features

- **Real-time Data Visualization**: Utilizes pyqtgraph for plotting data in real-time.
- **Serial Communication**: Reads data from a serial port using the `serial` library.
- **Digital Filtering**: Implements two types of digital filters:
  - **LiveLFilter**: A live filter using direct form I implementation.
  - **LiveSosFilter**: A live filter using second-order sections (SOS) for stability in higher-order filters.
- **Threaded Data Reading**: Uses `QThread` for reading data from the serial port without blocking the main GUI thread.

## Requirements

- Python 3
- PyQt5
- pyqtgraph
- numpy
- scipy
- pyserial

## Installation

To run this application, you need to install the required libraries. You can install them using pip:

```bash
pip install PyQt5 pyqtgraph numpy scipy pyserial
```

## Usage

1. Connect your data source to the serial port.
2. Configure the serial port settings in the code.
3. Run the application:

```bash
python main.py
```

4. The application will start reading data from the serial port, apply the selected filters, and display the results in real-time.

## Filters

The application includes two filter classes:

- `LiveLFilter`: This filter uses a direct form I structure. It requires the filter coefficients `b` and `a`.
- `LiveSosFilter`: This filter uses a second-order sections (SOS) structure. It requires the SOS matrix which contains the coefficients for each section.

## Customization

You can customize the filters by modifying the filter coefficients according to your requirements. The `iirfilter` function from SciPy's signal processing module can be used to design the filters.

