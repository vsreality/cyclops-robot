import numpy as np
import matplotlib.pyplot as plt
'''
a = np.arange(15).reshape(3, 5)
datapoints = 10
noize = 2*np.sin(np.arange(datapoints))
data = np.array([x * x - x for x in range(datapoints)])
measurments = data + noize
print data
print measurments
'''
iterations = 300
TrueValue =  np.arange(iterations) # np.full(iterations, 5)
Y = TrueValue + np.random.normal(0, 5, iterations)
T = np.arange(iterations)
print TrueValue
print Y
print T

EST = [0]
E_EST =  0.1
E_mear = 0.01

for i in range(1, iterations):
    KG = E_EST / (E_EST + E_mear)
    MEA = 0
    EST += [EST[-1] + KG*(Y[i]-EST[-1])]

    E_EST = (1-KG)*E_EST

print EST

plt.figure()
plt.plot(TrueValue,'b-',label='True value')
plt.plot(EST,'r-',label='Estimate')
plt.plot(Y,'k+',label='Measurment')
plt.legend()
plt.title('Estimate vs. iteration step', fontweight='bold')
plt.xlabel('Iteration')
plt.ylabel('Voltage')
plt.show()

'''
d_t = 1
X_0 = np.matrix([[0], [0]])
# Observation error
d_ax = 0.01
d_ay = 0.01

Y_km = [np.matrix('0.12; 0.21'),
        np.matrix('0.13; 0.27'),
        np.matrix('0.21; 0.41'),
        np.matrix('0.24; 0.53'),
        np.matrix('0.32; 0.58')]

# Process error
d_Px = 0.01
d_Py = 0.01
# Initial process covariance matrix
P_0 = np.matrix([[d_Px**2, 0],[0, d_Py**2]])
I = np.identity(2)
A = I
H = I
R = np.matrix([[d_ax, 0], [0, d_ay]])
C = I

# Initial state
X_k_1 = X_0
P_k_1 = P_0

for i in range(0, 5):
    # Prdictive covariance matrix
    P_kp = A*P_k_1*A.transpose()

    K = np.nan_to_num((P_kp*H) / (H*P_kp*H.transpose() + R))

    Y_k = C*Y_km[i]

    X_k = X_k_1 + K*(Y_k-H*X_k_1)
    P_k = (I - K*H)*P_kp
    print X_k

    X_kp = X_k
    P_k_1 = P_k
'''

'''
d_t = 1
X0 = np.matrix('0; 0; 1')
d_a = 0.05 # Sensor error
P_0 = np.matrix([[0,0,0],[0,0,0],[0, 0, d_a**2]])

A = np.matrix([[1, d_t, 0.5*d_t**2],[0, 1, d_t],[0, 0, 1]])
P_k = A*P_0*A.transpose()
H = np.matrix([[1,0,0],[0,1,0][0,0,1]])
R = np.matrix([[0,0,0],[0,0,0][0,0,d_a]])
K = (P_k*H) / H*P_k*H.transpose() + R
X_p = X0
X_k = X_p+K()
'''