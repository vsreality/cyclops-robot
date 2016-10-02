#Basic imports
from ctypes import *
import sys

#Phidget specific imports
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Events.Events import AttachEventArgs, DetachEventArgs, ErrorEventArgs, CurrentChangeEventArgs, InputChangeEventArgs, VelocityChangeEventArgs
from Phidgets.Devices.MotorControl import MotorControl

#import methods for sleeping thread
from time import sleep
from Phidgets.Phidget import PhidgetLogLevel

from motor import Motor

# Front: 487360
# Back: 147360

#			 x^
#			  |
#	 |0|-----|1|
#	  |		  |
#	  |		  |
# y<-|2|-----|3|


def motorControlError(e):
	print("Motor Control %i: Phidget Error %i: %s" % (source.getSerialNum(), e.eCode, e.description))
	
def _BuildPhidgetsMotorController (serial_number):
	#Create an motorcontrol object
	try:
		motorControl = MotorControl()
		motorControl.setOnErrorhandler(motorControlError)
		motorControl.openPhidget(serial_number)
		motorControl.waitForAttach(10000)
		print ("Serial number: %i" % motorControl.getSerialNum())
		
	except RuntimeError as e:
		motorControl.closePhidget()
		print("Runtime Exception: %s" % e.details)
		print("Exiting....")
		exit(1)
	return motorControl
		
class MecanumPlatform:
	def __init__(self):
		self.front_controller =_BuildPhidgetsMotorController (487360)
		sleep (0.00125)
		self.back_controller =_BuildPhidgetsMotorController (147360)
	
		self.motors = [
			Motor(self.front_controller, 0, True),
			Motor(self.front_controller, 1, False),
			Motor(self.back_controller, 0, True),
			Motor(self.back_controller, 1, False)]
		
		acceleration = 50
		for motor in self.motors:
			motor.SetAcceleration(acceleration)
		
	def move(self, V):
		self.motors[0].SetVelocity(V[0]-V[1]-V[2])
		self.motors[1].SetVelocity(V[0]+V[1]+V[2])
		self.motors[2].SetVelocity(V[0]+V[1]-V[2])
		self.motors[3].SetVelocity(V[0]-V[1]+V[2])
		
	def forward(self, velocity):
		self.move([velocity, 0, 0])

	def backward(self, velocity):
		self.move([-velocity, 0, 0])

	def rotate_left(self, velocity):
		self.move([0, 0, velocity])
		
	def rotate_right(self, velocity):
		self.move([0, 0, -velocity])
		
	def left(self, velocity):
		self.move([0, velocity, 0])
		
	def right(self, velocity):
		self.move([0, -velocity, 0])
		
	def stop(self):
		self.move([0, 0, 0])
		
	def __del__(self):
		self.stop()
		self.front_controller.closePhidget()
		self.back_controller.closePhidget()

	
	
	