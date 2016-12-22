class Motor:
	def __init__(self, controller,  id, reverce=False):
		self.controller = controller;
		self.id = id
		if reverce:
			self.reverce = -1
		else:
			self.reverce = 1

	def SetVelocity(self, velocity):
		if velocity > 100.0:
			velocity = 100.0
		elif velocity < -100.0:
			velocity = -100.0
		self.controller.setVelocity(self.id, self.reverce*velocity)

	def SetAcceleration(self, acceleration):
		self.controller.setAcceleration(self.id, acceleration)
