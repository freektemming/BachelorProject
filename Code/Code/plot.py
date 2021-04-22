# Script that makes plot

from data import *
from plots import *
from plotstyles import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np


def plot(model1, model2, ms):

    # ------ Set Plot Style ------
    default_style()
    fig, ax, colormap = HeC()

    if ms == True:
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

    # plot line
    ax.plot(model1.HeC[0:lim1], model1.CC[0:lim1], lw = 1, linestyle = 'solid', color = 'black', label= 'vink01')
    ax.plot(model2.HeC[0:lim2], model2.CC[0:lim2], lw = 1, linestyle = 'dashed', color = 'black', label= 'vink18')
    
    # plot colors
    ims1 = ax.scatter(model1.HeC[0:lim1], model1.CC[0:lim1], c= model1.age[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims2 = ax.scatter(model2.HeC[0:lim2], model2.CC[0:lim2], c= model2.age[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min2, vmax = max2)
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    ax.legend(shadow = False, edgecolor = 'k')

    fig.tight_layout()
    #plt.show()
    plt.savefig(f'Plots/Week1/He&Car{limit}.png')

plot(vink01, vink18, ms=False)