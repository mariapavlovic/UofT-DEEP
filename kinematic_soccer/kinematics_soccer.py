import numpy as np
import matplotlib.pyplot as plt

# soccer player position vs. time data was taken from real data at
# http://home.ifi.uio.no/paalh/dataset/alfheim/

# the line of code below loads values from the text file player_pos.txt
# be sure to download this file from the Google Drive and keep it
# in the same folder as this script!
t,x,y = np.loadtxt('player_pos.txt')
# t is time, and x and y are the position of the player, in metres
# t, x, and y are arrays

print(x) # example: take a look at x
print("y =", y)
dt = 0.05 # time increment

# plot the x position and the y position
plt.plot(x,y) # plot the arrays x and y
plt.title('Soccer player x-y position')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()

plt.plot(t,x) # plot the arrays t and x
plt.title('Soccer player x position vs. time')
plt.xlabel('t (s)')
plt.ylabel('x position (m)')
plt.show()

plt.plot(t,y) # plot the arrays t and x
plt.title('Soccer player y position vs. time')
plt.xlabel('t (s)')
plt.ylabel('y position (m)')
plt.show()

n = len(t) # number of steps: length of t
v_x = np.zeros(n-1) # create an array to store velocity, make 1 element shorter
v_y = np.zeros(n-1) # create an array to store velocity, make 1 element shorter

for i in np.arange(n-1): # iterate over numbers: i = 0, 1, 2, ... n-2
    v_x[i] = (x[i+1]-x[i])/dt # calculate derivative at i
    v_y[i] = (y[i+1]-y[i])/dt # calculate derivative at i

plt.plot(t[:-1], v_x)
plt.title('Soccer player speed in x direction vs. time')
plt.xlabel('t (s)')
plt.ylabel('v_x (m/s)')
plt.show()

plt.plot(t[:-1], v_y)
plt.title('Soccer player speed in y direction vs. time')
plt.xlabel('t (s)')
plt.ylabel('v_y (m/s)')
plt.show()

x_int = np.zeros(n) # array to store integrated x value
x_int[0] = x[0] # initial value
y_int = np.zeros(n) # array to store integrated x value
y_int[0] = y[0] # initial value


for i in np.arange(n-1):
    x_int[i+1] = x_int[i] + v_x[i]*dt
    y_int[i+1] = y_int[i] + v_y[i]*dt

# alternative approach:
x_int_2 = x[0] + np.cumsum(v_x)*dt
y_int_2 = y[0] + np.cumsum(v_y)*dt

plt.plot(t, x_int)
plt.plot(t[:-1],x_int_2)
plt.plot(t,x)
plt.title('Comparison of integrated x-values to original x-values')
plt.show()

plt.plot(t, y_int)
plt.plot(t[:-1],y_int_2)
plt.plot(t,y)
plt.title('Comparison of integrated y-values to original y-values')
plt.show()


v = np.sqrt(v_x**2 + v_y**2)
plt.plot(v)
plt.title('Velocity')
plt.show()










