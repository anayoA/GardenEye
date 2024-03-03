#!/bin/bash

# Start up
echo "Setting up GardenEye..."
# Function to check internet connection
check_internet() {
    if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; then
        echo "Internet connection detected."
        return 0
    else
        echo "No internet connection. Please check your connection and try again."
        return 1
    fi
}

# Check for internet connection
if check_internet; then
    # Internet connection is available, run the command
    curl https://get.pimoroni.com/bme680 | bash
else
    # No internet connection, exit with non-zero status
    exit 1
fi
# Function to check if sensors are connected
check_sensors() {
    # Add your sensor connection check here
    # Example: check if the BME680 sensor is connected
    if i2cdetect -y 1 | grep -q "77"; then
        echo "BME680 sensor detected."
        return 0
    else
        echo "BME680 sensor not detected. Please check the sensor connections."
        return 1
    fi
}

# Check for internet connection
if check_internet; then
    # Internet connection is available, proceed to check sensors
    if check_sensors; then
        # Sensors are connected, continue with next script
        echo "Sensors are connected. Proceeding with next script..."
        # Enter authentication key step
	python3 fetch_data.py
    else
        # Sensors are not connected, exit with non-zero status
        exit 1
    fi
else
    # No internet connection, exit with non-zero status
    exit 1
fi