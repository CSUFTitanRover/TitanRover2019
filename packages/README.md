# Using TitanRover Python Dependances:

## Recuired code to be added to script

'''
[
   import subprocess


    # To import packages from different Directories
    rootDir = subprocess.check_output('locate TitanRover2019 | head -n 1', shell=True).strip()
    sys.path.insert(0, rootDir + '/packages')
]
'''