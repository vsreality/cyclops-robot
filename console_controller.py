# Import
from platform.mecanum import MecanumPlatform
from time import sleep
from sys import stdin

# Main
if __name__ == "__main__":
	print("=== Console controller ===")
	print("Commands: forward, back, left, right, rotate_left, rotate_right, stop, quit\n")
	robot = MecanumPlatform ()
	
	print "\nEnter command:"
	
	while(True):
		command = stdin.readline()
		command = command[:-1]
		
		if command == "forward":
			robot.Move(40)
		elif command == "back":
			robot.Move(-40)
		elif command == "left":
			robot.Left(30)
		elif command == "right":
			robot.Right(30)	
		elif command == "rotate_left":
			robot.RotateLeft(20)
		elif command == "rotate_right":
			robot.RotateRight(20)	
		elif command == "stop":
			robot.Stop()
		elif command =="quit":
			robot.Stop()
			break
		else:
			print ("Wrong command")
	
	print("DONE.")
