from ClassData import Data
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

# ------ Models ------
vink01 = Data('../Data/40M_Vink01_out.data')
vink18 = Data('../Data/40M_Vink18_out.data')

def kip(model1,model2):

    # main sequence limit
    lim1 = 3090#model1.mainsequence()
    lim2 = model2.mainsequence()

    #rc('axes', linewidth=5)
    fig1, ax1 = plt.subplots(1,1, figsize=(9,6.5))
    #ax1.set_ylim(20,40)
    #ax1.set_ylim(0,1.05)
    #ax1.set_ylim(0,1.1)
    #ax1.set_xlim(12,16)
    ax1.set_xlabel('time [Myr]')
    #ax.set_ylabel('$\mathrm{\log (L/L_{\odot}) }$', size=44)
    ax1.set_ylabel('m / M$_{\star}$')  #_{\odot}}$', size=44)
    #ax1.tick_params(labelsize=36, width = 5, length = 32)

    ####

    #cbar.set_ticks([1,2,3])
    #cbar.ax.set_yticklabels(['10', '100', '1000'])

    #ax1.plot(vink01.time[0:lim1], vink01.nmass[0:lim1], linewidth = 3, color = 'red', label = 'nmass')
    ax1.plot(vink01.time[0:lim1], vink01.HC[0:lim1], linewidth = 3, color = 'black', label = 'H')
    ax1.plot(vink01.time[0:lim1], vink01.HeC[0:lim1], linewidth = 3, color = 'navy', label = 'He')
    ax1.plot(vink01.time[0:lim1], vink01.CC[0:lim1], linewidth = 3, color = 'green', label = 'C')
    # ax1.plot(vink01.time[0:lim1], vink01.NC[0:lim1], linewidth = 3, color = 'green', label = 'N')
    # ax1.plot(vink01.time[0:lim1], vink01.OC[0:lim1], linewidth = 3, color = 'darkred', label = 'O')
    
    #ax1.plot(vink01.time[0:lim1], vink01.convbot[0:lim1], linewidth = 3, color = 'blue', label = 'bot')
    ax1.plot(vink01.time[0:lim1], vink01.convtop[0:lim1], linewidth = 3, color = 'lime', label = 'conv-top')
    #ax1.plot(vink01.time[0:lim1], vink01.convective_core[0:lim1], linewidth = 3, color = 'pink', label = 'core')
    

    ax1.fill_between(vink01.time[0:lim1], vink01.convtop[0:lim1], vink01.nmass[0:lim1], alpha = 0.9, color = 'grey', hatch = '///')
    ax1.fill_between(vink01.time[0:lim1], 0, vink01.convective_core[0:lim1], alpha = 0.1, color = 'grey', hatch = '///')


    #ax1.fill_between(time, cv2t, cv3b, color = 'gray', hatch = '///')
    #ax1.fill_between(time, cv3b, cv3t, color = 'lime', hatch = '///')
    #ax1.fill_between(time, cv4b, cv4t, color = 'red', hatch = '///')

    #ax1.plot(vink01.time, vink01.nmass, linewidth = 5, color = 'red')

    plt.text(2, 0.2, 'convective core', fontweight = 'bold')
    plt.text(2, 0.8, 'radiative envelope', fontweight = 'bold')
    plt.text(3.5, 0.5, 'convective envelope?', fontweight = 'bold')

    ax1.set_title('Kip', size = 10)
    plt.legend(shadow = False, edgecolor = 'k', loc = 'upper right')

    fig1.tight_layout()
    plt.show()

    #print(model1.convective_core[0])
    #plt.savefig('plots/L4Kipp.png')

kip(vink01, vink18)
