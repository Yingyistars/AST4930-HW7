import matplotlib.pyplot as plt
from astropy import units as u
import numpy as np
import astropy as ast

data = open("sed.txt","r")
lines = data.readlines()

#gets rid of the first 3 lines
for i in range(0,3):
    lines.pop(0)
    
wavelength = np.asarray([float(x.split(",")[0]) for x in lines]) * u.micron
luminosity = np.asarray([float(x.split(",")[1]) for x in lines]) * u.Lsun/u.micron

domain = []
graph_range = []

#restricts data to the values we care about for the integral
for line in lines:
    if float(line.split(",")[0]) >= 10 and float(line.split(",")[0]) <= 1000:
             domain.append(float(line.split(",")[0]))
             graph_range.append(float(line.split(",")[1]))
                
domain = np.flip(domain)
graph_range = np.flip(graph_range)
             
integral = np.trapz(graph_range,domain) * u.Lsun
integral = integral.to(u.erg/u.second)
print(integral)

fig, figure = plt.subplots()
figure.plot(wavelength.value,luminosity.value)
figure.set_xscale('log')
figure.set_yscale('log')
figure.set_xlabel("Wavelength (microns)")
figure.set_ylabel("Luminosity (Lsun/micron)")
figure.set_title("Wavelength vs. Luminosity")

plt.savefig('cai_brian_hw7.png')