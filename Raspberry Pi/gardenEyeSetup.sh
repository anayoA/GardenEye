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
    pip3 install tkinter
    pip3 install customtkinter
    pip3 install requests
    pip3 install Pillow
    pip3 install CTkMessagebox
    python3 files/Authentication.py #authentication key step
else
    # No internet connection, exit with non-zero status
    exit 1
fi
