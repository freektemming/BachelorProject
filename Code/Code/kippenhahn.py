# script to plot kippenhahn diagrams

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

# ------ Convert Radius To Mass ------


# ------ Mass Fractions ------
def mass(model1,model2):

    # list for x-axis structure plot
    BaseZams = [0.0648] * len(zams.normR)
    BaseMid = [3.12] * len(mid.normR)
    BaseTams = [4.76] * len(tams.normR)
    colormap = plt.cm.cividis

    # main sequence limit
    lim1 = model1.mainsequence()
    lim2 = model2.mainsequence()
    

    # ------ set figure ------
    fig1, ax1 = plt.subplots(1,1)

    ax1.set_xlabel('Time [Myr]')
    ax1.set_ylabel('m / M$_{\star}$')
    ax1.set_title('Kippenhahn Diagram Mass', size = 10)

    ax1.set_xticks([0.0648,3.12,4.76])
    ax1.set_xticklabels(['Zams', 'Mid','Tams'], fontweight = 'bold')

    # ------ Plot Lines ------
    #ax1.plot(vink01.time[0:lim1], vink01.nmass[0:lim1], linewidth = 3, color = 'red', label = 'nmass')
    #ax1.plot(vink01.time[0:lim1], vink01.HC[0:lim1], linewidth = 3, color = 'black', label = 'H')
    #ax1.plot(vink01.time[0:lim1], vink01.HeC[0:lim1], linewidth = 3, color = 'navy', label = 'He')
    #ax1.plot(vink01.time[0:lim1], vink01.CC[0:lim1], linewidth = 3, color = 'green', label = 'C')
    #ax1.plot(vink01.time[0:lim1], vink01.NC[0:lim1], linewidth = 3, color = 'green', label = 'N')
    #ax1.plot(vink01.time[0:lim1], vink01.OC[0:lim1], linewidth = 3, color = 'darkred', label = 'O')
    
    #ax1.plot(vink01.time[0:lim1], vink01.convbot[0:lim1], linewidth = 3, color = 'blue', label = 'conv-bot')
    #ax1.plot(model1.time[0:lim1], model1.nczradius[0:lim1], linestyle = 'dashed', linewidth = 1, color = 'lime', label = 'Conv Core Radius')
    #ax1.plot(vink01.time[0:lim1], vink01.convective_core[0:lim1], linewidth = 3, color = 'pink', label = 'core')

    # ------ Plot Colors ------
    ims1 = ax1.scatter(BaseZams, zams.normM * model1.nmass[63 - 57], c= zams.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 5, zorder = 2)
    ims2 = ax1.scatter(BaseMid, mid.normM * model1.nmass[107 - 57], c= mid.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 5, zorder = 2)
    ims3 = ax1.scatter(BaseTams, tams.normM * model1.nmass[200 - 57], c= tams.mixtype, marker='_', edgecolors='none', s=100, cmap=colormap, vmin = 0, vmax = 5, zorder = 2)
    cbar1 = fig1.colorbar(ims1, ax = ax1)
    cbar1.set_label('Zones')

    # ------ Fill Planes ------
    #ax1.fill_between(model1.time[0:lim1], model1.convtop[0:lim1], model1.nmass[0:lim1], alpha = 0.5, color = 'grey', hatch = '///')
    ax1.fill_between(model1.time[0:lim1], 0, model1.convective_core[0:lim1], alpha = 0.4, color = 'grey', hatch = '/')
    ax1.fill_between(model1.time[0:lim1], model1.convbot2[0:lim1], model1.convtop2[0:lim1], alpha = 0.4, color = 'grey', hatch = '/')
    ax1.fill_between(model2.time[0:lim2], 0, model2.convective_core[0:lim2], alpha = 0.2, color = 'lime')
    ax1.fill_between(model2.time[0:lim2], model2.convbot2[0:lim2], model1.convtop2[0:lim2], alpha = 0.2, color = 'lime')
    #ax1.fill_between(model1.time[0:lim1], model1.convbot[0:lim1], model1.convtop[0:lim1], alpha = 0.2, color = 'grey', hatch = '///')


    # ------ Text ------
    ax1.text(1.3, 0.2, 'Convective core', fontweight = 'bold')
    #ax1.text(1.3, 0.56, 'Convective mix 1', fontweight = 'bold')
    ax1.text(1.3, 0.9, 'Convective mix 2', fontweight = 'bold')
    # ax1.text(1, 0.8, 'Radiative envelope', fontweight = 'bold')

    # ------ Show ------
    #plt.legend(shadow = False, edgecolor = 'k')
    fig1.tight_layout()
    #plt.show()

    plt.savefig('Plots/Kippenhahn/Kipmodels.png')

mass(vink01, vink18)

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