#!/usr/bin/python
import sys
sys.path.append('AdafruitCode/Adafruit_PWM_Servo_Driver')
from Adafruit_PWM_Servo_Driver import PWM
import time


def findvalue(pulse,freq):
# Retrun tick value (/4096) for a given ms pulse lenght

                pulseLength = 1000000                   # 1,000,000 us per second
                pulseLength /= freq                    
                #print "%d us per period" % pulseLength
                pulseLength /= 4096                     # 12 bits of resolution
                #print "%d us per bit" % pulseLength
                pulse *= 1000
                pulse /= pulseLength
        	return pulse


class servo:

	def __init__(self,adr,freq,channel,POS_MIDDLE):
	
		#Frequency in hertz
		#Adress found with I2cdetect

		pwm = PWM(adr)
		pwm.setPWMFreq(freq)
		self.channel = channel
		self.pos = POS_MIDDLE

	def update(pwm,servo,valeur):
	
		#The value is between 500 and 750
		#Servo is an object with .num .npos(newposition)
		#pwm is the chip (straight the output of Init_servo_driver
		pwm.setPWM(servo.channel, 0, servo.npos)


