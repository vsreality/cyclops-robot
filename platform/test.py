from math import pi

Rwheel = 0.1 # m
motor_speed = 152 # Rotation/min

Wmax = 2*pi*motor_speed/60 #Rad/sec
Vmax = Rwheel * Wmax
# Wmax -> 100% power

def wheels_velocity(Vx, Vy, Wz):
	Rwh = 0.1
	lx = 0.3
	ly = 0.3
	return [1/Rwh * (Vx - Vy - (lx+ly)*Wz),
			1/Rwh * (Vx + Vy + (lx+ly)*Wz),
			1/Rwh * (Vx + Vy - (lx+ly)*Wz),
			1/Rwh * (Vx - Vy + (lx+ly)*Wz)]


Vx = 1
Vy = 1
Wz = 0
W =  wheels_velocity(Vx, Vy, Wz)

print "Wmax = %f rad/sec" % Wmax
print "Vmax = %f m/sec" % Vmax


print(str(W[0])+ "\t" + str(W[1]))
print(str(W[2])+ "\t" + str(W[3]))