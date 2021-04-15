# Script that makes plot

from classData import Data
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np

# ------ Models ------
vink01 = Data('../Data/40M_Vink01_out.data')
vink18 = Data('../Data/40M_Vink18_out.data')

def plot(model1, model2):
    
    colormap = plt.cm.plasma
    fig, ax = plt.subplots(1,1, figsize=(9,6.5))

    #ax.set_xlim(51,2)
    ax.set_xlabel('log (L / L$_{\odot}$)')
    ax.set_ylabel('M$_{\mathrm{dot}}$')
    ax.set_title('L vs Mdot',fontweight='bold')

    # plot line
    ax.plot(model1.age, model1.coreH, lw = 1, linestyle = 'solid', color = 'black', label= 'vink01')
    ax.plot(model2.age, model2.coreH, lw = 1, linestyle = 'dashed', color = 'black', label= 'vink18')
    
    # plot colors
    ims1 = ax.scatter(model1.age, model1.coreH, c= model1.age, marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model1.get_min_bar(), vmax = model1.get_max_bar())
    ims2 = ax.scatter(model2.age, model2.coreH, c= model2.age, marker='o', edgecolors='none', s=100, cmap=colormap, vmin = model2.get_min_bar(), vmax = model2.get_max_bar())
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    ax.legend(shadow = False, edgecolor = 'k')

    fig.tight_layout()
    plt.show()
    #plt.savefig('Plots/L&Mdot.png')

plot(vink01, vink18)