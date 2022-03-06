import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as stats
import math


#100 instances of normal sine wave 

#Define Omega 
omega = 37*np.pi/11

#generate sequence of X
x_seq=np.arange(1, 101, 1)


#Define noise

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 0*sigma, mu + 1*sigma, 100)
noise= 25*x


#Define SCI

Sci= sorted(np.random.uniform(-np.pi,np.pi,100))
print(Sci)

#define Signal function 
Y= 100*np.cos(omega*x_seq + Sci)  + noise

#Plot Wave 
plt.plot(x_seq,Y)

plt.show()


#Corrupted Sinewave 

#100 instances of normal sine wave 

#Define Omega 
omega = 37*np.pi/11

#generate sequence of X
x_seq=np.arange(1, 101, 1)