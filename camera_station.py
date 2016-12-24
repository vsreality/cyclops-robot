from robotplatform.camerastation import CameraStation
from Phidgets.PhidgetException import PhidgetException

Y_SERVO = 7
Z_SERVO = 3

# Main
if __name__ == "__main__":
	try:
		CamStation = CameraStation(393323, Y_SERVO, Z_SERVO)
		CamStation.init(30, 30)
		CamStation.setPosition(45, 45)
		CamStation.setPosition(135, 135)
		CamStation.setPosition(90, 90)

	except PhidgetException as e:
		print "Phidget Exception {}: {}".format(e.code, e.details)
		CamStation.stop()

	CamStation.stop()
	print "Done."
