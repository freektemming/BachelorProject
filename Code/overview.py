# Script that makes plot

from data import *
from plots import *
from plotstyles import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np

def initial_values(amodel1, amodel2, amodel3, amodel4, amodel5, bmodel1, bmodel2, bmodel3, bmodel4, bmodel5, cmodel1, cmodel2, cmodel3, cmodel4, cmodel5, dmodel1, dmodel2, dmodel3, dmodel4, dmodel5,
amodel6, amodel7, amodel8, amodel9, amodel10, bmodel6, bmodel7, bmodel8, bmodel9, bmodel10, cmodel6, cmodel7, cmodel8, cmodel9, cmodel10, dmodel6, dmodel7, dmodel8, dmodel9, dmodel10,
amodel11, amodel12, amodel13, amodel14, amodel15, bmodel11, bmodel12, bmodel13, bmodel14, bmodel15, cmodel11, cmodel12, cmodel13, cmodel14, cmodel15, dmodel11, dmodel12, dmodel13, dmodel14, dmodel15,
amodel16, amodel17, amodel18, amodel19, amodel20, bmodel16, bmodel17, bmodel18, bmodel19, bmodel20, cmodel16, cmodel17, cmodel18, cmodel19, cmodel20, dmodel16, dmodel17, dmodel18, dmodel19, dmodel20):

    # end of list
    limit = -1

    # lim1 = len(amodel1.age)
    # lim2 = len(amodel2.age)
    # lim3 = len(amodel3.age)
    # lim4 = len(amodel4.age)
    # lim5 = len(amodel5.age)

    min1 = 0.8
    max1 = 1

    # ------ Set Plot Style ------
    default_style()
    fig, ax1, ax2, ax3, ax4, colormap = m_init()
    
    # ====== 1 ======
    # plot colors
    ims1 = ax1.scatter(amodel1.M[0], amodel1.vrot[0], c= amodel1.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel2.M[0], amodel2.vrot[0], c= amodel2.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel3.M[0], amodel3.vrot[0], c= amodel3.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel4.M[0], amodel4.vrot[0], c= amodel4.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel5.M[0], amodel5.vrot[0], c= amodel5.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(bmodel1.M[0], bmodel1.vrot[0], c= bmodel1.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel2.M[0], bmodel2.vrot[0], c= bmodel2.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel3.M[0], bmodel3.vrot[0], c= bmodel3.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel4.M[0], bmodel4.vrot[0], c= bmodel4.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel5.M[0], bmodel5.vrot[0], c= bmodel5.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(cmodel1.M[0], cmodel1.vrot[0], c= cmodel1.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel2.M[0], cmodel2.vrot[0], c= cmodel2.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel3.M[0], cmodel3.vrot[0], c= cmodel3.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel4.M[0], cmodel4.vrot[0], c= cmodel4.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel5.M[0], cmodel5.vrot[0], c= cmodel5.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(dmodel1.M[0], dmodel1.vrot[0], c= dmodel1.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel2.M[0], dmodel2.vrot[0], c= dmodel2.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel3.M[0], dmodel3.vrot[0], c= dmodel3.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel4.M[0], dmodel4.vrot[0], c= dmodel4.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel5.M[0], dmodel5.vrot[0], c= dmodel5.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar = fig.colorbar(ims1, ax = ax1)
    # cbar.set_label('Final Mass / Initial Mass')

    # ====== 2 ======
    # plot colors
    ims2 = ax2.scatter(amodel6.M[0], amodel6.vrot[0], c= amodel6.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel7.M[0], amodel7.vrot[0], c= amodel7.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel8.M[0], amodel8.vrot[0], c= amodel8.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel9.M[0], amodel9.vrot[0], c= amodel9.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel10.M[0], amodel10.vrot[0], c= amodel10.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(bmodel6.M[0], bmodel6.vrot[0], c= bmodel6.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel7.M[0], bmodel7.vrot[0], c= bmodel7.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel8.M[0], bmodel8.vrot[0], c= bmodel8.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel9.M[0], bmodel9.vrot[0], c= bmodel9.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel10.M[0], bmodel10.vrot[0], c= bmodel10.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(cmodel6.M[0], cmodel6.vrot[0], c= cmodel6.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel7.M[0], cmodel7.vrot[0], c= cmodel7.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel8.M[0], cmodel8.vrot[0], c= cmodel8.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel9.M[0], cmodel9.vrot[0], c= cmodel9.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel10.M[0], cmodel10.vrot[0], c= cmodel10.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(dmodel6.M[0], dmodel6.vrot[0], c= dmodel6.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel7.M[0], dmodel7.vrot[0], c= dmodel7.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel8.M[0], dmodel8.vrot[0], c= dmodel8.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel9.M[0], dmodel9.vrot[0], c= dmodel9.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel10.M[0], dmodel10.vrot[0], c= dmodel10.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    cbar2 = fig.colorbar(ims2, ax = ax2)
    cbar2.set_label('Final Mass / Initial Mass')

    # ====== 3 ======
    # plot colors
    ims3 = ax3.scatter(amodel11.M[0], amodel11.vrot[0], c= amodel11.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel12.M[0], amodel12.vrot[0], c= amodel12.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel13.M[0], amodel13.vrot[0], c= amodel13.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel14.M[0], amodel14.vrot[0], c= amodel14.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel15.M[0], amodel15.vrot[0], c= amodel15.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(bmodel11.M[0], bmodel11.vrot[0], c= bmodel11.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel12.M[0], bmodel12.vrot[0], c= bmodel12.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel13.M[0], bmodel13.vrot[0], c= bmodel13.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel14.M[0], bmodel14.vrot[0], c= bmodel14.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel15.M[0], bmodel15.vrot[0], c= bmodel15.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(cmodel11.M[0], cmodel11.vrot[0], c= cmodel11.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel12.M[0], cmodel12.vrot[0], c= cmodel12.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel13.M[0], cmodel13.vrot[0], c= cmodel13.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel14.M[0], cmodel14.vrot[0], c= cmodel14.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel15.M[0], cmodel15.vrot[0], c= cmodel15.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(dmodel11.M[0], dmodel11.vrot[0], c= dmodel11.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel12.M[0], dmodel12.vrot[0], c= dmodel12.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel13.M[0], dmodel13.vrot[0], c= dmodel13.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel14.M[0], dmodel14.vrot[0], c= dmodel14.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel15.M[0], dmodel15.vrot[0], c= dmodel15.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar3 = fig.colorbar(ims3, ax = ax3)
    # cbar3.set_label('Final Mass / Initial Mass')

    # ====== 4 ======
    # plot colors
    ims4 = ax4.scatter(amodel16.M[0], amodel16.vrot[0], c= amodel16.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel17.M[0], amodel17.vrot[0], c= amodel17.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel18.M[0], amodel18.vrot[0], c= amodel18.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel19.M[0], amodel19.vrot[0], c= amodel19.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel20.M[0], amodel20.vrot[0], c= amodel20.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(bmodel16.M[0], bmodel16.vrot[0], c= bmodel16.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel17.M[0], bmodel17.vrot[0], c= bmodel17.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel18.M[0], bmodel18.vrot[0], c= bmodel18.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel19.M[0], bmodel19.vrot[0], c= bmodel19.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel20.M[0], bmodel20.vrot[0], c= bmodel20.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(cmodel16.M[0], cmodel16.vrot[0], c= cmodel16.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel17.M[0], cmodel17.vrot[0], c= cmodel17.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel18.M[0], cmodel18.vrot[0], c= cmodel18.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel19.M[0], cmodel19.vrot[0], c= cmodel19.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel20.M[0], cmodel20.vrot[0], c= cmodel20.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(dmodel16.M[0], dmodel16.vrot[0], c= dmodel16.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel17.M[0], dmodel17.vrot[0], c= dmodel17.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel18.M[0], dmodel18.vrot[0], c= dmodel18.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel19.M[0], dmodel19.vrot[0], c= dmodel19.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel20.M[0], dmodel20.vrot[0], c= dmodel20.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    cbar4 = fig.colorbar(ims4, ax = ax4)
    cbar4.set_label('Final Mass / Initial Mass')

    fig.tight_layout()
    plt.savefig('Plots/Overview/Minit_Vinit.png')


initial_values(avink01_20, avink01_30, avink01_40, avink01_50, avink01_60, bvink01_20, bvink01_30, bvink01_40, bvink01_50, bvink01_60, cvink01_20, cvink01_30, cvink01_40, cvink01_50, cvink01_60, dvink01_20, dvink01_30, dvink01_40, dvink01_50, dvink01_60,
avink18_20, avink18_30, avink18_40, avink18_50, avink18_60, bvink18_20, bvink18_30, bvink18_40, bvink18_50, bvink18_60, cvink18_20, cvink18_30, cvink18_40, cvink18_50, cvink18_60, dvink18_20, dvink18_30, dvink18_40, dvink18_50, dvink18_60,
aleuven_20, aleuven_30, aleuven_40, aleuven_50, aleuven_60, bleuven_20, bleuven_30, bleuven_40, bleuven_50, bleuven_60, cleuven_20, cleuven_30, cleuven_40, cleuven_50, cleuven_60, dleuven_20, dleuven_30, dleuven_40, dleuven_50, dleuven_60,
akrticka_20, akrticka_30, akrticka_40, akrticka_50, akrticka_60, bkrticka_20, bkrticka_30, bkrticka_40, bkrticka_50, bkrticka_60, ckrticka_20, ckrticka_30, ckrticka_40, ckrticka_50, ckrticka_60, dkrticka_20, dkrticka_30, dkrticka_40, dkrticka_50, dkrticka_60)

# ============================================================

def envelopemass(amodel1, amodel2, amodel3, amodel4, amodel5, bmodel1, bmodel2, bmodel3, bmodel4, bmodel5, cmodel1, cmodel2, cmodel3, cmodel4, cmodel5, dmodel1, dmodel2, dmodel3, dmodel4, dmodel5,
amodel6, amodel7, amodel8, amodel9, amodel10, bmodel6, bmodel7, bmodel8, bmodel9, bmodel10, cmodel6, cmodel7, cmodel8, cmodel9, cmodel10, dmodel6, dmodel7, dmodel8, dmodel9, dmodel10,
amodel11, amodel12, amodel13, amodel14, amodel15, bmodel11, bmodel12, bmodel13, bmodel14, bmodel15, cmodel11, cmodel12, cmodel13, cmodel14, cmodel15, dmodel11, dmodel12, dmodel13, dmodel14, dmodel15,
amodel16, amodel17, amodel18, amodel19, amodel20, bmodel16, bmodel17, bmodel18, bmodel19, bmodel20, cmodel16, cmodel17, cmodel18, cmodel19, cmodel20, dmodel16, dmodel17, dmodel18, dmodel19, dmodel20):

    # end of list
    limit = -1

    # lim1 = len(amodel1.age)
    # lim2 = len(amodel2.age)
    # lim3 = len(amodel3.age)
    # lim4 = len(amodel4.age)
    # lim5 = len(amodel5.age)

    min1 = 0
    max1 = 60

    # ------ Set Plot Style ------
    default_style()
    fig, ax1, ax2, ax3, ax4, colormap = env_mass()
    
    # ====== 1 ======
    # plot colors
    ims1 = ax1.scatter(amodel1.M[0], amodel1.vrot[0], c= amodel1.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel2.M[0], amodel2.vrot[0], c= amodel2.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel3.M[0], amodel3.vrot[0], c= amodel3.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel4.M[0], amodel4.vrot[0], c= amodel4.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel5.M[0], amodel5.vrot[0], c= amodel5.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(bmodel1.M[0], bmodel1.vrot[0], c= bmodel1.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel2.M[0], bmodel2.vrot[0], c= bmodel2.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel3.M[0], bmodel3.vrot[0], c= bmodel3.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel4.M[0], bmodel4.vrot[0], c= bmodel4.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel5.M[0], bmodel5.vrot[0], c= bmodel5.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(cmodel1.M[0], cmodel1.vrot[0], c= cmodel1.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel2.M[0], cmodel2.vrot[0], c= cmodel2.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel3.M[0], cmodel3.vrot[0], c= cmodel3.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel4.M[0], cmodel4.vrot[0], c= cmodel4.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel5.M[0], cmodel5.vrot[0], c= cmodel5.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(dmodel1.M[0], dmodel1.vrot[0], c= dmodel1.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel2.M[0], dmodel2.vrot[0], c= dmodel2.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel3.M[0], dmodel3.vrot[0], c= dmodel3.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel4.M[0], dmodel4.vrot[0], c= dmodel4.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel5.M[0], dmodel5.vrot[0], c= dmodel5.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar = fig.colorbar(ims1, ax = ax1)
    # cbar.set_label('Final Mass / Initial Mass')

    # ====== 2 ======
    # plot colors
    ims2 = ax2.scatter(amodel6.M[0], amodel6.vrot[0], c= amodel6.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel7.M[0], amodel7.vrot[0], c= amodel7.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel8.M[0], amodel8.vrot[0], c= amodel8.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel9.M[0], amodel9.vrot[0], c= amodel9.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel10.M[0], amodel10.vrot[0], c= amodel10.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(bmodel6.M[0], bmodel6.vrot[0], c= bmodel6.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel7.M[0], bmodel7.vrot[0], c= bmodel7.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel8.M[0], bmodel8.vrot[0], c= bmodel8.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel9.M[0], bmodel9.vrot[0], c= bmodel9.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel10.M[0], bmodel10.vrot[0], c= bmodel10.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(cmodel6.M[0], cmodel6.vrot[0], c= cmodel6.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel7.M[0], cmodel7.vrot[0], c= cmodel7.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel8.M[0], cmodel8.vrot[0], c= cmodel8.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel9.M[0], cmodel9.vrot[0], c= cmodel9.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel10.M[0], cmodel10.vrot[0], c= cmodel10.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(dmodel6.M[0], dmodel6.vrot[0], c= dmodel6.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel7.M[0], dmodel7.vrot[0], c= dmodel7.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel8.M[0], dmodel8.vrot[0], c= dmodel8.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel9.M[0], dmodel9.vrot[0], c= dmodel9.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel10.M[0], dmodel10.vrot[0], c= dmodel10.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    cbar2 = fig.colorbar(ims2, ax = ax2)
    cbar2.set_label('Envelope Mass [M$_{\odot}$]')

    # ====== 3 ======
    # plot colors
    ims3 = ax3.scatter(amodel11.M[0], amodel11.vrot[0], c= amodel11.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel12.M[0], amodel12.vrot[0], c= amodel12.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel13.M[0], amodel13.vrot[0], c= amodel13.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel14.M[0], amodel14.vrot[0], c= amodel14.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel15.M[0], amodel15.vrot[0], c= amodel15.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(bmodel11.M[0], bmodel11.vrot[0], c= bmodel11.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel12.M[0], bmodel12.vrot[0], c= bmodel12.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel13.M[0], bmodel13.vrot[0], c= bmodel13.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel14.M[0], bmodel14.vrot[0], c= bmodel14.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel15.M[0], bmodel15.vrot[0], c= bmodel15.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(cmodel11.M[0], cmodel11.vrot[0], c= cmodel11.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel12.M[0], cmodel12.vrot[0], c= cmodel12.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel13.M[0], cmodel13.vrot[0], c= cmodel13.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel14.M[0], cmodel14.vrot[0], c= cmodel14.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel15.M[0], cmodel15.vrot[0], c= cmodel15.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(dmodel11.M[0], dmodel11.vrot[0], c= dmodel11.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel12.M[0], dmodel12.vrot[0], c= dmodel12.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel13.M[0], dmodel13.vrot[0], c= dmodel13.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel14.M[0], dmodel14.vrot[0], c= dmodel14.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel15.M[0], dmodel15.vrot[0], c= dmodel15.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar3 = fig.colorbar(ims3, ax = ax3)
    # cbar3.set_label('Final Mass / Initial Mass')

    # ====== 4 ======
    # plot colors
    ims4 = ax4.scatter(amodel16.M[0], amodel16.vrot[0], c= amodel16.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel17.M[0], amodel17.vrot[0], c= amodel17.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel18.M[0], amodel18.vrot[0], c= amodel18.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel19.M[0], amodel19.vrot[0], c= amodel19.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel20.M[0], amodel20.vrot[0], c= amodel20.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(bmodel16.M[0], bmodel16.vrot[0], c= bmodel16.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel17.M[0], bmodel17.vrot[0], c= bmodel17.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel18.M[0], bmodel18.vrot[0], c= bmodel18.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel19.M[0], bmodel19.vrot[0], c= bmodel19.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel20.M[0], bmodel20.vrot[0], c= bmodel20.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(cmodel16.M[0], cmodel16.vrot[0], c= cmodel16.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel17.M[0], cmodel17.vrot[0], c= cmodel17.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel18.M[0], cmodel18.vrot[0], c= cmodel18.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel19.M[0], cmodel19.vrot[0], c= cmodel19.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel20.M[0], cmodel20.vrot[0], c= cmodel20.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(dmodel16.M[0], dmodel16.vrot[0], c= dmodel16.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel17.M[0], dmodel17.vrot[0], c= dmodel17.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel18.M[0], dmodel18.vrot[0], c= dmodel18.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel19.M[0], dmodel19.vrot[0], c= dmodel19.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel20.M[0], dmodel20.vrot[0], c= dmodel20.envelope_mass[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    

    cbar4 = fig.colorbar(ims4, ax = ax4)
    cbar4.set_label('Envelope Mass [M$_{\odot}$]')

    fig.tight_layout()
    plt.savefig('Plots/Overview/Envelopemass.png')


envelopemass(avink01_20, avink01_30, avink01_40, avink01_50, avink01_60, bvink01_20, bvink01_30, bvink01_40, bvink01_50, bvink01_60, cvink01_20, cvink01_30, cvink01_40, cvink01_50, cvink01_60, dvink01_20, dvink01_30, dvink01_40, dvink01_50, dvink01_60,
avink18_20, avink18_30, avink18_40, avink18_50, avink18_60, bvink18_20, bvink18_30, bvink18_40, bvink18_50, bvink18_60, cvink18_20, cvink18_30, cvink18_40, cvink18_50, cvink18_60, dvink18_20, dvink18_30, dvink18_40, dvink18_50, dvink18_60,
aleuven_20, aleuven_30, aleuven_40, aleuven_50, aleuven_60, bleuven_20, bleuven_30, bleuven_40, bleuven_50, bleuven_60, cleuven_20, cleuven_30, cleuven_40, cleuven_50, cleuven_60, dleuven_20, dleuven_30, dleuven_40, dleuven_50, dleuven_60,
akrticka_20, akrticka_30, akrticka_40, akrticka_50, akrticka_60, bkrticka_20, bkrticka_30, bkrticka_40, bkrticka_50, bkrticka_60, ckrticka_20, ckrticka_30, ckrticka_40, ckrticka_50, ckrticka_60, dkrticka_20, dkrticka_30, dkrticka_40, dkrticka_50, dkrticka_60)

# ================================================================

def Nmass(amodel1, amodel2, amodel3, amodel4, amodel5, bmodel1, bmodel2, bmodel3, bmodel4, bmodel5, cmodel1, cmodel2, cmodel3, cmodel4, cmodel5, dmodel1, dmodel2, dmodel3, dmodel4, dmodel5,
amodel6, amodel7, amodel8, amodel9, amodel10, bmodel6, bmodel7, bmodel8, bmodel9, bmodel10, cmodel6, cmodel7, cmodel8, cmodel9, cmodel10, dmodel6, dmodel7, dmodel8, dmodel9, dmodel10,
amodel11, amodel12, amodel13, amodel14, amodel15, bmodel11, bmodel12, bmodel13, bmodel14, bmodel15, cmodel11, cmodel12, cmodel13, cmodel14, cmodel15, dmodel11, dmodel12, dmodel13, dmodel14, dmodel15,
amodel16, amodel17, amodel18, amodel19, amodel20, bmodel16, bmodel17, bmodel18, bmodel19, bmodel20, cmodel16, cmodel17, cmodel18, cmodel19, cmodel20, dmodel16, dmodel17, dmodel18, dmodel19, dmodel20):

    # end of list
    limit = -1

    # lim1 = len(amodel1.age)
    # lim2 = len(amodel2.age)
    # lim3 = len(amodel3.age)
    # lim4 = len(amodel4.age)
    # lim5 = len(amodel5.age)

    min1 = 0.00001
    max1 = 0.0001

    # ------ Set Plot Style ------
    default_style()
    fig, ax1, ax2, ax3, ax4, colormap = N_mass()
    
    # ====== 1 ======
    # plot colors
    ims1 = ax1.scatter(amodel1.M[0], amodel1.vrot[0], c= amodel1.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel2.M[0], amodel2.vrot[0], c= amodel2.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel3.M[0], amodel3.vrot[0], c= amodel3.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel4.M[0], amodel4.vrot[0], c= amodel4.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel5.M[0], amodel5.vrot[0], c= amodel5.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(bmodel1.M[0], bmodel1.vrot[0], c= bmodel1.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel2.M[0], bmodel2.vrot[0], c= bmodel2.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel3.M[0], bmodel3.vrot[0], c= bmodel3.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel4.M[0], bmodel4.vrot[0], c= bmodel4.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel5.M[0], bmodel5.vrot[0], c= bmodel5.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(cmodel1.M[0], cmodel1.vrot[0], c= cmodel1.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel2.M[0], cmodel2.vrot[0], c= cmodel2.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel3.M[0], cmodel3.vrot[0], c= cmodel3.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel4.M[0], cmodel4.vrot[0], c= cmodel4.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel5.M[0], cmodel5.vrot[0], c= cmodel5.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(dmodel1.M[0], dmodel1.vrot[0], c= dmodel1.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel2.M[0], dmodel2.vrot[0], c= dmodel2.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel3.M[0], dmodel3.vrot[0], c= dmodel3.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel4.M[0], dmodel4.vrot[0], c= dmodel4.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel5.M[0], dmodel5.vrot[0], c= dmodel5.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar = fig.colorbar(ims1, ax = ax1)
    # cbar.set_label('Final Mass / Initial Mass')

    # ====== 2 ======
    # plot colors
    ims2 = ax2.scatter(amodel6.M[0], amodel6.vrot[0], c= amodel6.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel7.M[0], amodel7.vrot[0], c= amodel7.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel8.M[0], amodel8.vrot[0], c= amodel8.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel9.M[0], amodel9.vrot[0], c= amodel9.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel10.M[0], amodel10.vrot[0], c= amodel10.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(bmodel6.M[0], bmodel6.vrot[0], c= bmodel6.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel7.M[0], bmodel7.vrot[0], c= bmodel7.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel8.M[0], bmodel8.vrot[0], c= bmodel8.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel9.M[0], bmodel9.vrot[0], c= bmodel9.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel10.M[0], bmodel10.vrot[0], c= bmodel10.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(cmodel6.M[0], cmodel6.vrot[0], c= cmodel6.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel7.M[0], cmodel7.vrot[0], c= cmodel7.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel8.M[0], cmodel8.vrot[0], c= cmodel8.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel9.M[0], cmodel9.vrot[0], c= cmodel9.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel10.M[0], cmodel10.vrot[0], c= cmodel10.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(dmodel6.M[0], dmodel6.vrot[0], c= dmodel6.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel7.M[0], dmodel7.vrot[0], c= dmodel7.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel8.M[0], dmodel8.vrot[0], c= dmodel8.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel9.M[0], dmodel9.vrot[0], c= dmodel9.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel10.M[0], dmodel10.vrot[0], c= dmodel10.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    cbar2 = fig.colorbar(ims2, ax = ax2)
    cbar2.set_label('Nitrogen Mass]')

    # ====== 3 ======
    # plot colors
    ims3 = ax3.scatter(amodel11.M[0], amodel11.vrot[0], c= amodel11.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel12.M[0], amodel12.vrot[0], c= amodel12.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel13.M[0], amodel13.vrot[0], c= amodel13.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel14.M[0], amodel14.vrot[0], c= amodel14.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel15.M[0], amodel15.vrot[0], c= amodel15.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(bmodel11.M[0], bmodel11.vrot[0], c= bmodel11.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel12.M[0], bmodel12.vrot[0], c= bmodel12.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel13.M[0], bmodel13.vrot[0], c= bmodel13.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel14.M[0], bmodel14.vrot[0], c= bmodel14.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel15.M[0], bmodel15.vrot[0], c= bmodel15.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(cmodel11.M[0], cmodel11.vrot[0], c= cmodel11.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel12.M[0], cmodel12.vrot[0], c= cmodel12.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel13.M[0], cmodel13.vrot[0], c= cmodel13.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel14.M[0], cmodel14.vrot[0], c= cmodel14.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel15.M[0], cmodel15.vrot[0], c= cmodel15.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(dmodel11.M[0], dmodel11.vrot[0], c= dmodel11.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel12.M[0], dmodel12.vrot[0], c= dmodel12.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel13.M[0], dmodel13.vrot[0], c= dmodel13.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel14.M[0], dmodel14.vrot[0], c= dmodel14.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel15.M[0], dmodel15.vrot[0], c= dmodel15.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar3 = fig.colorbar(ims3, ax = ax3)
    # cbar3.set_label('Final Mass / Initial Mass')

    # ====== 4 ======
    # plot colors
    ims4 = ax4.scatter(amodel16.M[0], amodel16.vrot[0], c= amodel16.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel17.M[0], amodel17.vrot[0], c= amodel17.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel18.M[0], amodel18.vrot[0], c= amodel18.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel19.M[0], amodel19.vrot[0], c= amodel19.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel20.M[0], amodel20.vrot[0], c= amodel20.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(bmodel16.M[0], bmodel16.vrot[0], c= bmodel16.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel17.M[0], bmodel17.vrot[0], c= bmodel17.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel18.M[0], bmodel18.vrot[0], c= bmodel18.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel19.M[0], bmodel19.vrot[0], c= bmodel19.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel20.M[0], bmodel20.vrot[0], c= bmodel20.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(cmodel16.M[0], cmodel16.vrot[0], c= cmodel16.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel17.M[0], cmodel17.vrot[0], c= cmodel17.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel18.M[0], cmodel18.vrot[0], c= cmodel18.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel19.M[0], cmodel19.vrot[0], c= cmodel19.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel20.M[0], cmodel20.vrot[0], c= cmodel20.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(dmodel16.M[0], dmodel16.vrot[0], c= dmodel16.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel17.M[0], dmodel17.vrot[0], c= dmodel17.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel18.M[0], dmodel18.vrot[0], c= dmodel18.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel19.M[0], dmodel19.vrot[0], c= dmodel19.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel20.M[0], dmodel20.vrot[0], c= dmodel20.nnit[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    

    cbar4 = fig.colorbar(ims4, ax = ax4)
    cbar4.set_label('Nitrogen Mass')

    fig.tight_layout()
    plt.savefig('Plots/Overview/Nmass.png')


Nmass(avink01_20, avink01_30, avink01_40, avink01_50, avink01_60, bvink01_20, bvink01_30, bvink01_40, bvink01_50, bvink01_60, cvink01_20, cvink01_30, cvink01_40, cvink01_50, cvink01_60, dvink01_20, dvink01_30, dvink01_40, dvink01_50, dvink01_60,
avink18_20, avink18_30, avink18_40, avink18_50, avink18_60, bvink18_20, bvink18_30, bvink18_40, bvink18_50, bvink18_60, cvink18_20, cvink18_30, cvink18_40, cvink18_50, cvink18_60, dvink18_20, dvink18_30, dvink18_40, dvink18_50, dvink18_60,
aleuven_20, aleuven_30, aleuven_40, aleuven_50, aleuven_60, bleuven_20, bleuven_30, bleuven_40, bleuven_50, bleuven_60, cleuven_20, cleuven_30, cleuven_40, cleuven_50, cleuven_60, dleuven_20, dleuven_30, dleuven_40, dleuven_50, dleuven_60,
akrticka_20, akrticka_30, akrticka_40, akrticka_50, akrticka_60, bkrticka_20, bkrticka_30, bkrticka_40, bkrticka_50, bkrticka_60, ckrticka_20, ckrticka_30, ckrticka_40, ckrticka_50, ckrticka_60, dkrticka_20, dkrticka_30, dkrticka_40, dkrticka_50, dkrticka_60)

# ================================================================

def Hemass(amodel1, amodel2, amodel3, amodel4, amodel5, bmodel1, bmodel2, bmodel3, bmodel4, bmodel5, cmodel1, cmodel2, cmodel3, cmodel4, cmodel5, dmodel1, dmodel2, dmodel3, dmodel4, dmodel5,
amodel6, amodel7, amodel8, amodel9, amodel10, bmodel6, bmodel7, bmodel8, bmodel9, bmodel10, cmodel6, cmodel7, cmodel8, cmodel9, cmodel10, dmodel6, dmodel7, dmodel8, dmodel9, dmodel10,
amodel11, amodel12, amodel13, amodel14, amodel15, bmodel11, bmodel12, bmodel13, bmodel14, bmodel15, cmodel11, cmodel12, cmodel13, cmodel14, cmodel15, dmodel11, dmodel12, dmodel13, dmodel14, dmodel15,
amodel16, amodel17, amodel18, amodel19, amodel20, bmodel16, bmodel17, bmodel18, bmodel19, bmodel20, cmodel16, cmodel17, cmodel18, cmodel19, cmodel20, dmodel16, dmodel17, dmodel18, dmodel19, dmodel20):

    # end of list
    limit = -1

    # lim1 = len(amodel1.age)
    # lim2 = len(amodel2.age)
    # lim3 = len(amodel3.age)
    # lim4 = len(amodel4.age)
    # lim5 = len(amodel5.age)

    min1 = 0.00001
    max1 = 0.0001

    # ------ Set Plot Style ------
    default_style()
    fig, ax1, ax2, ax3, ax4, colormap = He_mass()
    
    # ====== 1 ======
    # plot colors
    ims1 = ax1.scatter(amodel1.M[0], amodel1.vrot[0], c= amodel1.histM[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel2.M[0], amodel2.vrot[0], c= amodel2.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel3.M[0], amodel3.vrot[0], c= amodel3.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel4.M[0], amodel4.vrot[0], c= amodel4.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel5.M[0], amodel5.vrot[0], c= amodel5.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(bmodel1.M[0], bmodel1.vrot[0], c= bmodel1.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel2.M[0], bmodel2.vrot[0], c= bmodel2.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel3.M[0], bmodel3.vrot[0], c= bmodel3.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel4.M[0], bmodel4.vrot[0], c= bmodel4.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel5.M[0], bmodel5.vrot[0], c= bmodel5.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(cmodel1.M[0], cmodel1.vrot[0], c= cmodel1.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel2.M[0], cmodel2.vrot[0], c= cmodel2.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel3.M[0], cmodel3.vrot[0], c= cmodel3.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel4.M[0], cmodel4.vrot[0], c= cmodel4.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel5.M[0], cmodel5.vrot[0], c= cmodel5.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(dmodel1.M[0], dmodel1.vrot[0], c= dmodel1.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel2.M[0], dmodel2.vrot[0], c= dmodel2.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel3.M[0], dmodel3.vrot[0], c= dmodel3.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel4.M[0], dmodel4.vrot[0], c= dmodel4.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel5.M[0], dmodel5.vrot[0], c= dmodel5.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar = fig.colorbar(ims1, ax = ax1)
    # cbar.set_label('Final Mass / Initial Mass')

    # ====== 2 ======
    # plot colors
    ims2 = ax2.scatter(amodel6.M[0], amodel6.vrot[0], c= amodel6.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel7.M[0], amodel7.vrot[0], c= amodel7.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel8.M[0], amodel8.vrot[0], c= amodel8.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel9.M[0], amodel9.vrot[0], c= amodel9.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel10.M[0], amodel10.vrot[0], c= amodel10.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(bmodel6.M[0], bmodel6.vrot[0], c= bmodel6.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel7.M[0], bmodel7.vrot[0], c= bmodel7.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel8.M[0], bmodel8.vrot[0], c= bmodel8.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel9.M[0], bmodel9.vrot[0], c= bmodel9.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel10.M[0], bmodel10.vrot[0], c= bmodel10.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(cmodel6.M[0], cmodel6.vrot[0], c= cmodel6.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel7.M[0], cmodel7.vrot[0], c= cmodel7.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel8.M[0], cmodel8.vrot[0], c= cmodel8.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel9.M[0], cmodel9.vrot[0], c= cmodel9.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel10.M[0], cmodel10.vrot[0], c= cmodel10.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(dmodel6.M[0], dmodel6.vrot[0], c= dmodel6.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel7.M[0], dmodel7.vrot[0], c= dmodel7.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel8.M[0], dmodel8.vrot[0], c= dmodel8.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel9.M[0], dmodel9.vrot[0], c= dmodel9.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel10.M[0], dmodel10.vrot[0], c= dmodel10.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    cbar2 = fig.colorbar(ims2, ax = ax2)
    cbar2.set_label('Helium Mass')

    # ====== 3 ======
    # plot colors
    ims3 = ax3.scatter(amodel11.M[0], amodel11.vrot[0], c= amodel11.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel12.M[0], amodel12.vrot[0], c= amodel12.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel13.M[0], amodel13.vrot[0], c= amodel13.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel14.M[0], amodel14.vrot[0], c= amodel14.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel15.M[0], amodel15.vrot[0], c= amodel15.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(bmodel11.M[0], bmodel11.vrot[0], c= bmodel11.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel12.M[0], bmodel12.vrot[0], c= bmodel12.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel13.M[0], bmodel13.vrot[0], c= bmodel13.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel14.M[0], bmodel14.vrot[0], c= bmodel14.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel15.M[0], bmodel15.vrot[0], c= bmodel15.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(cmodel11.M[0], cmodel11.vrot[0], c= cmodel11.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel12.M[0], cmodel12.vrot[0], c= cmodel12.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel13.M[0], cmodel13.vrot[0], c= cmodel13.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel14.M[0], cmodel14.vrot[0], c= cmodel14.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel15.M[0], cmodel15.vrot[0], c= cmodel15.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(dmodel11.M[0], dmodel11.vrot[0], c= dmodel11.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel12.M[0], dmodel12.vrot[0], c= dmodel12.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel13.M[0], dmodel13.vrot[0], c= dmodel13.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel14.M[0], dmodel14.vrot[0], c= dmodel14.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel15.M[0], dmodel15.vrot[0], c= dmodel15.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar3 = fig.colorbar(ims3, ax = ax3)
    # cbar3.set_label('Final Mass / Initial Mass')

    # ====== 4 ======
    # plot colors
    ims4 = ax4.scatter(amodel16.M[0], amodel16.vrot[0], c= amodel16.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel17.M[0], amodel17.vrot[0], c= amodel17.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel18.M[0], amodel18.vrot[0], c= amodel18.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel19.M[0], amodel19.vrot[0], c= amodel19.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel20.M[0], amodel20.vrot[0], c= amodel20.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(bmodel16.M[0], bmodel16.vrot[0], c= bmodel16.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel17.M[0], bmodel17.vrot[0], c= bmodel17.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel18.M[0], bmodel18.vrot[0], c= bmodel18.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel19.M[0], bmodel19.vrot[0], c= bmodel19.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel20.M[0], bmodel20.vrot[0], c= bmodel20.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(cmodel16.M[0], cmodel16.vrot[0], c= cmodel16.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel17.M[0], cmodel17.vrot[0], c= cmodel17.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel18.M[0], cmodel18.vrot[0], c= cmodel18.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel19.M[0], cmodel19.vrot[0], c= cmodel19.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel20.M[0], cmodel20.vrot[0], c= cmodel20.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(dmodel16.M[0], dmodel16.vrot[0], c= dmodel16.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel17.M[0], dmodel17.vrot[0], c= dmodel17.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel18.M[0], dmodel18.vrot[0], c= dmodel18.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel19.M[0], dmodel19.vrot[0], c= dmodel19.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel20.M[0], dmodel20.vrot[0], c= dmodel20.nhe[limit], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    

    cbar4 = fig.colorbar(ims4, ax = ax4)
    cbar4.set_label('Helium Mass')

    fig.tight_layout()
    plt.savefig('Plots/Overview/Hemass.png')


Hemass(avink01_20, avink01_30, avink01_40, avink01_50, avink01_60, bvink01_20, bvink01_30, bvink01_40, bvink01_50, bvink01_60, cvink01_20, cvink01_30, cvink01_40, cvink01_50, cvink01_60, dvink01_20, dvink01_30, dvink01_40, dvink01_50, dvink01_60,
avink18_20, avink18_30, avink18_40, avink18_50, avink18_60, bvink18_20, bvink18_30, bvink18_40, bvink18_50, bvink18_60, cvink18_20, cvink18_30, cvink18_40, cvink18_50, cvink18_60, dvink18_20, dvink18_30, dvink18_40, dvink18_50, dvink18_60,
aleuven_20, aleuven_30, aleuven_40, aleuven_50, aleuven_60, bleuven_20, bleuven_30, bleuven_40, bleuven_50, bleuven_60, cleuven_20, cleuven_30, cleuven_40, cleuven_50, cleuven_60, dleuven_20, dleuven_30, dleuven_40, dleuven_50, dleuven_60,
akrticka_20, akrticka_30, akrticka_40, akrticka_50, akrticka_60, bkrticka_20, bkrticka_30, bkrticka_40, bkrticka_50, bkrticka_60, ckrticka_20, ckrticka_30, ckrticka_40, ckrticka_50, ckrticka_60, dkrticka_20, dkrticka_30, dkrticka_40, dkrticka_50, dkrticka_60)