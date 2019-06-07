# MultiJoy

This package collates a number of joystick states together and publishes the joystick states in one message.

# Generating new launch files

A script to generate appropriate launch files is provided. For example, if you want to use 5 joysticks then run 
```
python generate.py 5
```
Simply move the generated file to the `/launch` directory. 

# Device support

`MultiJoy` supports what ever `Joy` supports. See `joy`  package summary [here](http://wiki.ros.org/joy).
