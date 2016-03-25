#!/usr/bin/python

import sys
import smbus
import math
from Adafruit_PWM_Servo_Driver import PWM
import os

from Jay_class import Servo,Pid,Imu

pwm=PWM(0x40)
pwm.setPWMFreq(50)
import time
VALEUR=320
i=275
while 1:
	pwm.setPWM(1,0,i)
	pwm.setPWM(0,0,i)
	i=i+1
	time.sleep(.02)
	print i
