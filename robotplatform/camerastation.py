
from time import sleep
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Events.Events import AttachEventArgs, DetachEventArgs, ErrorEventArgs, CurrentChangeEventArgs, PositionChangeEventArgs, VelocityChangeEventArgs
from Phidgets.Devices.AdvancedServo import AdvancedServo
from Phidgets.Devices.Servo import ServoTypes
from Phidgets.Phidget import PhidgetLogLevel

HARDWARE_CONNECTION_TIMEOUT = 10000
Y_SERVO = 7
Z_SERVO = 3

class CameraStation(object):
	def __init__(self, serial_number, yservo, zservo):
		self.controller = AdvancedServo()
		self.serial_number = serial_number
		self.yservo = yservo
		self.zservo = zservo

	def initServo(self, index, vel):
		print("Speed Ramping state: %s" % self.controller.getSpeedRampingOn(index))
		print("Stopped state: %s" % self.controller.getStopped(index))
		print("Engaged state: %s" % self.controller.getEngaged(index))

		self.controller.setServoType(index, ServoTypes.PHIDGET_SERVO_HITEC_HS322HD)

		self.controller.setEngaged(index, False)
		maxAcceleration = self.controller.getAccelerationMax(index)
		maxVelocity = self.controller.getVelocityMax(index)

		print "Max Velocity: {}".format(maxVelocity)
		print "Max Acceleration: {}".format(maxAcceleration)

		self.controller.setAcceleration(index, maxAcceleration*0.5)
		self.controller.setVelocityLimit(index, maxVelocity*vel/100)

		self.controller.setEngaged(index, True)
		self.controller.setPosition(index, 90)
		sleep(0.5)


	def initController(self, yvel, zvel):
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

	def closeController(self):
		self.controller.setEngaged(self.yservo, False)
		self.controller.setEngaged(self.zservo, False)
		self.controller.closePhidget()

try:
	CamStation = CameraStation(393323, Y_SERVO, Z_SERVO)
	CamStation.initController(20, 20)
	CamStation.setPosition(45, 45)
	CamStation.setPosition(135, 135)
	CamStation.setPosition(90, 90)

except PhidgetException as e:
	print "Phidget Exception {}: {}".format(e.code, e.details)
	CamStation.closeController()

CamStation.closeController()
print "Done."
