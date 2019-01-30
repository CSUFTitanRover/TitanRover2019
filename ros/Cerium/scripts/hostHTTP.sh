#!/usr/bin/env python

import subprocess
subprocess.run(["cd", "/home/nvidia/TitanRover2019/Cerium"])
subprocess.run(["sudo", "python", "-m", "SimpleHTTPServer"])
subprocess.run(["nvidia"])

