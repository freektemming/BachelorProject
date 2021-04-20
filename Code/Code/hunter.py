# code to plot a Hunter diagram

from classData import Data
from classStructure import Structure
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib.ticker import FormatStrFormatter 
from matplotlib.collections import LineCollection
import numpy as np
import math
from pylab import *


#------ Constants ------
sigma = 5.67051 * pow(10,-5)  # cgs
Rsun = 6.957 * pow(10,10)
Lsun = 3.828 * pow(10,33)
Msun = 1.99 * pow(10,33)
pi = np.pi

# ------ Models ------
vink01 = Data('../Data/40M_Vink01_out.data')
vink18 = Data('../Data/40M_Vink18_out.data')
zams = Structure('../Data/prof_ZAMS.data')
mid = Structure('../Data/prof_midMS.data')
tams = Structure('../Data/prof_tams.data')

def plot(model1, model2):

    # limits were main sequence ends
    lim1 = model1.mainsequence()
    lim2 = model2.mainsequence()
    
    colormap = plt.cm.plasma
    fig, ax = plt.subplots(1,1, figsize=(9,6.5))

    ax.set_xlabel('V$_{\mathrm{rot}}$')
    ax.set_ylabel('N/N$_{\star}$')
    ax.set_title('Hunter',fontweight='bold')


    # plot line
    ax.plot(model1.vrot[0:lim1], model1.nnit[0:lim1], lw = 1, linestyle = 'solid', color = 'black', label= 'vink01')
    ax.plot(model2.vrot[0:lim2], model2.nnit[0:lim2], lw = 1, linestyle = 'dashed', color = 'black', label= 'vink18')
    
    # plot colors
    ims1 = ax.scatter(model1.vrot[0:lim1], model1.nnit[0:lim1], c= model1.age[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_age(lim1))
    ims2 = ax.scatter(model2.vrot[0:lim2], model2.nnit[0:lim2], c= model2.age[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model2.get_min_bar(), vmax = model1.get_age(lim1))
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    ax.legend(shadow = False, edgecolor = 'k')

    fig.tight_layout()
    #plt.show()
    plt.savefig('Plots/Hunter/normnit.png')

plot(vink01, vink18)