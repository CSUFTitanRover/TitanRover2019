import subprocess
import sys

# To import packages from different Directories
rootDir = subprocess.check_output('locate TitanRover2019 | head -1', shell=True).strip().decode('utf-8')
sys.path.insert(0, rootDir + '/build/resources/python-packages')
from pysaber import DriveEsc

motors = DriveEsc(129, "mixed")

while True:
    motors.driveBoth(127, 127)