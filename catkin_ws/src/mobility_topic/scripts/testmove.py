from smbus2 import SMBusWrapper
import time
ADDRESS = 0x08

def writeToBus(roverMode, frequency):
    #if roverMode not in range(11) or frequency not in range(11):
        #return False
    #if type(mode) != int or type(freq) != int:
    #return False
    try:
        with SMBusWrapper(1) as bus:
            bus.write_byte_data(ADDRESS, roverMode, frequency)
            print('Done')
        #return True
    except IOError:
        print("Error writing")
        #return False


if __name__ == '__main__':
    #main()
    writeToBus(10, 11)
    time.sleep(.05)
    #writeToBus(10, 20)
    #time.sleep(.05)
    #writeToBus(10, 30)
    #time.sleep(.05)
    #writeToBus(10, 40)
