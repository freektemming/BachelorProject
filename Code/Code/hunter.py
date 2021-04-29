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

# ------ Plot Nitrogen Main Sequence 2 Models ------
def plot(model1, model2, typ):

    # ------ Set Plot Style ------
    default_style()
    if typ == 'N':
        fig, ax, colormap = hunter()
    if typ =='NH':
        fig, ax, colormap = hunterNH()

    # limits were main sequence ends
    lim1 = model1.mainsequence()
    lim2 = model2.mainsequence()
    
    # plot line
    if typ == 'N':
        ax.plot(model1.vrot[0:lim1], model1.nnit[0:lim1], lw = 1, linestyle = 'solid', color = 'black', label= 'vink01')
        ax.plot(model2.vrot[0:lim2], model2.nnit[0:lim2], lw = 1, linestyle = 'dashed', color = 'black', label= 'vink18')
    if typ == 'NH':
        ax.plot(model1.vrot[0:lim1], model1.lognit[0:lim1], lw = 1, linestyle = 'solid', color = 'black', label= 'vink01')
        ax.plot(model2.vrot[0:lim2], model2.lognit[0:lim2], lw = 1, linestyle = 'dashed', color = 'black', label= 'vink18')

    # plot colors
    if typ == 'N':
        ims1 = ax.scatter(model1.vrot[0:lim1], model1.nnit[0:lim1], c= model1.age[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_age(lim1))
        ims2 = ax.scatter(model2.vrot[0:lim2], model2.nnit[0:lim2], c= model2.age[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model2.get_min_bar(), vmax = model1.get_age(lim1))
    if typ == 'NH':
        ims1 = ax.scatter(model1.vrot[0:lim1], model1.lognit[0:lim1], c= model1.age[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_age(lim1))
        ims2 = ax.scatter(model2.vrot[0:lim2], model2.lognit[0:lim2], c= model2.age[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model2.get_min_bar(), vmax = model1.get_age(lim1))       
    
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    ax.legend(shadow = False, edgecolor = 'k')

    fig.tight_layout()
    #plt.show()

    if typ == 'N':
        plt.savefig('Plots/Hunter/normnit.png')
    if typ == 'NH':
        plt.savefig('Plots/Hunter/NH+12.png')

#plot(vink01, vink18, 'NH')


# ------ Plot Nitrogen Main Sequence 4 Models 1 Mass ------
def huntermass(model1, model2, model3, model4, typ, number):

    # mass for plot
    mass = number

    # # model for plot
    # if model == 1:
    #     model == 'Vink 01 Model'
    # if model == 2:
    #     model == 'Vink 18 Model'
    # if model == 3:
    #     model == 'Leuven Model'
    # if model == 4:
    #     model == 'Krticka Model'

    # ------ Set Plot Style ------
    default_style()
    if typ == 'N':
        fig, ax, colormap = hunter(mass)
    if typ =='NH':
        fig, ax, colormap = hunterNH(mass)

    # limits were main sequence ends
    lim1 = model1.mainsequence()
    lim2 = model2.mainsequence()
    lim3 = model3.mainsequence()
    lim4 = model4.mainsequence()
    #lim5 = model5.mainsequence()
    
    # plot line
    if typ == 'N':
        ax.plot(model1.vrot[0:lim1], model1.lognnit[0:lim1], lw = 1, color = 'black', linestyle = 'solid', label = 'Vink 01')
        ax.plot(model2.vrot[0:lim2], model2.lognnit[0:lim2], lw = 1, color = 'black', linestyle = 'dashed', label = 'Vink 18')
        ax.plot(model3.vrot[0:lim3], model3.lognnit[0:lim3], lw = 1, color = 'black', linestyle = 'dashdot', label = 'Leuven')
        ax.plot(model4.vrot[0:lim4], model4.lognnit[0:lim4], lw = 1, color = 'black', linestyle = 'dotted', label = 'Krticka')
        #ax.plot(model5.vrot[0:lim5], model5.nnit[0:lim5], lw = 1, color = 'black')

    if typ == 'NH':
        ax.plot(model1.vrot[0:lim1], model1.lognit[0:lim1], lw = 1, color = 'black', linestyle = 'solid', label = 'Vink 01')
        ax.plot(model2.vrot[0:lim2], model2.lognit[0:lim2], lw = 1, color = 'black', linestyle = 'dashed', label = 'Vink 18')
        ax.plot(model3.vrot[0:lim3], model3.lognit[0:lim3], lw = 1, color = 'black', linestyle = 'dashdot', label = 'Leuven')
        ax.plot(model4.vrot[0:lim4], model4.lognit[0:lim4], lw = 1, color = 'black', linestyle = 'dotted', label = 'Krticka')
        #ax.plot(model5.vrot[0:lim5], model5.lognit[0:lim5], lw = 1, color = 'black')

    # plot colors
    if typ == 'N':
        ims1 = ax.scatter(model1.vrot[0:lim1], model1.lognnit[0:lim1], c= model1.age[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_age(lim1))
        ims2 = ax.scatter(model2.vrot[0:lim2], model2.lognnit[0:lim2], c= model2.age[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_age(lim1))       
        ims3 = ax.scatter(model3.vrot[0:lim3], model3.lognnit[0:lim3], c= model3.age[0:lim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_age(lim1))
        ims4 = ax.scatter(model4.vrot[0:lim4], model4.lognnit[0:lim4], c= model4.age[0:lim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_age(lim1))       
        #ims5 = ax.scatter(model5.vrot[0:lim5], model5.nnit[0:lim5], c= model5.age[0:lim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_age(lim1))
        
    if typ == 'NH':
        ims1 = ax.scatter(model1.vrot[0:lim1], model1.lognit[0:lim1], c= model1.age[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_age(lim1))
        ims2 = ax.scatter(model2.vrot[0:lim2], model2.lognit[0:lim2], c= model2.age[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_age(lim1))       
        ims3 = ax.scatter(model3.vrot[0:lim3], model3.lognit[0:lim3], c= model3.age[0:lim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_age(lim1))
        ims4 = ax.scatter(model4.vrot[0:lim4], model4.lognit[0:lim4], c= model4.age[0:lim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_age(lim1))       
        #ims5 = ax.scatter(model5.vrot[0:lim5], model5.lognit[0:lim5], c= model5.age[0:lim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_age(lim1))
        
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    ax.legend(shadow = False, edgecolor = 'k')

    fig.tight_layout()
    #plt.show()

    if typ == 'N':
        plt.savefig(f'Plots/4x4/Hunter/Nitrogen/nit{mass}.png')
    if typ == 'NH':
        plt.savefig(f'Plots/4x4/Hunter/NH+12/NH{mass}.png')

# Nitrogen
huntermass(vink01_20, vink18_20, leuven_20, krticka_20, 'N', '20')
huntermass(vink01_30, vink18_30, leuven_30, krticka_30, 'N', '30')
huntermass(vink01_40, vink18_40, leuven_40, krticka_40, 'N', '40')
huntermass(vink01_50, vink18_50, leuven_50, krticka_50, 'N', '50')
huntermass(vink01_60, vink18_60, leuven_60, krticka_60, 'N', '60')

# N/H + 12
# huntermass(vink01_20, vink18_20, leuven_20, krticka_20, 'NH', '20')
# huntermass(vink01_30, vink18_30, leuven_30, krticka_30, 'NH', '30')
# huntermass(vink01_40, vink18_40, leuven_40, krticka_40, 'NH', '40')
# huntermass(vink01_50, vink18_50, leuven_50, krticka_50, 'NH', '50')
# huntermass(vink01_60, vink18_60, leuven_60, krticka_60, 'NH', '60')