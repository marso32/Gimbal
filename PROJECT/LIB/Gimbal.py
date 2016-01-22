#!/usr/bin/python

import sys
import smbus
import math
import Acc
from myclass import servo,pid,acc
import time


DELTA_T = 0.05

s1=servo(0x40,100,0,550)
acc=imu(0x68)
while 1:
	acc.updateIMU()

	print acc.roll

