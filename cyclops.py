# Import
from time import sleep

from platform.mecanum import MecanumPlatform, PhidgetException
from vswebsoket.server import *
import json

# Server parameters
ip = '10.0.1.4'
port = 8080

def normalize (V):
	sum = reduce(lambda x, y: abs(x)+abs(y), V)
	if sum == 0:
		return V
	elif sum > 100.0:
		k = 100.0/sum
		return [k*v for v in V]
	else:
		return V

# Main
if __name__ == "__main__":
	robot = MecanumPlatform ()
	server = CWsServer('10.0.1.21', port)
	client = server.WaitForClient ()
	try:
		while True:
			msg = client.wait_message()
			if msg.type == CLOSE_MESSAGE:
				raise Exception()
			msg = json.loads(msg.data)
			keys = msg['keys']
			#print keys
			V = [0.0,0.0,0.0]
			if ord('W') in keys:
				V[0] += 60
			if ord('S') in keys:
				V[0] -= 60

			if ord('A') in keys:
				V[1] += 60
			if ord('D') in keys:
				V[1] -= 60

			if ord('Q') in keys:
				V[2] += 60
			if ord('E') in keys:
				V[2] -= 60
			print V
			V = normalize(V)
			print V
			robot.move(V)
	except:
		client.close()
