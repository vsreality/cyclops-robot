
from time import sleep
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Events.Events import AttachEventArgs, DetachEventArgs, ErrorEventArgs, CurrentChangeEventArgs, PositionChangeEventArgs, VelocityChangeEventArgs
from Phidgets.Devices.AdvancedServo import AdvancedServo
from Phidgets.Devices.Servo import ServoTypes
from Phidgets.Phidget import PhidgetLogLevel

HARDWARE_CONNECTION_TIMEOUT = 10000

class CameraStation(object):
	def __init__(self, serial_number, yservo, zservo):
		self.controller = AdvancedServo()
		self.serial_number = serial_number
		self.yservo = yservo
		self.zservo = zservo

	def initServo(self, index, vel):
		self.controller.setServoType(index, ServoTypes.PHIDGET_SERVO_HITEC_HS322HD)

		self.controller.setEngaged(index, False)
		maxAcceleration = self.controller.getAccelerationMax(index)
		maxVelocity = self.controller.getVelocityMax(index)

		self.controller.setAcceleration(index, maxAcceleration*0.5)
		self.controller.setVelocityLimit(index, maxVelocity*vel/100)

		self.controller.setEngaged(index, True)
		self.controller.setPosition(index, 90)
		sleep(0.5)
		print "Servo {} initialized.".format(index)


	def init(self, yvel, zvel):
		# Opening servo controller
		self.controller.openPhidget(self.serial_number)
		self.controller.waitForAttach(HARDWARE_CONNECTION_TIMEOUT)
		self.initServo(self.yservo, yvel)
		self.initServo(self.zservo, zvel)

	def setPosition (self, yangle, zangle):
		# Calculate movement time for both servos
		dy = abs(yangle - self.controller.getPosition(self.yservo))
		dz = abs(zangle - self.controller.getPosition(self.zservo))
		ty = dy/self.controller.getVelocityLimit(self.yservo)
		tz = dz/self.controller.getVelocityLimit(self.zservo)
		# Set new position for each servo
		self.controller.setPosition(self.yservo, yangle)
		self.controller.setPosition(self.zservo, zangle)
		# Wait until motors sets to desire positions
		sleep(max(ty, tz))

	def stop(self):
		self.controller.setEngaged(self.yservo, False)
		self.controller.setEngaged(self.zservo, False)

	def __del__(self):
		self.stop()
		self.controller.closePhidget()
