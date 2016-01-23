#!/usr/bin/python

import sys
import smbus
import math
import Acc



from Jay_class import servo,pid,imu
import time




DELTA_T = 0.05
MIDDLE_POS = 550
P = 0
I = 0
D = 0
SET_ANGLE_ROLL = 0
SET_ANGLE_PITCH = 0
acc=imu()
sroll=servo(0,1,MIDDLE_POS,MIDDLE_POS)
spitch=servo(1,1,MIDDLE_POS,MIDDLE_POS)
pidroll = pid(P,I,D)
pidpitch = pid(P,I,D)


while 1:
	t=time.time()
	
	imu.ReadIMU(acc,5)
	
	pidroll.finderror(acc.roll,SET_ANGLE_ROLL)
	pidpitch.finderror(acc.pitch,SET_ANGLE_PITCH)

	sroll.move_pid(pidroll)
	spitch.move_pid(pidpitch)
	
	delta_t = time.time()-t
	if delta_t > 0 :
		time.sleep(DELTA_T-delta_t)
		print delta_t
	else :
		print "L'intervalle de temps est trop faible"
	
	
	

