# Using TitanRover Python Dependances:

## Recuired code to be added to script

```python

   import subprocess

    # To import packages from different Directories
    rootDir = subprocess.check_output('locate TitanRover2019 | head -n 1', shell=True).strip()
    sys.path.insert(0, rootDir + '/packages')
```



# Mobility

### Last Year

- The mobility worked using TX2, arduino and the ESC's (2x60).
- The command flow was as mentioned:-
***Joystick --> TX2 --> Arduino --> Sabertooth --> Motors***
- [Sabertooth](https://www.dimensionengineering.com/products/sabertooth2x60) allows you to control two motors with: analog voltage, radio control, serial and packetized serial.
- Serial mode was being used to communicate between the arduino and the sabertooth.
 - Last year's Mobility code can be found [here](https://github.com/CSUFTitanRover/TitanRover2018/tree/master/rover/core/servers/ArduinoSocketServer).

### This Year

- The mobility worked using TX2, arduino and the ESC's (2x60).
- The command flow without the Arduino is as mentioned:-
***Joystick --> TX2 -->  Sabertooth --> Motors***
- Doing this servers us two purpose.
	1. *weight Reduction.*
	2. *Improved response time.*
- By eliminating the use of Arduino, we can use packetized serial mode which allows us to make use of checksum.
- Checksums are used to ensure the integrity of data portions for data transmission or storage. Hence, we can be sure the command was successfully sent to the motors.
- For using the [Sabertooth](https://www.dimensionengineering.com/products/sabertooth2x60) directly with the TX2 we need to use USB to TTL adapter.
- The TX and GND pins of the adapter is connected to S1 and 0V of the sabertooth, respectively.
- We wrote a custom module in python by using the original [PySabertooth](https://github.com/MomsFriendlyRobotCompany/pysabertooth) library.

#### How to use the custom sabertooth module
- In order to use this in software you can import the pysaber module from the packages folder and call the method to drive the motors.
- The steps to import the package are:-
```
    import subprocess
	
    # To import packages from different Directories
    rootDir = subprocess.check_output('locate TitanRover2019 | head -n 1', shell=True).strip()
    sys.path.insert(0, rootDir + '/packages')
```
- After following the above step you can simply import the module, make a [class object](http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html), and use it.
- While instantiating a class object you can use either "**_Mixed mode_**" or "**_Independent mode_**" for driving the motors.
- **_Mixed Mode_** --> Used to control the wheels proportionally (Takes the joystick input as vector(x,y)).
    - To use this mode, initialize the class as:
    ```
    object = DriveEsc(ESC_Address, "mixed")
    ```
- **_Independent Mode_** -- > Used to Drive each motor seperately.
    - To use this mode, initialize the class as:
    ```
    object = DriveEsc(ESC_Address, "notMixed")
    ```