from time import sleep
import sys, subprocess
sys.path.insert(0, subprocess.check_output('locate TitanRover2019 | head -1', shell=True).strip().decode('utf-8') + '/gpio/')

from tx2gpio import Tx2Gpio


disable = 466
dir = 298
pulse = 396


#pin = [255, 388, 254, 397, 396, 398, 389, 296, 430, 297, 394, 393, 427, 428, 429, 395, 392, 467]
pin = [disable, dir, pulse] #[466, 298, 396]
tx2 =  Tx2Gpio(pin)

for x in pin:
  tx2.setup(x,'out')

#while True:
tx2.output(disable, 0)
tx2.output(dir, 0)

for y in range(2):
  for x in range(100000):
    #print(x)
    tx2.output(pulse, 1)
    #sleep(.0005)
    tx2.output(pulse, 0)
    sleep(.05)
  
  sleep(5)
  tx2.output(dir, 1)

tx2.output(disable, 1)

#tx2.output(466 , 0)
#tx2.output(298 , 0)
#tx2.output(396 , 1)
#sleep(10)



''' Voltage found
go 255, 298, 388, 254, 466, 
no 397, 396, 398, 389, 296, 430, 297, 394, 393, 427, 428, 429, 395, 392, 467

	started		On		off

396 = 	0		1.44		
397 = 	3.32		

'''
