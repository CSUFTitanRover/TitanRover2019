# TX2 GPIO

## Linux SysFS GPIO access via Python
==================================

This Document provides a guideline on how to access J21 GPIO Pins on TX2 in Python.

## How to use it

1. Download this repository

```shell

    git clone https://github.com/derekstavis/python-sysfs-gpio.git

```

2. Follow the commands:

```shell

    cd python-sysfs-gpio
    sudo python setup.py install

```

3. Sample Code:
You need to Have Titanrover2019 Folder on your machine. If you Don't use this command and if you do make sure to do a ```git pull```

```shell

    cd ~/
    git clone https://github.com/CSUFTitanRover/TitanRover2019
    cd TitanRover2019/
    git checkout development

```

```python
    
    import sys
    import subprocess

    # Add the GPIO Module to python packages
    sys.path.insert(0, subprocess.check_output('locate TitanRover2019 | head -1' shell=True).strip().decode('utf-8') + '/gpio/')
    from tx2gpio import Tx2Gpio

    # Define what pins are to be used
    pinsUsed = [1, 2, 3, 4]

    # Create an Object
    tx2 = Tx2Gpio(pinsUsed)

    # If you want the Pins to be used as OUTPUT
    tx2.setup(PIN_NUM, 'out')           # PIN_NUM is the gpio pin you want to use
    
    # If You want the Pins to be used as INPUT
    tx2.setup(PIN_NUM, 'in')            # PIN_NUM is the gpio pin you want to use

    
    tx2.output(PIN_NUM, 0)              # Sends a LOW signal to the pin
    tx2.output(PIN_NUM, 1)              # Sends a HIGH signal to the pin

    tx2.read(PIN_NUM)                   # Reads pin logic level

```
