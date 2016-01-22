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





