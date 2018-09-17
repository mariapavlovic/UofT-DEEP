# SHO: simple pendulum
import numpy as np
import matplotlib.pyplot as plt

# physical parameters
m = 4.4e-3 # mass: 4.4 g = 4.4e-3 kg
L = 20e-2 # 20 cm = 2e-1 m 
g = 9.81 # m/s**2, gravitational acceleration
n = 20001 #number of steps
t_tot = 20. # total time simulated (seconds)
dt = t_tot/(n-1) #time step (s)

# constant k (to simplify)
k = g/L

# initial angle in degrees
# try changing this
init_deg = 30

# initial conditions
theta_0 = init_deg*np.pi/180 # initial angle: 10 degrees = pi/18 radians
w_0 = 0. # Initial angular velocity (rad/s)

## initialize arrays
t = np.linspace(0.,t_tot,n) # Array of n points with start time of 0 s and end time of 20 s
theta = np.zeros(n) # angle array
w = np.zeros(n) # angular velocity array

theta_actual = np.zeros(n)
w_actual = np.zeros(n)

## set initial positions and initial velocities in arrays
theta[0] = theta_0
w[0] = w_0
theta_actual[0] = theta_0
w_actual[0] = w_0

## solve the ODE for the pendulum
for i in range(n-1):
    # simple pendulum: linear ode
    w[i+1] = w[i] - k*theta[i]*dt # update w based on theta
    theta[i+1] = theta[i] + w[i+1]*dt # update theta based on w

    # simple pendulum, no small-angle approximation
    w_actual[i+1] = w_actual[i] -k*np.sin(theta_actual[i])*dt
    theta_actual[i+1] = theta_actual[i] + w_actual[i+1]*dt


plt.plot(t,theta, label='approx.') # label argument is for the legend
plt.plot(t,theta_actual,label='no approx.')
plt.title('Angle vs time: with and without small-angle approximation')
plt.legend() # show the legend
plt.show()


plt.plot(t,w, label='approx')
plt.plot(t,w_actual, label='no approx')
plt.title('Angular velocity vs. time: with and without small-angle approximation')
plt.legend()
plt.show()

# maximum velocity
# linear velocity = angular velocity * radius
vmax = L*np.max(w_actual)
print('the maximum velocity is {} m/s'.format(vmax))

# conservation of energy

# kinetic; with and without small-angle approx.
K = 0.5*m*(L*w)**2
K_actual = 0.5*m*(L*w_actual)**2
# grav. potential; with and without approx.
U = m*g*L*(1-np.cos(theta))
U_actual = m*g*L*(1-np.cos(theta_actual))
# total energy
E = K+U
E_actual = K_actual + U_actual

plt.plot(t,K, label='K')
plt.plot(t,U, label='U')
plt.plot(t,K+U, label='K+U')
plt.title('Energy vs. time with small-angle approx.')
plt.legend()
plt.show()

dE_dt = (E[1:]-E[:-1])/dt
plt.plot(t[:-1],dE_dt)
plt.title('Time derivative of total energy for small-angle approximation')
plt.legend()
plt.show()

plt.plot(t,K_actual,label='K')
plt.plot(t,U_actual, label='U')
plt.plot(t,K_actual+U_actual,label='K+U')
plt.legend()
plt.title('Energy vs. time without small-angle approx')
plt.show()

dE_dt_actual = (E_actual[1:]-E_actual[:-1])/dt
plt.plot(t[:-1],dE_dt_actual)
plt.title('Time derivative of total energy without small-angle approximation')
plt.legend()
plt.show()

