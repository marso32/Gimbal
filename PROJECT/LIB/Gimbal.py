#!/usr/bin/python

import sys
import smbus
import math

import Acc
from Servo import servo 

"""class accelerometre:
	def init(ax,ay,az,gx,gy,gz,pitch,roll):
		ax=0
		ay=0
		az=0
		gx=0
		gy=0
		gz=0
		pitch=1
		roll=1
"""
DELTA_T = 0.05

s1=servo(0x40,100,0,550)
acc=imu(0x68)
while 1:
	acc.updateIMU()

	print acc.roll

