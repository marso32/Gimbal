#!/usr/bin/python

import sys
import smbus
import math

from Jay_class import Servo,Pid,Imu
import time




DELTA_T = 0.005
MIDDLE_POS = 550
P = 1.5
I = 0.02
D = 0
SET_ANGLE_ROLL = 0
SET_ANGLE_PITCH = 0
acc=Imu()
sroll=Servo(0,-1,MIDDLE_POS,MIDDLE_POS)
spitch=Servo(1,1,MIDDLE_POS,MIDDLE_POS)
pidroll = Pid(P,I,D)
pidpitch = Pid(P,I,D)

t = time.time()

while 1:
	
	
	acc.ReadIMU(1)
	

	if time.time() - t > DELTA_T: 
		pidroll.finderror(acc.roll,SET_ANGLE_ROLL)
		pidpitch.finderror(acc.pitch,SET_ANGLE_PITCH)

		sroll.move_pid(pidroll)
		spitch.move_pid(pidpitch)
		t= time.time()
	  
		print "Roll angle",acc.roll	

	

