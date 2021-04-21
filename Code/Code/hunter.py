# code to plot a Hunter diagram

from data import *
from plots import *
from plotstyles import *
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


def plot(model1, model2):

    # ------ Set Plot Style ------
    default_style()
    fig, ax, colormap = hunterNH()

    # limits were main sequence ends
    lim1 = model1.mainsequence()
    lim2 = model2.mainsequence()
    
    # plot line
    ax.plot(model1.vrot[0:lim1], model1.lognit[0:lim1], lw = 1, linestyle = 'solid', color = 'black', label= 'vink01')
    ax.plot(model2.vrot[0:lim2], model2.lognit[0:lim2], lw = 1, linestyle = 'dashed', color = 'black', label= 'vink18')
    
    # plot colors
    ims1 = ax.scatter(model1.vrot[0:lim1], model1.lognit[0:lim1], c= model1.age[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_age(lim1))
    ims2 = ax.scatter(model2.vrot[0:lim2], model2.lognit[0:lim2], c= model2.age[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model2.get_min_bar(), vmax = model1.get_age(lim1))
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    ax.legend(shadow = False, edgecolor = 'k')

    fig.tight_layout()
    #plt.show()
    plt.savefig('Plots/Hunter/NH+12.png')

plot(vink01, vink18)