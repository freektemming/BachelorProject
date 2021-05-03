# script to plot kippenhahn diagrams

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

# ----- Function to Plot Labels on Axis
def multicolor_ylabel(ax,list_of_strings,list_of_colors,axis='x',anchorpad=0,**kw):
    """this function creates axes labels with multiple colors
    ax specifies the axes object where the labels should be drawn
    list_of_strings is a list of all of the text items
    list_if_colors is a corresponding list of colors for the strings
    axis='x', 'y', or 'both' and specifies which label(s) should be drawn"""
    from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, HPacker, VPacker

    # x-axis label
    if axis=='x' or axis=='both':
        boxes = [TextArea(text, textprops=dict(color=color, ha='left',va='bottom',**kw)) 
                    for text,color in zip(list_of_strings,list_of_colors) ]
        xbox = HPacker(children=boxes,align="center",pad=0, sep=5)
        anchored_xbox = AnchoredOffsetbox(loc=3, child=xbox, pad=anchorpad,frameon=False,bbox_to_anchor=(0.2, -0.09),
                                          bbox_transform=ax.transAxes, borderpad=0.)
        ax.add_artist(anchored_xbox)

    # y-axis label
    if axis=='yleft' or axis=='both':
        boxes = [TextArea(text, textprops=dict(color=color, ha='left',va='bottom',rotation=90,**kw)) 
                     for text,color in zip(list_of_strings[::-1],list_of_colors) ]
        ybox = VPacker(children=boxes,align="center", pad=0, sep=50)
        anchored_ybox = AnchoredOffsetbox(loc=3, child=ybox, pad=anchorpad, frameon=False, bbox_to_anchor=(-.20, 0.05), 
                                          bbox_transform=ax.transAxes, borderpad=0.)
        ax.add_artist(anchored_ybox)
    
    # y-axis label
    if axis=='yright' or axis=='both':
        boxes = [TextArea(text, textprops=dict(color=color, ha='left',va='bottom',rotation=90,**kw)) 
                     for text,color in zip(list_of_strings[::-1],list_of_colors) ]
        ybox = VPacker(children=boxes,align="center", pad=0, sep=30)
        anchored_ybox = AnchoredOffsetbox(loc=3, child=ybox, pad=anchorpad, frameon=False, bbox_to_anchor=(1.1, 0.05), 
                                          bbox_transform=ax.transAxes, borderpad=0.)
        ax.add_artist(anchored_ybox)


# ------ Mass Fractions and Convection ------
def massconv(model, zams, mid, tams, number, mass, ms):

    if ms == True:
        # main sequence limit
        lim = model.mainsequence()
        limit = '_ms'
        folder = 'MainSequence'
    else:
        # full simulation
        lim = len(model.age)
        limit = ''
        folder = 'FullSimulation'

    # ------ Set Plot Style ------
    default_style()
    fig, ax, colormap = kippenhahn(number, mass)

    # list for x-axis structure plot
    baseZ = zams.age()
    baseM = mid.age()
    baseT = tams.age()

    BaseZams = [baseZ] * len(zams.normR)
    BaseMid = [baseM] * len(mid.normR)
    BaseTams = [baseT] * len(tams.normR)
    
    # ------ Plot Lines ------
    ax.plot(model.time[0:lim], model.ntoth1[0:lim], color = 'deeppink', label = 'Hydrogen')
    ax.plot(model.time[0:lim], model.ntothe[0:lim], color = 'darkred', label = 'Helium')
    
    # ------ Plot Colors ------
    ims1 = ax.scatter(BaseZams, zams.normM * model.nmass[zams.model() - model.x], c= zams.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 6, zorder = 2)
    ims2 = ax.scatter(BaseMid, mid.normM * model.nmass[mid.model() - model.x], c= mid.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 6, zorder = 2)
    ims3 = ax.scatter(BaseTams, tams.normM * model.nmass[tams.model() - model.x], c= tams.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 6, zorder = 2)
    # cbar1 = fig.colorbar(ims1, ax = ax)
    # cbar1.set_label('Zones')

    # ------ Fill Planes ------
    ax.fill_between(model.time[0:lim], model.convtop[0:lim], model.nmass[0:lim], alpha = 0.5, color = 'grey', hatch = '///')
    ax.fill_between(model.time[0:lim], 0, model.convective_core[0:lim], alpha = 0.2, color = 'grey', hatch = '///')

    # ------ Text ------
    ax.text(1.3, 0.2, 'Convective core', fontweight = 'bold')
    ax.text(1, 0.8, 'Radiative envelope', fontweight = 'bold')

    # ------ Plot Colors On Axis ------
    multicolor_ylabel(ax,('Hydrogen','Helium'),('darkred','deeppink'),axis='yleft',size=14,weight='bold')
    multicolor_ylabel(ax,('Convection','Overshoot','Radiation'),('lightblue','seagreen','navy'),axis='yright',size=14,weight='bold')

    # ------ Show ------
    #plt.legend(shadow = False, edgecolor = 'k')
    fig.tight_layout()
    #plt.show()

    plt.savefig(f'Plots/{datafolder}/Kippenhahn/{folder}/Kip{number}_{mass}{limit}.png')

# ====== Mass Conv ======
lim = True

# # ------ Vink 01 Plots ------
# massconv(vink01_20, vink01_20z, vink01_20m, vink01_20t, '1', '20', ms=lim)
# massconv(vink01_30, vink01_30z, vink01_30m, vink01_30t, '1', '30', ms=lim)
# massconv(vink01_40, vink01_40z, vink01_40m, vink01_40t, '1', '40', ms=lim)
# massconv(vink01_50, vink01_50z, vink01_50m, vink01_50t, '1', '50', ms=lim)
# massconv(vink01_60, vink01_60z, vink01_60m, vink01_60t, '1', '60', ms=lim)

# # ------ Vink 18 Plots ------
# massconv(vink18_20, vink18_20z, vink18_20m, vink18_20t, '2', '20', ms=lim)
# massconv(vink18_30, vink18_30z, vink18_30m, vink18_30t, '2', '30', ms=lim)
# massconv(vink18_40, vink18_40z, vink18_40m, vink18_40t, '2', '40', ms=lim)
# massconv(vink18_50, vink18_50z, vink18_50m, vink18_50t, '2', '50', ms=lim)
# massconv(vink18_60, vink18_60z, vink18_60m, vink18_60t, '2', '60', ms=lim)

# # ------ Leuven Plots ------
# massconv(leuven_20, leuven_20z, leuven_20m, leuven_20t, '3', '20', ms=lim)
# massconv(leuven_30, leuven_30z, leuven_30m, leuven_30t, '3', '30', ms=lim)
# massconv(leuven_40, leuven_40z, leuven_40m, leuven_40t, '3', '40', ms=lim)
# massconv(leuven_50, leuven_50z, leuven_50m, leuven_50t, '3', '50', ms=lim)
# massconv(leuven_60, leuven_60z, leuven_60m, leuven_60t, '3', '60', ms=lim)

# # ------ Krticka Plots ------
# massconv(krticka_20, krticka_20z, krticka_20m, krticka_20t, '4', '20', ms=lim)
# massconv(krticka_30, krticka_30z, krticka_30m, krticka_30t, '4', '30', ms=lim)
# massconv(krticka_40, krticka_40z, krticka_40m, krticka_40t, '4', '40', ms=lim)
# massconv(krticka_50, krticka_50z, krticka_50m, krticka_50t, '4', '50', ms=lim)
# massconv(krticka_60, krticka_60z, krticka_60m, krticka_60t, '4', '60', ms=lim)


def plotcore(model1, model2, model3, model4, number, ms):

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

        # age limit colorbar
        min1 = model1.get_min_bar()
        max1 = model1.get_age(lim1)
        limit = '_ms'
        folder = 'MainSequence'
    else:
        # full simulation
        lim1 = len(model1.age)
        lim2 = len(model2.age)
        lim3 = len(model3.age)
        lim4 = len(model4.age)

        min1 = model1.get_min_bar()
        max1 = model1.get_max_bar()
        limit = ''
        folder = 'FullSimulation'
    # ------ Set Plot Style ------
    default_style()
    fig, ax, colormap = Core(model)
    
    # ------ Plot Lines ------
    ax.plot(model1.time[0:lim1], model1.convective_core[0:lim1], lw = 1, color = 'black', linestyle = 'solid', label = 'Vink 01')
    ax.plot(model2.time[0:lim2], model2.convective_core[0:lim2], lw = 1, color = 'black', linestyle = 'dashed', label = 'Vink 18')
    ax.plot(model3.time[0:lim3], model3.convective_core[0:lim3], lw = 1, color = 'black', linestyle = 'dashdot', label = 'Leuven')
    ax.plot(model4.time[0:lim4], model4.convective_core[0:lim4], lw = 1, color = 'black', linestyle = 'dotted', label = 'Krticka')
    
    # ------ Plot Colors ------
    # ims1 = ax.scatter(model1.Teff[0:lim1], model1.logL[0:lim1], c= model1.age[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    # ims2 = ax.scatter(model2.Teff[0:lim2], model2.logL[0:lim2], c= model2.age[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    # ims3 = ax.scatter(model3.Teff[0:lim3], model3.logL[0:lim3], c= model3.age[0:lim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    # ims4 = ax.scatter(model4.Teff[0:lim4], model4.logL[0:lim4], c= model4.age[0:lim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    # cbar1 = fig.colorbar(ims1, ax = ax)
    # cbar1.set_label('Age [Myr]')

        # ------ Show ------
    plt.legend(shadow = False, edgecolor = 'k')
    fig.tight_layout()
    #plt.show()

    plt.savefig(f'Plots/{datafolder}/Kippenhahn/Core/{folder}/Core{number}{limit}.png')

lim = False
plotcore(vink01_20, vink18_20, leuven_20, krticka_20, '20', ms=lim)
plotcore(vink01_30, vink18_30, leuven_30, krticka_30, '30', ms=lim)
plotcore(vink01_40, vink18_40, leuven_40, krticka_40, '40', ms=lim)
plotcore(vink01_50, vink18_50, leuven_50, krticka_50, '50', ms=lim)
plotcore(vink01_60, vink18_60, leuven_60, krticka_60, '60', ms=lim)
lim = True
plotcore(vink01_20, vink18_20, leuven_20, krticka_20, '20', ms=lim)
plotcore(vink01_30, vink18_30, leuven_30, krticka_30, '30', ms=lim)
plotcore(vink01_40, vink18_40, leuven_40, krticka_40, '40', ms=lim)
plotcore(vink01_50, vink18_50, leuven_50, krticka_50, '50', ms=lim)
plotcore(vink01_60, vink18_60, leuven_60, krticka_60, '60', ms=lim)






# =========================================
# ------ Mass Fractions and Elements ------
def mass(model1,model2, ms):

    if ms == True:
        # main sequence limit
        lim1 = model1.mainsequence()
        lim2 = model2.mainsequence()
        limit = '_ms'
    else:
        # full simulation
        lim1 = len(model1.age)
        lim2 = len(model1.age)
        limit = ''

    # ------ Set Plot Style ------
    default_style()
    #plt.style.use('dark_background')
    fig, ax, colormap = kippenhahn()

    # list for x-axis structure plot
    BaseZams = [0.0648] * len(zams.normR)
    BaseMid = [3.12] * len(mid.normR)
    BaseTams = [4.76] * len(tams.normR)
    
    # ------ Plot Lines ------
    ax.plot(model1.time[0:lim1], model1.convective_core[0:lim1], linestyle = 'dashed', color = 'black', label = 'Convective Core')
    #ax.plot(model1.time[0:lim1], model1.convtop[0:lim1], linestyle = 'dotted', color = 'black', label = 'Convective Top')

    # ------ Plot Colors ------
    ims1 = ax.scatter(BaseZams, zams.normM * model1.nmass[63 - 57], c= zams.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 6, zorder = 2)
    ims2 = ax.scatter(BaseMid, mid.normM * model1.nmass[107 - 57], c= mid.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 6, zorder = 2)
    ims3 = ax.scatter(BaseTams, tams.normM * model1.nmass[200 - 57], c= tams.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 6, zorder = 2)
    # cbar1 = fig.colorbar(ims1, ax = ax)
    # cbar1.set_label('Zones')

    # ------ Fill Planes ------
    
    ax.fill_between(model1.time[0:lim1], model1.botsurfh1[0:lim1], model1.ntoth1[0:lim1], alpha = 0.6, color = 'darkgreen')
    ax.fill_between(model1.time[0:lim1], 0, model1.botsurfh1[0:lim1], alpha = 0.6, color = 'lime')

    ax.fill_between(model1.time[0:lim1], model1.nmass[0:lim1], model1.nhemin[0:lim1], alpha = 0.6, color = 'darkred')
    ax.fill_between(model1.time[0:lim1], model1.nhemin[0:lim1], model1.ntotheminsurfmin[0:lim1], alpha = 0.6, color = 'red')

    ax.fill_between(model1.time[0:lim1], model1.ntoth1[0:lim1], model1.surfcartoplim[0:lim1], alpha = 0.6, color = 'navy')
    ax.fill_between(model1.time[0:lim1], model1.surfcartoplim[0:lim1], model1.surfnittoplim[0:lim1], alpha = 0.6, color = 'pink')
    ax.fill_between(model1.time[0:lim1], model1.surfnittoplim[0:lim1], model1.surfoxtoplim[0:lim1], alpha = 0.6, color = 'black')
    # ------ Text ------
    #ax.text(1.3, 0.2, 'Convective core', fontweight = 'bold')
    #ax1.text(1.3, 0.56, 'Convective mix 1', fontweight = 'bold')
    #ax.text(1.3, 0.9, 'Convective mix 2', fontweight = 'bold')
    # ax1.text(1, 0.8, 'Radiative envelope', fontweight = 'bold')

    # ------ Plot Colors On Axis ------
    multicolor_ylabel(ax,('H','H$_{\mathregular{surf}}$','He','He$_{\mathregular{surf}}$'),('darkred','red','darkgreen','lime'),axis='yleft',size=14,weight='bold')
    multicolor_ylabel(ax,('Convection','Overshoot','Radiation'),('lightgrey','seagreen','navy'),axis='yright',size=14,weight='bold')

    # ------ Show ------
    plt.legend(shadow = False, edgecolor = 'k')
    fig.tight_layout()
    plt.show()

    #plt.savefig(f'Plots/Kippenhahn/Kippenhahn{limit}.png')

#mass(vink01, vink18, ms=False)


def radius(model1,model2):

    # list for x-axis structure plot
    BaseZams = [0.0648] * len(zams.normR)
    BaseMid = [3.12] * len(mid.normR)
    BaseTams = [4.76] * len(tams.normR)

    colormap = plt.cm.cividis

    # main sequence limit
    lim1 = model1.mainsequence()
    lim2 = model2.mainsequence()

    #maxR = model1.maxlist(lim1)

    # ------ set figure ------
    fig1, ax1 = plt.subplots(1,1, figsize=(9,6.5))
    ax1.set_title('Kippenhahn Diagram Radius', size = 10)
    ax1.set_xlabel('Time [Myr]')
    ax1.set_ylabel('r (R$_{\star}$)')

    ax1.set_xticks([0.0648,3.12,4.76])
    ax1.set_xticklabels(['Zams', 'Mid','Tams'], fontweight = 'bold')

    # ------ Plot Lines ------
    #ax1.plot(model1.time[0:lim1], model1.czradius[0:lim1], linewidth = 3, color = 'black', label = 'Conv Core Top')
    ax1.plot(model1.time[0:lim1], model1.R[0:lim1], linewidth = 3, color = 'black', label = 'R')

    # ------ Plot Colors ------
    ims1 = ax1.scatter(BaseZams, zams.R, c= zams.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 5, zorder = 4)
    ims2 = ax1.scatter(BaseMid, mid.R, c= mid.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 5, zorder = 4)
    ims3 = ax1.scatter(BaseTams, tams.R, c= tams.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 5, zorder = 4)
   
    cbar1 = fig1.colorbar(ims1, ax = ax1)
    cbar1.set_label('Zones')
    
    # ------ Fill Planes ------
    ax1.fill_between(model1.time[0:lim1], 0, model1.czradius[0:lim1], alpha = 0.9, color = 'grey', hatch = '///')

    # ------ Text ------
    plt.text(2, 0.1, 'convective core', fontweight = 'bold')

    # ------ Show ------
    plt.legend(shadow = False, edgecolor = 'k')
    fig1.tight_layout()
    #plt.savefig('Plots/Kippenhahn/KipRadius.png')
    plt.show()


#radius(vink01, vink18)

# Plot for 2 Kippenhahn diagrams: mass and radius
def sub(model1, model2):

    # ------ Figure ------
    fig, (ax1, ax2) = plt.subplots(2)
    
    # list for x-axis structure plot
    BaseZams = [0.0648] * len(zams.normR)
    BaseMid = [3.12] * len(mid.normR)
    BaseTams = [4.76] * len(tams.normR)
    colormap = plt.cm.cividis

    # main sequence limit
    lim1 = model1.mainsequence()
    lim2 = model2.mainsequence()

    # ------ Plot 1 ------
    ax1.set_xlabel('Time [Myr]')
    ax1.set_ylabel('m / M$_{\star}$')
    ax1.set_title('Kippenhahn Diagram Mass', size = 10)

    ax1.set_xticks([0.0648,3.12,4.76])
    ax1.set_xticklabels(['Zams', 'Mid','Tams'], fontweight = 'bold')

    # Plot Lines
    #ax1.plot(model1.time[0:lim1], model1.nczradius[0:lim1], linestyle = 'dashed', linewidth = 1, color = 'lime', label = 'Conv Core Radius')
    #ax1.plot(vink01.time[0:lim1], vink01.convective_core[0:lim1], linewidth = 3, color = 'pink', label = 'core')

    # Plot Colors
    ims1 = ax1.scatter(BaseZams, zams.normR, c= zams.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 5, zorder = 2)
    ims2 = ax1.scatter(BaseMid, mid.normR, c= mid.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 5, zorder = 2)
    ims3 = ax1.scatter(BaseTams, tams.normR, c= tams.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 5, zorder = 2)
    cbar1 = fig.colorbar(ims1, ax = ax1)
    cbar1.set_label('Zones')

    # Fill Planes
    ax1.fill_between(model1.time[0:lim1], model1.convtop[0:lim1], model1.nmass[0:lim1], alpha = 0.5, color = 'grey', hatch = '///')
    ax1.fill_between(model1.time[0:lim1], 0, model1.convective_core[0:lim1], alpha = 0.2, color = 'grey', hatch = '///')
    #ax1.fill_between(model1.time[0:lim1], model1.convbot2[0:lim1], model1.convtop2[0:lim1], alpha = 0.2, color = 'lime', hatch = '///')

    # Tekst
    ax1.text(1, 0.2, 'Convective core', fontweight = 'bold')
    ax1.text(1, 0.8, 'Radiative envelope', fontweight = 'bold')
    #ax1.text(3.2, 0.5, 'Overshooting / Convection', fontweight = 'bold')

    # ------ Plot 2 ------
    ax2.set_title('Kippenhahn Diagram Radius', size = 10)
    ax2.set_xlabel('Time [Myr]')
    ax2.set_ylabel('log(r / R$_{\star}$)')

    ax2.set_ylim(-1,2)

    ax2.set_xticks([0.0648,3.12,4.76])
    ax2.set_xticklabels(['Zams', 'Mid','Tams'], fontweight = 'bold')

    # Plot Lines
    #ax1.plot(model1.time[0:lim1], model1.czradius[0:lim1], linewidth = 3, color = 'black', label = 'Conv Core Top')
    ax2.plot(model1.time[0:lim1], model1.logR[0:lim1], linewidth = 3, color = 'black', label = 'r (R$_{\star}$)$')

    # Plot Colors 
    ims1 = ax2.scatter(BaseZams, zams.logR, c= zams.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 5, zorder = 4)
    ims2 = ax2.scatter(BaseMid, mid.logR, c= mid.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 5, zorder = 4)
    ims3 = ax2.scatter(BaseTams, tams.logR, c= tams.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 5, zorder = 4)
    cbar2 = fig.colorbar(ims1, ax = ax2)
    cbar2.set_label('Zones')
    
    # Fill Planes
    ax2.fill_between(model1.time[0:lim1], model1.logconvbot[0:lim1], model1.logczradius[0:lim1], alpha = 0.9, color = 'grey', hatch = '///')

    # Text 
    ax2.text(1, -0.5, 'Convective core', fontweight = 'bold', zorder = 5)

    # ------ Show ------
    #ax1.legend(shadow = False, edgecolor = 'k', loc = 'lower left')
    #ax2.legend(shadow = False, edgecolor = 'k')
    fig.tight_layout()
    plt.show()
    #plt.savefig('Plots/Kippenhahn/KipSub.png')

#sub(vink01, vink18)


# self.colors['clr_LightSkyBlue'], #Convection
# self.colors['clr_LightSteelBlue'], #Softened convection
# self.colors['clr_SlateGray'], # Overshoot
# self.colors['clr_Lilac'], #Semi convection
# self.colors['clr_LightSkyGreen'], #Thermohaline
# self.colors['clr_BrightBlue'], #Rotation
# self.colors['clr_Beige'], #Minimum
# self.colors['clr_Tan'] #Anonymous