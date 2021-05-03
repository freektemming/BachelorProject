# Script that makes plot of Teff and (Vrot or Mdot)

from data import *
from plots import *
from plotstyles import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np

# ------ Plot Teff against Vrot and Mdot ------
def Teff(model1, model2, model3, model4, number, plottype, ms):

    # plot name of model in legend
    if number == '20':
        model = '20 M$_{\odot}$'
        mass = '20'
    if number == '30':
        model = '30 M$_{\odot}$'
        mass = '30'
    if number == '40':
        model = '40 M$_{\odot}$'
        mass = '40'
    if number == '50':
        model = '50 M$_{\odot}$'
        mass = '50'
    if number == '60':
        model = '60 M$_{\odot}$'
        mass = '60'

    if ms == True:
        # main sequence limit
        lim1 = model1.mainsequence()
        lim2 = model2.mainsequence()
        lim3 = model3.mainsequence()
        lim4 = model4.mainsequence()

        # gravitaton limit colorbar
        min1 = model1.get_grav(lim1)
        max1 = model1.get_max_grav()
        limit = '_ms'
        folder = 'MainSequence'
    else:
        # full simulation
        lim1 = len(model1.age)
        lim2 = len(model2.age)
        lim3 = len(model3.age)
        lim4 = len(model4.age)

        min1 = model1.get_min_grav()
        max1 = model1.get_max_grav()
        limit = ''
        folder = 'FullSimulation'

    # ------ Set Plot Style ------
    default_style()
    fig, ax, colormap = vrotmdot(plottype, model)

    # plot mas loss
    if plottype == 'Mdot':

        # plot line
        ax.plot(model1.Teff[0:lim1], model1.logMdot[0:lim1], lw = 1, color = 'black', linestyle = 'solid', label = 'Vink 01')
        ax.plot(model2.Teff[0:lim2], model2.logMdot[0:lim2], lw = 1, color = 'black', linestyle = 'dashed', label = 'Vink 18')
        ax.plot(model3.Teff[0:lim3], model3.logMdot[0:lim3], lw = 1, color = 'black', linestyle = 'dashdot', label = 'Leuven')
        ax.plot(model4.Teff[0:lim4], model4.logMdot[0:lim4], lw = 1, color = 'black', linestyle = 'dotted', label = 'Krticka')
        
        # plot colors
        ims1 = ax.scatter(model1.Teff[0:lim1], model1.logMdot[0:lim1], c= model1.logg[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
        ims2 = ax.scatter(model2.Teff[0:lim2], model2.logMdot[0:lim2], c= model2.logg[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
        ims3 = ax.scatter(model3.Teff[0:lim3], model3.logMdot[0:lim3], c= model3.logg[0:lim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
        ims4 = ax.scatter(model4.Teff[0:lim4], model4.logMdot[0:lim4], c= model4.logg[0:lim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
        cbar1 = fig.colorbar(ims1, ax = ax)
        cbar1.set_label('log(g) [m / $s^2$]')
        ax.legend(shadow = False, edgecolor = 'k')
    
    # plot rotational velocity
    if plottype == 'Vrot':

        # plot line
        ax.plot(model1.Teff[0:lim1], model1.vrot[0:lim1], lw = 1, color = 'black', linestyle = 'solid', label = 'Vink 01')
        ax.plot(model2.Teff[0:lim2], model2.vrot[0:lim2], lw = 1, color = 'black', linestyle = 'dashed', label = 'Vink 18')
        ax.plot(model3.Teff[0:lim3], model3.vrot[0:lim3], lw = 1, color = 'black', linestyle = 'dashdot', label = 'Leuven')
        ax.plot(model4.Teff[0:lim4], model4.vrot[0:lim4], lw = 1, color = 'black', linestyle = 'dotted', label = 'Krticka')
        
        # plot colors
        ims1 = ax.scatter(model1.Teff[0:lim1], model1.vrot[0:lim1], c= model1.logg[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
        ims2 = ax.scatter(model2.Teff[0:lim2], model2.vrot[0:lim2], c= model2.logg[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
        ims3 = ax.scatter(model3.Teff[0:lim3], model3.vrot[0:lim3], c= model3.logg[0:lim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
        ims4 = ax.scatter(model4.Teff[0:lim4], model4.vrot[0:lim4], c= model4.logg[0:lim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
        cbar1 = fig.colorbar(ims1, ax = ax)
        cbar1.set_label('log(g) [m / $s^2$]')
        ax.legend(shadow = False, edgecolor = 'k')

    fig.tight_layout()
    plt.savefig(f'Plots/{datafolder}/Teff{plottype}/{folder}/{plottype}{mass}{limit}.png')
    #plt.show()

lim = True

Teff(vink01_20, vink18_20, leuven_20, krticka_20, '20', 'Mdot', ms=lim)
Teff(vink01_30, vink18_30, leuven_30, krticka_30, '30', 'Mdot', ms=lim)
Teff(vink01_40, vink18_40, leuven_40, krticka_40, '40', 'Mdot', ms=lim)
Teff(vink01_50, vink18_50, leuven_50, krticka_50, '50', 'Mdot', ms=lim)
Teff(vink01_60, vink18_60, leuven_60, krticka_60, '60', 'Mdot', ms=lim)

Teff(vink01_20, vink18_20, leuven_20, krticka_20, '20', 'Vrot', ms=lim)
Teff(vink01_30, vink18_30, leuven_30, krticka_30, '30', 'Vrot', ms=lim)
Teff(vink01_40, vink18_40, leuven_40, krticka_40, '40', 'Vrot', ms=lim)
Teff(vink01_50, vink18_50, leuven_50, krticka_50, '50', 'Vrot', ms=lim)
Teff(vink01_60, vink18_60, leuven_60, krticka_60, '60', 'Vrot', ms=lim)

lim = False

Teff(vink01_20, vink18_20, leuven_20, krticka_20, '20', 'Mdot', ms=lim)
Teff(vink01_30, vink18_30, leuven_30, krticka_30, '30', 'Mdot', ms=lim)
Teff(vink01_40, vink18_40, leuven_40, krticka_40, '40', 'Mdot', ms=lim)
Teff(vink01_50, vink18_50, leuven_50, krticka_50, '50', 'Mdot', ms=lim)
Teff(vink01_60, vink18_60, leuven_60, krticka_60, '60', 'Mdot', ms=lim)

Teff(vink01_20, vink18_20, leuven_20, krticka_20, '20', 'Vrot', ms=lim)
Teff(vink01_30, vink18_30, leuven_30, krticka_30, '30', 'Vrot', ms=lim)
Teff(vink01_40, vink18_40, leuven_40, krticka_40, '40', 'Vrot', ms=lim)
Teff(vink01_50, vink18_50, leuven_50, krticka_50, '50', 'Vrot', ms=lim)
Teff(vink01_60, vink18_60, leuven_60, krticka_60, '60', 'Vrot', ms=lim)