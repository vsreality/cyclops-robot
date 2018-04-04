from inputs import DeviceManager, UnpluggedError, EVENT_MAP
import os, time

# Absolute
# ABS_HAT0X, ABS_HAT0Y (-1, 0, 1)
# ABS_X, ABS_Y, ABS_RX, ABS_RY,
# ABS_Z, ABS_RZ (0 - 255)

# Key
# BTN_TL, BTN_TR
# BTN_START, BTN_SELECT (0,1)
# BTN_NORTH, BTN_EAST, BTN_SOUTH, BTN_WEST (0,1)
# BTN_THUMBL, BTN_THUMBR

#Sync

keys_dictionary = {"BTN_NORTH":"Y",
					"BTN_EAST":"B",
					"BTN_SOUTH":"A",
					"BTN_WEST":"X",
					"BTN_TR":"RB",
					"BTN_TL":"LB",
					"BTN_THUMBL": "LS",
					"BTN_THUMBR": "RS",
					"BTN_START": "VIEW",
					"BTN_SELECT": "MENU"
					}

class Position(object):
	def __init__(self):
		self.x = 0
		self.y = 0


class Gamepad(object):
	def __init__(self, index=0):
		self.device_manager = DeviceManager()
		if len(self.device_manager.gamepads) > 0:
			self.gamepad = self.device_manager.gamepads[index]
		else:
			raise UnpluggedError("No gamepad connected")
		self.right_stick = Position()
		self.left_stick = Position()
		self.pad = Position()
		self.MAX_STICK_VALUE = 32768
		self.STICK_CHANGE_VALUE = self.MAX_STICK_VALUE/4

	def onKeyDown(self, key):
		pass

	def onKeyUp(self, key):
		pass

	def onLeftStickChange(self, position):
		pass

	def onRightStickChange(self, position):
		pass

	def onLeftTriggerChange(self, value):
		pass

	def onRightTriggerChange(self, value):
		pass

	def onPadChange(self, position):
		pass

	def update(self):
		events = self.gamepad.read();
		for event in events:
			if event.ev_type == "Key":
				if event.state == 1:
					self.onKeyDown(keys_dictionary[event.code])
				else:
					self.onKeyUp(keys_dictionary[event.code])

			elif event.ev_type == "Absolute":
				if event.code == "ABS_X":
					value = int(round(event.state / self.STICK_CHANGE_VALUE))
					if self.left_stick.x != value:
						self.left_stick.x = value
						self.onLeftStickChange(self.left_stick)

				elif event.code == "ABS_Y":
					value = int(round(event.state / self.STICK_CHANGE_VALUE))
					if self.left_stick.y != value:
						self.left_stick.y = value
						self.onLeftStickChange(self.left_stick)

				if event.code == "ABS_RX":
					value = int(round(event.state / self.STICK_CHANGE_VALUE))
					if self.right_stick.x != value:
						self.right_stick.x = value
						self.onRightStickChange(self.right_stick)

				elif event.code == "ABS_RY":
					value = int(round(event.state / self.STICK_CHANGE_VALUE))
					if self.right_stick.y != value:
						self.right_stick.y = value
						self.onRightStickChange(self.right_stick)

				elif event.code == "ABS_Z":
					self.onLeftTriggerChange(event.state)

				elif event.code == "ABS_RZ":
					self.onRightTriggerChange(event.state)

				elif event.code == "ABS_HAT0X":
					self.pad.x = event.state
					self.onPadChange(self.pad)

				elif event.code == "ABS_HAT0Y":
					self.pad.y = event.state
					self.onPadChange(self.pad)
