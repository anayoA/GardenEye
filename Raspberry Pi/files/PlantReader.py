#!/usr/bin/env python

import bme680
import time
import requests

print("""temperature-pressure-humidity.py - Displays temperature, pressure, and humidity.

If you don't need gas readings, then you can read temperature,
pressure and humidity quickly.

Press Ctrl+C to exit

""")


def read_data():
    try:
        sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
    except (RuntimeError, IOError):
        sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
    # These oversampling settings can be tweaked to
    # change the balance between accuracy and noise in
    # the data.
    sensor.set_humidity_oversample(bme680.OS_2X)
    sensor.set_temperature_oversample(bme680.OS_8X)
    sensor.set_filter(bme680.FILTER_SIZE_3)
    print('Polling:')
    try:
        while True:
            if sensor.get_sensor_data():
                output = '{0:.2f} C,{2:.3f} %RH'.format(
                    sensor.data.temperature,
                    sensor.data.humidity)
                print(output)
                return output
            else:
                print("Error: Reading not taken. Ensure sensor connection is secure.")
            time.sleep(60)

    except KeyboardInterrupt:
        pass


def send_data(temperature, humidity):
    # API endpoint for data
    data_endpoint = "http://localhost/gardeneye/api/data/collectData.php"

    params = {
        "env_ID"
        "token"
        "username"
        "temperature": temperature,
        "humidity": humidity
    }
    try:
        response = requests.post(data_endpoint, params)
        if response.status_code == 200:
            print("Data sent successfully to the API.")
            return response.json()  # Return the response data if needed
        else:
            print(f"Failed to send data to the API. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while sending data to the API: {e}")
        return None

# def authenticate(username, token):
#     # API endpoint for authentication
#     auth_endpoint = "http://localhost/gardeneye/api/authentication/authenticateUser.php"
#
#     # Parameters for the authentication request
#     params = {
#         "username": username,
#         "token": token
#
#     }
#
#     try:
#         response = requests.post(auth_endpoint, params)
#         data = response.json()
#
#         if data["success"]:
#             print("Authentication successful:", data["message"])
#             auth_success("Success", data["message"])
#         else:
#             print("Authentication failed:", data["message"])
#             auth_warning(data["message"])
#     except requests.exceptions.RequestException as e:
#         print("Error:", e)
