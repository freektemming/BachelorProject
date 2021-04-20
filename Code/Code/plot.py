# Script that makes plot

from classData import Data
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np
from plots import *

# ------ Models ------
vink01 = Data('../Data/40M_Vink01_out.data')
vink18 = Data('../Data/40M_Vink18_out.data')

def plot(model1, model2, ms):

    if ms == 'ms':
        # main sequence limit
        lim1 = model1.mainsequence()
        lim2 = model2.mainsequence()
        min1 = model1.get_min_bar()
        max1 = model1.get_age(lim1)
        min2 = model1.get_min_bar()
        max2 = model1.get_age(lim1)
        limit = '_ms'
    else:
        # full simulation
        lim1 = len(model1.age)
        lim2 = len(model1.age)
        min1 = model1.get_min_bar()
        max1 = model1.get_max_bar()
        min2 = model1.get_min_bar()
        max2 = model1.get_max_bar()
        limit = ''
    
    colormap = plt.cm.plasma
    fig, ax = plt.subplots(1,1, figsize=(9,6.5))

    ax.set_xlabel('log (L / L$_{\odot}$)')
    ax.set_ylabel('M$_{\mathrm{dot}}$ [M$_{\odot}$ yr$^{-1}$]')
    ax.set_title('L vs Mdot',fontweight='bold')

    # plot line
    ax.plot(model1.logL[0:lim1], model1.Mdot[0:lim1], lw = 1, linestyle = 'solid', color = 'black', label= 'vink01')
    ax.plot(model2.logL[0:lim2], model2.Mdot[0:lim2], lw = 1, linestyle = 'dashed', color = 'black', label= 'vink18')
    
    # plot colors
    ims1 = ax.scatter(model1.logL[0:lim1], model1.Mdot[0:lim1], c= model1.age[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims2 = ax.scatter(model2.logL[0:lim2], model2.Mdot[0:lim2], c= model2.age[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min2, vmax = max2)
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    ax.legend(shadow = False, edgecolor = 'k')

    fig.tight_layout()
    #plt.show()
    plt.savefig(f'Plots/Week1/L&Mdot{limit}.png')

plot(vink01, vink18, 'ms')