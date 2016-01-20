#!/usr/bin/python



import sys
import smbus
import math

bus = smbus.SMBus(1)
address = 0x68

class imu:
	def __init__(self,address):
		bus = smbus.SMBus(1)
		# Power management registers
		power_mgmt_1 = 0x6b
		power_mgmt_2 = 0x6c
	
		# Now wake the 6050 up as it starts in sleep mode
		bus.write_byte_data(address, power_mgmt_1, 0)
		self.address = address
		self.ax=0
                self.ay=0
                self.az=0
                self.gx=0
                self.gy=0
                self.gz=0
                self.pitch = 0
                self.roll = 0
		

	def updateIMU(self):
		#imu is an object that has 8 characteristics imu.ax .ay .az .gx .gy .gz .pitch .roll
		self.ax=read_word_2c(0x3b)/16384.0
		self.ay=read_word_2c(0x3d)/16384.0
		self.az=read_word_2c(0x3f)/16384.0
		self.gx=read_word_2c(0x43)/131
		self.gy=read_word_2c(0x45)/131 
		self.gz=read_word_2c(0x47)/131 
		self.pitch = -math.degrees(math.atan2(self.ax, dist(self.ay,self.az)))
		self.roll = math.degrees(math.atan2(self.ay, dist(self.ax,self.az)))

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
   
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
def dist(a,b):
    return math.sqrt((a*a)+(b*b))

