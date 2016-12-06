import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plot

def Ps(t): #Power as a function of time
    tao = 0.85 # the transmittance factor
    ISC = 1.367 # kW/m^2, intensity of the extraterrestrial normal solar radiation
    r0 = 149597890. # km, mean sun-earth distance

    epsilon = 0.0167 # eccentricity ratio of the earth

    dn = 196. # day number
    phi = .492 # radians, latitude of location
#formulas
    w = np.pi - (np.pi*t/12.0)
    delta = ((23.45*np.pi*np.sin(360.0*(284.+ dn)/365.0))/180.0)
    theta = (np.pi/2.) - (np.arccos(np.sin(phi)*np.sin(delta)) + np.cos(phi)*np.cos(delta)*np.c
    alpha = 2.*np.pi*(dn-4.0)/365.0
    r = r0* (1.-(epsilon**2.))/(1.+(epsilon*np.cos(alpha)))
    I0n = ISC*((r0/r)**2)
    if (I0n * tao * np.sin(theta)) < 0
        solar_power = 0
    else
        solar_power = I0n * tao * np.sin(theta)
    return solar_power
N = 50 #Number of points to calculate for the graph
time = np.linspace(0,24, N)
#initialize arrays for graphs
P_s = np.zeros(N)
Es = np.zeros(N)
P_ms = np.ones(N)
for i in np.arange(np.size(time)):
    P_s[i] = Ps(i)
for i in range(N):
    Es[i] = integrate.quad(Ps,0,time[i])[0]

Pms = (integrate.quad(Ps,0,24))/24.
P_ms = Pms * P_ms
fig = plt.figure(1)
plt.plot(time,P_s,label=’Solar power’)
plt.plot(time,P_ms,label=’Mean power’)
plt.legend()
fig = plt.figure(2)
plt.plot(time,Es,lable=’Total power received’)
plt.legend(loc=’lower right’)
plt.show()
print(’Total energy in a day: ’, Es[-0], ’Wh/m^2’)