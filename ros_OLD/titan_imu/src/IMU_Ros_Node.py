####################################################################################
#
#       Program dependancies the IMU must circuit must be placed either facing up
#       or facing down for accurate initialization process.  Depending on up/down
#       several lines of codes need to be commented out or used.  These sections
#       of code are titled:
#                       ##########Direction Requirement###########
#       for the purposes of this project which used the Adafruit 10-DOF the unit
#       is considered upside down if the IC's on the IMU are facing the direction
#       of the earth.  Right side up is IC's facing the sky.
#
####################################################################################
#!/usr/bin/env python

import sys, rospy, time
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion, Vector3, PoseStamped
#from tf.transformations import euler_from_quaternion
import smbus, time, math, datetime
from LSM303_U import *
from L3GD20_GYRO import *
from std_msgs.msg import String

bus = smbus.SMBus(0)

RAD_TO_DEG = 57.29578
M_PI = 3.14159265358979323846
G_GAIN = 0.070  # [deg/s/LSB]  If you change the dps for gyro, you need to update this value accordingly
AA =  0.40      # Complementary filter constant
try:
	print(sys.argv[1])	
	MAGNETIC_DECLINATION=float(sys.argv[1])

except:
	print("Missing Arguments: MAGNETIC_DECLINATION = set to 0.00")
	#exit(0)
	MAGNETIC_DECLINATION=0.00

#Kalman filter variables
Q_angle = 0.02
Q_gyro = 0.0015
R_angle = 0.005
x_bias = y_bias = 0.0
XP_00 = XP_01 = XP_10 = XP_11 = 0.0
YP_00 = YP_01 = YP_10 = YP_11 = 0.0
KFangleX = KFangleY = 0.0

def kalmanFilterY ( accAngle, gyroRate, DT):
	y=0.0
	S=0.0

	global KFangleY
	global Q_angle
	global Q_gyro
	global y_bias
	global YP_00
	global YP_01
	global YP_10
	global YP_11

	KFangleY = KFangleY + DT * (gyroRate - y_bias)

	YP_00 = YP_00 + ( - DT * (YP_10 + YP_01) + Q_angle * DT )
	YP_01 = YP_01 + ( - DT * YP_11 )
	YP_10 = YP_10 + ( - DT * YP_11 )
	YP_11 = YP_11 + ( + Q_gyro * DT )

	y = accAngle - KFangleY
	S = YP_00 + R_angle
	K_0 = YP_00 / S
	K_1 = YP_10 / S
	
	KFangleY = KFangleY + ( K_0 * y )
	y_bias = y_bias + ( K_1 * y )
	
	YP_00 = YP_00 - ( K_0 * YP_00 )
	YP_01 = YP_01 - ( K_0 * YP_01 )
	YP_10 = YP_10 - ( K_1 * YP_00 )
	YP_11 = YP_11 - ( K_1 * YP_01 )
	
	return KFangleY

def kalmanFilterX ( accAngle, gyroRate, DT):
	x=0.0
	S=0.0

	global KFangleX
	global Q_angle
	global Q_gyro
	global x_bias
	global XP_00
	global XP_01
	global XP_10
	global XP_11


	KFangleX = KFangleX + DT * (gyroRate - x_bias)

	XP_00 = XP_00 + ( - DT * (XP_10 + XP_01) + Q_angle * DT )
	XP_01 = XP_01 + ( - DT * XP_11 )
	XP_10 = XP_10 + ( - DT * XP_11 )
	XP_11 = XP_11 + ( + Q_gyro * DT )

	x = accAngle - KFangleX
	S = XP_00 + R_angle
	K_0 = XP_00 / S
	K_1 = XP_10 / S
	
	KFangleX = KFangleX + ( K_0 * x )
	x_bias = x_bias + ( K_1 * x )
	
	XP_00 = XP_00 - ( K_0 * XP_00 )
	XP_01 = XP_01 - ( K_0 * XP_01 )
	XP_10 = XP_10 - ( K_1 * XP_00 )
	XP_11 = XP_11 - ( K_1 * XP_01 )
	
	return KFangleX

'''
def writeRegisterAxis(Address, register, value):
	bus.write_byte_data(Address, register, value)
	return -1
'''

def writeACC(register,value):
        bus.write_byte_data(LSM303_ADDRESS_ACCEL , register, value)
        return -1

def writeMAG(register,value):
        bus.write_byte_data(LSM303_ADDRESS_MAG, register, value)
        return -1

def writeGRY(register,value):
        bus.write_byte_data(L3GD20_ADDRESS_GYRO, register, value)
        return -1

def readACCx():
        acc_l = bus.read_byte_data(LSM303_ADDRESS_ACCEL, LSM303_ACCEL_OUT_X_L_A)
        acc_h = bus.read_byte_data(LSM303_ADDRESS_ACCEL, LSM303_ACCEL_OUT_X_H_A)
        acc_combined = (acc_l | acc_h <<8)

        return acc_combined  if acc_combined < 32768 else acc_combined - 65536


def readACCy():
        acc_l = bus.read_byte_data(LSM303_ADDRESS_ACCEL, LSM303_ACCEL_OUT_Y_L_A)
        acc_h = bus.read_byte_data(LSM303_ADDRESS_ACCEL, LSM303_ACCEL_OUT_Y_H_A)
        acc_combined = (acc_l | acc_h <<8)

        return acc_combined  if acc_combined < 32768 else acc_combined - 65536


def readACCz():
        acc_l = bus.read_byte_data(LSM303_ADDRESS_ACCEL, LSM303_ACCEL_OUT_Z_L_A)
        acc_h = bus.read_byte_data(LSM303_ADDRESS_ACCEL, LSM303_ACCEL_OUT_Z_H_A)
        acc_combined = (acc_l | acc_h <<8)

        return acc_combined  if acc_combined < 32768 else acc_combined - 65536


def readMAGx():
        mag_l = bus.read_byte_data(LSM303_ADDRESS_MAG, LSM303_MAG_OUT_X_L_M)
        mag_h = bus.read_byte_data(LSM303_ADDRESS_MAG, LSM303_MAG_OUT_X_H_M)
        mag_combined = (mag_l | mag_h <<8)

        return mag_combined  if mag_combined < 32768 else mag_combined - 65536


def readMAGy():
        mag_l = bus.read_byte_data(LSM303_ADDRESS_MAG, LSM303_MAG_OUT_Y_L_M)
        mag_h = bus.read_byte_data(LSM303_ADDRESS_MAG, LSM303_MAG_OUT_Y_H_M)
        mag_combined = (mag_l | mag_h <<8)

        return mag_combined  if mag_combined < 32768 else mag_combined - 65536


def readMAGz():
        mag_l = bus.read_byte_data(LSM303_ADDRESS_MAG, LSM303_MAG_OUT_Z_L_M)
        mag_h = bus.read_byte_data(LSM303_ADDRESS_MAG, LSM303_MAG_OUT_Z_H_M)
        mag_combined = (mag_l | mag_h <<8)

        return mag_combined  if mag_combined < 32768 else mag_combined - 65536



def readGYRx():
        gyr_l = bus.read_byte_data(L3GD20_ADDRESS_GYRO, L3GD20_OUT_X_L)
        gyr_h = bus.read_byte_data(L3GD20_ADDRESS_GYRO, L3GD20_OUT_X_H)
        gyr_combined = (gyr_l | gyr_h <<8)

        return gyr_combined  if gyr_combined < 32768 else gyr_combined - 65536
  

def readGYRy():
        gyr_l = bus.read_byte_data(L3GD20_ADDRESS_GYRO, L3GD20_OUT_Y_L)
        gyr_h = bus.read_byte_data(L3GD20_ADDRESS_GYRO, L3GD20_OUT_Y_H)
        gyr_combined = (gyr_l | gyr_h <<8)

        return gyr_combined  if gyr_combined < 32768 else gyr_combined - 65536

def readGYRz():
        gyr_l = bus.read_byte_data(L3GD20_ADDRESS_GYRO, L3GD20_OUT_Z_L)
        gyr_h = bus.read_byte_data(L3GD20_ADDRESS_GYRO, L3GD20_OUT_Z_H)
        gyr_combined = (gyr_l | gyr_h <<8)

        return gyr_combined  if gyr_combined < 32768 else gyr_combined - 65536

#initialise the accelerometer
writeACC(LSM303_ACCEL_CTRL_REG1_A, 0b01100111) #z,y,x axis enabled, continuos update,  100Hz data rate
writeACC(LSM303_ACCEL_CTRL_REG2_A, 0b00100000) #+/- 16G full scale

#initialise the magnetometer
writeMAG(LSM303_CRA_REG_M, 0b11110000) #Temp enable, M data rate = 50Hz
writeMAG(LSM303_CRB_REG_M, 0b01100000) #+/-12gauss
writeMAG(LSM303_MR_REG_M, 0b00000000) #Continuous-conversion mode

#initialise the gyroscope
writeGRY(L3GD20_CTRL_REG1, 0b00001111) #Normal power mode, all axes enabled
writeGRY(L3GD20_CTRL_REG4, 0b00110000) #Continuos update, 2000 dps full scale


gyroXangle = gyroYangle = gyroZangle = 0.0
CFangleX = CFangleY = 0.0
kalmanX = kalmanY = 0.0

a = datetime.datetime.now()                                             #Gyro Timing Control

def create_quaternion(q1, q2, q3, q4):
    print ("Creating quaternion from:")
    print (q1, q2, q3, q4)
    d = math.sqrt(q1*q1 + q2*q2 + q3*q3 + q4*q4)    # norm coefficient
    q = Quaternion()
    q.x = q1 * 1.0 / d 
    q.y = q2 * 1.0 / d 
    q.z = q3 * 1.0 / d 
    q.w = q4 * 1.0 / d 
    return q

def create_vector3(groll, gpitch, gyaw):
    print ("Creating Vector3 from:")
    print (groll, gpitch, gyaw)
    v = Vector3()
    # I guess the units will be like that, but I don't know
    v.x = groll / 1000.0
    v.y = gpitch / 1000.0
    v.z = gyaw / 1000.0
    return v

def IMU_Post(imu_pub, ps_pub):
	
	pub = rospy.Publisher('imu', String, queue_size=1)
	rospy.init_node('magnetometer', anonymous=True)
	rate = rospy.Rate(50) # 50Hz
	while not rospy.is_shutdown():
		

		total_heading = 0.0
		#loop = 1                     #High the loops the greater the accuracy
						#The longer the cycle
		#n = 0
		#while n < loop: #True:                    #Continous run Disabled to allow Node.js control
		#        n = n + 1

		#for num in range(0,loop):	        #Currently this loop runs for 20 reads providing greater accuracy
	
		#Read the accelerometer,gyroscope and magnetometer values
		
		ACCx = readACCx()
		ACCy = readACCy()
		ACCz = readACCz()
		GYRx = readGYRx()
		GYRy = readGYRy()
		GYRz = readGYRz()
		MAGx = readMAGx()
		MAGy = readMAGy()
		MAGz = readMAGz()

		i = Imu()
		i.header.stamp = rospy.Time.now()
		i.header.frame_id = 'BMP180'
		i.orientation = create_quaternion(MAGx, MAGy, MAGz, 0)
		i.angular_velocity = create_vector3(GYRx, GYRy, GYRz)
		i.linear_acceleration = create_vector3(ACCx, ACCy, ACCz)
		imu_pub.publish(i)
		ps = PoseStamped()
		ps.header = i.header
		ps.pose.orientation = i.orientation
		ps_pub.publish(ps)
	
if __name__ == '__main__':
	rospy.loginfo("Initializing imu publisher")
	imu_pub = rospy.Publisher('/imu', Imu, queue_size=5)
	rospy.loginfo("Publishing Imu at: " + imu_pub.resolved_name)
	ps_pub = rospy.Publisher('/posestamped', PoseStamped, queue_size=5)
	try:
		IMU_Post(imu_pub, ps_pub)
	except rospy.ROSInterruptException:
		pass
