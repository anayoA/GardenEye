<img src="../misc/Logo.png" alt="Designed by FreePik" title="GardenEye Logo" width="150">


# GardenEye
___
GardenEye is a smart gardening assistant that helps you monitor and manage your plants' environment with ease. Whether you're a
seasoned gardener or just starting out, GardenEye provides vital information to keep your plants *healthy* and *happy*.

## Features
___
***Real-time Monitoring***: Sensors that detect temperature and humidity ensure your plants are in optimum condition.  
***Customizable Alerts***: Set up custom alerts to notify you when your plants need attention, such as when humidity
levels drop below a certain threshold.  
***Data Analysis***: Analyze historical data to gain insights into your plants' environment. Identify
trends and patterns to hone your green thumb.  
***User-friendly Website***: GardenEye's user-friendly website makes it easy to add and keep track of several plants at once.

## Installation
___
### Clone the repository onto your Raspberry Pi (Alternatively download the .zip):

```bash
git clone -b raspberry-pi https://github.com/anayoA/GardenEye.git
```

### Navigate to the project directory:

```bash
cd "gardeneye/Raspberry Pi"
```

### Run gardenEyeSetup:

**Note**: Ensure your Raspberry Pi is connected to both the internet and the provided BME680 sensor before running.
```
./ gardenEyeSetup.sh
```
If nothing happens, file permissions may need to be changed. This can be done by inputting:
```bash
chmod +x gardenEyeSetup.sh
```
### Follow onscreen instructions from here. Enjoy your GardenEye!


## Credits

*Anayo Agwunobi*  
*Leon Rymer*  
*Avi Patel*  

*Logo designed by FreePik.*
