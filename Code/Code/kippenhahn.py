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
    #plt.show()

    plt.savefig(f'Plots/Kippenhahn/Kippenhahn{limit}.png')

mass(vink01, vink18, ms=False)


# ------ Mass Fractions and Elements ------
def massconv(model1,model2, ms):

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
    ax.plot(model1.time[0:lim1], model1.ntoth1[0:lim1], color = 'deeppink', label = 'Hydrogen')
    ax.plot(model1.time[0:lim1], model1.ntothe[0:lim1], color = 'darkred', label = 'Helium')
    # ------ Plot Colors ------
    ims1 = ax.scatter(BaseZams, zams.normM * model1.nmass[63 - 57], c= zams.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 6, zorder = 2)
    ims2 = ax.scatter(BaseMid, mid.normM * model1.nmass[107 - 57], c= mid.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 6, zorder = 2)
    ims3 = ax.scatter(BaseTams, tams.normM * model1.nmass[200 - 57], c= tams.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 6, zorder = 2)
    # cbar1 = fig.colorbar(ims1, ax = ax)
    # cbar1.set_label('Zones')

    # ------ Fill Planes ------
    
    # ax.fill_between(model1.time[0:lim1], model1.botsurfh1[0:lim1], model1.ntoth1[0:lim1], alpha = 0.6, color = 'darkgreen')
    # ax.fill_between(model1.time[0:lim1], 0, model1.botsurfh1[0:lim1], alpha = 0.6, color = 'lime')

    # ax.fill_between(model1.time[0:lim1], model1.nmass[0:lim1], model1.nhemin[0:lim1], alpha = 0.6, color = 'darkred')
    # ax.fill_between(model1.time[0:lim1], model1.nhemin[0:lim1], model1.ntotheminsurfmin[0:lim1], alpha = 0.6, color = 'red')
    
    ax.fill_between(model1.time[0:lim1], model1.convtop[0:lim1], model1.nmass[0:lim1], alpha = 0.5, color = 'grey', hatch = '///')
    ax.fill_between(model1.time[0:lim1], 0, model1.convective_core[0:lim1], alpha = 0.2, color = 'grey', hatch = '///')

    # ------ Text ------
    ax.text(1.3, 0.2, 'Convective core', fontweight = 'bold')
    #ax.text(1.3, 0.56, 'Convective mix 1', fontweight = 'bold')
    #ax.text(1.3, 0.9, 'Convective mix 2', fontweight = 'bold')
    ax.text(1, 0.8, 'Radiative envelope', fontweight = 'bold')

    # ------ Plot Colors On Axis ------
    multicolor_ylabel(ax,('Hydrogen','Helium'),('darkred','deeppink'),axis='yleft',size=14,weight='bold')
    multicolor_ylabel(ax,('Convection','Overshoot','Radiation'),('lightblue','seagreen','navy'),axis='yright',size=14,weight='bold')

    # ------ Show ------
    #plt.legend(shadow = False, edgecolor = 'k')
    fig.tight_layout()
    #plt.show()

    plt.savefig(f'Plots/Kippenhahn/Kipconv{limit}.png')

massconv(vink01, vink18, ms=False)




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