from pygamepad import Gamepad, UnpluggedError
from time import sleep

class RobotGamepad(Gamepad):

	def onKeyDown(self, key):
		print "onKeyDown: {}".format(key)


	def onKeyUp(self, key):
		print "onKeyUp: {}".format(key)

	def onLeftStickChange(self, position):
		print "Left stick position: ({}, {})".format(position.x, position.y)

	def onRightStickChange(self, position):
		print "Right stick position: ({}, {})".format(position.x, position.y)

	def onLeftTriggerChange(self, value):
		print "onLeftTriggerChange: {}".format(value)

	def onRightTriggerChange(self, value):
		print "onRightTriggerChange: {}".format(value)

	def onPadChange(self, position):
		print "Pad position: ({}, {})".format(position.x, position.y)

if __name__ == "__main__":
	while True:
		try:
			controller = RobotGamepad()
			while True:
				controller.update()
		except UnpluggedError:
			print("Waiting for controller...")
			sleep(1)
		except KeyboardInterrupt:
			print "Done."
			break
		except:
			print "Something else happens."
			sleep(1)
