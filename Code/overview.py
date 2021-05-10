# Script that makes plot

from data import *
from plots import *
from plotstyles import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np

ms = False

def initial_values(amodel1, amodel2, amodel3, amodel4, amodel5, bmodel1, bmodel2, bmodel3, bmodel4, bmodel5, cmodel1, cmodel2, cmodel3, cmodel4, cmodel5, dmodel1, dmodel2, dmodel3, dmodel4, dmodel5,
amodel6, amodel7, amodel8, amodel9, amodel10, bmodel6, bmodel7, bmodel8, bmodel9, bmodel10, cmodel6, cmodel7, cmodel8, cmodel9, cmodel10, dmodel6, dmodel7, dmodel8, dmodel9, dmodel10,
amodel11, amodel12, amodel13, amodel14, amodel15, bmodel11, bmodel12, bmodel13, bmodel14, bmodel15, cmodel11, cmodel12, cmodel13, cmodel14, cmodel15, dmodel11, dmodel12, dmodel13, dmodel14, dmodel15,
amodel16, amodel17, amodel18, amodel19, amodel20, bmodel16, bmodel17, bmodel18, bmodel19, bmodel20, cmodel16, cmodel17, cmodel18, cmodel19, cmodel20, dmodel16, dmodel17, dmodel18, dmodel19, dmodel20,
ms):

    # end of list
    if ms == True:
        # main sequence limit
        alim1 = amodel1.mainsequence()
        alim2 = amodel2.mainsequence()
        alim3 = amodel3.mainsequence()
        alim4 = amodel4.mainsequence()
        alim5 = amodel5.mainsequence()
        alim6 = amodel6.mainsequence()
        alim7 = amodel7.mainsequence()
        alim8 = amodel8.mainsequence()
        alim9 = amodel9.mainsequence()
        alim10 = amodel10.mainsequence()
        alim11 = amodel11.mainsequence()
        alim12 = amodel12.mainsequence()
        alim13 = amodel13.mainsequence()
        alim14 = amodel14.mainsequence()
        alim15 = amodel15.mainsequence()
        alim16 = amodel16.mainsequence()
        alim17 = amodel17.mainsequence()
        alim18 = amodel18.mainsequence()
        alim19 = amodel19.mainsequence()
        alim20 = amodel20.mainsequence()

        blim1 = bmodel1.mainsequence()
        blim2 = bmodel2.mainsequence()
        blim3 = bmodel3.mainsequence()
        blim4 = bmodel4.mainsequence()
        blim5 = bmodel5.mainsequence()
        blim6 = bmodel6.mainsequence()
        blim7 = bmodel7.mainsequence()
        blim8 = bmodel8.mainsequence()
        blim9 = bmodel9.mainsequence()
        blim10 = bmodel10.mainsequence()
        blim11 = bmodel11.mainsequence()
        blim12 = bmodel12.mainsequence()
        blim13 = bmodel13.mainsequence()
        blim14 = bmodel14.mainsequence()
        blim15 = bmodel15.mainsequence()
        blim16 = bmodel16.mainsequence()
        blim17 = bmodel17.mainsequence()
        blim18 = bmodel18.mainsequence()
        blim19 = bmodel19.mainsequence()
        blim20 = bmodel20.mainsequence()

        clim1 = cmodel1.mainsequence()
        clim2 = cmodel2.mainsequence()
        clim3 = cmodel3.mainsequence()
        clim4 = cmodel4.mainsequence()
        clim5 = cmodel5.mainsequence()
        clim6 = cmodel6.mainsequence()
        clim7 = cmodel7.mainsequence()
        clim8 = cmodel8.mainsequence()
        clim9 = cmodel9.mainsequence()
        clim10 = cmodel10.mainsequence()
        clim11 = cmodel11.mainsequence()
        clim12 = cmodel12.mainsequence()
        clim13 = cmodel13.mainsequence()
        clim14 = cmodel14.mainsequence()
        clim15 = cmodel15.mainsequence()
        clim16 = cmodel16.mainsequence()
        clim17 = cmodel17.mainsequence()
        clim18 = cmodel18.mainsequence()
        clim19 = cmodel19.mainsequence()
        clim20 = cmodel20.mainsequence()

        dlim1 = dmodel1.mainsequence()
        dlim2 = dmodel2.mainsequence()
        dlim3 = dmodel3.mainsequence()
        dlim4 = dmodel4.mainsequence()
        dlim5 = dmodel5.mainsequence()
        dlim6 = dmodel6.mainsequence()
        dlim7 = dmodel7.mainsequence()
        dlim8 = dmodel8.mainsequence()
        dlim9 = dmodel9.mainsequence()
        dlim10 = dmodel10.mainsequence()
        dlim11 = dmodel11.mainsequence()
        dlim12 = dmodel12.mainsequence()
        dlim13 = dmodel13.mainsequence()
        dlim14 = dmodel14.mainsequence()
        dlim15 = dmodel15.mainsequence()
        dlim16 = dmodel16.mainsequence()
        dlim17 = dmodel17.mainsequence()
        dlim18 = dmodel18.mainsequence()
        dlim19 = dmodel19.mainsequence()
        dlim20 = dmodel20.mainsequence()
        

        # limit colorbar
        min1 = 0.8
        max1 = 1
        limit = '_ms'
        folder = 'MainSequence'
    else:
        # full simulation
        alim1 = -1
        alim2 = -1
        alim3 = -1
        alim4 = -1
        alim5 = -1
        alim6 = -1
        alim7 = -1
        alim8 = -1
        alim9 = -1
        alim10 = -1
        alim11 = -1
        alim12 = -1
        alim13 = -1
        alim14 = -1
        alim15 = -1
        alim16 = -1
        alim17 = -1
        alim18 = -1
        alim19 = -1
        alim20 = -1

        blim1 = -1
        blim2 = -1
        blim3 = -1
        blim4 = -1
        blim5 = -1
        blim6 = -1
        blim7 = -1
        blim8 = -1
        blim9 = -1
        blim10 = -1
        blim11 = -1
        blim12 = -1
        blim13 = -1
        blim14 = -1
        blim15 = -1
        blim16 = -1
        blim17 = -1
        blim18 = -1
        blim19 = -1
        blim20 = -1

        clim1 = -1
        clim2 = -1
        clim3 = -1
        clim4 = -1
        clim5 = -1
        clim6 = -1
        clim7 = -1
        clim8 = -1
        clim9 = -1
        clim10 = -1
        clim11 = -1
        clim12 = -1
        clim13 = -1
        clim14 = -1
        clim15 = -1
        clim16 = -1
        clim17 = -1
        clim18 = -1
        clim19 = -1
        clim20 = -1

        dlim1 = -1
        dlim2 = -1
        dlim3 = -1
        dlim4 = -1
        dlim5 = -1
        dlim6 = -1
        dlim7 = -1
        dlim8 = -1
        dlim9 = -1
        dlim10 = -1
        dlim11 = -1
        dlim12 = -1
        dlim13 = -1
        dlim14 = -1
        dlim15 = -1
        dlim16 = -1
        dlim17 = -1
        dlim18 = -1
        dlim19 = -1
        dlim20 = -1

        # colorbar
        min1 = 0.8
        max1 = 1

        limit = ''
        folder = 'FullSimulation'

    # ------ Set Plot Style ------
    default_style()
    fig, ax1, ax2, ax3, ax4, colormap = m_init(ms)
    
    # ====== 1 ======
    # plot colors
    ims1 = ax1.scatter(amodel1.M[0], amodel1.vrot[0], c= amodel1.histM[alim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel2.M[0], amodel2.vrot[0], c= amodel2.histM[alim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel3.M[0], amodel3.vrot[0], c= amodel3.histM[alim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel4.M[0], amodel4.vrot[0], c= amodel4.histM[alim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel5.M[0], amodel5.vrot[0], c= amodel5.histM[alim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(bmodel1.M[0], bmodel1.vrot[0], c= bmodel1.histM[blim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel2.M[0], bmodel2.vrot[0], c= bmodel2.histM[blim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel3.M[0], bmodel3.vrot[0], c= bmodel3.histM[blim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel4.M[0], bmodel4.vrot[0], c= bmodel4.histM[blim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel5.M[0], bmodel5.vrot[0], c= bmodel5.histM[blim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(cmodel1.M[0], cmodel1.vrot[0], c= cmodel1.histM[clim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel2.M[0], cmodel2.vrot[0], c= cmodel2.histM[clim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel3.M[0], cmodel3.vrot[0], c= cmodel3.histM[clim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel4.M[0], cmodel4.vrot[0], c= cmodel4.histM[clim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel5.M[0], cmodel5.vrot[0], c= cmodel5.histM[clim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(dmodel1.M[0], dmodel1.vrot[0], c= dmodel1.histM[dlim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel2.M[0], dmodel2.vrot[0], c= dmodel2.histM[dlim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel3.M[0], dmodel3.vrot[0], c= dmodel3.histM[dlim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel4.M[0], dmodel4.vrot[0], c= dmodel4.histM[dlim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel5.M[0], dmodel5.vrot[0], c= dmodel5.histM[dlim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar = fig.colorbar(ims1, ax = ax1)
    # cbar.set_label('Final Mass / Initial Mass')

    # ====== 2 ======
    # plot colors
    ims2 = ax2.scatter(amodel6.M[0], amodel6.vrot[0], c= amodel6.histM[alim6], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel7.M[0], amodel7.vrot[0], c= amodel7.histM[alim7], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel8.M[0], amodel8.vrot[0], c= amodel8.histM[alim8], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel9.M[0], amodel9.vrot[0], c= amodel9.histM[alim9], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel10.M[0], amodel10.vrot[0], c= amodel10.histM[alim10], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(bmodel6.M[0], bmodel6.vrot[0], c= bmodel6.histM[blim6], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel7.M[0], bmodel7.vrot[0], c= bmodel7.histM[blim7], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel8.M[0], bmodel8.vrot[0], c= bmodel8.histM[blim8], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel9.M[0], bmodel9.vrot[0], c= bmodel9.histM[blim9], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel10.M[0], bmodel10.vrot[0], c= bmodel10.histM[blim10], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(cmodel6.M[0], cmodel6.vrot[0], c= cmodel6.histM[clim6], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel7.M[0], cmodel7.vrot[0], c= cmodel7.histM[clim7], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel8.M[0], cmodel8.vrot[0], c= cmodel8.histM[clim8], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel9.M[0], cmodel9.vrot[0], c= cmodel9.histM[clim9], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel10.M[0], cmodel10.vrot[0], c= cmodel10.histM[clim10], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(dmodel6.M[0], dmodel6.vrot[0], c= dmodel6.histM[dlim6], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel7.M[0], dmodel7.vrot[0], c= dmodel7.histM[dlim7], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel8.M[0], dmodel8.vrot[0], c= dmodel8.histM[dlim8], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel9.M[0], dmodel9.vrot[0], c= dmodel9.histM[dlim9], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel10.M[0], dmodel10.vrot[0], c= dmodel10.histM[dlim10], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    cbar2 = fig.colorbar(ims2, ax = ax2)
    cbar2.set_label('Final Mass / Initial Mass')

    # ====== 3 ======
    # plot colors
    ims3 = ax3.scatter(amodel11.M[0], amodel11.vrot[0], c= amodel11.histM[alim11], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel12.M[0], amodel12.vrot[0], c= amodel12.histM[alim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel13.M[0], amodel13.vrot[0], c= amodel13.histM[alim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel14.M[0], amodel14.vrot[0], c= amodel14.histM[alim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel15.M[0], amodel15.vrot[0], c= amodel15.histM[alim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    #ax3.scatter(bmodel11.M[0], bmodel11.vrot[0], c= bmodel11.histM[130], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel12.M[0], bmodel12.vrot[0], c= bmodel12.histM[blim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel13.M[0], bmodel13.vrot[0], c= bmodel13.histM[blim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel14.M[0], bmodel14.vrot[0], c= bmodel14.histM[blim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel15.M[0], bmodel15.vrot[0], c= bmodel15.histM[blim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(cmodel11.M[0], cmodel11.vrot[0], c= cmodel11.histM[clim11], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel12.M[0], cmodel12.vrot[0], c= cmodel12.histM[clim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel13.M[0], cmodel13.vrot[0], c= cmodel13.histM[clim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel14.M[0], cmodel14.vrot[0], c= cmodel14.histM[clim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel15.M[0], cmodel15.vrot[0], c= cmodel15.histM[clim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(dmodel11.M[0], dmodel11.vrot[0], c= dmodel11.histM[dlim11], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel12.M[0], dmodel12.vrot[0], c= dmodel12.histM[dlim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel13.M[0], dmodel13.vrot[0], c= dmodel13.histM[dlim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel14.M[0], dmodel14.vrot[0], c= dmodel14.histM[dlim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel15.M[0], dmodel15.vrot[0], c= dmodel15.histM[dlim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar3 = fig.colorbar(ims3, ax = ax3)
    # cbar3.set_label('Final Mass / Initial Mass')

    # ====== 4 ======
    # plot colors
    ims4 = ax4.scatter(amodel16.M[0], amodel16.vrot[0], c= amodel16.histM[alim16], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel17.M[0], amodel17.vrot[0], c= amodel17.histM[alim17], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel18.M[0], amodel18.vrot[0], c= amodel18.histM[alim18], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel19.M[0], amodel19.vrot[0], c= amodel19.histM[alim19], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel20.M[0], amodel20.vrot[0], c= amodel20.histM[alim20], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(bmodel16.M[0], bmodel16.vrot[0], c= bmodel16.histM[blim16], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel17.M[0], bmodel17.vrot[0], c= bmodel17.histM[blim17], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel18.M[0], bmodel18.vrot[0], c= bmodel18.histM[blim18], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel19.M[0], bmodel19.vrot[0], c= bmodel19.histM[blim19], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel20.M[0], bmodel20.vrot[0], c= bmodel20.histM[blim20], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(cmodel16.M[0], cmodel16.vrot[0], c= cmodel16.histM[clim16], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel17.M[0], cmodel17.vrot[0], c= cmodel17.histM[clim17], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel18.M[0], cmodel18.vrot[0], c= cmodel18.histM[clim18], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel19.M[0], cmodel19.vrot[0], c= cmodel19.histM[clim19], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel20.M[0], cmodel20.vrot[0], c= cmodel20.histM[clim20], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(dmodel16.M[0], dmodel16.vrot[0], c= dmodel16.histM[dlim16], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel17.M[0], dmodel17.vrot[0], c= dmodel17.histM[dlim17], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel18.M[0], dmodel18.vrot[0], c= dmodel18.histM[dlim18], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel19.M[0], dmodel19.vrot[0], c= dmodel19.histM[dlim19], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel20.M[0], dmodel20.vrot[0], c= dmodel20.histM[dlim20], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    cbar4 = fig.colorbar(ims4, ax = ax4)
    cbar4.set_label('Final Mass / Initial Mass')

    fig.tight_layout()
    plt.savefig(f'Plots/Overview/{folder}/Final_mass{limit}.png')


initial_values(avink01_20, avink01_30, avink01_40, avink01_50, avink01_60, bvink01_20, bvink01_30, bvink01_40, bvink01_50, bvink01_60, cvink01_20, cvink01_30, cvink01_40, cvink01_50, cvink01_60, dvink01_20, dvink01_30, dvink01_40, dvink01_50, dvink01_60,
avink18_20, avink18_30, avink18_40, avink18_50, avink18_60, bvink18_20, bvink18_30, bvink18_40, bvink18_50, bvink18_60, cvink18_20, cvink18_30, cvink18_40, cvink18_50, cvink18_60, dvink18_20, dvink18_30, dvink18_40, dvink18_50, dvink18_60,
aleuven_20, aleuven_30, aleuven_40, aleuven_50, aleuven_60, bleuven_20, bleuven_30, bleuven_40, bleuven_50, bleuven_60, cleuven_20, cleuven_30, cleuven_40, cleuven_50, cleuven_60, dleuven_20, dleuven_30, dleuven_40, dleuven_50, dleuven_60,
akrticka_20, akrticka_30, akrticka_40, akrticka_50, akrticka_60, bkrticka_20, bkrticka_30, bkrticka_40, bkrticka_50, bkrticka_60, ckrticka_20, ckrticka_30, ckrticka_40, ckrticka_50, ckrticka_60, dkrticka_20, dkrticka_30, dkrticka_40, dkrticka_50, dkrticka_60,
ms)

# ============================================================

def envelopemass(amodel1, amodel2, amodel3, amodel4, amodel5, bmodel1, bmodel2, bmodel3, bmodel4, bmodel5, cmodel1, cmodel2, cmodel3, cmodel4, cmodel5, dmodel1, dmodel2, dmodel3, dmodel4, dmodel5,
amodel6, amodel7, amodel8, amodel9, amodel10, bmodel6, bmodel7, bmodel8, bmodel9, bmodel10, cmodel6, cmodel7, cmodel8, cmodel9, cmodel10, dmodel6, dmodel7, dmodel8, dmodel9, dmodel10,
amodel11, amodel12, amodel13, amodel14, amodel15, bmodel11, bmodel12, bmodel13, bmodel14, bmodel15, cmodel11, cmodel12, cmodel13, cmodel14, cmodel15, dmodel11, dmodel12, dmodel13, dmodel14, dmodel15,
amodel16, amodel17, amodel18, amodel19, amodel20, bmodel16, bmodel17, bmodel18, bmodel19, bmodel20, cmodel16, cmodel17, cmodel18, cmodel19, cmodel20, dmodel16, dmodel17, dmodel18, dmodel19, dmodel20,
ms):

    # end of list
    if ms == True:
        # main sequence limit
        alim1 = amodel1.mainsequence()
        alim2 = amodel2.mainsequence()
        alim3 = amodel3.mainsequence()
        alim4 = amodel4.mainsequence()
        alim5 = amodel5.mainsequence()
        alim6 = amodel6.mainsequence()
        alim7 = amodel7.mainsequence()
        alim8 = amodel8.mainsequence()
        alim9 = amodel9.mainsequence()
        alim10 = amodel10.mainsequence()
        alim11 = amodel11.mainsequence()
        alim12 = amodel12.mainsequence()
        alim13 = amodel13.mainsequence()
        alim14 = amodel14.mainsequence()
        alim15 = amodel15.mainsequence()
        alim16 = amodel16.mainsequence()
        alim17 = amodel17.mainsequence()
        alim18 = amodel18.mainsequence()
        alim19 = amodel19.mainsequence()
        alim20 = amodel20.mainsequence()

        blim1 = bmodel1.mainsequence()
        blim2 = bmodel2.mainsequence()
        blim3 = bmodel3.mainsequence()
        blim4 = bmodel4.mainsequence()
        blim5 = bmodel5.mainsequence()
        blim6 = bmodel6.mainsequence()
        blim7 = bmodel7.mainsequence()
        blim8 = bmodel8.mainsequence()
        blim9 = bmodel9.mainsequence()
        blim10 = bmodel10.mainsequence()
        blim11 = bmodel11.mainsequence()
        blim12 = bmodel12.mainsequence()
        blim13 = bmodel13.mainsequence()
        blim14 = bmodel14.mainsequence()
        blim15 = bmodel15.mainsequence()
        blim16 = bmodel16.mainsequence()
        blim17 = bmodel17.mainsequence()
        blim18 = bmodel18.mainsequence()
        blim19 = bmodel19.mainsequence()
        blim20 = bmodel20.mainsequence()

        clim1 = cmodel1.mainsequence()
        clim2 = cmodel2.mainsequence()
        clim3 = cmodel3.mainsequence()
        clim4 = cmodel4.mainsequence()
        clim5 = cmodel5.mainsequence()
        clim6 = cmodel6.mainsequence()
        clim7 = cmodel7.mainsequence()
        clim8 = cmodel8.mainsequence()
        clim9 = cmodel9.mainsequence()
        clim10 = cmodel10.mainsequence()
        clim11 = cmodel11.mainsequence()
        clim12 = cmodel12.mainsequence()
        clim13 = cmodel13.mainsequence()
        clim14 = cmodel14.mainsequence()
        clim15 = cmodel15.mainsequence()
        clim16 = cmodel16.mainsequence()
        clim17 = cmodel17.mainsequence()
        clim18 = cmodel18.mainsequence()
        clim19 = cmodel19.mainsequence()
        clim20 = cmodel20.mainsequence()

        dlim1 = dmodel1.mainsequence()
        dlim2 = dmodel2.mainsequence()
        dlim3 = dmodel3.mainsequence()
        dlim4 = dmodel4.mainsequence()
        dlim5 = dmodel5.mainsequence()
        dlim6 = dmodel6.mainsequence()
        dlim7 = dmodel7.mainsequence()
        dlim8 = dmodel8.mainsequence()
        dlim9 = dmodel9.mainsequence()
        dlim10 = dmodel10.mainsequence()
        dlim11 = dmodel11.mainsequence()
        dlim12 = dmodel12.mainsequence()
        dlim13 = dmodel13.mainsequence()
        dlim14 = dmodel14.mainsequence()
        dlim15 = dmodel15.mainsequence()
        dlim16 = dmodel16.mainsequence()
        dlim17 = dmodel17.mainsequence()
        dlim18 = dmodel18.mainsequence()
        dlim19 = dmodel19.mainsequence()
        dlim20 = dmodel20.mainsequence()
        
        # limit colorbar
        min1 = 0
        max1 = 60
        limit = '_ms'
        folder = 'MainSequence'
    else:
        # full simulation
        alim1 = -1
        alim2 = -1
        alim3 = -1
        alim4 = -1
        alim5 = -1
        alim6 = -1
        alim7 = -1
        alim8 = -1
        alim9 = -1
        alim10 = -1
        alim11 = -1
        alim12 = -1
        alim13 = -1
        alim14 = -1
        alim15 = -1
        alim16 = -1
        alim17 = -1
        alim18 = -1
        alim19 = -1
        alim20 = -1

        blim1 = -1
        blim2 = -1
        blim3 = -1
        blim4 = -1
        blim5 = -1
        blim6 = -1
        blim7 = -1
        blim8 = -1
        blim9 = -1
        blim10 = -1
        blim11 = -1
        blim12 = -1
        blim13 = -1
        blim14 = -1
        blim15 = -1
        blim16 = -1
        blim17 = -1
        blim18 = -1
        blim19 = -1
        blim20 = -1

        clim1 = -1
        clim2 = -1
        clim3 = -1
        clim4 = -1
        clim5 = -1
        clim6 = -1
        clim7 = -1
        clim8 = -1
        clim9 = -1
        clim10 = -1
        clim11 = -1
        clim12 = -1
        clim13 = -1
        clim14 = -1
        clim15 = -1
        clim16 = -1
        clim17 = -1
        clim18 = -1
        clim19 = -1
        clim20 = -1

        dlim1 = -1
        dlim2 = -1
        dlim3 = -1
        dlim4 = -1
        dlim5 = -1
        dlim6 = -1
        dlim7 = -1
        dlim8 = -1
        dlim9 = -1
        dlim10 = -1
        dlim11 = -1
        dlim12 = -1
        dlim13 = -1
        dlim14 = -1
        dlim15 = -1
        dlim16 = -1
        dlim17 = -1
        dlim18 = -1
        dlim19 = -1
        dlim20 = -1

        # limit colorbar
        min1 = 0
        max1 = 60

        limit = ''
        folder = 'FullSimulation'

    # ------ Set Plot Style ------
    default_style()
    fig, ax1, ax2, ax3, ax4, colormap = env_mass(ms)
    
    # ====== 1 ======
    # plot colors
    ims1 = ax1.scatter(amodel1.M[0], amodel1.vrot[0], c= amodel1.envelope_mass[alim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel2.M[0], amodel2.vrot[0], c= amodel2.envelope_mass[alim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel3.M[0], amodel3.vrot[0], c= amodel3.envelope_mass[alim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel4.M[0], amodel4.vrot[0], c= amodel4.envelope_mass[alim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel5.M[0], amodel5.vrot[0], c= amodel5.envelope_mass[alim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(bmodel1.M[0], bmodel1.vrot[0], c= bmodel1.envelope_mass[blim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel2.M[0], bmodel2.vrot[0], c= bmodel2.envelope_mass[blim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel3.M[0], bmodel3.vrot[0], c= bmodel3.envelope_mass[blim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel4.M[0], bmodel4.vrot[0], c= bmodel4.envelope_mass[blim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel5.M[0], bmodel5.vrot[0], c= bmodel5.envelope_mass[blim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(cmodel1.M[0], cmodel1.vrot[0], c= cmodel1.envelope_mass[clim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel2.M[0], cmodel2.vrot[0], c= cmodel2.envelope_mass[clim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel3.M[0], cmodel3.vrot[0], c= cmodel3.envelope_mass[clim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel4.M[0], cmodel4.vrot[0], c= cmodel4.envelope_mass[clim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel5.M[0], cmodel5.vrot[0], c= cmodel5.envelope_mass[clim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(dmodel1.M[0], dmodel1.vrot[0], c= dmodel1.envelope_mass[dlim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel2.M[0], dmodel2.vrot[0], c= dmodel2.envelope_mass[dlim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel3.M[0], dmodel3.vrot[0], c= dmodel3.envelope_mass[dlim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel4.M[0], dmodel4.vrot[0], c= dmodel4.envelope_mass[dlim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel5.M[0], dmodel5.vrot[0], c= dmodel5.envelope_mass[dlim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar = fig.colorbar(ims1, ax = ax1)
    # cbar.set_label('Final Mass / Initial Mass')

    # ====== 2 ======
    # plot colors
    ims2 = ax2.scatter(amodel6.M[0], amodel6.vrot[0], c= amodel6.envelope_mass[alim6], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel7.M[0], amodel7.vrot[0], c= amodel7.envelope_mass[alim7], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel8.M[0], amodel8.vrot[0], c= amodel8.envelope_mass[alim8], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel9.M[0], amodel9.vrot[0], c= amodel9.envelope_mass[alim9], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel10.M[0], amodel10.vrot[0], c= amodel10.envelope_mass[alim10], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(bmodel6.M[0], bmodel6.vrot[0], c= bmodel6.envelope_mass[blim6], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel7.M[0], bmodel7.vrot[0], c= bmodel7.envelope_mass[blim7], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel8.M[0], bmodel8.vrot[0], c= bmodel8.envelope_mass[blim8], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel9.M[0], bmodel9.vrot[0], c= bmodel9.envelope_mass[blim9], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel10.M[0], bmodel10.vrot[0], c= bmodel10.envelope_mass[blim10], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(cmodel6.M[0], cmodel6.vrot[0], c= cmodel6.envelope_mass[clim6], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel7.M[0], cmodel7.vrot[0], c= cmodel7.envelope_mass[clim7], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel8.M[0], cmodel8.vrot[0], c= cmodel8.envelope_mass[clim8], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel9.M[0], cmodel9.vrot[0], c= cmodel9.envelope_mass[clim9], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel10.M[0], cmodel10.vrot[0], c= cmodel10.envelope_mass[clim10], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(dmodel6.M[0], dmodel6.vrot[0], c= dmodel6.envelope_mass[dlim6], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel7.M[0], dmodel7.vrot[0], c= dmodel7.envelope_mass[dlim7], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel8.M[0], dmodel8.vrot[0], c= dmodel8.envelope_mass[dlim8], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel9.M[0], dmodel9.vrot[0], c= dmodel9.envelope_mass[dlim9], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel10.M[0], dmodel10.vrot[0], c= dmodel10.envelope_mass[dlim10], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    cbar2 = fig.colorbar(ims2, ax = ax2)
    cbar2.set_label('Envelope Mass [M$_{\odot}$]')

    # ====== 3 ======
    # plot colors
    ims3 = ax3.scatter(amodel11.M[0], amodel11.vrot[0], c= amodel11.envelope_mass[alim11], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel12.M[0], amodel12.vrot[0], c= amodel12.envelope_mass[alim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel13.M[0], amodel13.vrot[0], c= amodel13.envelope_mass[alim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel14.M[0], amodel14.vrot[0], c= amodel14.envelope_mass[alim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel15.M[0], amodel15.vrot[0], c= amodel15.envelope_mass[alim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    #ax3.scatter(bmodel11.M[0], bmodel11.vrot[0], c= bmodel11.envelope_mass[blim11], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel12.M[0], bmodel12.vrot[0], c= bmodel12.envelope_mass[blim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel13.M[0], bmodel13.vrot[0], c= bmodel13.envelope_mass[blim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel14.M[0], bmodel14.vrot[0], c= bmodel14.envelope_mass[blim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel15.M[0], bmodel15.vrot[0], c= bmodel15.envelope_mass[blim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(cmodel11.M[0], cmodel11.vrot[0], c= cmodel11.envelope_mass[clim11], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel12.M[0], cmodel12.vrot[0], c= cmodel12.envelope_mass[clim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel13.M[0], cmodel13.vrot[0], c= cmodel13.envelope_mass[clim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel14.M[0], cmodel14.vrot[0], c= cmodel14.envelope_mass[clim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel15.M[0], cmodel15.vrot[0], c= cmodel15.envelope_mass[clim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(dmodel11.M[0], dmodel11.vrot[0], c= dmodel11.envelope_mass[dlim11], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel12.M[0], dmodel12.vrot[0], c= dmodel12.envelope_mass[dlim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel13.M[0], dmodel13.vrot[0], c= dmodel13.envelope_mass[dlim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel14.M[0], dmodel14.vrot[0], c= dmodel14.envelope_mass[dlim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel15.M[0], dmodel15.vrot[0], c= dmodel15.envelope_mass[dlim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar3 = fig.colorbar(ims3, ax = ax3)
    # cbar3.set_label('Final Mass / Initial Mass')

    # ====== 4 ======
    # plot colors
    ims4 = ax4.scatter(amodel16.M[0], amodel16.vrot[0], c= amodel16.envelope_mass[alim16], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel17.M[0], amodel17.vrot[0], c= amodel17.envelope_mass[alim17], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel18.M[0], amodel18.vrot[0], c= amodel18.envelope_mass[alim18], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel19.M[0], amodel19.vrot[0], c= amodel19.envelope_mass[alim19], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel20.M[0], amodel20.vrot[0], c= amodel20.envelope_mass[alim20], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(bmodel16.M[0], bmodel16.vrot[0], c= bmodel16.envelope_mass[blim16], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel17.M[0], bmodel17.vrot[0], c= bmodel17.envelope_mass[blim17], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel18.M[0], bmodel18.vrot[0], c= bmodel18.envelope_mass[blim18], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel19.M[0], bmodel19.vrot[0], c= bmodel19.envelope_mass[blim19], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel20.M[0], bmodel20.vrot[0], c= bmodel20.envelope_mass[blim20], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(cmodel16.M[0], cmodel16.vrot[0], c= cmodel16.envelope_mass[clim16], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel17.M[0], cmodel17.vrot[0], c= cmodel17.envelope_mass[clim17], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel18.M[0], cmodel18.vrot[0], c= cmodel18.envelope_mass[clim18], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel19.M[0], cmodel19.vrot[0], c= cmodel19.envelope_mass[clim19], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel20.M[0], cmodel20.vrot[0], c= cmodel20.envelope_mass[clim20], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(dmodel16.M[0], dmodel16.vrot[0], c= dmodel16.envelope_mass[dlim16], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel17.M[0], dmodel17.vrot[0], c= dmodel17.envelope_mass[dlim17], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel18.M[0], dmodel18.vrot[0], c= dmodel18.envelope_mass[dlim18], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel19.M[0], dmodel19.vrot[0], c= dmodel19.envelope_mass[dlim19], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel20.M[0], dmodel20.vrot[0], c= dmodel20.envelope_mass[dlim20], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
  

    cbar4 = fig.colorbar(ims4, ax = ax4)
    cbar4.set_label('Envelope Mass [M$_{\odot}$]')

    fig.tight_layout()
    plt.savefig(f'Plots/Overview/{folder}/Envelope_mass{limit}.png')


envelopemass(avink01_20, avink01_30, avink01_40, avink01_50, avink01_60, bvink01_20, bvink01_30, bvink01_40, bvink01_50, bvink01_60, cvink01_20, cvink01_30, cvink01_40, cvink01_50, cvink01_60, dvink01_20, dvink01_30, dvink01_40, dvink01_50, dvink01_60,
avink18_20, avink18_30, avink18_40, avink18_50, avink18_60, bvink18_20, bvink18_30, bvink18_40, bvink18_50, bvink18_60, cvink18_20, cvink18_30, cvink18_40, cvink18_50, cvink18_60, dvink18_20, dvink18_30, dvink18_40, dvink18_50, dvink18_60,
aleuven_20, aleuven_30, aleuven_40, aleuven_50, aleuven_60, bleuven_20, bleuven_30, bleuven_40, bleuven_50, bleuven_60, cleuven_20, cleuven_30, cleuven_40, cleuven_50, cleuven_60, dleuven_20, dleuven_30, dleuven_40, dleuven_50, dleuven_60,
akrticka_20, akrticka_30, akrticka_40, akrticka_50, akrticka_60, bkrticka_20, bkrticka_30, bkrticka_40, bkrticka_50, bkrticka_60, ckrticka_20, ckrticka_30, ckrticka_40, ckrticka_50, ckrticka_60, dkrticka_20, dkrticka_30, dkrticka_40, dkrticka_50, dkrticka_60,
ms)

# ================================================================

def Nmass(amodel1, amodel2, amodel3, amodel4, amodel5, bmodel1, bmodel2, bmodel3, bmodel4, bmodel5, cmodel1, cmodel2, cmodel3, cmodel4, cmodel5, dmodel1, dmodel2, dmodel3, dmodel4, dmodel5,
amodel6, amodel7, amodel8, amodel9, amodel10, bmodel6, bmodel7, bmodel8, bmodel9, bmodel10, cmodel6, cmodel7, cmodel8, cmodel9, cmodel10, dmodel6, dmodel7, dmodel8, dmodel9, dmodel10,
amodel11, amodel12, amodel13, amodel14, amodel15, bmodel11, bmodel12, bmodel13, bmodel14, bmodel15, cmodel11, cmodel12, cmodel13, cmodel14, cmodel15, dmodel11, dmodel12, dmodel13, dmodel14, dmodel15,
amodel16, amodel17, amodel18, amodel19, amodel20, bmodel16, bmodel17, bmodel18, bmodel19, bmodel20, cmodel16, cmodel17, cmodel18, cmodel19, cmodel20, dmodel16, dmodel17, dmodel18, dmodel19, dmodel20,
ms):

    # end of list
    if ms == True:
        # main sequence limit
        alim1 = amodel1.mainsequence()
        alim2 = amodel2.mainsequence()
        alim3 = amodel3.mainsequence()
        alim4 = amodel4.mainsequence()
        alim5 = amodel5.mainsequence()
        alim6 = amodel6.mainsequence()
        alim7 = amodel7.mainsequence()
        alim8 = amodel8.mainsequence()
        alim9 = amodel9.mainsequence()
        alim10 = amodel10.mainsequence()
        alim11 = amodel11.mainsequence()
        alim12 = amodel12.mainsequence()
        alim13 = amodel13.mainsequence()
        alim14 = amodel14.mainsequence()
        alim15 = amodel15.mainsequence()
        alim16 = amodel16.mainsequence()
        alim17 = amodel17.mainsequence()
        alim18 = amodel18.mainsequence()
        alim19 = amodel19.mainsequence()
        alim20 = amodel20.mainsequence()

        blim1 = bmodel1.mainsequence()
        blim2 = bmodel2.mainsequence()
        blim3 = bmodel3.mainsequence()
        blim4 = bmodel4.mainsequence()
        blim5 = bmodel5.mainsequence()
        blim6 = bmodel6.mainsequence()
        blim7 = bmodel7.mainsequence()
        blim8 = bmodel8.mainsequence()
        blim9 = bmodel9.mainsequence()
        blim10 = bmodel10.mainsequence()
        blim11 = bmodel11.mainsequence()
        blim12 = bmodel12.mainsequence()
        blim13 = bmodel13.mainsequence()
        blim14 = bmodel14.mainsequence()
        blim15 = bmodel15.mainsequence()
        blim16 = bmodel16.mainsequence()
        blim17 = bmodel17.mainsequence()
        blim18 = bmodel18.mainsequence()
        blim19 = bmodel19.mainsequence()
        blim20 = bmodel20.mainsequence()

        clim1 = cmodel1.mainsequence()
        clim2 = cmodel2.mainsequence()
        clim3 = cmodel3.mainsequence()
        clim4 = cmodel4.mainsequence()
        clim5 = cmodel5.mainsequence()
        clim6 = cmodel6.mainsequence()
        clim7 = cmodel7.mainsequence()
        clim8 = cmodel8.mainsequence()
        clim9 = cmodel9.mainsequence()
        clim10 = cmodel10.mainsequence()
        clim11 = cmodel11.mainsequence()
        clim12 = cmodel12.mainsequence()
        clim13 = cmodel13.mainsequence()
        clim14 = cmodel14.mainsequence()
        clim15 = cmodel15.mainsequence()
        clim16 = cmodel16.mainsequence()
        clim17 = cmodel17.mainsequence()
        clim18 = cmodel18.mainsequence()
        clim19 = cmodel19.mainsequence()
        clim20 = cmodel20.mainsequence()

        dlim1 = dmodel1.mainsequence()
        dlim2 = dmodel2.mainsequence()
        dlim3 = dmodel3.mainsequence()
        dlim4 = dmodel4.mainsequence()
        dlim5 = dmodel5.mainsequence()
        dlim6 = dmodel6.mainsequence()
        dlim7 = dmodel7.mainsequence()
        dlim8 = dmodel8.mainsequence()
        dlim9 = dmodel9.mainsequence()
        dlim10 = dmodel10.mainsequence()
        dlim11 = dmodel11.mainsequence()
        dlim12 = dmodel12.mainsequence()
        dlim13 = dmodel13.mainsequence()
        dlim14 = dmodel14.mainsequence()
        dlim15 = dmodel15.mainsequence()
        dlim16 = dmodel16.mainsequence()
        dlim17 = dmodel17.mainsequence()
        dlim18 = dmodel18.mainsequence()
        dlim19 = dmodel19.mainsequence()
        dlim20 = dmodel20.mainsequence()
        
        # limit colorbar
        min1 = 0.00001
        max1 = 0.0001

        limit = '_ms'
        folder = 'MainSequence'
    else:
        # full simulation
        alim1 = -1
        alim2 = -1
        alim3 = -1
        alim4 = -1
        alim5 = -1
        alim6 = -1
        alim7 = -1
        alim8 = -1
        alim9 = -1
        alim10 = -1
        alim11 = -1
        alim12 = -1
        alim13 = -1
        alim14 = -1
        alim15 = -1
        alim16 = -1
        alim17 = -1
        alim18 = -1
        alim19 = -1
        alim20 = -1

        blim1 = -1
        blim2 = -1
        blim3 = -1
        blim4 = -1
        blim5 = -1
        blim6 = -1
        blim7 = -1
        blim8 = -1
        blim9 = -1
        blim10 = -1
        blim11 = -1
        blim12 = -1
        blim13 = -1
        blim14 = -1
        blim15 = -1
        blim16 = -1
        blim17 = -1
        blim18 = -1
        blim19 = -1
        blim20 = -1

        clim1 = -1
        clim2 = -1
        clim3 = -1
        clim4 = -1
        clim5 = -1
        clim6 = -1
        clim7 = -1
        clim8 = -1
        clim9 = -1
        clim10 = -1
        clim11 = -1
        clim12 = -1
        clim13 = -1
        clim14 = -1
        clim15 = -1
        clim16 = -1
        clim17 = -1
        clim18 = -1
        clim19 = -1
        clim20 = -1

        dlim1 = -1
        dlim2 = -1
        dlim3 = -1
        dlim4 = -1
        dlim5 = -1
        dlim6 = -1
        dlim7 = -1
        dlim8 = -1
        dlim9 = -1
        dlim10 = -1
        dlim11 = -1
        dlim12 = -1
        dlim13 = -1
        dlim14 = -1
        dlim15 = -1
        dlim16 = -1
        dlim17 = -1
        dlim18 = -1
        dlim19 = -1
        dlim20 = -1

        # limit colorbar
        min1 = 0.00001
        max1 = 0.0001

        limit = ''
        folder = 'FullSimulation'


    # ------ Set Plot Style ------
    default_style()
    fig, ax1, ax2, ax3, ax4, colormap = N_mass(ms)
    
    # ====== 1 ======
    # plot colors
    ims1 = ax1.scatter(amodel1.M[0], amodel1.vrot[0], c= amodel1.nnit[alim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel2.M[0], amodel2.vrot[0], c= amodel2.nnit[alim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel3.M[0], amodel3.vrot[0], c= amodel3.nnit[alim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel4.M[0], amodel4.vrot[0], c= amodel4.nnit[alim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel5.M[0], amodel5.vrot[0], c= amodel5.nnit[alim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(bmodel1.M[0], bmodel1.vrot[0], c= bmodel1.nnit[blim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel2.M[0], bmodel2.vrot[0], c= bmodel2.nnit[blim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel3.M[0], bmodel3.vrot[0], c= bmodel3.nnit[blim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel4.M[0], bmodel4.vrot[0], c= bmodel4.nnit[blim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel5.M[0], bmodel5.vrot[0], c= bmodel5.nnit[blim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(cmodel1.M[0], cmodel1.vrot[0], c= cmodel1.nnit[clim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel2.M[0], cmodel2.vrot[0], c= cmodel2.nnit[clim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel3.M[0], cmodel3.vrot[0], c= cmodel3.nnit[clim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel4.M[0], cmodel4.vrot[0], c= cmodel4.nnit[clim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel5.M[0], cmodel5.vrot[0], c= cmodel5.nnit[clim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(dmodel1.M[0], dmodel1.vrot[0], c= dmodel1.nnit[dlim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel2.M[0], dmodel2.vrot[0], c= dmodel2.nnit[dlim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel3.M[0], dmodel3.vrot[0], c= dmodel3.nnit[dlim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel4.M[0], dmodel4.vrot[0], c= dmodel4.nnit[dlim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel5.M[0], dmodel5.vrot[0], c= dmodel5.nnit[dlim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar = fig.colorbar(ims1, ax = ax1)
    # cbar.set_label('Final Mass / Initial Mass')

    # ====== 2 ======
    # plot colors
    ims2 = ax2.scatter(amodel6.M[0], amodel6.vrot[0], c= amodel6.nnit[alim6], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel7.M[0], amodel7.vrot[0], c= amodel7.nnit[alim7], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel8.M[0], amodel8.vrot[0], c= amodel8.nnit[alim8], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel9.M[0], amodel9.vrot[0], c= amodel9.nnit[alim9], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel10.M[0], amodel10.vrot[0], c= amodel10.nnit[alim10], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(bmodel6.M[0], bmodel6.vrot[0], c= bmodel6.nnit[blim6], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel7.M[0], bmodel7.vrot[0], c= bmodel7.nnit[blim7], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel8.M[0], bmodel8.vrot[0], c= bmodel8.nnit[blim8], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel9.M[0], bmodel9.vrot[0], c= bmodel9.nnit[blim9], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel10.M[0], bmodel10.vrot[0], c= bmodel10.nnit[blim10], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(cmodel6.M[0], cmodel6.vrot[0], c= cmodel6.nnit[clim6], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel7.M[0], cmodel7.vrot[0], c= cmodel7.nnit[clim7], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel8.M[0], cmodel8.vrot[0], c= cmodel8.nnit[clim8], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel9.M[0], cmodel9.vrot[0], c= cmodel9.nnit[clim9], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel10.M[0], cmodel10.vrot[0], c= cmodel10.nnit[clim10], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(dmodel6.M[0], dmodel6.vrot[0], c= dmodel6.nnit[dlim6], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel7.M[0], dmodel7.vrot[0], c= dmodel7.nnit[dlim7], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel8.M[0], dmodel8.vrot[0], c= dmodel8.nnit[dlim8], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel9.M[0], dmodel9.vrot[0], c= dmodel9.nnit[dlim9], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel10.M[0], dmodel10.vrot[0], c= dmodel10.nnit[dlim10], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    cbar2 = fig.colorbar(ims2, ax = ax2)
    cbar2.set_label('Nitrogen Mass')

    # ====== 3 ======
    # plot colors
    ims3 = ax3.scatter(amodel11.M[0], amodel11.vrot[0], c= amodel11.nnit[alim11], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel12.M[0], amodel12.vrot[0], c= amodel12.nnit[alim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel13.M[0], amodel13.vrot[0], c= amodel13.nnit[alim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel14.M[0], amodel14.vrot[0], c= amodel14.nnit[alim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel15.M[0], amodel15.vrot[0], c= amodel15.nnit[alim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    #ax3.scatter(bmodel11.M[0], bmodel11.vrot[0], c= bmodel11.nnit[blim11], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel12.M[0], bmodel12.vrot[0], c= bmodel12.nnit[blim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel13.M[0], bmodel13.vrot[0], c= bmodel13.nnit[blim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel14.M[0], bmodel14.vrot[0], c= bmodel14.nnit[blim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel15.M[0], bmodel15.vrot[0], c= bmodel15.nnit[blim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(cmodel11.M[0], cmodel11.vrot[0], c= cmodel11.nnit[clim11], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel12.M[0], cmodel12.vrot[0], c= cmodel12.nnit[clim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel13.M[0], cmodel13.vrot[0], c= cmodel13.nnit[clim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel14.M[0], cmodel14.vrot[0], c= cmodel14.nnit[clim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel15.M[0], cmodel15.vrot[0], c= cmodel15.nnit[clim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(dmodel11.M[0], dmodel11.vrot[0], c= dmodel11.nnit[dlim11], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel12.M[0], dmodel12.vrot[0], c= dmodel12.nnit[dlim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel13.M[0], dmodel13.vrot[0], c= dmodel13.nnit[dlim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel14.M[0], dmodel14.vrot[0], c= dmodel14.nnit[dlim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel15.M[0], dmodel15.vrot[0], c= dmodel15.nnit[dlim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar3 = fig.colorbar(ims3, ax = ax3)
    # cbar3.set_label('Final Mass / Initial Mass')

    # ====== 4 ======
    # plot colors
    ims4 = ax4.scatter(amodel16.M[0], amodel16.vrot[0], c= amodel16.nnit[alim16], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel17.M[0], amodel17.vrot[0], c= amodel17.nnit[alim17], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel18.M[0], amodel18.vrot[0], c= amodel18.nnit[alim18], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel19.M[0], amodel19.vrot[0], c= amodel19.nnit[alim19], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel20.M[0], amodel20.vrot[0], c= amodel20.nnit[alim20], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(bmodel16.M[0], bmodel16.vrot[0], c= bmodel16.nnit[blim16], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel17.M[0], bmodel17.vrot[0], c= bmodel17.nnit[blim17], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel18.M[0], bmodel18.vrot[0], c= bmodel18.nnit[blim18], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel19.M[0], bmodel19.vrot[0], c= bmodel19.nnit[blim19], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel20.M[0], bmodel20.vrot[0], c= bmodel20.nnit[blim20], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(cmodel16.M[0], cmodel16.vrot[0], c= cmodel16.nnit[clim16], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel17.M[0], cmodel17.vrot[0], c= cmodel17.nnit[clim17], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel18.M[0], cmodel18.vrot[0], c= cmodel18.nnit[clim18], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel19.M[0], cmodel19.vrot[0], c= cmodel19.nnit[clim19], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel20.M[0], cmodel20.vrot[0], c= cmodel20.nnit[clim20], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(dmodel16.M[0], dmodel16.vrot[0], c= dmodel16.nnit[dlim16], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel17.M[0], dmodel17.vrot[0], c= dmodel17.nnit[dlim17], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel18.M[0], dmodel18.vrot[0], c= dmodel18.nnit[dlim18], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel19.M[0], dmodel19.vrot[0], c= dmodel19.nnit[dlim19], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel20.M[0], dmodel20.vrot[0], c= dmodel20.nnit[dlim20], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
  

    cbar4 = fig.colorbar(ims4, ax = ax4)
    cbar4.set_label('Nitrogen Mass')

    fig.tight_layout()
    plt.savefig(f'Plots/Overview/{folder}/Nmass{limit}.png')


Nmass(avink01_20, avink01_30, avink01_40, avink01_50, avink01_60, bvink01_20, bvink01_30, bvink01_40, bvink01_50, bvink01_60, cvink01_20, cvink01_30, cvink01_40, cvink01_50, cvink01_60, dvink01_20, dvink01_30, dvink01_40, dvink01_50, dvink01_60,
avink18_20, avink18_30, avink18_40, avink18_50, avink18_60, bvink18_20, bvink18_30, bvink18_40, bvink18_50, bvink18_60, cvink18_20, cvink18_30, cvink18_40, cvink18_50, cvink18_60, dvink18_20, dvink18_30, dvink18_40, dvink18_50, dvink18_60,
aleuven_20, aleuven_30, aleuven_40, aleuven_50, aleuven_60, bleuven_20, bleuven_30, bleuven_40, bleuven_50, bleuven_60, cleuven_20, cleuven_30, cleuven_40, cleuven_50, cleuven_60, dleuven_20, dleuven_30, dleuven_40, dleuven_50, dleuven_60,
akrticka_20, akrticka_30, akrticka_40, akrticka_50, akrticka_60, bkrticka_20, bkrticka_30, bkrticka_40, bkrticka_50, bkrticka_60, ckrticka_20, ckrticka_30, ckrticka_40, ckrticka_50, ckrticka_60, dkrticka_20, dkrticka_30, dkrticka_40, dkrticka_50, dkrticka_60,
ms)

# ================================================================

def Hemass(amodel1, amodel2, amodel3, amodel4, amodel5, bmodel1, bmodel2, bmodel3, bmodel4, bmodel5, cmodel1, cmodel2, cmodel3, cmodel4, cmodel5, dmodel1, dmodel2, dmodel3, dmodel4, dmodel5,
amodel6, amodel7, amodel8, amodel9, amodel10, bmodel6, bmodel7, bmodel8, bmodel9, bmodel10, cmodel6, cmodel7, cmodel8, cmodel9, cmodel10, dmodel6, dmodel7, dmodel8, dmodel9, dmodel10,
amodel11, amodel12, amodel13, amodel14, amodel15, bmodel11, bmodel12, bmodel13, bmodel14, bmodel15, cmodel11, cmodel12, cmodel13, cmodel14, cmodel15, dmodel11, dmodel12, dmodel13, dmodel14, dmodel15,
amodel16, amodel17, amodel18, amodel19, amodel20, bmodel16, bmodel17, bmodel18, bmodel19, bmodel20, cmodel16, cmodel17, cmodel18, cmodel19, cmodel20, dmodel16, dmodel17, dmodel18, dmodel19, dmodel20,
ms):

    # end of list
    if ms == True:
        # main sequence limit
        alim1 = amodel1.mainsequence()
        alim2 = amodel2.mainsequence()
        alim3 = amodel3.mainsequence()
        alim4 = amodel4.mainsequence()
        alim5 = amodel5.mainsequence()
        alim6 = amodel6.mainsequence()
        alim7 = amodel7.mainsequence()
        alim8 = amodel8.mainsequence()
        alim9 = amodel9.mainsequence()
        alim10 = amodel10.mainsequence()
        alim11 = amodel11.mainsequence()
        alim12 = amodel12.mainsequence()
        alim13 = amodel13.mainsequence()
        alim14 = amodel14.mainsequence()
        alim15 = amodel15.mainsequence()
        alim16 = amodel16.mainsequence()
        alim17 = amodel17.mainsequence()
        alim18 = amodel18.mainsequence()
        alim19 = amodel19.mainsequence()
        alim20 = amodel20.mainsequence()

        blim1 = bmodel1.mainsequence()
        blim2 = bmodel2.mainsequence()
        blim3 = bmodel3.mainsequence()
        blim4 = bmodel4.mainsequence()
        blim5 = bmodel5.mainsequence()
        blim6 = bmodel6.mainsequence()
        blim7 = bmodel7.mainsequence()
        blim8 = bmodel8.mainsequence()
        blim9 = bmodel9.mainsequence()
        blim10 = bmodel10.mainsequence()
        blim11 = bmodel11.mainsequence()
        blim12 = bmodel12.mainsequence()
        blim13 = bmodel13.mainsequence()
        blim14 = bmodel14.mainsequence()
        blim15 = bmodel15.mainsequence()
        blim16 = bmodel16.mainsequence()
        blim17 = bmodel17.mainsequence()
        blim18 = bmodel18.mainsequence()
        blim19 = bmodel19.mainsequence()
        blim20 = bmodel20.mainsequence()

        clim1 = cmodel1.mainsequence()
        clim2 = cmodel2.mainsequence()
        clim3 = cmodel3.mainsequence()
        clim4 = cmodel4.mainsequence()
        clim5 = cmodel5.mainsequence()
        clim6 = cmodel6.mainsequence()
        clim7 = cmodel7.mainsequence()
        clim8 = cmodel8.mainsequence()
        clim9 = cmodel9.mainsequence()
        clim10 = cmodel10.mainsequence()
        clim11 = cmodel11.mainsequence()
        clim12 = cmodel12.mainsequence()
        clim13 = cmodel13.mainsequence()
        clim14 = cmodel14.mainsequence()
        clim15 = cmodel15.mainsequence()
        clim16 = cmodel16.mainsequence()
        clim17 = cmodel17.mainsequence()
        clim18 = cmodel18.mainsequence()
        clim19 = cmodel19.mainsequence()
        clim20 = cmodel20.mainsequence()

        dlim1 = dmodel1.mainsequence()
        dlim2 = dmodel2.mainsequence()
        dlim3 = dmodel3.mainsequence()
        dlim4 = dmodel4.mainsequence()
        dlim5 = dmodel5.mainsequence()
        dlim6 = dmodel6.mainsequence()
        dlim7 = dmodel7.mainsequence()
        dlim8 = dmodel8.mainsequence()
        dlim9 = dmodel9.mainsequence()
        dlim10 = dmodel10.mainsequence()
        dlim11 = dmodel11.mainsequence()
        dlim12 = dmodel12.mainsequence()
        dlim13 = dmodel13.mainsequence()
        dlim14 = dmodel14.mainsequence()
        dlim15 = dmodel15.mainsequence()
        dlim16 = dmodel16.mainsequence()
        dlim17 = dmodel17.mainsequence()
        dlim18 = dmodel18.mainsequence()
        dlim19 = dmodel19.mainsequence()
        dlim20 = dmodel20.mainsequence()
        
        # limit colorbar
        min1 = 0
        max1 = 0.05

        limit = '_ms'
        folder = 'MainSequence'
    else:
        # full simulation
        alim1 = -1
        alim2 = -1
        alim3 = -1
        alim4 = -1
        alim5 = -1
        alim6 = -1
        alim7 = -1
        alim8 = -1
        alim9 = -1
        alim10 = -1
        alim11 = -1
        alim12 = -1
        alim13 = -1
        alim14 = -1
        alim15 = -1
        alim16 = -1
        alim17 = -1
        alim18 = -1
        alim19 = -1
        alim20 = -1

        blim1 = -1
        blim2 = -1
        blim3 = -1
        blim4 = -1
        blim5 = -1
        blim6 = -1
        blim7 = -1
        blim8 = -1
        blim9 = -1
        blim10 = -1
        blim11 = -1
        blim12 = -1
        blim13 = -1
        blim14 = -1
        blim15 = -1
        blim16 = -1
        blim17 = -1
        blim18 = -1
        blim19 = -1
        blim20 = -1

        clim1 = -1
        clim2 = -1
        clim3 = -1
        clim4 = -1
        clim5 = -1
        clim6 = -1
        clim7 = -1
        clim8 = -1
        clim9 = -1
        clim10 = -1
        clim11 = -1
        clim12 = -1
        clim13 = -1
        clim14 = -1
        clim15 = -1
        clim16 = -1
        clim17 = -1
        clim18 = -1
        clim19 = -1
        clim20 = -1

        dlim1 = -1
        dlim2 = -1
        dlim3 = -1
        dlim4 = -1
        dlim5 = -1
        dlim6 = -1
        dlim7 = -1
        dlim8 = -1
        dlim9 = -1
        dlim10 = -1
        dlim11 = -1
        dlim12 = -1
        dlim13 = -1
        dlim14 = -1
        dlim15 = -1
        dlim16 = -1
        dlim17 = -1
        dlim18 = -1
        dlim19 = -1
        dlim20 = -1

        # limit colorbar
        min1 = 0
        max1 = 0.05

        limit = ''
        folder = 'FullSimulation'


    min1 = 0
    max1 = 0.05

    # ------ Set Plot Style ------
    default_style()
    fig, ax1, ax2, ax3, ax4, colormap = He_mass(ms)
    
   # ====== 1 ======
    # plot colors
    ims1 = ax1.scatter(amodel1.M[0], amodel1.vrot[0], c= amodel1.nhe[alim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel2.M[0], amodel2.vrot[0], c= amodel2.nhe[alim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel3.M[0], amodel3.vrot[0], c= amodel3.nhe[alim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel4.M[0], amodel4.vrot[0], c= amodel4.nhe[alim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel5.M[0], amodel5.vrot[0], c= amodel5.nhe[alim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(bmodel1.M[0], bmodel1.vrot[0], c= bmodel1.nhe[blim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel2.M[0], bmodel2.vrot[0], c= bmodel2.nhe[blim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel3.M[0], bmodel3.vrot[0], c= bmodel3.nhe[blim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel4.M[0], bmodel4.vrot[0], c= bmodel4.nhe[blim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel5.M[0], bmodel5.vrot[0], c= bmodel5.nhe[blim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(cmodel1.M[0], cmodel1.vrot[0], c= cmodel1.nhe[clim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel2.M[0], cmodel2.vrot[0], c= cmodel2.nhe[clim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel3.M[0], cmodel3.vrot[0], c= cmodel3.nhe[clim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel4.M[0], cmodel4.vrot[0], c= cmodel4.nhe[clim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel5.M[0], cmodel5.vrot[0], c= cmodel5.nhe[clim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(dmodel1.M[0], dmodel1.vrot[0], c= dmodel1.nhe[dlim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel2.M[0], dmodel2.vrot[0], c= dmodel2.nhe[dlim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel3.M[0], dmodel3.vrot[0], c= dmodel3.nhe[dlim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel4.M[0], dmodel4.vrot[0], c= dmodel4.nhe[dlim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel5.M[0], dmodel5.vrot[0], c= dmodel5.nhe[dlim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar = fig.colorbar(ims1, ax = ax1)
    # cbar.set_label('Final Mass / Initial Mass')

    # ====== 2 ======
    # plot colors
    ims2 = ax2.scatter(amodel6.M[0], amodel6.vrot[0], c= amodel6.nhe[alim6], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel7.M[0], amodel7.vrot[0], c= amodel7.nhe[alim7], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel8.M[0], amodel8.vrot[0], c= amodel8.nhe[alim8], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel9.M[0], amodel9.vrot[0], c= amodel9.nhe[alim9], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel10.M[0], amodel10.vrot[0], c= amodel10.nhe[alim10], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(bmodel6.M[0], bmodel6.vrot[0], c= bmodel6.nhe[blim6], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel7.M[0], bmodel7.vrot[0], c= bmodel7.nhe[blim7], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel8.M[0], bmodel8.vrot[0], c= bmodel8.nhe[blim8], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel9.M[0], bmodel9.vrot[0], c= bmodel9.nhe[blim9], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel10.M[0], bmodel10.vrot[0], c= bmodel10.nhe[blim10], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(cmodel6.M[0], cmodel6.vrot[0], c= cmodel6.nhe[clim6], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel7.M[0], cmodel7.vrot[0], c= cmodel7.nhe[clim7], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel8.M[0], cmodel8.vrot[0], c= cmodel8.nhe[clim8], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel9.M[0], cmodel9.vrot[0], c= cmodel9.nhe[clim9], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel10.M[0], cmodel10.vrot[0], c= cmodel10.nhe[clim10], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(dmodel6.M[0], dmodel6.vrot[0], c= dmodel6.nhe[dlim6], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel7.M[0], dmodel7.vrot[0], c= dmodel7.nhe[dlim7], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel8.M[0], dmodel8.vrot[0], c= dmodel8.nhe[dlim8], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel9.M[0], dmodel9.vrot[0], c= dmodel9.nhe[dlim9], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel10.M[0], dmodel10.vrot[0], c= dmodel10.nhe[dlim10], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    cbar2 = fig.colorbar(ims2, ax = ax2)
    cbar2.set_label('Helium Mass')

    # ====== 3 ======
    # plot colors
    ims3 = ax3.scatter(amodel11.M[0], amodel11.vrot[0], c= amodel11.nhe[alim11], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel12.M[0], amodel12.vrot[0], c= amodel12.nhe[alim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel13.M[0], amodel13.vrot[0], c= amodel13.nhe[alim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel14.M[0], amodel14.vrot[0], c= amodel14.nhe[alim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel15.M[0], amodel15.vrot[0], c= amodel15.nhe[alim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    #ax3.scatter(bmodel11.M[0], bmodel11.vrot[0], c= bmodel11.nhe[130], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel12.M[0], bmodel12.vrot[0], c= bmodel12.nhe[blim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel13.M[0], bmodel13.vrot[0], c= bmodel13.nhe[blim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel14.M[0], bmodel14.vrot[0], c= bmodel14.nhe[blim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel15.M[0], bmodel15.vrot[0], c= bmodel15.nhe[blim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(cmodel11.M[0], cmodel11.vrot[0], c= cmodel11.nhe[clim11], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel12.M[0], cmodel12.vrot[0], c= cmodel12.nhe[clim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel13.M[0], cmodel13.vrot[0], c= cmodel13.nhe[clim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel14.M[0], cmodel14.vrot[0], c= cmodel14.nhe[clim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel15.M[0], cmodel15.vrot[0], c= cmodel15.nhe[clim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(dmodel11.M[0], dmodel11.vrot[0], c= dmodel11.nhe[dlim11], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel12.M[0], dmodel12.vrot[0], c= dmodel12.nhe[dlim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel13.M[0], dmodel13.vrot[0], c= dmodel13.nhe[dlim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel14.M[0], dmodel14.vrot[0], c= dmodel14.nhe[dlim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel15.M[0], dmodel15.vrot[0], c= dmodel15.nhe[dlim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar3 = fig.colorbar(ims3, ax = ax3)
    # cbar3.set_label('Final Mass / Initial Mass')

    # ====== 4 ======
    # plot colors
    ims4 = ax4.scatter(amodel16.M[0], amodel16.vrot[0], c= amodel16.nhe[alim16], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel17.M[0], amodel17.vrot[0], c= amodel17.nhe[alim17], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel18.M[0], amodel18.vrot[0], c= amodel18.nhe[alim18], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel19.M[0], amodel19.vrot[0], c= amodel19.nhe[alim19], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel20.M[0], amodel20.vrot[0], c= amodel20.nhe[alim20], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(bmodel16.M[0], bmodel16.vrot[0], c= bmodel16.nhe[blim16], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel17.M[0], bmodel17.vrot[0], c= bmodel17.nhe[blim17], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel18.M[0], bmodel18.vrot[0], c= bmodel18.nhe[blim18], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel19.M[0], bmodel19.vrot[0], c= bmodel19.nhe[blim19], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel20.M[0], bmodel20.vrot[0], c= bmodel20.nhe[blim20], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(cmodel16.M[0], cmodel16.vrot[0], c= cmodel16.nhe[clim16], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel17.M[0], cmodel17.vrot[0], c= cmodel17.nhe[clim17], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel18.M[0], cmodel18.vrot[0], c= cmodel18.nhe[clim18], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel19.M[0], cmodel19.vrot[0], c= cmodel19.nhe[clim19], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel20.M[0], cmodel20.vrot[0], c= cmodel20.nhe[clim20], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(dmodel16.M[0], dmodel16.vrot[0], c= dmodel16.nhe[dlim16], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel17.M[0], dmodel17.vrot[0], c= dmodel17.nhe[dlim17], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel18.M[0], dmodel18.vrot[0], c= dmodel18.nhe[dlim18], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel19.M[0], dmodel19.vrot[0], c= dmodel19.nhe[dlim19], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel20.M[0], dmodel20.vrot[0], c= dmodel20.nhe[dlim20], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
  

    cbar4 = fig.colorbar(ims4, ax = ax4)
    cbar4.set_label('Helium Mass')

    fig.tight_layout()
    plt.savefig(f'Plots/Overview/{folder}/Hemass{limit}.png')


Hemass(avink01_20, avink01_30, avink01_40, avink01_50, avink01_60, bvink01_20, bvink01_30, bvink01_40, bvink01_50, bvink01_60, cvink01_20, cvink01_30, cvink01_40, cvink01_50, cvink01_60, dvink01_20, dvink01_30, dvink01_40, dvink01_50, dvink01_60,
avink18_20, avink18_30, avink18_40, avink18_50, avink18_60, bvink18_20, bvink18_30, bvink18_40, bvink18_50, bvink18_60, cvink18_20, cvink18_30, cvink18_40, cvink18_50, cvink18_60, dvink18_20, dvink18_30, dvink18_40, dvink18_50, dvink18_60,
aleuven_20, aleuven_30, aleuven_40, aleuven_50, aleuven_60, bleuven_20, bleuven_30, bleuven_40, bleuven_50, bleuven_60, cleuven_20, cleuven_30, cleuven_40, cleuven_50, cleuven_60, dleuven_20, dleuven_30, dleuven_40, dleuven_50, dleuven_60,
akrticka_20, akrticka_30, akrticka_40, akrticka_50, akrticka_60, bkrticka_20, bkrticka_30, bkrticka_40, bkrticka_50, bkrticka_60, ckrticka_20, ckrticka_30, ckrticka_40, ckrticka_50, ckrticka_60, dkrticka_20, dkrticka_30, dkrticka_40, dkrticka_50, dkrticka_60,
ms)