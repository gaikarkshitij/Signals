#-------
# Author - Kshitij Gaikar 
# problem - to generate 100 instances for normal and corrupte waves based on functions given
# date - 6th March 2022
#--------

from operator import mod
import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as stats
import math


#100 instances of normal sine wave # get 100 data points 

#Define Omega 
omega = 37*np.pi/11

#generate sequence of X
x_seq=np.arange(1, 101, 1)

#Define noise

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 0*sigma, mu + 1*sigma, 100)
noise= 25*stats.norm.pdf(x,mu,variance)

#Define SCI

Sci= sorted(np.random.uniform(-np.pi,np.pi,100))


#define Signal function 
Y= 100*np.cos(omega*x_seq + Sci)  + noise



#Corrupted Sinewave 

#100 instances of normal sine wave 

#Define Omega 
omega_corrupted = 37*np.pi/11

#generate sequence of X
x_seq_corrupted=np.arange(1, 101, 1)

#Define SCI_corrupted

SCI_corrupted= sorted(np.random.uniform(-np.pi,np.pi,100))


#Define Alpha 

Alpha= np.random.uniform(20,25,100)

#Define Additive A_of_n 
# Part 1 which has 50 percent probablity in three parts 
# find expected value or A and give in 50  percent probablity i.e multiply by 0.5

mu_1 = 0
variance_1 = 0.25
sigma_1 = math.sqrt(variance_1)
x_1 = np.linspace(mu_1 - 0*sigma_1, mu_1 + 1*sigma_1, 100)
noise_x_1= 0.3*stats.norm.pdf(x_1,mu_1,variance_1)

mu_2 = 0
variance_2 = 0.5
sigma_2 = math.sqrt(variance_2)
x_2 = np.linspace(mu_2 - 0*sigma_2, mu_2 + 1*sigma_2, 100)
noise_x_2= 0.3*stats.norm.pdf(x_2,mu_2,variance_2)

mu_3 = 0
variance_3 = 0.75
sigma_3 = math.sqrt(variance_3)
x_3 = np.linspace(mu_3 - 0*sigma_3, mu + 1*sigma_3, 100)
noise_x_3= 0.4*stats.norm.pdf(x_3,mu_3,variance_3)

#define PDF 
A_of_n= noise_x_1+noise_x_2+noise_x_3

#Get expectation 
E_of_A_of_n= (x_1*noise_x_1 + x_2*noise_x_2 + x_3*noise_x_3) 

#form 2 define directly by expectation given 

#Define K
K=np.arange(0, 1, 0.01)
E_of_AnK= 0.5*(abs(K+1)**1.4 - 2*abs(K)**1.4 + abs(K-1)**1.4)


#Define Noise Corrupted
noise_corrupted=Alpha*(0.5*E_of_A_of_n+ 0.5*E_of_AnK)

#Define Corrupted Noise function 
Y_corrupted= 100*np.cos(omega_corrupted*x_seq_corrupted + SCI_corrupted)  + noise_corrupted

#plot both function 

figure, axis = plt.subplots(2, 1)

# For Sine Function
axis[0].plot(x_seq,Y)
axis[0].set_title("Normal Sine Function")

# For Sine  Corrupted Function
axis[1].plot(x_seq_corrupted, Y_corrupted)
axis[1].set_title("Corrupted Sine Function")

# Combine all the operations and display
plt.show()