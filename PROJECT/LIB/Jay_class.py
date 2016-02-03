#!/usr/bin/python
import sys
#sys.path.append('AdafruitCode/Adafruit_PWM_Servo_Driver')
from Adafruit_PWM_Servo_Driver import PWM
import time
import getopt
import math
sys.path.append('.')
import RTIMU
import os.path

pwm = PWM(0x40)
pwm.setPWMFreq(100)
SERVO_MIN = 300
SERVO_MAX = 650
ANGLE_MAX = 25
class Servo():
	def __init__(self,channel,direction,position,old_position):
		if direction == 0 :
			direction = 1
		direction = direction/abs(direction)
		self.direction = direction
		self.position = position
		self.old_position= position
		self.channel = channel		
		
	def move_pid(self,pid):
		
		self.old_position = self.position
		self.position = self.position + (pid.update()*self.direction)
		if self.position < SERVO_MIN:
			self.position = SERVO_MIN
		elif self.position > SERVO_MAX:
			self.position = SERVO_MAX
		pwm.setPWM(self.channel,0,int(self.position))
		

class Pid():

	
	#Calculate the pid value with a given error (IT DOESN'T CALCULATE THE ERROR!)
	
	def __init__(self, P, I, D):

		self.Kp=P
		self.Ki=I
		self.Kd=D
		self.Derivator=0
		self.Integrator=0
		self.Integrator_max=5
		self.Integrator_min=-5
		self.error=0

	def update(self):
		
		#Calculate PID output value for given reference input and feedback
		

		self.P_value = self.Kp * self.error
		self.D_value = self.Kd * ( self.error - self.Derivator)
		self.Derivator = self.error

		self.Integrator = self.Integrator + self.error

		if self.Integrator > self.Integrator_max:
			self.Integrator = self.Integrator_max
		elif self.Integrator < self.Integrator_min:
			self.Integrator = self.Integrator_min

		self.I_value = self.Integrator * self.Ki

		PID = self.P_value + self.I_value + self.D_value
		#return a float 
		return PID

	def finderror(self,current_angle,set_angle):
		
		"""Will work with an angle error 
		"""
		self.error = current_angle - set_angle 

SETTINGS_FILE = "RTIMULib"
s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

class Imu():
	def __init__(self):
	
		k=0
		if k==0:
#			SETTINGS_FILE = "RTIMULib"
		
			print ("Using settings file" +  SETTINGS_FILE +  ".ini")
		
			if not os.path.exists(SETTINGS_FILE + ".ini"):
		
				print("Settings file does not esist, will be created")
		
#			s = RTIMU.Settings(SETTINGS_FILE)
#			imu = RTIMU.RTIMU(s)
		
			print ("IMU Name : " + imu.IMUName())
		
			if (not imu.IMUInit()):
				print ("IMU Init Failed")
				sys.exit(1)
			else:
				print("IMU Init Succeeded")
		
		# this is a good time to set any fusion parameters 
		
			imu.setSlerpPower(0.02)
			imu.setGyroEnable(True)
			imu.setAccelEnable(True)
			imu.setCompassEnable(True)
		
			poll_interval = imu.IMUGetPollInterval()
			print("Recommended Poll Interval: %dmS\n" % poll_interval)
		


			self.roll = 0
			self.pitch = 0
			self.yaw = 0
			k=1
		

	def ReadIMU(self,x):
	
		r=0
		p=0
		y=0
	
	
		#Faire une moyenne des x  donnees
		
		if imu.IMURead():
			#time.sleep(.5)
			data = imu.getIMUData()
			fusionPose = data["fusionPose"]
#			print("r: %f p: %f y: %f" %(math.degrees(fusionPose[0]),
			#math.degrees(fusionPose[1]),math.degrees(fusionPose[2])))
			r = math.degrees(fusionPose[0])			
			p  = math.degrees(fusionPose[1])
			y = math.degrees(fusionPose[2])
		
			if abs(r) < ANGLE_MAX:
                                self.roll = r
                        else:
                                self.roll = ANGLE_MAX * (r/abs(r))

                        if abs(p) < ANGLE_MAX:
                                self.pitch  = p
                        else:
                                self.pitch = ANGLE_MAX * (p/abs(p))

                        if abs(y) < ANGLE_MAX:
                                self.yaw = y
                        else:
                                self.yaw = ANGLE_MAX * (y/abs(y))*360			


	
			
