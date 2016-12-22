from pygamepad import Gamepad, UnpluggedError
from robotplatform.mecanum import MecanumPlatform
from time import sleep
from Phidgets.PhidgetException import PhidgetException

def normalize (V):
	sum = reduce(lambda x, y: abs(x)+abs(y), V)
	if sum == 0:
		return V
	elif sum > 100.0:
		k = 100.0/sum
		return [k*v for v in V]
	else:
		return V

class RobotGamepad(Gamepad):
	def __init__(self, robot):
		super(RobotGamepad, self).__init__()
		self.robot = robot
		self.move_vec = [0.0, 0.0, 0.0]
		self.speed = 20 # %

	def onKeyDown(self, key):
		print "onKeyDown: {}".format(key)

	def onKeyUp(self, key):
		print "onKeyUp: {}".format(key)

	def onLeftStickChange(self, position):
		print "Left stick position: ({}, {})".format(position.x, position.y)
		self.move_vec[0] = position.y * self.speed
		self.move_vec[2] = -position.x * self.speed
		self.robot.move(self.move_vec)

	def onRightStickChange(self, position):
		print "Right stick position: ({}, {})".format(position.x, position.y)
		self.move_vec[1] = -position.x * self.speed
		self.robot.move(self.move_vec)

	def onLeftTriggerChange(self, value):
		print "onLeftTriggerChange: {}".format(value)

	def onRightTriggerChange(self, value):
		print "onRightTriggerChange: {}".format(value)

	def onPadChange(self, position):
		print "Pad position: ({}, {})".format(position.x, position.y)
		self.move_vec[0] = -position.y * self.speed
		self.move_vec[1] = position.x * self.speed
		self.robot.move(self.move_vec)

if __name__ == "__main__":
	robot = MecanumPlatform ()
	while True:
		try:
			controller = RobotGamepad(robot)
			while True:
				controller.update()
		except UnpluggedError:
			print "Waiting for controller..."
			robot.stop()
			sleep(1)
		except PhidgetException as e:
			print ("Phidget Exception %i" % (e.code))
			sleep(2)
		except KeyboardInterrupt:
			print "Done."
			break
