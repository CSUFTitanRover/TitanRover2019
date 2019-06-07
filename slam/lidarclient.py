# Python TCP Client
import socket 
import pickle
from time import sleep

_WIDTH     = 320
_HEIGHT    = 24
_TOTALDATA = 2 * _WIDTH * _HEIGHT

#MESSAGE_Stop    = 'StopRequestPacket                                  '
MESSAGE_Ver     = b'version                                            ' 
MESSAGE_Start   = b'getDistanceAndAmplitudeSorted                      '
MESSAGE_Stop    = 'join                                               '
MESSAGE_Dis     = 'disconnect                                         '
MESSAGE_setID   = 'setLidarID 1234567                                 ' # + id
#MESSAGE_enFeat  = 'enableFeatures ' + # FilterRequestPacket= 104876,  
#MESSAGE_disFeat = 'disableFeatures ' + # SafetyModeRequestPacket = 268435456 
MESSAGE_Int     = 'setIntegrationTime3D 1600                          '
MESSAGE_roi     = 'roi 0 0 3                                          '
MESSAGE_getID   = 'getLidarID                                         '
MESSAGE_Time    = 'updateTimeStamp                                    '
MESSAGE_enGray  = 'enableGrayOutput 1                                 '
MESSAGE_disGray = 'enableGrayOutput 0                                 '


host = "192.168.1.80" 
port = 2368
BUFFERSIZE = 816 
data = ''

Client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
Client.connect((host, port))
try:
    #print(Client.send(MESSAGE_Start))
    if (Client.send(MESSAGE_getID) < 0):
        print ('Error starting Lidar')
    else:
        #for x in range(BUFFERSIZE):
        data, servers = Client.recvfrom(_TOTALDATA) #BUFFERSIZE)
        print('Lidar Receive Started')
except:
    print('Lidar Client receive ERROR')
    Client.send(MESSAGE_Stop)
    Client.close()
    exit(1)
    #break
print(' Client A received data: ' + data) # int(data, 16))
Client.send(MESSAGE_Stop)
Client.close()
#sleep(.3)



'''
#while True:
try:
    print 'start Lidar'
    print Client.send(MESSAGE_Start)     
    
    data = Client.recv(PACKET_SIZE)
    print 'stop Lidar'
    #data = data.split(',')
    
    #data = pickle.loads(data)
    print(data)
'''