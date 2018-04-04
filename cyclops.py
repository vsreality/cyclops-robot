# Import
import time
import paho.mqtt.client as mqtt
from options import broker
from robotplatform.mecanum import MecanumPlatform

hardware = True
platform_velocity_topic = "robot/platform/velocity"
velocity_p = [-1, -1, -1]

def normalize (V):
	sum = reduce(lambda x, y: abs(x)+abs(y), V)
	if sum == 0:
		return V
	elif sum > 100.0:
		k = 100.0/sum
		return [k*v for v in V]
	else:
		return V

def on_connect(client, userdata, flags, rc):
	print "Connected with result code " + str(rc)
	client.subscribe(platform_velocity_topic)

def on_message(client, userdata, msg):
	global velocity_p
	if msg.topic == platform_velocity_topic:
		try:
			# Convert string vector to list
			strVector = msg.payload.split(',')
			if len(strVector) != 3:
				return
			velocity = [float(s) for s in strVector]
		except:
			return

		velocity = normalize(velocity)
		#print velocity
		if velocity_p != velocity:
			# Apply new velocity
			if hardware:
				robot.move(velocity)
			velocity_p = velocity

# Main
if __name__ == "__main__":
	try:
		print "Cyclops"
		if hardware:
			robot = MecanumPlatform()
		client = mqtt.Client()
		client.on_connect = on_connect
		client.on_message = on_message
		client.username_pw_set(broker["username"], broker["password"])

		client.connect(broker["host"], broker["port"], 60)
		# Start publishing
		client.loop_forever()

	except KeyboardInterrupt:
		# Clean up
		client.loop_stop()