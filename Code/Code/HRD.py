# Script that makes multiple HRD plots

from data import *
from plots import *
from plotstyles import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np


# ------ plot normal HRD ------
def hrd(model1, model2, ms):

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

    # ------ Set Plot Style ------
    default_style()
    fig, ax, colormap = HRD()

    # plot line
    ax.plot(model1.Teff[0:lim1], model1.logL[0:lim1], lw = 1, linestyle = 'solid', color = 'black', label= 'vink01')
    ax.plot(model2.Teff[0:lim2], model2.logL[0:lim2], lw = 1, linestyle = 'dashed', color = 'black', label= 'vink18')
    
    # plot colors
    ims1 = ax.scatter(model1.Teff[0:lim1], model1.logL[0:lim1], c= model1.age[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims2 = ax.scatter(model2.Teff[0:lim2], model2.logL[0:lim2], c= model2.age[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min2, vmax = max2)
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    ax.legend(shadow = False, edgecolor = 'k')

    fig.tight_layout()
    plt.savefig(f'Plots/Week1/HRD{limit}.png')
    #plt.show()

hrd(vink01, vink18, ms=False)

# ------ Plot multiple HRD ------
def subhrd(model1, model2):

    # ------ Set Plot Style ------
    default_style()
    fig, ax1, ax2, colormap = subHRD()

    # ------ first plot ------
    # plot line
    ax1.plot(model1.Teff, model1.logL, lw = 1, linestyle = '-', color = 'black', zorder=1)
    
    # plot colors
    ims1 = ax1.scatter(model1.Teff, model1.logL,c= model1.age, marker='o', edgecolors='none', s=200, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_max_bar())
    ims1 = ax1.scatter(model2.Teff, model2.logL,c= model2.age, marker='o', edgecolors='none', s=200, cmap=colormap, vmin = model2.get_min_bar(), vmax = model2.get_max_bar())
    cbar = fig.colorbar(ims1, ax = ax1)
    cbar.set_label('Age [Myr]')

    # ----- Second plot ------
    # plot line
    ax2.plot(model2.Teff, model2.logL, lw = 1, linestyle = '-', color = 'black', zorder=1)
    
    # plot colors
    ims2 = ax2.scatter(model2.Teff, model2.logL,c= model2.age, marker='o', edgecolors='none', s=200, cmap=colormap, vmin = model2.get_min_bar(), vmax = model2.get_max_bar())
    cbar = fig.colorbar(ims2, ax = ax2)
    cbar.set_label('Age [Myr]')

    fig.tight_layout()
    plt.savefig('Plots/Week1/HRD-sub.png')
    #plt.show()

subhrd(vink01, vink18)
