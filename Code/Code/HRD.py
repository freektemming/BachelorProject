# Script that makes multiple HRD plots

from ClassData import Data
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np

# ------ Models ------
vink01 = Data('../Data/40M_Vink01_out.data')
vink18 = Data('../Data/40M_Vink18_out.data')

# ------ plot normal HRD ------
def hrd(model1, model2):
    
    colormap = plt.cm.plasma
    fig, ax = plt.subplots(1,1, figsize=(9,6.5))

    ax.set_xlim(51,2)
    ax.set_xlabel('T$_{\mathrm{eff}}$ [kK]')
    ax.set_ylabel('log (L / L$_{\odot}$)')
    ax.set_title('Both Models',fontweight='bold')

    # plot line
    ax.plot(model1.Teff, model1.logL, lw = 1, linestyle = 'solid', color = 'black', label= 'vink01')
    ax.plot(model2.Teff, model2.logL, lw = 1, linestyle = 'dashed', color = 'black', label= 'vink18')
    
    # plot colors
    ims1 = ax.scatter(model1.Teff, model1.logL, c= model1.age, marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_max_bar())
    ims2 = ax.scatter(model2.Teff, model2.logL, c= model2.age, marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model2.get_min_bar(), vmax = model2.get_max_bar())
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    ax.legend()

    fig.tight_layout()
    plt.savefig('Plots/HRD.png')

hrd(vink01, vink18)

# ------ Plot multiple HRD ------
def subhrd(model1, model2):
    
    colormap = plt.cm.plasma
    fig, (ax1, ax2) = plt.subplots(2, figsize=(9,9))
    fig.suptitle('HRD 2 Models', fontweight='bold')

    # ------ first plot ------
    ax1.set_xlim(51,2)
    ax1.set_xlabel('T$_{\mathrm{eff}}$ [kK]')
    ax1.set_ylabel('log (L / L$_{\odot}$)')
    ax1.set_title('Vink01',fontweight='bold')

    # plot line
    ax1.plot(model1.Teff, model1.logL, lw = 1, linestyle = '-', color = 'black', zorder=1)
    
    # plot colors
    ims1 = ax1.scatter(model1.Teff, model1.logL,c= model1.age, marker='o', edgecolors='none', s=200, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_max_bar())
    ims1 = ax1.scatter(model2.Teff, model2.logL,c= model2.age, marker='o', edgecolors='none', s=200, cmap=colormap, vmin = model2.get_min_bar(), vmax = model2.get_max_bar())
    cbar = fig.colorbar(ims1, ax = ax1)
    cbar.set_label('Age [Myr]')

    # ----- Second plot ------
    ax2.set_xlim(51,2)
    ax2.set_xlabel('T$_{\mathrm{eff}}$ [kK]')
    ax2.set_ylabel('log (L / L$_{\odot}$)')
    ax2.set_title('Vink18',fontweight='bold')

    # plot line
    ax2.plot(model2.Teff, model2.logL, lw = 1, linestyle = '-', color = 'black', zorder=1)
    
    # plot colors
    ims2 = ax2.scatter(model2.Teff, model2.logL,c= model2.age, marker='o', edgecolors='none', s=200, cmap=colormap, vmin = model2.get_min_bar(), vmax = model2.get_max_bar())
    cbar = fig.colorbar(ims2, ax = ax2)
    cbar.set_label('Age [Myr]')

    fig.tight_layout()
    plt.savefig('Plots/HRD-sub.png')

subhrd(vink01, vink18)

# ------ Plot main sequence HRD ------ 
def mainsequence(model1, model2):

    colormap = plt.cm.plasma

    # limits were main sequence ends
    lim1 = model1.mainsequence()
    lim2 = model2.mainsequence()
    
    # ------ Plot ------
    fig, ax = plt.subplots(1,1, figsize=(9,6.5))

    ax.set_xlim(51,2)
    ax.set_xlabel('T$_{\mathrm{eff}}$ [kK]')
    ax.set_ylabel('log (L / L$_{\odot}$)')
    ax.set_title('Both Models',fontweight='bold')

    # plot line
    ax.plot(model1.Teff[0:lim1], model1.logL[0:lim1], lw = 1, linestyle = 'solid', color = 'black', label= 'vink01')
    ax.plot(model2.Teff[0:lim2], model2.logL[0:lim2], lw = 1, linestyle = 'dashed', color = 'black', label= 'vink18')
    
    # plot colors
    ims1 = ax.scatter(model1.Teff[0:lim1], model1.logL[0:lim1], c= model1.age[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_age(lim1))
    ims2 = ax.scatter(model2.Teff[0:lim2], model2.logL[0:lim2], c= model2.age[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model2.get_min_bar(), vmax = model2.get_age(lim2))
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    ax.legend(loc = 'upper left')

    fig.tight_layout()
    plt.savefig('Plots/HRD-main.png')

mainsequence(vink01, vink18)