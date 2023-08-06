import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import os
import seaborn as sns

#parameters in the differential equation of w. 
#While these parameters were included in the script, 
#they are not effective in our simulations as they are multiplificaiton terms set as 1.
a  = 1.
b  = 1.
c  = 1.

#This parameter correponds to /alpha in the equation. 
alpha  = 10.

#This parameter corresponds to k_K in the equation.
k = 10.

#offset in Vm. Note that this parameter does not affect the dynamics. 
vm0 = 1.5

#time step size
dt = 0.001

#time scale of the events
tscale = 60.

#max time to simulate
Tmax = 10.

tvec = np.arange(0, Tmax, dt)


#duration of electrical stimulation
ees_duration = 2.5

#tvec for electrical stimulaiton
t_ees = np.arange(0,(ees_duration*(Tmax/dt)/(Tmax*tscale))*dt,dt)

#initial parameter for v and w
vw0 = [-.5,-.5]

#external stimulation in v and w.
#v is membrane potential and w is recovery variables
Iv =  0.01
Iw = -0.075
I1 = np.array([Iv, Iw])/dt

#parameter for I when no electrical field is applied
I0 = [0,0]

#ODE
def f(vw, t):
    v, w = vw
    dvdt = k*((v+vm0) - alpha*(v+vm0)**3 + w) +Iv
    dwdt = a*(-(v+vm0) + b - c*w) +Iw
    return [dvdt, dwdt]

def Gauss(x, A, B):
    y = A*np.exp(-1*B*x**2)
    return y