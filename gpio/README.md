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

```python
    
    # Import this package objects
    
    from sysfs.gpio import Controller, OUTPUT, INPUT, RISING
    
    # Refer to your chip GPIO numbers and set them this way
    
    Controller.available_pins = [1, 2, 3, 4]
    
    # Allocate a pin as Output signal
    
    pin = Controller.alloc_pin(1, OUTPUT)
    pin.set()   # Sets pin to high logic level
    pin.reset() # Sets pin to low logic level
    pin.read()  # Reads pin logic level
    
    # Allocate a pin as simple Input signal
    
    pin = Controller.alloc_pin(1, INPUT)
    pin.read()  # Reads pin logic level

```
