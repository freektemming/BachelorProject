# code to plot a Hunter diagram

from classData import Data
#from data import *
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

# ------ Plot Nitrogen Main Sequence 4 Models 1 Mass ------
def huntermass(model1, model2, model3, model4, typ, number, ms):

    # mass for plot
    mass = number

    # ------ Set Plot Style ------
    default_style()
    if typ == 'N':
        fig, ax, colormap = hunter(mass)
    if typ =='NH':
        fig, ax, colormap = hunterNH(mass)

    if lim == True:
        # limits where main sequence ends
        lim1 = model1.mainsequence()
        lim2 = model2.mainsequence()
        lim3 = model3.mainsequence()
        lim4 = model4.mainsequence()
        #lim5 = model5.mainsequence()

        # gravitation limit colorbar
        min1 = model2.minlist(model2.mainsequence())
        max1 = model1.get_max_grav()
        limit = '_ms'
        folder = 'MainSequence'
    else:
        # full simulation
        lim1 = model1.end()
        lim2 = model2.end()
        lim3 = model3.end()
        lim4 = model4.end()

        min1 = model2.minlist(model2.end())
        max1 = model1.get_max_grav()
        limit = ''
        folder = 'FullSimulation'

    x1 = []
    y1 = []

    x2 = []
    y2 = []

    x3 = []
    y3 = []

    # log lines 3.8

    for b in range(len(model2.logg[0:lim2])):
        if model2.logg[b] < 3.8:
            x1.append(model2.vrot[b])
            y1.append(model2.lognit[b])
            break

    for a in range(len(model1.logg[0:lim1])):
        if model1.logg[a] < 3.8:
            x1.append(model1.vrot[a])
            y1.append(model1.lognit[a])
            break

    for d in range(len(model4.logg[0:lim4])):
        if model4.logg[d] < 3.8:
            x1.append(model4.vrot[d])
            y1.append(model4.lognit[d])
            break   


    for c in range(len(model3.logg[0:lim3])):
        if model3.logg[c] < 3.8:
            x1.append(model3.vrot[c])
            y1.append(model3.lognit[c])
            break

    # log lines 3.6

    for b in range(len(model2.logg[0:lim2])):
        if model2.logg[b] < 3.6:
            x2.append(model2.vrot[b])
            y2.append(model2.lognit[b])
            break

    for a in range(len(model1.logg[0:lim1])):
        if model1.logg[a] < 3.6:
            x2.append(model1.vrot[a])
            y2.append(model1.lognit[a])
            break

    for d in range(len(model4.logg[0:lim4])):
        if model4.logg[d] < 3.6:
            x2.append(model4.vrot[d])
            y2.append(model4.lognit[d])
            break   


    for c in range(len(model3.logg[0:lim3])):
        if model3.logg[c] < 3.6:
            x2.append(model3.vrot[c])
            y2.append(model3.lognit[c])
            break

    # log lines 3.4

    for b in range(len(model2.logg[0:lim2])):
        if model2.logg[b] < 3.4:
            x3.append(model2.vrot[b])
            y3.append(model2.lognit[b])
            break

    for a in range(len(model1.logg[0:lim1])):
        if model1.logg[a] < 3.4:
            x3.append(model1.vrot[a])
            y3.append(model1.lognit[a])
            break

    for d in range(len(model4.logg[0:lim4])):
        if model4.logg[d] < 3.4:
            x3.append(model4.vrot[d])
            y3.append(model4.lognit[d])
            break   


    for c in range(len(model3.logg[0:lim3])):
        if model3.logg[c] < 3.4:
            x3.append(model3.vrot[c])
            y3.append(model3.lognit[c])
            break

    # plot line
    if typ == 'N':
        ax.plot(model1.vrot[0:lim1], model1.lognnit[0:lim1], lw = 1, color = 'black', linestyle = 'solid', label = 'Vink 01')
        ax.plot(model2.vrot[0:lim2], model2.lognnit[0:lim2], lw = 1, color = 'black', linestyle = 'dashed', label = 'Vink 18')
        ax.plot(model3.vrot[0:lim3], model3.lognnit[0:lim3], lw = 1, color = 'black', linestyle = 'dashdot', label = 'Leuven')
        ax.plot(model4.vrot[0:lim4], model4.lognnit[0:lim4], lw = 1, color = 'black', linestyle = 'dotted', label = 'Krticka')

    if typ == 'NH':
        ax.plot(model1.vrot[0:lim1], model1.lognit[0:lim1], lw = 1, color = 'black', linestyle = 'solid', label = 'Vink 01')
        ax.plot(model2.vrot[0:lim2], model2.lognit[0:lim2], lw = 1, color = 'black', linestyle = 'dashed', label = 'Vink 18')
        ax.plot(model3.vrot[0:lim3], model3.lognit[0:lim3], lw = 1, color = 'black', linestyle = 'dashdot', label = 'Leuven')
        ax.plot(model4.vrot[0:lim4], model4.lognit[0:lim4], lw = 1, color = 'black', linestyle = 'dotted', label = 'Krticka')
        ax.plot(x1,y1, color='black')
        ax.plot(x2,y2, color='black')
        ax.plot(x3,y3, color='black')
        ax.text(60,y1[0] + 0.0025, 'log g = 3.8', rotation=3)
        ax.text(60,y2[0] + 0.008, 'log g = 3.6', rotation=11)
        ax.text(60,y3[0] + 0.013, 'log g = 3.4', rotation=18)

    # plot colors
    if typ == 'N':
        ims1 = ax.scatter(model1.vrot[0:lim1], model1.lognnit[0:lim1], c= model1.logg[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
        ims2 = ax.scatter(model2.vrot[0:lim2], model2.lognnit[0:lim2], c= model2.logg[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)       
        ims3 = ax.scatter(model3.vrot[0:lim3], model3.lognnit[0:lim3], c= model3.logg[0:lim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
        ims4 = ax.scatter(model4.vrot[0:lim4], model4.lognnit[0:lim4], c= model4.logg[0:lim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)       
        
    if typ == 'NH':
        ims1 = ax.scatter(model1.vrot[0:lim1], model1.lognit[0:lim1], c= model1.logg[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
        ims2 = ax.scatter(model2.vrot[0:lim2], model2.lognit[0:lim2], c= model2.logg[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)       
        ims3 = ax.scatter(model3.vrot[0:lim3], model3.lognit[0:lim3], c= model3.logg[0:lim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
        ims4 = ax.scatter(model4.vrot[0:lim4], model4.lognit[0:lim4], c= model4.logg[0:lim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)       
        
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('log(g) [m / $s^2$]')
    ax.legend(shadow = False, edgecolor = 'k')

    fig.tight_layout()

    if typ == 'N':
        plt.savefig(f'Plots/{datafolder}/Hunter/{folder}/Nitrogen/nit{mass}{limit}.png', dpi=200)
    if typ == 'NH':
        plt.savefig(f'Plots/{datafolder}/Hunter/{folder}/NH+12/NH{mass}{limit}.png', dpi=200)


# ----------------------- Call with all data files ----------------------------------
# both main sequence and full simulation, all datafolders
datalist = ['Z014Om2']#,'Z014Om4','Z014Om6','Z002Om2','Z002Om4','Z002Om6','Z007Om2','Z007Om4','Z007Om6']
for datafolder in datalist:

    print(datafolder)

    # Vink 01
    vink01_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/out.data')
    vink01_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/30/LOGS/out.data')
    vink01_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/40/LOGS/out.data')
    vink01_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/50/LOGS/out.data')
    vink01_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/60/LOGS/out.data')

    # Vink 18
    vink18_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/20/LOGS/out.data')
    vink18_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/30/LOGS/out.data')
    vink18_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/40/LOGS/out.data')
    vink18_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/50/LOGS/out.data')
    vink18_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/60/LOGS/out.data')

    # Leuven
    leuven_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/20/LOGS/out.data')
    leuven_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/30/LOGS/out.data')
    leuven_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/40/LOGS/out.data')
    leuven_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/50/LOGS/out.data')
    leuven_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/60/LOGS/out.data')

    # Krticka
    krticka_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/20/LOGS/out.data')
    krticka_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/30/LOGS/out.data')
    krticka_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/40/LOGS/out.data')
    krticka_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/50/LOGS/out.data')
    krticka_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/60/LOGS/out.data')
    
    # both main sequence and full simulation
    for i in range(2):
        if i == 0:
            lim = False
        if i == 1:
            lim = True

        print(lim)

        # Nitrogen
        huntermass(vink01_20, vink18_20, leuven_20, krticka_20, 'N', '20', ms=lim)
        huntermass(vink01_30, vink18_30, leuven_30, krticka_30, 'N', '30', ms=lim)
        huntermass(vink01_40, vink18_40, leuven_40, krticka_40, 'N', '40', ms=lim)
        huntermass(vink01_50, vink18_50, leuven_50, krticka_50, 'N', '50', ms=lim)
        huntermass(vink01_60, vink18_60, leuven_60, krticka_60, 'N', '60', ms=lim)

        # N/H + 12
        huntermass(vink01_20, vink18_20, leuven_20, krticka_20, 'NH', '20', ms=lim)
        huntermass(vink01_30, vink18_30, leuven_30, krticka_30, 'NH', '30', ms=lim)
        huntermass(vink01_40, vink18_40, leuven_40, krticka_40, 'NH', '40', ms=lim)
        huntermass(vink01_50, vink18_50, leuven_50, krticka_50, 'NH', '50', ms=lim)
        huntermass(vink01_60, vink18_60, leuven_60, krticka_60, 'NH', '60', ms=lim)