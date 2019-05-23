# main.py -- put your code here!
from pyb import Pin, Timer, UART, ADC
import pyb
import time
import _thread


                   # Pwm      # Dir      # Enab (HIGH = Disable)
armAction = { 0 : {4 : 'X1',  5 : 'X5',  6 : 'X6'},               # CH1 TIM2    Joint 1 ===> low = CLKW,    high = CCW,     freq = 1250  (Top)
              1 : {4 : 'X2',  5 : 'X7',  6 : 'X8'},               # CH2 TIM2    Joint 2 ===> low = DOWN,    high = UP,      freq = 1250  (Front)
              2 : {4 : 'X3',  5 : 'X9',  6 : 'X10'},              # CH3 TIM2    Joint 3 ===> low = CLKW,    high = CCW      freq = 1250  (Top)
              3 : {4 : 'X4',  5 : 'X11', 6 : 'X12'}               # CH4 TIM2    Joint 4 ===> low = OPEN/CLOSE, high = OPEN/CLOSE    freq = 1250  (Front)
            }

                       # Counter Clockwise / Left                  # Clockwise / Right                          # Stop                                       # Start 
movements = { 0 : {4 : Pin(armAction[0][5], Pin.OUT_PP).high, 5 : Pin(armAction[0][5], Pin.OUT_PP).low, 6 : Pin(armAction[0][6], Pin.OUT_PP).high, 7 : Pin(armAction[0][6], Pin.OUT_PP).low},
                       # UP                                         # Down                                      # Stop                                       # Start 
              1 : {4 : Pin(armAction[1][5], Pin.OUT_PP).high, 5 : Pin(armAction[1][5], Pin.OUT_PP).low, 6 : Pin(armAction[1][6], Pin.OUT_PP).high, 7 : Pin(armAction[1][6], Pin.OUT_PP).low},
                       # Counter Clockwise / Left                  # Clockwise / Right                          # Stop                                       # Start 
              2 : {4 : Pin(armAction[2][5], Pin.OUT_PP).high, 5 : Pin(armAction[2][5], Pin.OUT_PP).low, 6 : Pin(armAction[2][6], Pin.OUT_PP).high, 7 : Pin(armAction[2][6], Pin.OUT_PP).low},
                       # Close / Open                               # Close / Open                              # Stop                                       # Start 
              3 : {4 : Pin(armAction[3][5], Pin.OUT_PP).high, 5 : Pin(armAction[3][5], Pin.OUT_PP).low, 6 : Pin(armAction[3][6], Pin.OUT_PP).high, 7 : Pin(armAction[3][6], Pin.OUT_PP).low}
            }

                   # CCW / Left           # Clockwise / Right    # Stop                 # Start
ledMove = { 0 : {4 : pyb.LED(1).on, 5 : pyb.LED(1).on, 6 : pyb.LED(1).off, 7 : pyb.LED(1).on},
                   # UP                   # Down                 # Stop                 # Start 
            1 : {4 : pyb.LED(2).on, 5 : pyb.LED(2).on, 6 : pyb.LED(2).off, 7 : pyb.LED(2).on},
                   # CCW / Left           # Clockwise / Right    # Stop                 # Start 
            2 : {4 : pyb.LED(3).on, 5 : pyb.LED(3).on, 6 : pyb.LED(3).off, 7 : pyb.LED(3).on},
                   # Close / Open         # Close / Open         # Stop                 # Start 
            3 : {4 : pyb.LED(4).on, 5 : pyb.LED(4).on, 6 : pyb.LED(4).off, 7 : pyb.LED(4).on}
            }

#  SAMPLE COMMAND READ S##E
def getcommand(port):
    ser = UART(6, 115200)
    while True:
        try:
            data = ser.read(1)
            if str(data.decode('utf-8')) == 's':
                move = ser.read(3)
                move = move.decode('utf-8')
                if str(move[2]) == 'e':
                    #ledMove[int(move[0])][int(move[1])]()
                    movements[int(move[0])][int(move[1])]()
        except:
            pass

def sendFeedback(port):
    serPot = UART(3, 115200)
    while True:
        try:
            lol = pot.read()
            if int(lol) < 10:
                lol = "000" + str(lol)
            elif int(lol) < 100:
                lol = "00" + str(lol)
            elif int(lol) < 1000:
                lol = "0" + str(lol)
            serPot.write(str(lol))
            time.sleep(0.1)
        except:
            pass




if __name__ == "__main__":
    for i in range(4):
        Pin(armAction[i][6], Pin.OUT_PP).high()
        Pin(armAction[i][5], Pin.OUT_PP).high()
        Timer(2, freq=1250).channel(i+1, Timer.PWM, pin=Pin(armAction[i][4])).pulse_width_percent(50)
    pot = ADC(Pin('X19'))
    pyb.LED(2).toggle()
    time.sleep(1)
    pyb.LED(2).toggle()
    _thread.start_new_thread(getcommand, (6, ))
    _thread.start_new_thread(sendFeedback, (3, ))


'''

# main.py -- put your code here!
from pyb import Pin, Timer, LED, UART, ADC
import time
import pyb

p = Pin('X4') # X1 has TIM2, CH1
q = Pin('X11', Pin.OUT_PP)
q.low()

tim = Timer(2, freq=1250)
ch = tim.channel(4, Timer.PWM, pin=p)
ch.pulse_width_percent(50)
pyb.LED(3).toggle()
time.sleep(5)
ch.pulse_width_percent(0)
pyb.LED(3).toggle()



'''



'''
# main.py -- put your code here!
from pyb import Pin, Timer, LED, UART, ADC
import time
import pyb

p = Pin('X1') # X1 has TIM2, CH1
q = Pin('X2', Pin.OUT_PP)
q.low()

tim = Timer(2, freq=1250)
ch = tim.channel(1, Timer.PWM, pin=p)
ch.pulse_width_percent(50)
time.sleep(1)
ch.pulse_width_percent(0)


ser = UART(1, 115200)                         # init with given baudrate
#ser.init(9600, bits=8, parity=None, stop=1) # init with given parameters

# FeedBack Shit HERE
feed = ADC(Pin('Y12'))

pin1_a = Pin('X12', Pin.IN)
pin2_b = Pin('X11', Pin.IN)
pin3_ind = Pin('X22', Pin.IN)

while True:
    lol = pin1_a.value() # read value, 0-4095
    lol2 = pin2_b.value() # read value, 0-4095

    ser.write(str(lol) + str(lol2))

    if int(lol) < 10:
        lol = "000" + str(lol)
    elif int(lol) < 100:
        lol = "00" + str(lol)
    elif int(lol) < 1000:
        lol = "0" + str(lol)
    #ser.write(str(lol))
    time.sleep(.1)


ser = UART(1, 9600)                         # init with given baudrate

p = Pin('X1') # X1 has TIM2, CH1
q = Pin('X2', Pin.OUT_PP)
#r = Pin('X5', Pin.OUT_PP)

#s = Pin('X3')
#t = Pin('X4', Pin.OUT_PP)
q.high()
#r.low()
#s.low()
tim1 = Timer(2, freq=1250)
ch1 = tim1.channel(1, Timer.PWM, pin=p)
ch1.pulse_width_percent(50)
time.sleep(1)

while True:
    data = ser.read(1)
    if int(data) is 0:
        r.low()
        break
    elif int(data) is 1:
        r.high()
        break

tim1 = Timer(2, freq=1250)
ch1 = tim1.channel(1, Timer.PWM, pin=p)
#tim2 = Timer(2, freq=1250)
#ch2 = tim2.channel(3, Timer.PWM, pin=r)
ch1.pulse_width_percent(50)
#ch2.pulse_width_percent(50)
time.sleep(2)
ch1.pulse_width_percent(0)
#ch2.pulse_width_percent(0)


ser = UART(1, 9600)                         # init with given baudrate
#ser.init(9600, bits=8, parity=None, stop=1) # init with given parameters


while True:
    data = ser.read(1)
    if int(data) > 5:
        LED(4).toggle()
    else:
        LED(3).toggle()

armAction = { 0 : {'pwm' : 'X1', 'dir' : 'X2'},         # low = CW   , high = CCW   //// freq = 1250  (Top)
              1 : {'pwm' : 'X3', 'dir' : 'X4'},         # low = Down , high = up    //// freq = 1250  (Front)
              2 : {'pwm' : 'X5', 'dir' : 'X6'},         # low = CW   , high = CCW   //// freq = 1250  (Top)
              3 : {'pwm' : 'XX', 'dir' : 'XX'}          # low =  , high =     //// freq = 1250
            }

#for i in range(len(armAction)):
#    pyb.Pin(armAction[i]['pwm'], pyb.Pin.OUT_PP)
#    pyb.Pin(armAction[i]['dir'], pyb.Pin.OUT_PP)

p = pyb.Pin('X1', pyb.Pin.OUT_PP)
q = pyb.Pin('X2', pyb.Pin.OUT_PP)
#r = pyb.Pin('X3', pyb.Pin.OUT_PP)
#s = pyb.Pin('X4', pyb.Pin.OUT_PP)
q.low()
#q.high()

for i in range(150):
    p.high()
    time.sleep_us(1000)
    p.low()
    time.sleep_us(1000)

'''