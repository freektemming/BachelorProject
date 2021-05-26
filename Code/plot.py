# Script that makes plot

from typing import Sized
from data import *
from plots import *
from plotstyles import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np


def plot(model1, model2, model3, model4, ms):

    # ------ Set Plot Style ------
    default_style()
    fig, ax, colormap = HeC()

    if ms == True:
        # main sequence limit
        lim1 = model1.mainsequence()
        lim2 = model2.mainsequence()
        lim3 = model3.mainsequence()
        lim4 = model4.mainsequence()
        limit = '_ms'
    else:
        # full simulation
        lim1 = model1.end()
        lim2 = model2.end()
        lim3 = model3.end()
        lim4 = model4.end()
        limit = ''

    # plot line
    ax.plot(model1.HeC[0:lim1], model1.CC[0:lim1], lw = 1, linestyle = 'solid', color = 'black', label= 'vink01')
    ax.plot(model2.HeC[0:lim2], model2.CC[0:lim2], lw = 1, linestyle = 'dashed', color = 'black', label= 'vink18')
    
    # plot colors
    ims1 = ax.scatter(model1.HeC[0:lim1], model1.CC[0:lim1], c= model1.age[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims2 = ax.scatter(model2.HeC[0:lim2], model2.CC[0:lim2], c= model2.age[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min2, vmax = max2)
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    ax.legend(shadow = False, edgecolor = 'k')

    fig.tight_layout()
    plt.show()
    #plt.savefig(f'Plots/Week1/He&Car{limit}.png')

#plot(vink01_40, vink18_40, ms=False)



# ------ Plot multiple HRD 4 Models Main Sequence------
def subhrd(model11, model12, model13, model14, model15, model21, model22, model23, model24, model25, model31, model32, model33, model34, model35, model41, model42, model43, model44, model45, ms):
    
    # distance of text in plot
    txt = 7

    # region of dataset
    if datafolder == '4x4':
        region = 'Galaxy'
    if datafolder == 'Z002Om2':
        region = 'SMC'
    if datafolder == 'Z007Om2':
        region = 'LMC'

    # limits
    if ms == True:
        # main sequence limit
        lim11 = model11.mainsequence()
        lim12 = model12.mainsequence()
        lim13 = model13.mainsequence()
        lim14 = model14.mainsequence()
        lim15 = model15.mainsequence()

        lim21 = model21.mainsequence()
        lim22 = model22.mainsequence()
        lim23 = model23.mainsequence()
        lim24 = model24.mainsequence()
        lim25 = model25.mainsequence()

        lim31 = model31.mainsequence()
        lim32 = model32.mainsequence()
        lim33 = model33.mainsequence()
        lim34 = model34.mainsequence()
        lim35 = model35.mainsequence()

        lim41 = model41.mainsequence()
        lim42 = model42.mainsequence()
        lim43 = model43.mainsequence()
        lim44 = model44.mainsequence()
        lim45 = model45.mainsequence()

        limit = '_ms'
    else:
        # full simulation
        lim11 = model11.end()
        lim12 = model12.end()
        lim13 = model13.end()
        lim14 = model14.end()
        lim15 = model15.end()

        lim21 = model21.end()
        lim22 = model22.end()
        lim23 = model23.end()
        lim24 = model24.end()
        lim25 = model25.end()

        lim31 = model31.end()
        lim32 = model32.end()
        lim33 = model33.end()
        lim34 = model34.end()
        lim35 = model35.end()

        lim41 = model41.end()
        lim42 = model42.end()
        lim43 = model43.end()
        lim44 = model44.end()
        lim45 = model45.end()

        limit = ''

    # ------ Set Plot Style ------
    default_style()
    fig, ((ax1, ax2), (ax3, ax4)), colormap = overview_Mdot_Teff(region)

    # ------ first plot ------
    # plot line
    ax1.plot(model11.Teff[0:lim11], model11.Mdot[0:lim11], lw = 1, color = 'black', label = '20M$_{\odot}$')
    ax1.plot(model12.Teff[0:lim12], model12.Mdot[0:lim12], lw = 1, color = 'navy', label = '30M$_{\odot}$')
    ax1.plot(model13.Teff[0:lim13], model13.Mdot[0:lim13], lw = 1, color = 'darkgreen', label = '40M$_{\odot}$')
    ax1.plot(model14.Teff[0:lim14], model14.Mdot[0:lim14], lw = 1, color = 'darkred', label = '50M$_{\odot}$')
    ax1.plot(model15.Teff[0:lim15], model15.Mdot[0:lim15], lw = 1, color = 'pink', label = '60M$_{\odot}$')

    ax1.legend(shadow = False, edgecolor = 'k', fontsize=6.5)

    # plot text
    # ax1.text(model11.Teff[0] + txt, model11.Mdot[0], '20M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax1.text(model12.Teff[0] + txt, model12.Mdot[0], '30M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax1.text(model13.Teff[0] + txt, model13.Mdot[0], '40M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax1.text(model14.Teff[0] + txt, model14.Mdot[0], '50M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax1.text(model15.Teff[0] + txt, model15.Mdot[0], '60M$_{\odot}$', fontweight = 'bold', fontsize=8)
    
    # ----- Second plot ------
    # plot line
    ax2.plot(model21.Teff[0:lim21], model21.Mdot[0:lim21], lw = 1, color = 'black', label = '20M$_{\odot}$')
    ax2.plot(model22.Teff[0:lim22], model22.Mdot[0:lim22], lw = 1, color = 'navy', label = '30M$_{\odot}$')
    ax2.plot(model23.Teff[0:lim23], model23.Mdot[0:lim23], lw = 1, color = 'darkgreen', label = '40M$_{\odot}$')
    ax2.plot(model24.Teff[0:lim24], model24.Mdot[0:lim24], lw = 1, color = 'darkred', label = '50M$_{\odot}$')
    ax2.plot(model25.Teff[0:lim25], model25.Mdot[0:lim25], lw = 1, color = 'pink', label = '60M$_{\odot}$')

    ax2.legend(shadow = False, edgecolor = 'k', fontsize=6.5)

    # plot text
    # ax2.text(model21.Teff[0] + txt, model21.Mdot[0], '20M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax2.text(model22.Teff[0] + txt, model22.Mdot[0], '30M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax2.text(model23.Teff[0] + txt, model23.Mdot[0], '40M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax2.text(model24.Teff[0] + txt, model24.Mdot[0], '50M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax2.text(model25.Teff[0] + txt, model25.Mdot[0], '60M$_{\odot}$', fontweight = 'bold', fontsize=8)
    
    # ------ Third Plot ------
    ax3.plot(model31.Teff[0:lim31], model31.Mdot[0:lim31], lw = 1, color = 'black', label = '20M$_{\odot}$')
    ax3.plot(model32.Teff[0:lim32], model32.Mdot[0:lim32], lw = 1, color = 'navy', label = '30M$_{\odot}$')
    ax3.plot(model33.Teff[0:lim33], model33.Mdot[0:lim33], lw = 1, color = 'darkgreen', label = '40M$_{\odot}$')
    ax3.plot(model34.Teff[0:lim34], model34.Mdot[0:lim34], lw = 1, color = 'darkred', label = '50M$_{\odot}$')
    ax3.plot(model35.Teff[0:lim35], model35.Mdot[0:lim35], lw = 1, color = 'pink', label = '60M$_{\odot}$')

    ax3.legend(shadow = False, edgecolor = 'k', fontsize=6.5)

    # plot text
    # ax3.text(model31.Teff[0] + txt, model31.Mdot[0], '20M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax3.text(model32.Teff[0] + txt, model32.Mdot[0], '30M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax3.text(model33.Teff[0] + txt, model33.Mdot[0], '40M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax3.text(model34.Teff[0] + txt, model34.Mdot[0], '50M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax3.text(model35.Teff[0] + txt, model35.Mdot[0], '60M$_{\odot}$', fontweight = 'bold', fontsize=8)
    
     # ------ Fourth Plot ------
    ax4.plot(model41.Teff[0:lim41], model41.Mdot[0:lim41], lw = 1, color = 'black', label = '20M$_{\odot}$')
    ax4.plot(model42.Teff[0:lim42], model42.Mdot[0:lim42], lw = 1, color = 'navy', label = '30M$_{\odot}$')
    ax4.plot(model43.Teff[0:lim43], model43.Mdot[0:lim43], lw = 1, color = 'darkgreen', label = '40M$_{\odot}$')
    ax4.plot(model44.Teff[0:lim44], model44.Mdot[0:lim44], lw = 1, color = 'darkred', label = '50M$_{\odot}$')
    ax4.plot(model45.Teff[0:lim45], model45.Mdot[0:lim45], lw = 1, color = 'pink', label = '60M$_{\odot}$')

    ax4.legend(shadow = False, edgecolor = 'k', fontsize=6.5)

    # plot text
    # ax4.text(model41.Teff[0] + txt, model41.Mdot[0], '20M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax4.text(model42.Teff[0] + txt, model42.Mdot[0], '30M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax4.text(model43.Teff[0] + txt, model43.Mdot[0], '40M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax4.text(model44.Teff[0] + txt, model44.Mdot[0], '50M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax4.text(model45.Teff[0] + txt, model45.Mdot[0], '60M$_{\odot}$', fontweight = 'bold', fontsize=8)
    
    fig.tight_layout()
    plt.savefig(f'Plots/Overview/Mdot-Teff/{region}{limit}.png')
    #plt.show()

subhrd(vink01_20, vink01_30, vink01_40, vink01_50, vink01_60, vink18_20, vink18_30, vink18_40, vink18_50, vink18_60, leuven_20, leuven_30, leuven_40, leuven_50, leuven_60, krticka_20, krticka_30, krticka_40, krticka_50, krticka_60, ms=True)



# ------ Plot multiple HRD 4 Models Main Sequence------
def timeMdot(model11, model12, model13, model14, model15, model21, model22, model23, model24, model25, model31, model32, model33, model34, model35, model41, model42, model43, model44, model45, ms):
    
    # distance of text in plot
    txt = 7

    # region of dataset
    if datafolder == '4x4':
        region = 'Galaxy'
    if datafolder == 'Z002Om2':
        region = 'SMC'
    if datafolder == 'Z007Om2':
        region = 'LMC'

    # limits
    if ms == True:
        # main sequence limit
        lim11 = model11.mainsequence()
        lim12 = model12.mainsequence()
        lim13 = model13.mainsequence()
        lim14 = model14.mainsequence()
        lim15 = model15.mainsequence()

        lim21 = model21.mainsequence()
        lim22 = model22.mainsequence()
        lim23 = model23.mainsequence()
        lim24 = model24.mainsequence()
        lim25 = model25.mainsequence()

        lim31 = model31.mainsequence()
        lim32 = model32.mainsequence()
        lim33 = model33.mainsequence()
        lim34 = model34.mainsequence()
        lim35 = model35.mainsequence()

        lim41 = model41.mainsequence()
        lim42 = model42.mainsequence()
        lim43 = model43.mainsequence()
        lim44 = model44.mainsequence()
        lim45 = model45.mainsequence()

        limit = '_ms'
    else:
        # full simulation
        lim11 = model11.end()
        lim12 = model12.end()
        lim13 = model13.end()
        lim14 = model14.end()
        lim15 = model15.end()

        lim21 = model21.end()
        lim22 = model22.end()
        lim23 = model23.end()
        lim24 = model24.end()
        lim25 = model25.end()

        lim31 = model31.end()
        lim32 = model32.end()
        lim33 = model33.end()
        lim34 = model34.end()
        lim35 = model35.end()

        lim41 = model41.end()
        lim42 = model42.end()
        lim43 = model43.end()
        lim44 = model44.end()
        lim45 = model45.end()

        limit = ''

    # ------ Set Plot Style ------
    default_style()
    fig, ((ax1, ax2), (ax3, ax4)), colormap = overview_Mdot_Time(region)

    # ------ first plot ------
    # plot line
    ax1.plot(model11.age[0:lim11], model11.Mdot[0:lim11], lw = 1, color = 'black', label = '20M$_{\odot}$')
    ax1.plot(model12.age[0:lim12], model12.Mdot[0:lim12], lw = 1, color = 'navy', label = '30M$_{\odot}$')
    ax1.plot(model13.age[0:lim13], model13.Mdot[0:lim13], lw = 1, color = 'darkgreen', label = '40M$_{\odot}$')
    ax1.plot(model14.age[0:lim14], model14.Mdot[0:lim14], lw = 1, color = 'darkred', label = '50M$_{\odot}$')
    ax1.plot(model15.age[0:lim15], model15.Mdot[0:lim15], lw = 1, color = 'pink', label = '60M$_{\odot}$')

    ax1.legend(shadow = False, edgecolor = 'k', fontsize=6.5)

    # plot text
    # ax1.text(model11.Teff[0] + txt, model11.Mdot[0], '20M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax1.text(model12.Teff[0] + txt, model12.Mdot[0], '30M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax1.text(model13.Teff[0] + txt, model13.Mdot[0], '40M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax1.text(model14.Teff[0] + txt, model14.Mdot[0], '50M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax1.text(model15.Teff[0] + txt, model15.Mdot[0], '60M$_{\odot}$', fontweight = 'bold', fontsize=8)
    
    # ----- Second plot ------
    # plot line
    ax2.plot(model21.age[0:lim21], model21.Mdot[0:lim21], lw = 1, color = 'black', label = '20M$_{\odot}$')
    ax2.plot(model22.age[0:lim22], model22.Mdot[0:lim22], lw = 1, color = 'navy', label = '30M$_{\odot}$')
    ax2.plot(model23.age[0:lim23], model23.Mdot[0:lim23], lw = 1, color = 'darkgreen', label = '40M$_{\odot}$')
    ax2.plot(model24.age[0:lim24], model24.Mdot[0:lim24], lw = 1, color = 'darkred', label = '50M$_{\odot}$')
    ax2.plot(model25.age[0:lim25], model25.Mdot[0:lim25], lw = 1, color = 'pink', label = '60M$_{\odot}$')

    ax2.legend(shadow = False, edgecolor = 'k', fontsize=6.5)

    # plot text
    # ax2.text(model21.Teff[0] + txt, model21.Mdot[0], '20M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax2.text(model22.Teff[0] + txt, model22.Mdot[0], '30M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax2.text(model23.Teff[0] + txt, model23.Mdot[0], '40M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax2.text(model24.Teff[0] + txt, model24.Mdot[0], '50M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax2.text(model25.Teff[0] + txt, model25.Mdot[0], '60M$_{\odot}$', fontweight = 'bold', fontsize=8)
    
    # ------ Third Plot ------
    ax3.plot(model31.age[0:lim31], model31.Mdot[0:lim31], lw = 1, color = 'black', label = '20M$_{\odot}$')
    ax3.plot(model32.age[0:lim32], model32.Mdot[0:lim32], lw = 1, color = 'navy', label = '30M$_{\odot}$')
    ax3.plot(model33.age[0:lim33], model33.Mdot[0:lim33], lw = 1, color = 'darkgreen', label = '40M$_{\odot}$')
    ax3.plot(model34.age[0:lim34], model34.Mdot[0:lim34], lw = 1, color = 'darkred', label = '50M$_{\odot}$')
    ax3.plot(model35.age[0:lim35], model35.Mdot[0:lim35], lw = 1, color = 'pink', label = '60M$_{\odot}$')

    ax3.legend(shadow = False, edgecolor = 'k', fontsize=6.5)

    # plot text
    # ax3.text(model31.Teff[0] + txt, model31.Mdot[0], '20M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax3.text(model32.Teff[0] + txt, model32.Mdot[0], '30M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax3.text(model33.Teff[0] + txt, model33.Mdot[0], '40M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax3.text(model34.Teff[0] + txt, model34.Mdot[0], '50M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax3.text(model35.Teff[0] + txt, model35.Mdot[0], '60M$_{\odot}$', fontweight = 'bold', fontsize=8)
    
     # ------ Fourth Plot ------
    ax4.plot(model41.age[0:lim41], model41.Mdot[0:lim41], lw = 1, color = 'black', label = '20M$_{\odot}$')
    ax4.plot(model42.age[0:lim42], model42.Mdot[0:lim42], lw = 1, color = 'navy', label = '30M$_{\odot}$')
    ax4.plot(model43.age[0:lim43], model43.Mdot[0:lim43], lw = 1, color = 'darkgreen', label = '40M$_{\odot}$')
    ax4.plot(model44.age[0:lim44], model44.Mdot[0:lim44], lw = 1, color = 'darkred', label = '50M$_{\odot}$')
    ax4.plot(model45.age[0:lim45], model45.Mdot[0:lim45], lw = 1, color = 'pink', label = '60M$_{\odot}$')

    ax4.legend(shadow = False, edgecolor = 'k', fontsize=6.5)

    # plot text
    # ax4.text(model41.Teff[0] + txt, model41.Mdot[0], '20M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax4.text(model42.Teff[0] + txt, model42.Mdot[0], '30M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax4.text(model43.Teff[0] + txt, model43.Mdot[0], '40M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax4.text(model44.Teff[0] + txt, model44.Mdot[0], '50M$_{\odot}$', fontweight = 'bold', fontsize=8)
    # ax4.text(model45.Teff[0] + txt, model45.Mdot[0], '60M$_{\odot}$', fontweight = 'bold', fontsize=8)
    
    fig.tight_layout()
    plt.savefig(f'Plots/Overview/Mdot-Time/{region}{limit}.png')
    #plt.show()

timeMdot(vink01_20, vink01_30, vink01_40, vink01_50, vink01_60, vink18_20, vink18_30, vink18_40, vink18_50, vink18_60, leuven_20, leuven_30, leuven_40, leuven_50, leuven_60, krticka_20, krticka_30, krticka_40, krticka_50, krticka_60, ms=True)
