# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 10:39:51 2018

@author: Student
"""

import numpy as np
#import matplotlib.pyplot as plt

# c = 299792458 # speed of light
c  = 1 # speed of light: set to 1 for simplicity, first

# position, velocity, time in Bob's frame
x = 0.5
v = 0.5
t = 1


def calc_gamma(v): # function to calculate gamma (the Lorentz factor), given v
    return 1/np.sqrt(1-(v/c)**2)


def lorentz(t,x,v): # function to calculate lorentz transformation, given t, x, and v
    g = calc_gamma(v) # calculate the Lorentz factor using the function above
    xt = g*(x-v*t) # calculate x'
    tt = g*(t-v*x/c**2) # calculate t'
    return tt, xt # return calculated vlaues


def inverseLorentz(c, x, v, t):
    g = calc_gamma(v)
    tt, xt = lorentz(t, x, v)
    tA = g*(tt + (v*xt)/c**2)
    xA = g*(xt + v*tt)
    return tA, xA


tt, xt = lorentz(t,x,v)
print("tt =", round(tt, 3), "\nxt =", xt)

tA, xA = inverseLorentz(c, x, v, t) 
print("t =", round(tA, 2), "\nx =", round(xA,2))

# write functions to calculate Lorentz transformations