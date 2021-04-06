# read data and test

from ClassData import Data
#from plotset import *
import matplotlib.pyplot as plt

import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np

vink01 = Data('../Data/40M_Vink01_out.data')
vink18 = Data('../Data/40M_Vink18_out.data')

def hrd(model1, model2):
    
    colormap = plt.cm.plasma

    fig, ax = plt.subplots(1,1, figsize=(9,6.5))
    #fig.suptitle('HRD Comparison Models', fontweight='bold')

    ax.set_xlim(51,2)
    ax.set_xlabel('T$_{\mathrm{eff}}$ [kK]')
    ax.set_ylabel('log (L / L$_{\odot}$)')
    ax.set_title('Both Models',fontweight='bold')
    ax.plot(model1.Teff/1e3, model1.logL, lw = 1, linestyle = 'solid', color = 'black', label= 'vink01')
    ax.plot(model2.Teff/1e3, model2.logL, lw = 1, linestyle = 'dashed', color = 'black', label= 'vink18')
    ims1 = ax.scatter(model1.Teff/1e3, model1.logL,c= model1.age, marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_max_bar())
    ims2 = ax.scatter(model2.Teff/1e3, model2.logL,c= model2.age, marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model2.get_min_bar(), vmax = model2.get_max_bar())
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    ax.legend()
    #fig1, ax1 = plt.subplots(1,1, figsize=(9,6))
    # for p in (da1,da2,da3, da4):
    #     ax1.plot(Teff[p]/1e3, logL[p], linestyle = '', marker = 'X', markersize = 10, color = 'white', zorder=2, label=f'Age =  {round(age[p]/1e6)} Myr')
    #ax1.legend(fancybox = True, scatterpoints =1, labelspacing = 1, loc='upper left', shadow=True)


    fig.tight_layout()
    plt.savefig('Plots/HRD.png')

hrd(vink01, vink18)

def subhrd(model1, model2):
    
    colormap = plt.cm.plasma

    fig, (ax1, ax2) = plt.subplots(2, figsize=(9,6.5))
    #fig.suptitle('HRD Comparison Models', fontweight='bold')

    # ------ first plot ------
    ax1.set_xlim(51,2)
    ax1.set_xlabel('T$_{\mathrm{eff}}$ [kK]')
    ax1.set_ylabel('log (L / L$_{\odot}$)')
    ax1.set_title('Vink01',fontweight='bold')
    ax1.plot(model1.Teff/1e3, model1.logL, lw = 1, linestyle = '-', color = 'black', zorder=1)
    ax1.plot(model2.Teff/1e3, model2.logL, lw = 1, linestyle = '-', color = 'black', zorder=1)
    ims1 = ax1.scatter(model1.Teff/1e3, model1.logL,c= model1.age, marker='o', edgecolors='none', s=200, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_max_bar())
    ims1 = ax1.scatter(model2.Teff/1e3, model2.logL,c= model2.age, marker='o', edgecolors='none', s=200, cmap=colormap, vmin = model2.get_min_bar(), vmax = model2.get_max_bar())
    cbar = fig.colorbar(ims1, ax = ax1)
    cbar.set_label('Age [Myr]')
    #fig1, ax1 = plt.subplots(1,1, figsize=(9,6))
    # for p in (da1,da2,da3, da4):
    #     ax1.plot(Teff[p]/1e3, logL[p], linestyle = '', marker = 'X', markersize = 10, color = 'white', zorder=2, label=f'Age =  {round(age[p]/1e6)} Myr')
    #ax1.legend(fancybox = True, scatterpoints =1, labelspacing = 1, loc='upper left', shadow=True)

    # ----- Second plot ------
    ax2.set_xlim(51,2)
    ax2.set_xlabel('T$_{\mathrm{eff}}$ [kK]')
    ax2.set_ylabel('log (L / L$_{\odot}$)')
    ax2.set_title('Vink18',fontweight='bold')
    ax2.plot(model2.Teff/1e3, model2.logL, lw = 1, linestyle = '-', color = 'black', zorder=1)
    ims2 = ax2.scatter(model2.Teff/1e3, model2.logL,c= model2.age, marker='o', edgecolors='none', s=200, cmap=colormap, vmin = model2.get_min_bar(), vmax = model2.get_max_bar())
    cbar = fig.colorbar(ims2, ax = ax2)
    cbar.set_label('Age [Myr]')
    #fig1, ax1 = plt.subplots(1,1, figsize=(9,6))
    # for p in (da1,da2,da3, da4):
    #     ax1.plot(Teff[p]/1e3, logL[p], linestyle = '', marker = 'X', markersize = 10, color = 'white', zorder=2, label=f'Age =  {round(age[p]/1e6)} Myr')

    fig.tight_layout()
    plt.savefig('Plots/subHRD.png')

#subhrd(vink01, vink18)

def subplots(model1, model2):

    # ------ figure ------
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(9,6.5))
    fig.suptitle('Comparison Models', fontweight='bold')

    # ------ plot 1 ------
    ax1.plot(model1.age, model1.M, label = 'Vink01', color = 'navy')
    ax1.plot(model2.age, model2.M, label = 'Vink18', color = 'darkred')
    ax1.legend(fancybox = True, scatterpoints = 1, labelspacing = 1, loc='lower left', shadow=True)
    ax1.set_xlabel('Age [Myr]')
    ax1.set_ylabel('Mass [M$_{\odot}$]')
    ax1.set_title('Mass Loss')
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    # ------ plot 2 ------
    ax2.plot(model1.age, model1.vrot, label = 'Vink01', color = 'navy')
    ax2.plot(model2.age, model2.vrot, label = 'Vink18', color = 'darkred')
    ax2.set_xlabel('Age [Myr]')
    ax2.set_ylabel('Rotational Velocity [m/s]')
    ax2.set_title('Rotational Velocity')
    ax2.legend(fancybox = True, scatterpoints = 1, labelspacing = 1, loc='lower left', shadow=True)

    # ------ plot 3 ------
    ax3.plot(model1.age, model1.surfh1, label = 'Vink01', color = 'navy')
    ax3.plot(model2.age, model2.surfh1, label = 'Vink18', color = 'darkred')
    ax3.legend(fancybox = True, scatterpoints = 1, labelspacing = 1, loc='lower left', shadow=True)
    ax3.set_xlabel('Age [Myr]')
    ax3.set_ylabel('Surface H')
    ax3.set_title('H')

    # ------ plot 4 ------
    ax4.plot(model1.age, model1.R, label = 'Vink01', color = 'navy')
    ax4.plot(model2.age, model2.R, label = 'Vink18', color = 'darkred')
    ax4.legend(fancybox = True, scatterpoints = 1, labelspacing = 1, loc='lower left', shadow=True)
    ax4.set_xlabel('Age [Myr]')
    ax4.set_ylabel('Radius')
    ax4.set_title('Radius')
    
    plt.tight_layout()
    plt.savefig('Plots/subplot.png')

#subplots(vink01, vink18)

def histogram(model1, model2):

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

    ax1.bar(2, model1.M[len(model1.M)-1], 1, label='vink01', color = 'navy')
    ax1.bar(3, model2.M[len(model2.M)-1], 1, label='vink18', color = 'darkred')
    ax1.set_xlim(0,7)
    ax1.set_xticks([2,3])
    ax1.set_xticklabels(['', ''])
    ax1.set_ylabel('Solar Mass')
    ax1.set_title('Results')
    ax1.legend()

    ax2.bar(2, model1.R[len(model1.R)-1], 1, label='vink01', color = 'navy')
    ax2.bar(3, model2.R[len(model2.R)-1], 1, label='vink18', color = 'darkred')
    ax2.set_xlim(0,7)
    ax2.set_xticks([2,3])
    ax2.set_xticklabels(['', ''])
    ax2.set_ylabel('Solar Radius')
    ax2.set_title('Results')
    ax2.legend()

    ax3.bar(2, model1.Teff[len(model1.Teff)-1], 1, label='vink01', color = 'navy')
    ax3.bar(3, model2.Teff[len(model2.Teff)-1], 1, label='vink18', color = 'darkred')
    ax3.set_xlim(0,7)
    ax3.set_xticks([2,3])
    ax3.set_xticklabels(['', ''])
    ax3.set_ylabel('Teff')
    ax3.set_title('Results')
    ax3.legend()

    ax4.bar(2, model1.logL[len(model1.logL)-1], 1, label='vink01', color = 'navy')
    ax4.bar(3, model2.logL[len(model2.logL)-1], 1, label='vink18', color = 'darkred')
    ax4.set_xlim(0,7)
    ax4.set_xticks([2,3])
    ax4.set_xticklabels(['', ''])
    ax4.set_ylabel('LogL')
    ax4.set_title('Results')
    ax4.legend()

    fig.tight_layout()
    plt.savefig('Plots/histogram.png')

#histogram(vink01, vink18)

def difference(model1,model2, var):

    if var == 1:
        variable1 = model1.M
        variable2 = model2.M

    if var == 2:
        variable1 = model1.vrot
        variable2 = model2.vrot

    if var == 3:
        variable1 = model1.surfh1
        variable2 = model2.surfh1

    if var == 4:
        variable1 = model1.R
        variable2 = model2.R

    length = 0
    DifferenceList = []
    steps = []

    if len(variable1) < len(variable2):
        for i in range(len(variable1)):
            difference = variable1[i] - variable2[i]
            DifferenceList.append(difference)
        length = len(variable1)

    if len(variable2) < len(variable1):
        for i in range(len(variable2)):
            difference = variable1[i] - variable2[i]
            DifferenceList.append(difference)
        length = len(variable2)
    
    for i in range(length):
        steps.append(i)

    return DifferenceList, steps
    
def difplot(model1,model2):

    dif1, steps1 = difference(model1,model2,1)
    dif2, steps2 = difference(model1,model2,2)
    dif3, steps3 = difference(model1,model2,3)
    dif4, steps4 = difference(model1,model2,4)

    # ------ figure ------
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(9,6.5))
    fig.suptitle('Difference Between Models', fontweight='bold')

    # ------ plot 1 ------
    ax1.plot(steps1, dif1, color = 'navy')
    ax1.set_xlabel('Model [step]')
    ax1.set_ylabel('Mass [M$_{\odot}$]')
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    # ------ plot 2 ------
    ax2.plot(steps2, dif2, color = 'navy')
    ax2.set_xlabel('Model [step]')
    ax2.set_ylabel('Vrot')
    ax2.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    # ------ plot 3 ------
    ax3.plot(steps3, dif3, color = 'navy')
    ax3.set_xlabel('Model [step]')
    ax3.set_ylabel('Surface H')
    ax3.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    # ------ plot 4 ------
    ax4.plot(steps4, dif4, color = 'navy')
    ax4.set_xlabel('Model [step]')
    ax4.set_ylabel('Radius')
    ax4.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    fig.tight_layout()
    plt.savefig('Plots/difference.png')

#difplot(vink01,vink18)