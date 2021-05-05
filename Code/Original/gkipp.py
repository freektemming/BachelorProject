import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib.ticker import FormatStrFormatter 
from matplotlib.collections import LineCollection
import numpy as np
import math
from pylab import *


#----------------------------------------------
sigma = 5.67051 * pow(10,-5)  # cgs
Rsun = 6.957 * pow(10,10)
Lsun = 3.828 * pow(10,33)
Msun = 1.99 * pow(10,33)
pi = np.pi

#model
mes = ['models/L4.wg'] 

k = ['green','yellow']

num = len(mes)


rc('axes', linewidth=5)
fig1, ax1 = plt.subplots(1,1, figsize=(20,15))
#ax1.set_ylim(20,40)
#ax1.set_ylim(0,1.05)
ax1.set_ylim(0,1.1)
#ax1.set_xlim(12,16)
ax1.set_xlabel('time [Myr]', size=44)
#ax.set_ylabel('$\mathrm{\log (L/L_{\odot}) }$', size=44)
ax1.set_ylabel('m / M$_{\star}$', size = 44)  #_{\odot}}$', size=44)
ax1.tick_params(labelsize=36, width = 5, length = 32)



####

##### GENEC files input ######  
#for i in range(0,num) : 
data = np.genfromtxt(mes[0],skip_header=0)  
 #-----------------------------------------------
coreh = data[:,51]
xd = coreh.compress((coreh>coreh[0]*0.99).flat) 
x = len(xd)


age = data[x:,1]
leng = len(age)
mass = data[x:,2]
nmass = mass / np.max(mass) 
#lognmass = np.log10(nmass)
logM = np.log10(mass)
logMdot = data[x:,18]
logTeff = data[x:,4]
logL = data[x:,3]


convcore = data[x:,16] 
cv1b = data[x:,69] * nmass
cv1t = data[x:,70] * nmass
cv2b = data[x:,71] * nmass
cv2t = data[x:,72] * nmass
cv3b = data[x:,73] * nmass
cv3t = data[x:,74] * nmass
cv4b = data[x:,75] * nmass
cv4t = data[x:,76] * nmass

time = age /pow(10,6)

#time = np.log10(time)

#=========  END of GENEC file input ==============================================================

#cbar.set_ticks([1,2,3])
#cbar.ax.set_yticklabels(['10', '100', '1000'])

#ax1.plot(time, nmass, linewidth = 14, color = 'red')
ax1.plot(time, convcore, linewidth = 14, color = 'lime')
#ax1.plot(time, cv1b, linewidth = 14, color = 'blue')
#ax1.plot(time, cv1t, linewidth = 14, color = 'blue')
#ax1.plot(time, cv2b, linewidth = 14, color = 'gray')
#ax1.plot(time, cv2t, linewidth = 14, color = 'gray')
#ax1.plot(time, cv3b, linewidth = 12, color = 'lime')
#ax1.plot(time, cv3t, linewidth = 12, color = 'lime')
#ax1.plot(time, cv4b, linewidth = 12, color = 'red')
#ax1.plot(time, cv4t, linewidth = 12, color = 'red')

ax1.fill_between(time, cv1b, cv1t, color = 'blue', hatch = '///')
ax1.fill_between(time, cv2b, cv2t, color = 'gray', hatch = '///')
#ax1.fill_between(time, cv2t, cv2t, color = 'gray', hatch = '///')

#ax1.fill_between(time, cv2t, cv3b, color = 'gray', hatch = '///')
#ax1.fill_between(time, cv3b, cv3t, color = 'lime', hatch = '///')
#ax1.fill_between(time, cv4b, cv4t, color = 'red', hatch = '///')

ax1.plot(time, nmass, linewidth = 14, color = 'red')

ax1.text(3, 0.2, 'convective core', color = 'white', size = 44)
ax1.text(3, 0.8, 'radiative envelope', color = 'black', size = 44)

ax1.set_title('model L4', size = 44)

#plt.show()
plt.savefig('plots/L4Kipp.png')



