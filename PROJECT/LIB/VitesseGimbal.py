#!/usr/bin/python

import sys
import smbus
import math
import os

from Jay_class import Servo,Pid,Imu

import time




DELTA_T = 0.02-.005  #50 Hz
MIDDLE_VIT = 300
P = 0.15
I = 0.02
D = 0 #Always 0 for now if not you have to check the init pid
SET_ANGLE_ROLL = 0
SET_ANGLE_PITCH = 0
OFFSET_ROLL = -.8
OFFSET_PITCH = 3.285
acc=Imu()
sroll=Servo(0,-1,MIDDLE_VIT,MIDDLE_VIT)
spitch=Servo(1,1,MIDDLE_VIT,MIDDLE_VIT)
pidroll = Pid(P,I,D)
pidpitch = Pid(P,I,D)
PRINTTIME = 0
WaitTime = 0
i=0
INIT_END=0
#Programme d'initialisation de la camera sans tout decalisser (pid vraiment lent)
acc.ReadIMU(1)
acc.ReadIMU(1)
pidroll.finderror(acc.roll,SET_ANGLE_ROLL)
pidpitch.finderror(acc.pitch,SET_ANGLE_PITCH)
OldTime = time.time()
#Initialisation Cycle
while i == 1: # Minimum of 10 cycle for init 
	
	acc.ReadIMU(1)
	pidroll.finderror(acc.roll,SET_ANGLE_ROLL)
	pidpitch.finderror(acc.pitch,SET_ANGLE_PITCH)

	pidroll.Ki= .01
	pidroll.Kp = .3

	pidpitch.Ki = pidroll.Ki
	pidpitch.Kp = pidroll.Kp

	sroll.vit_move_pid(pidroll)
	spitch.vit_move_pid(pidpitch)
	print sroll.position	
	print"JINITIALISE !!!!", pidroll.error	
	if abs(pidroll.error * pidpitch.error) < .3 :
		i=i+1
	else: 
		i=0

INIT_END=1
print "ON COMMENCE LE PROGRAMME"
pidroll.Ki = I
pidroll.Kp = P
pidpitch.Ki = pidroll.Ki
pidpitch.Kp = pidroll.Kp
#time.sleep(2)

fichier = open("Data.txt","w")

while INIT_END==1:

	#Remember the time to calculate the lenght of the cycle
	NewTime = time.time()
	
	#ReFresh IMU Data
	acc.ReadIMU(1)

	#Find error on each axis
	pidroll.finderror(acc.roll-OFFSET_ROLL,SET_ANGLE_ROLL)
	pidpitch.finderror(acc.pitch-OFFSET_PITCH,SET_ANGLE_PITCH)

	if WaitTime > DELTA_T:

		#Move each servo and calculate the pid value
		sroll.vit_move_pid(pidroll)
		spitch.vit_move_pid(pidpitch)
#		print "Lenght of a full cycle", time.time()-OldTime		
		#Measure the time 
		OldTime= time.time()
		
	#Wait to have a constant cycle lenght
	WaitTime = (NewTime-OldTime)
	if WaitTime < 0:
		if PRINTTIME == 1:
			print "La valeur d'attente est inferieur a 0", WaitTime


 	print acc.roll-OFFSET_ROLL, acc.pitch-OFFSET_PITCH
 
	fichier.write(str(acc.roll) + " " + str(acc.pitch) + " " + str(WaitTime))
		
	#print the lenght of a full cycle (Suppose to be equal to DELTA_T)

#	print "Lenght of a full cycle : ", (time.time()-OldTime)
	
	#Print the roll angle
	
#	print"Roll angle", pidroll.error * pidpitch.error
			

	

