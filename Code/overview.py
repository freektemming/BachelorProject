# Script that makes plot

from data_allfiles import *
from plots import *
from plotstyles import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import matplotlib.lines as mlines

ms = True

def initial_values(amodel1, amodel2, amodel3, amodel4, amodel5, bmodel1, bmodel2, bmodel3, bmodel4, bmodel5, cmodel1, cmodel2, cmodel3, cmodel4, cmodel5, dmodel1, dmodel2, dmodel3, dmodel4, dmodel5, emodel1, emodel2, emodel3, emodel4, emodel5, fmodel1, fmodel2, fmodel3, fmodel4, fmodel5,
amodel6, amodel7, amodel8, amodel9, amodel10, bmodel6, bmodel7, bmodel8, bmodel9, bmodel10, cmodel6, cmodel7, cmodel8, cmodel9, cmodel10, dmodel6, dmodel7, dmodel8, dmodel9, dmodel10, emodel6, emodel7, emodel8, emodel9, emodel10, fmodel6, fmodel7, fmodel8, fmodel9, fmodel10,
amodel11, amodel12, amodel13, amodel14, amodel15, bmodel11, bmodel12, bmodel13, bmodel14, bmodel15, cmodel11, cmodel12, cmodel13, cmodel14, cmodel15, dmodel11, dmodel12, dmodel13, dmodel14, dmodel15, emodel11, emodel12, emodel13, emodel14, emodel15, fmodel11, fmodel12, fmodel13, fmodel14, fmodel15,
amodel16, amodel17, amodel18, amodel19, amodel20, bmodel16, bmodel17, bmodel18, bmodel19, bmodel20, cmodel16, cmodel17, cmodel18, cmodel19, cmodel20, dmodel16, dmodel17, dmodel18, dmodel19, dmodel20, emodel16, emodel17, emodel18, emodel19, emodel20, fmodel16, fmodel17, fmodel18, fmodel19, fmodel20,
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

        elim1 = emodel1.mainsequence()
        elim2 = emodel2.mainsequence()
        elim3 = emodel3.mainsequence()
        elim4 = emodel4.mainsequence()
        elim5 = emodel5.mainsequence()
        elim6 = emodel6.mainsequence()
        elim7 = emodel7.mainsequence()
        elim8 = emodel8.mainsequence()
        elim9 = emodel9.mainsequence()
        elim10 = emodel10.mainsequence()
        elim11 = emodel11.mainsequence()
        elim12 = emodel12.mainsequence()
        elim13 = emodel13.mainsequence()
        elim14 = emodel14.mainsequence()
        elim15 = emodel15.mainsequence()
        elim16 = emodel16.mainsequence()
        elim17 = emodel17.mainsequence()
        elim18 = emodel18.mainsequence()
        elim19 = emodel19.mainsequence()
        elim20 = emodel20.mainsequence()

        flim1 = fmodel1.mainsequence()
        flim2 = fmodel2.mainsequence()
        flim3 = fmodel3.mainsequence()
        flim4 = fmodel4.mainsequence()
        flim5 = fmodel5.mainsequence()
        flim6 = fmodel6.mainsequence()
        flim7 = fmodel7.mainsequence()
        flim8 = fmodel8.mainsequence()
        flim9 = fmodel9.mainsequence()
        flim10 = fmodel10.mainsequence()
        flim11 = fmodel11.mainsequence()
        flim12 = fmodel12.mainsequence()
        flim13 = fmodel13.mainsequence()
        flim14 = fmodel14.mainsequence()
        flim15 = fmodel15.mainsequence()
        flim16 = fmodel16.mainsequence()
        flim17 = fmodel17.mainsequence()
        flim18 = fmodel18.mainsequence()
        flim19 = fmodel19.mainsequence()
        flim20 = fmodel20.mainsequence()
    

        # limit colorbar
        min1 = 0.8
        max1 = 1
        limit = '_ms'
        folder = 'MainSequence'
    else:
        # full simulation
        alim1 = amodel1.end()
        alim2 = amodel2.end()
        alim3 = amodel3.end()
        alim4 = amodel4.end()
        alim5 = amodel5.end()
        alim6 = amodel6.end()
        alim7 = amodel7.end()
        alim8 = amodel8.end()
        alim9 = amodel9.end()
        alim10 = amodel10.end()
        alim11 = amodel11.end()
        alim12 = amodel12.end()
        alim13 = amodel13.end()
        alim14 = amodel14.end()
        alim15 = amodel15.end()
        alim16 = amodel16.end()
        alim17 = amodel17.end()
        alim18 = amodel18.end()
        alim19 = amodel19.end()
        alim20 = amodel20.end()

        blim1 = bmodel1.end()
        blim2 = bmodel2.end()
        blim3 = bmodel3.end()
        blim4 = bmodel4.end()
        blim5 = bmodel5.end()
        blim6 = bmodel6.end()
        blim7 = bmodel7.end()
        blim8 = bmodel8.end()
        blim9 = bmodel9.end()
        blim10 = bmodel10.end()
        blim11 = bmodel11.end()
        blim12 = bmodel12.end()
        blim13 = bmodel13.end()
        blim14 = bmodel14.end()
        blim15 = bmodel15.end()
        blim16 = bmodel16.end()
        blim17 = bmodel17.end()
        blim18 = bmodel18.end()
        blim19 = bmodel19.end()
        blim20 = bmodel20.end()

        clim1 = cmodel1.end()
        clim2 = cmodel2.end()
        clim3 = cmodel3.end()
        clim4 = cmodel4.end()
        clim5 = cmodel5.end()
        clim6 = cmodel6.end()
        clim7 = cmodel7.end()
        clim8 = cmodel8.end()
        clim9 = cmodel9.end()
        clim10 = cmodel10.end()
        clim11 = cmodel11.end()
        clim12 = cmodel12.end()
        clim13 = cmodel13.end()
        clim14 = cmodel14.end()
        clim15 = cmodel15.end()
        clim16 = cmodel16.end()
        clim17 = cmodel17.end()
        clim18 = cmodel18.end()
        clim19 = cmodel19.end()
        clim20 = cmodel20.end()

        dlim1 = dmodel1.end()
        dlim2 = dmodel2.end()
        dlim3 = dmodel3.end()
        dlim4 = dmodel4.end()
        dlim5 = dmodel5.end()
        dlim6 = dmodel6.end()
        dlim7 = dmodel7.end()
        dlim8 = dmodel8.end()
        dlim9 = dmodel9.end()
        dlim10 = dmodel10.end()
        dlim11 = dmodel11.end()
        dlim12 = dmodel12.end()
        dlim13 = dmodel13.end()
        dlim14 = dmodel14.end()
        dlim15 = dmodel15.end()
        dlim16 = dmodel16.end()
        dlim17 = dmodel17.end()
        dlim18 = dmodel18.end()
        dlim19 = dmodel19.end()
        dlim20 = dmodel20.end()

        elim1 = emodel1.end()
        elim2 = emodel2.end()
        elim3 = emodel3.end()
        elim4 = emodel4.end()
        elim5 = emodel5.end()
        elim6 = emodel6.end()
        elim7 = emodel7.end()
        elim8 = emodel8.end()
        elim9 = emodel9.end()
        elim10 = emodel10.end()
        elim11 = emodel11.end()
        elim12 = emodel12.end()
        elim13 = emodel13.end()
        elim14 = emodel14.end()
        elim15 = emodel15.end()
        elim16 = emodel16.end()
        elim17 = emodel17.end()
        elim18 = emodel18.end()
        elim19 = emodel19.end()
        elim20 = emodel20.end()

        flim1 = fmodel1.end()
        flim2 = fmodel2.end()
        flim3 = fmodel3.end()
        flim4 = fmodel4.end()
        flim5 = fmodel5.end()
        flim6 = fmodel6.end()
        flim7 = fmodel7.end()
        flim8 = fmodel8.end()
        flim9 = fmodel9.end()
        flim10 = fmodel10.end()
        flim11 = fmodel11.end()
        flim12 = fmodel12.end()
        flim13 = fmodel13.end()
        flim14 = fmodel14.end()
        flim15 = fmodel15.end()
        flim16 = fmodel16.end()
        flim17 = fmodel17.end()
        flim18 = fmodel18.end()
        flim19 = fmodel19.end()
        flim20 = fmodel20.end()

        # colorbar
        min1 = 0.8
        max1 = 1

        limit = ''
        folder = 'FullSimulation'

    # ------ Set Plot Style ------
    default_style()
    fig, ax1, ax2, ax3, ax4, colormap = m_init(ms)

    # ------ Set Legend ------
    circle = mlines.Line2D([], [], color = 'grey',  marker='o', linestyle='None',
                          markersize=5, label='SMC')
    square = mlines.Line2D([], [], color = 'grey', marker='s', linestyle='None',
                          markersize=5, label='GAL')
    triangle = mlines.Line2D([], [], color = 'grey', marker='^', linestyle='None',
                          markersize=5, label='LMC')
    
    # ====== 1 ======
    # plot colors
    ims1 = ax1.scatter(amodel1.M[0], amodel1.vrot[0], c= amodel1.histM[alim1], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel2.M[0], amodel2.vrot[0], c= amodel2.histM[alim2], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel3.M[0], amodel3.vrot[0], c= amodel3.histM[alim3], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel4.M[0], amodel4.vrot[0], c= amodel4.histM[alim4], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel5.M[0], amodel5.vrot[0], c= amodel5.histM[alim5], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(bmodel1.M[0], bmodel1.vrot[0], c= bmodel1.histM[blim1], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel2.M[0], bmodel2.vrot[0], c= bmodel2.histM[blim2], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel3.M[0], bmodel3.vrot[0], c= bmodel3.histM[blim3], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel4.M[0], bmodel4.vrot[0], c= bmodel4.histM[blim4], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel5.M[0], bmodel5.vrot[0], c= bmodel5.histM[blim5], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(cmodel1.M[0], cmodel1.vrot[0], c= cmodel1.histM[clim1], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel2.M[0], cmodel2.vrot[0], c= cmodel2.histM[clim2], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel3.M[0], cmodel3.vrot[0], c= cmodel3.histM[clim3], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel4.M[0], cmodel4.vrot[0], c= cmodel4.histM[clim4], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel5.M[0], cmodel5.vrot[0], c= cmodel5.histM[clim5], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(dmodel1.M[0], dmodel1.vrot[0], c= dmodel1.histM[dlim1], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel2.M[0], dmodel2.vrot[0], c= dmodel2.histM[dlim2], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel3.M[0], dmodel3.vrot[0], c= dmodel3.histM[dlim3], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel4.M[0], dmodel4.vrot[0], c= dmodel4.histM[dlim4], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel5.M[0], dmodel5.vrot[0], c= dmodel5.histM[dlim5], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(emodel1.M[0], emodel1.vrot[0], c= emodel1.histM[elim1], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(emodel2.M[0], emodel2.vrot[0], c= emodel2.histM[elim2], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(emodel3.M[0], emodel3.vrot[0], c= emodel3.histM[elim3], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(emodel4.M[0], emodel4.vrot[0], c= emodel4.histM[elim4], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(emodel5.M[0], emodel5.vrot[0], c= emodel5.histM[elim5], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(fmodel1.M[0], fmodel1.vrot[0], c= fmodel1.histM[flim1], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(fmodel2.M[0], fmodel2.vrot[0], c= fmodel2.histM[flim2], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(fmodel3.M[0], fmodel3.vrot[0], c= fmodel3.histM[flim3], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(fmodel4.M[0], fmodel4.vrot[0], c= fmodel4.histM[flim4], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(fmodel5.M[0], fmodel5.vrot[0], c= fmodel5.histM[flim5], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax1.legend(handles=[circle, triangle, square], loc='center left')
    
    # cbar = fig.colorbar(ims1, ax = ax1)
    # cbar.set_label('Final Mass / Initial Mass')

    # ====== 2 ======
    # plot colors
    ims2 = ax2.scatter(amodel6.M[0], amodel6.vrot[0], c= amodel6.histM[alim6], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel7.M[0], amodel7.vrot[0], c= amodel7.histM[alim7], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel8.M[0], amodel8.vrot[0], c= amodel8.histM[alim8], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel9.M[0], amodel9.vrot[0], c= amodel9.histM[alim9], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel10.M[0], amodel10.vrot[0], c= amodel10.histM[alim10], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(bmodel6.M[0], bmodel6.vrot[0], c= bmodel6.histM[blim6], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel7.M[0], bmodel7.vrot[0], c= bmodel7.histM[blim7], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel8.M[0], bmodel8.vrot[0], c= bmodel8.histM[blim8], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel9.M[0], bmodel9.vrot[0], c= bmodel9.histM[blim9], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel10.M[0], bmodel10.vrot[0], c= bmodel10.histM[blim10], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(cmodel6.M[0], cmodel6.vrot[0], c= cmodel6.histM[clim6], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel7.M[0], cmodel7.vrot[0], c= cmodel7.histM[clim7], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel8.M[0], cmodel8.vrot[0], c= cmodel8.histM[clim8], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel9.M[0], cmodel9.vrot[0], c= cmodel9.histM[clim9], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel10.M[0], cmodel10.vrot[0], c= cmodel10.histM[clim10], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(dmodel6.M[0], dmodel6.vrot[0], c= dmodel6.histM[dlim6], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel7.M[0], dmodel7.vrot[0], c= dmodel7.histM[dlim7], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel8.M[0], dmodel8.vrot[0], c= dmodel8.histM[dlim8], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel9.M[0], dmodel9.vrot[0], c= dmodel9.histM[dlim9], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel10.M[0], dmodel10.vrot[0], c= dmodel10.histM[dlim10], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(emodel6.M[0], emodel6.vrot[0], c= emodel6.histM[elim6], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(emodel7.M[0], emodel7.vrot[0], c= emodel7.histM[elim7], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(emodel8.M[0], emodel8.vrot[0], c= emodel8.histM[elim8], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(emodel9.M[0], emodel9.vrot[0], c= emodel9.histM[elim9], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(emodel10.M[0], emodel10.vrot[0], c= emodel10.histM[elim10], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(fmodel6.M[0], fmodel6.vrot[0], c= fmodel6.histM[flim6], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(fmodel7.M[0], fmodel7.vrot[0], c= fmodel7.histM[flim7], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(fmodel8.M[0], fmodel8.vrot[0], c= fmodel8.histM[flim8], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(fmodel9.M[0], fmodel9.vrot[0], c= fmodel9.histM[flim9], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(fmodel10.M[0], fmodel10.vrot[0], c= fmodel10.histM[flim10], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    
    cbar2 = fig.colorbar(ims2, ax = ax2)
    cbar2.set_label('Final Mass / Initial Mass')
    ax2.legend(handles=[circle, triangle, square], loc='center left')

    # ====== 3 ======
    # plot colors
    ims3 = ax3.scatter(amodel11.M[0], amodel11.vrot[0], c= amodel11.histM[alim11], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel12.M[0], amodel12.vrot[0], c= amodel12.histM[alim12], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel13.M[0], amodel13.vrot[0], c= amodel13.histM[alim13], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel14.M[0], amodel14.vrot[0], c= amodel14.histM[alim14], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel15.M[0], amodel15.vrot[0], c= amodel15.histM[alim15], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    #ax3.scatter(bmodel11.M[0], bmodel11.vrot[0], c= bmodel11.histM[130], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel12.M[0], bmodel12.vrot[0], c= bmodel12.histM[blim12], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel13.M[0], bmodel13.vrot[0], c= bmodel13.histM[blim13], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel14.M[0], bmodel14.vrot[0], c= bmodel14.histM[blim14], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel15.M[0], bmodel15.vrot[0], c= bmodel15.histM[blim15], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(cmodel11.M[0], cmodel11.vrot[0], c= cmodel11.histM[clim11], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel12.M[0], cmodel12.vrot[0], c= cmodel12.histM[clim12], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel13.M[0], cmodel13.vrot[0], c= cmodel13.histM[clim13], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel14.M[0], cmodel14.vrot[0], c= cmodel14.histM[clim14], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel15.M[0], cmodel15.vrot[0], c= cmodel15.histM[clim15], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(dmodel11.M[0], dmodel11.vrot[0], c= dmodel11.histM[dlim11], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel12.M[0], dmodel12.vrot[0], c= dmodel12.histM[dlim12], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel13.M[0], dmodel13.vrot[0], c= dmodel13.histM[dlim13], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel14.M[0], dmodel14.vrot[0], c= dmodel14.histM[dlim14], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel15.M[0], dmodel15.vrot[0], c= dmodel15.histM[dlim15], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(emodel11.M[0], emodel11.vrot[0], c= emodel11.histM[elim11], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(emodel12.M[0], emodel12.vrot[0], c= emodel12.histM[elim12], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(emodel13.M[0], emodel13.vrot[0], c= emodel13.histM[elim13], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(emodel14.M[0], emodel14.vrot[0], c= emodel14.histM[elim14], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(emodel15.M[0], emodel15.vrot[0], c= emodel15.histM[elim15], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(fmodel11.M[0], fmodel11.vrot[0], c= fmodel11.histM[flim11], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(fmodel12.M[0], fmodel12.vrot[0], c= fmodel12.histM[flim12], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(fmodel13.M[0], fmodel13.vrot[0], c= fmodel13.histM[flim13], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(fmodel14.M[0], fmodel14.vrot[0], c= fmodel14.histM[flim14], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(fmodel15.M[0], fmodel15.vrot[0], c= fmodel15.histM[flim15], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    
    ax3.legend(handles=[circle, triangle, square], loc='center left')

    # cbar3 = fig.colorbar(ims3, ax = ax3)
    # cbar3.set_label('Final Mass / Initial Mass')

    # ====== 4 ======
    # plot colors
    ims4 = ax4.scatter(amodel16.M[0], amodel16.vrot[0], c= amodel16.histM[alim16], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel17.M[0], amodel17.vrot[0], c= amodel17.histM[alim17], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel18.M[0], amodel18.vrot[0], c= amodel18.histM[alim18], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel19.M[0], amodel19.vrot[0], c= amodel19.histM[alim19], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel20.M[0], amodel20.vrot[0], c= amodel20.histM[alim20], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(bmodel16.M[0], bmodel16.vrot[0], c= bmodel16.histM[blim16], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel17.M[0], bmodel17.vrot[0], c= bmodel17.histM[blim17], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel18.M[0], bmodel18.vrot[0], c= bmodel18.histM[blim18], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel19.M[0], bmodel19.vrot[0], c= bmodel19.histM[blim19], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel20.M[0], bmodel20.vrot[0], c= bmodel20.histM[blim20], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(cmodel16.M[0], cmodel16.vrot[0], c= cmodel16.histM[clim16], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel17.M[0], cmodel17.vrot[0], c= cmodel17.histM[clim17], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel18.M[0], cmodel18.vrot[0], c= cmodel18.histM[clim18], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel19.M[0], cmodel19.vrot[0], c= cmodel19.histM[clim19], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel20.M[0], cmodel20.vrot[0], c= cmodel20.histM[clim20], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(dmodel16.M[0], dmodel16.vrot[0], c= dmodel16.histM[dlim16], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel17.M[0], dmodel17.vrot[0], c= dmodel17.histM[dlim17], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel18.M[0], dmodel18.vrot[0], c= dmodel18.histM[dlim18], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel19.M[0], dmodel19.vrot[0], c= dmodel19.histM[dlim19], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel20.M[0], dmodel20.vrot[0], c= dmodel20.histM[dlim20], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(emodel16.M[0], emodel16.vrot[0], c= emodel16.histM[elim16], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(emodel17.M[0], emodel17.vrot[0], c= emodel17.histM[elim17], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(emodel18.M[0], emodel18.vrot[0], c= emodel18.histM[elim18], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(emodel19.M[0], emodel19.vrot[0], c= emodel19.histM[elim19], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(emodel20.M[0], emodel20.vrot[0], c= emodel20.histM[elim20], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(fmodel16.M[0], fmodel16.vrot[0], c= fmodel16.histM[flim16], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(fmodel17.M[0], fmodel17.vrot[0], c= fmodel17.histM[flim17], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(fmodel18.M[0], fmodel18.vrot[0], c= fmodel18.histM[flim18], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(fmodel19.M[0], fmodel19.vrot[0], c= fmodel19.histM[flim19], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(fmodel20.M[0], fmodel20.vrot[0], c= fmodel20.histM[flim20], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    cbar4 = fig.colorbar(ims4, ax = ax4)
    cbar4.set_label('Final Mass / Initial Mass')
    ax4.legend(handles=[circle, triangle, square], loc='center left')

    fig.tight_layout()
    plt.savefig(f'Plots/Overview/{folder}/Final_mass{limit}.png')


initial_values(avink01_20, avink01_30, avink01_40, avink01_50, avink01_60, bvink01_20, bvink01_30, bvink01_40, bvink01_50, bvink01_60, cvink01_20, cvink01_30, cvink01_40, cvink01_50, cvink01_60, dvink01_20, dvink01_30, dvink01_40, dvink01_50, dvink01_60, evink01_20, evink01_30, evink01_40, evink01_50, evink01_60, fvink01_20, fvink01_30, fvink01_40, fvink01_50, fvink01_60,
avink18_20, avink18_30, avink18_40, avink18_50, avink18_60, bvink18_20, bvink18_30, bvink18_40, bvink18_50, bvink18_60, cvink18_20, cvink18_30, cvink18_40, cvink18_50, cvink18_60, dvink18_20, dvink18_30, dvink18_40, dvink18_50, dvink18_60, evink18_20, evink18_30, evink18_40, evink18_50, evink18_60, fvink18_20, fvink18_30, fvink18_40, fvink18_50, fvink18_60,
aleuven_20, aleuven_30, aleuven_40, aleuven_50, aleuven_60, bleuven_20, bleuven_30, bleuven_40, bleuven_50, bleuven_60, cleuven_20, cleuven_30, cleuven_40, cleuven_50, cleuven_60, dleuven_20, dleuven_30, dleuven_40, dleuven_50, dleuven_60, eleuven_20, eleuven_30, eleuven_40, eleuven_50, eleuven_60, fleuven_20, fleuven_30, fleuven_40, fleuven_50, fleuven_60,
akrticka_20, akrticka_30, akrticka_40, akrticka_50, akrticka_60, bkrticka_20, bkrticka_30, bkrticka_40, bkrticka_50, bkrticka_60, ckrticka_20, ckrticka_30, ckrticka_40, ckrticka_50, ckrticka_60, dkrticka_20, dkrticka_30, dkrticka_40, dkrticka_50, dkrticka_60, ekrticka_20, ekrticka_30, ekrticka_40, ekrticka_50, ekrticka_60, fkrticka_20, fkrticka_30, fkrticka_40, fkrticka_50, fkrticka_60,
ms)

# ============================================================

def envelopemass(amodel1, amodel2, amodel3, amodel4, amodel5, bmodel1, bmodel2, bmodel3, bmodel4, bmodel5, cmodel1, cmodel2, cmodel3, cmodel4, cmodel5, dmodel1, dmodel2, dmodel3, dmodel4, dmodel5, emodel1, emodel2, emodel3, emodel4, emodel5, fmodel1, fmodel2, fmodel3, fmodel4, fmodel5,
amodel6, amodel7, amodel8, amodel9, amodel10, bmodel6, bmodel7, bmodel8, bmodel9, bmodel10, cmodel6, cmodel7, cmodel8, cmodel9, cmodel10, dmodel6, dmodel7, dmodel8, dmodel9, dmodel10, emodel6, emodel7, emodel8, emodel9, emodel10, fmodel6, fmodel7, fmodel8, fmodel9, fmodel10,
amodel11, amodel12, amodel13, amodel14, amodel15, bmodel11, bmodel12, bmodel13, bmodel14, bmodel15, cmodel11, cmodel12, cmodel13, cmodel14, cmodel15, dmodel11, dmodel12, dmodel13, dmodel14, dmodel15, emodel11, emodel12, emodel13, emodel14, emodel15, fmodel11, fmodel12, fmodel13, fmodel14, fmodel15,
amodel16, amodel17, amodel18, amodel19, amodel20, bmodel16, bmodel17, bmodel18, bmodel19, bmodel20, cmodel16, cmodel17, cmodel18, cmodel19, cmodel20, dmodel16, dmodel17, dmodel18, dmodel19, dmodel20, emodel16, emodel17, emodel18, emodel19, emodel20, fmodel16, fmodel17, fmodel18, fmodel19, fmodel20,
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

        elim1 = emodel1.mainsequence()
        elim2 = emodel2.mainsequence()
        elim3 = emodel3.mainsequence()
        elim4 = emodel4.mainsequence()
        elim5 = emodel5.mainsequence()
        elim6 = emodel6.mainsequence()
        elim7 = emodel7.mainsequence()
        elim8 = emodel8.mainsequence()
        elim9 = emodel9.mainsequence()
        elim10 = emodel10.mainsequence()
        elim11 = emodel11.mainsequence()
        elim12 = emodel12.mainsequence()
        elim13 = emodel13.mainsequence()
        elim14 = emodel14.mainsequence()
        elim15 = emodel15.mainsequence()
        elim16 = emodel16.mainsequence()
        elim17 = emodel17.mainsequence()
        elim18 = emodel18.mainsequence()
        elim19 = emodel19.mainsequence()
        elim20 = emodel20.mainsequence()

        flim1 = fmodel1.mainsequence()
        flim2 = fmodel2.mainsequence()
        flim3 = fmodel3.mainsequence()
        flim4 = fmodel4.mainsequence()
        flim5 = fmodel5.mainsequence()
        flim6 = fmodel6.mainsequence()
        flim7 = fmodel7.mainsequence()
        flim8 = fmodel8.mainsequence()
        flim9 = fmodel9.mainsequence()
        flim10 = fmodel10.mainsequence()
        flim11 = fmodel11.mainsequence()
        flim12 = fmodel12.mainsequence()
        flim13 = fmodel13.mainsequence()
        flim14 = fmodel14.mainsequence()
        flim15 = fmodel15.mainsequence()
        flim16 = fmodel16.mainsequence()
        flim17 = fmodel17.mainsequence()
        flim18 = fmodel18.mainsequence()
        flim19 = fmodel19.mainsequence()
        flim20 = fmodel20.mainsequence()
        
        # limit colorbar
        min1 = 10
        max1 = 35
        limit = '_ms'
        folder = 'MainSequence'
    else:
        # full simulation
        alim1 = amodel1.end()
        alim2 = amodel2.end()
        alim3 = amodel3.end()
        alim4 = amodel4.end()
        alim5 = amodel5.end()
        alim6 = amodel6.end()
        alim7 = amodel7.end()
        alim8 = amodel8.end()
        alim9 = amodel9.end()
        alim10 = amodel10.end()
        alim11 = amodel11.end()
        alim12 = amodel12.end()
        alim13 = amodel13.end()
        alim14 = amodel14.end()
        alim15 = amodel15.end()
        alim16 = amodel16.end()
        alim17 = amodel17.end()
        alim18 = amodel18.end()
        alim19 = amodel19.end()
        alim20 = amodel20.end()

        blim1 = bmodel1.end()
        blim2 = bmodel2.end()
        blim3 = bmodel3.end()
        blim4 = bmodel4.end()
        blim5 = bmodel5.end()
        blim6 = bmodel6.end()
        blim7 = bmodel7.end()
        blim8 = bmodel8.end()
        blim9 = bmodel9.end()
        blim10 = bmodel10.end()
        blim11 = bmodel11.end()
        blim12 = bmodel12.end()
        blim13 = bmodel13.end()
        blim14 = bmodel14.end()
        blim15 = bmodel15.end()
        blim16 = bmodel16.end()
        blim17 = bmodel17.end()
        blim18 = bmodel18.end()
        blim19 = bmodel19.end()
        blim20 = bmodel20.end()

        clim1 = cmodel1.end()
        clim2 = cmodel2.end()
        clim3 = cmodel3.end()
        clim4 = cmodel4.end()
        clim5 = cmodel5.end()
        clim6 = cmodel6.end()
        clim7 = cmodel7.end()
        clim8 = cmodel8.end()
        clim9 = cmodel9.end()
        clim10 = cmodel10.end()
        clim11 = cmodel11.end()
        clim12 = cmodel12.end()
        clim13 = cmodel13.end()
        clim14 = cmodel14.end()
        clim15 = cmodel15.end()
        clim16 = cmodel16.end()
        clim17 = cmodel17.end()
        clim18 = cmodel18.end()
        clim19 = cmodel19.end()
        clim20 = cmodel20.end()

        dlim1 = dmodel1.end()
        dlim2 = dmodel2.end()
        dlim3 = dmodel3.end()
        dlim4 = dmodel4.end()
        dlim5 = dmodel5.end()
        dlim6 = dmodel6.end()
        dlim7 = dmodel7.end()
        dlim8 = dmodel8.end()
        dlim9 = dmodel9.end()
        dlim10 = dmodel10.end()
        dlim11 = dmodel11.end()
        dlim12 = dmodel12.end()
        dlim13 = dmodel13.end()
        dlim14 = dmodel14.end()
        dlim15 = dmodel15.end()
        dlim16 = dmodel16.end()
        dlim17 = dmodel17.end()
        dlim18 = dmodel18.end()
        dlim19 = dmodel19.end()
        dlim20 = dmodel20.end()

        elim1 = emodel1.end()
        elim2 = emodel2.end()
        elim3 = emodel3.end()
        elim4 = emodel4.end()
        elim5 = emodel5.end()
        elim6 = emodel6.end()
        elim7 = emodel7.end()
        elim8 = emodel8.end()
        elim9 = emodel9.end()
        elim10 = emodel10.end()
        elim11 = emodel11.end()
        elim12 = emodel12.end()
        elim13 = emodel13.end()
        elim14 = emodel14.end()
        elim15 = emodel15.end()
        elim16 = emodel16.end()
        elim17 = emodel17.end()
        elim18 = emodel18.end()
        elim19 = emodel19.end()
        elim20 = emodel20.end()

        flim1 = fmodel1.end()
        flim2 = fmodel2.end()
        flim3 = fmodel3.end()
        flim4 = fmodel4.end()
        flim5 = fmodel5.end()
        flim6 = fmodel6.end()
        flim7 = fmodel7.end()
        flim8 = fmodel8.end()
        flim9 = fmodel9.end()
        flim10 = fmodel10.end()
        flim11 = fmodel11.end()
        flim12 = fmodel12.end()
        flim13 = fmodel13.end()
        flim14 = fmodel14.end()
        flim15 = fmodel15.end()
        flim16 = fmodel16.end()
        flim17 = fmodel17.end()
        flim18 = fmodel18.end()
        flim19 = fmodel19.end()
        flim20 = fmodel20.end()

        # limit colorbar
        min1 = 0
        max1 = 50

        limit = ''
        folder = 'FullSimulation'

    # ------ Set Plot Style ------
    default_style()
    fig, ax1, ax2, ax3, ax4, colormap = env_mass(ms)

    # ------ Set Legend ------
    circle = mlines.Line2D([], [], color = 'grey',  marker='o', linestyle='None',
                          markersize=5, label='SMC')
    square = mlines.Line2D([], [], color = 'grey', marker='s', linestyle='None',
                          markersize=5, label='GAL')
    triangle = mlines.Line2D([], [], color = 'grey', marker='^', linestyle='None',
                          markersize=5, label='LMC')
    
    # ====== 1 ======
    # plot colors
    ims1 = ax1.scatter(amodel1.M[0], amodel1.vrot[0], c= amodel1.envelope_mass[alim1], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel2.M[0], amodel2.vrot[0], c= amodel2.envelope_mass[alim2], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel3.M[0], amodel3.vrot[0], c= amodel3.envelope_mass[alim3], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel4.M[0], amodel4.vrot[0], c= amodel4.envelope_mass[alim4], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel5.M[0], amodel5.vrot[0], c= amodel5.envelope_mass[alim5], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(bmodel1.M[0], bmodel1.vrot[0], c= bmodel1.envelope_mass[blim1], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel2.M[0], bmodel2.vrot[0], c= bmodel2.envelope_mass[blim2], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel3.M[0], bmodel3.vrot[0], c= bmodel3.envelope_mass[blim3], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel4.M[0], bmodel4.vrot[0], c= bmodel4.envelope_mass[blim4], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel5.M[0], bmodel5.vrot[0], c= bmodel5.envelope_mass[blim5], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(cmodel1.M[0], cmodel1.vrot[0], c= cmodel1.envelope_mass[clim1], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel2.M[0], cmodel2.vrot[0], c= cmodel2.envelope_mass[clim2], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel3.M[0], cmodel3.vrot[0], c= cmodel3.envelope_mass[clim3], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel4.M[0], cmodel4.vrot[0], c= cmodel4.envelope_mass[clim4], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel5.M[0], cmodel5.vrot[0], c= cmodel5.envelope_mass[clim5], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(dmodel1.M[0], dmodel1.vrot[0], c= dmodel1.envelope_mass[dlim1], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel2.M[0], dmodel2.vrot[0], c= dmodel2.envelope_mass[dlim2], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel3.M[0], dmodel3.vrot[0], c= dmodel3.envelope_mass[dlim3], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel4.M[0], dmodel4.vrot[0], c= dmodel4.envelope_mass[dlim4], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel5.M[0], dmodel5.vrot[0], c= dmodel5.envelope_mass[dlim5], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(emodel1.M[0], emodel1.vrot[0], c= emodel1.envelope_mass[elim1], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(emodel2.M[0], emodel2.vrot[0], c= emodel2.envelope_mass[elim2], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(emodel3.M[0], emodel3.vrot[0], c= emodel3.envelope_mass[elim3], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(emodel4.M[0], emodel4.vrot[0], c= emodel4.envelope_mass[elim4], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(emodel5.M[0], emodel5.vrot[0], c= emodel5.envelope_mass[elim5], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(fmodel1.M[0], fmodel1.vrot[0], c= fmodel1.envelope_mass[flim1], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(fmodel2.M[0], fmodel2.vrot[0], c= fmodel2.envelope_mass[flim2], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(fmodel3.M[0], fmodel3.vrot[0], c= fmodel3.envelope_mass[flim3], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(fmodel4.M[0], fmodel4.vrot[0], c= fmodel4.envelope_mass[flim4], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(fmodel5.M[0], fmodel5.vrot[0], c= fmodel5.envelope_mass[flim5], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    
    ax1.legend(handles=[circle, triangle, square], loc='center left')

    # cbar = fig.colorbar(ims1, ax = ax1)
    # cbar.set_label('Final Mass / Initial Mass')

    # ====== 2 ======
    # plot colors
    ims2 = ax2.scatter(amodel6.M[0], amodel6.vrot[0], c= amodel6.envelope_mass[alim6], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel7.M[0], amodel7.vrot[0], c= amodel7.envelope_mass[alim7], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel8.M[0], amodel8.vrot[0], c= amodel8.envelope_mass[alim8], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel9.M[0], amodel9.vrot[0], c= amodel9.envelope_mass[alim9], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel10.M[0], amodel10.vrot[0], c= amodel10.envelope_mass[alim10], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(bmodel6.M[0], bmodel6.vrot[0], c= bmodel6.envelope_mass[blim6], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel7.M[0], bmodel7.vrot[0], c= bmodel7.envelope_mass[blim7], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel8.M[0], bmodel8.vrot[0], c= bmodel8.envelope_mass[blim8], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel9.M[0], bmodel9.vrot[0], c= bmodel9.envelope_mass[blim9], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel10.M[0], bmodel10.vrot[0], c= bmodel10.envelope_mass[blim10], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(cmodel6.M[0], cmodel6.vrot[0], c= cmodel6.envelope_mass[clim6], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel7.M[0], cmodel7.vrot[0], c= cmodel7.envelope_mass[clim7], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel8.M[0], cmodel8.vrot[0], c= cmodel8.envelope_mass[clim8], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel9.M[0], cmodel9.vrot[0], c= cmodel9.envelope_mass[clim9], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel10.M[0], cmodel10.vrot[0], c= cmodel10.envelope_mass[clim10], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(dmodel6.M[0], dmodel6.vrot[0], c= dmodel6.envelope_mass[dlim6], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel7.M[0], dmodel7.vrot[0], c= dmodel7.envelope_mass[dlim7], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel8.M[0], dmodel8.vrot[0], c= dmodel8.envelope_mass[dlim8], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel9.M[0], dmodel9.vrot[0], c= dmodel9.envelope_mass[dlim9], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel10.M[0], dmodel10.vrot[0], c= dmodel10.envelope_mass[dlim10], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(emodel6.M[0], emodel6.vrot[0], c= emodel6.envelope_mass[elim6], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(emodel7.M[0], emodel7.vrot[0], c= emodel7.envelope_mass[elim7], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(emodel8.M[0], emodel8.vrot[0], c= emodel8.envelope_mass[elim8], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(emodel9.M[0], emodel9.vrot[0], c= emodel9.envelope_mass[elim9], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(emodel10.M[0], emodel10.vrot[0], c= emodel10.envelope_mass[elim10], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(fmodel6.M[0], fmodel6.vrot[0], c= fmodel6.envelope_mass[flim6], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(fmodel7.M[0], fmodel7.vrot[0], c= fmodel7.envelope_mass[flim7], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(fmodel8.M[0], fmodel8.vrot[0], c= fmodel8.envelope_mass[flim8], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(fmodel9.M[0], fmodel9.vrot[0], c= fmodel9.envelope_mass[flim9], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(fmodel10.M[0], fmodel10.vrot[0], c= fmodel10.envelope_mass[flim10], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    
    cbar2 = fig.colorbar(ims2, ax = ax2)
    cbar2.set_label('Envelope Mass [M$_{\odot}$]')

    ax2.legend(handles=[circle, triangle, square], loc='center left')

    # ====== 3 ======
    # plot colors
    ims3 = ax3.scatter(amodel11.M[0], amodel11.vrot[0], c= amodel11.envelope_mass[alim11], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel12.M[0], amodel12.vrot[0], c= amodel12.envelope_mass[alim12], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel13.M[0], amodel13.vrot[0], c= amodel13.envelope_mass[alim13], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel14.M[0], amodel14.vrot[0], c= amodel14.envelope_mass[alim14], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel15.M[0], amodel15.vrot[0], c= amodel15.envelope_mass[alim15], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    #ax3.scatter(bmodel11.M[0], bmodel11.vrot[0], c= bmodel11.envelope_mass[130], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel12.M[0], bmodel12.vrot[0], c= bmodel12.envelope_mass[blim12], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel13.M[0], bmodel13.vrot[0], c= bmodel13.envelope_mass[blim13], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel14.M[0], bmodel14.vrot[0], c= bmodel14.envelope_mass[blim14], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel15.M[0], bmodel15.vrot[0], c= bmodel15.envelope_mass[blim15], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(cmodel11.M[0], cmodel11.vrot[0], c= cmodel11.envelope_mass[clim11], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel12.M[0], cmodel12.vrot[0], c= cmodel12.envelope_mass[clim12], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel13.M[0], cmodel13.vrot[0], c= cmodel13.envelope_mass[clim13], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel14.M[0], cmodel14.vrot[0], c= cmodel14.envelope_mass[clim14], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel15.M[0], cmodel15.vrot[0], c= cmodel15.envelope_mass[clim15], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(dmodel11.M[0], dmodel11.vrot[0], c= dmodel11.envelope_mass[dlim11], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel12.M[0], dmodel12.vrot[0], c= dmodel12.envelope_mass[dlim12], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel13.M[0], dmodel13.vrot[0], c= dmodel13.envelope_mass[dlim13], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel14.M[0], dmodel14.vrot[0], c= dmodel14.envelope_mass[dlim14], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel15.M[0], dmodel15.vrot[0], c= dmodel15.envelope_mass[dlim15], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(emodel11.M[0], emodel11.vrot[0], c= emodel11.envelope_mass[elim11], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(emodel12.M[0], emodel12.vrot[0], c= emodel12.envelope_mass[elim12], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(emodel13.M[0], emodel13.vrot[0], c= emodel13.envelope_mass[elim13], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(emodel14.M[0], emodel14.vrot[0], c= emodel14.envelope_mass[elim14], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(emodel15.M[0], emodel15.vrot[0], c= emodel15.envelope_mass[elim15], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(fmodel11.M[0], fmodel11.vrot[0], c= fmodel11.envelope_mass[flim11], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(fmodel12.M[0], fmodel12.vrot[0], c= fmodel12.envelope_mass[flim12], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(fmodel13.M[0], fmodel13.vrot[0], c= fmodel13.envelope_mass[flim13], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(fmodel14.M[0], fmodel14.vrot[0], c= fmodel14.envelope_mass[flim14], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(fmodel15.M[0], fmodel15.vrot[0], c= fmodel15.envelope_mass[flim15], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    
    ax3.legend(handles=[circle, triangle, square], loc='center left')

    # cbar3 = fig.colorbar(ims3, ax = ax3)
    # cbar3.set_label('Final Mass / Initial Mass')

    # ====== 4 ======
    # plot colors
    ims4 = ax4.scatter(amodel16.M[0], amodel16.vrot[0], c= amodel16.envelope_mass[alim16], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel17.M[0], amodel17.vrot[0], c= amodel17.envelope_mass[alim17], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel18.M[0], amodel18.vrot[0], c= amodel18.envelope_mass[alim18], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel19.M[0], amodel19.vrot[0], c= amodel19.envelope_mass[alim19], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel20.M[0], amodel20.vrot[0], c= amodel20.envelope_mass[alim20], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(bmodel16.M[0], bmodel16.vrot[0], c= bmodel16.envelope_mass[blim16], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel17.M[0], bmodel17.vrot[0], c= bmodel17.envelope_mass[blim17], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel18.M[0], bmodel18.vrot[0], c= bmodel18.envelope_mass[blim18], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel19.M[0], bmodel19.vrot[0], c= bmodel19.envelope_mass[blim19], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel20.M[0], bmodel20.vrot[0], c= bmodel20.envelope_mass[blim20], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(cmodel16.M[0], cmodel16.vrot[0], c= cmodel16.envelope_mass[clim16], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel17.M[0], cmodel17.vrot[0], c= cmodel17.envelope_mass[clim17], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel18.M[0], cmodel18.vrot[0], c= cmodel18.envelope_mass[clim18], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel19.M[0], cmodel19.vrot[0], c= cmodel19.envelope_mass[clim19], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel20.M[0], cmodel20.vrot[0], c= cmodel20.envelope_mass[clim20], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(dmodel16.M[0], dmodel16.vrot[0], c= dmodel16.envelope_mass[dlim16], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel17.M[0], dmodel17.vrot[0], c= dmodel17.envelope_mass[dlim17], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel18.M[0], dmodel18.vrot[0], c= dmodel18.envelope_mass[dlim18], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel19.M[0], dmodel19.vrot[0], c= dmodel19.envelope_mass[dlim19], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel20.M[0], dmodel20.vrot[0], c= dmodel20.envelope_mass[dlim20], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(emodel16.M[0], emodel16.vrot[0], c= emodel16.envelope_mass[elim16], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(emodel17.M[0], emodel17.vrot[0], c= emodel17.envelope_mass[elim17], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(emodel18.M[0], emodel18.vrot[0], c= emodel18.envelope_mass[elim18], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(emodel19.M[0], emodel19.vrot[0], c= emodel19.envelope_mass[elim19], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(emodel20.M[0], emodel20.vrot[0], c= emodel20.envelope_mass[elim20], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(fmodel16.M[0], fmodel16.vrot[0], c= fmodel16.envelope_mass[flim16], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(fmodel17.M[0], fmodel17.vrot[0], c= fmodel17.envelope_mass[flim17], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(fmodel18.M[0], fmodel18.vrot[0], c= fmodel18.envelope_mass[flim18], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(fmodel19.M[0], fmodel19.vrot[0], c= fmodel19.envelope_mass[flim19], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(fmodel20.M[0], fmodel20.vrot[0], c= fmodel20.envelope_mass[flim20], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    cbar4 = fig.colorbar(ims4, ax = ax4)
    cbar4.set_label('Envelope Mass [M$_{\odot}$]')

    ax4.legend(handles=[circle, triangle, square], loc='center left')

    fig.tight_layout()
    plt.savefig(f'Plots/Overview/{folder}/Envelope_mass{limit}.png')


envelopemass(avink01_20, avink01_30, avink01_40, avink01_50, avink01_60, bvink01_20, bvink01_30, bvink01_40, bvink01_50, bvink01_60, cvink01_20, cvink01_30, cvink01_40, cvink01_50, cvink01_60, dvink01_20, dvink01_30, dvink01_40, dvink01_50, dvink01_60, evink01_20, evink01_30, evink01_40, evink01_50, evink01_60, fvink01_20, fvink01_30, fvink01_40, fvink01_50, fvink01_60,
avink18_20, avink18_30, avink18_40, avink18_50, avink18_60, bvink18_20, bvink18_30, bvink18_40, bvink18_50, bvink18_60, cvink18_20, cvink18_30, cvink18_40, cvink18_50, cvink18_60, dvink18_20, dvink18_30, dvink18_40, dvink18_50, dvink18_60, evink18_20, evink18_30, evink18_40, evink18_50, evink18_60, fvink18_20, fvink18_30, fvink18_40, fvink18_50, fvink18_60,
aleuven_20, aleuven_30, aleuven_40, aleuven_50, aleuven_60, bleuven_20, bleuven_30, bleuven_40, bleuven_50, bleuven_60, cleuven_20, cleuven_30, cleuven_40, cleuven_50, cleuven_60, dleuven_20, dleuven_30, dleuven_40, dleuven_50, dleuven_60, eleuven_20, eleuven_30, eleuven_40, eleuven_50, eleuven_60, fleuven_20, fleuven_30, fleuven_40, fleuven_50, fleuven_60,
akrticka_20, akrticka_30, akrticka_40, akrticka_50, akrticka_60, bkrticka_20, bkrticka_30, bkrticka_40, bkrticka_50, bkrticka_60, ckrticka_20, ckrticka_30, ckrticka_40, ckrticka_50, ckrticka_60, dkrticka_20, dkrticka_30, dkrticka_40, dkrticka_50, dkrticka_60, ekrticka_20, ekrticka_30, ekrticka_40, ekrticka_50, ekrticka_60, fkrticka_20, fkrticka_30, fkrticka_40, fkrticka_50, fkrticka_60,
ms)

# ================================================================

def Nmass(amodel1, amodel2, amodel3, amodel4, amodel5, bmodel1, bmodel2, bmodel3, bmodel4, bmodel5, cmodel1, cmodel2, cmodel3, cmodel4, cmodel5, dmodel1, dmodel2, dmodel3, dmodel4, dmodel5, emodel1, emodel2, emodel3, emodel4, emodel5, fmodel1, fmodel2, fmodel3, fmodel4, fmodel5,
amodel6, amodel7, amodel8, amodel9, amodel10, bmodel6, bmodel7, bmodel8, bmodel9, bmodel10, cmodel6, cmodel7, cmodel8, cmodel9, cmodel10, dmodel6, dmodel7, dmodel8, dmodel9, dmodel10, emodel6, emodel7, emodel8, emodel9, emodel10, fmodel6, fmodel7, fmodel8, fmodel9, fmodel10,
amodel11, amodel12, amodel13, amodel14, amodel15, bmodel11, bmodel12, bmodel13, bmodel14, bmodel15, cmodel11, cmodel12, cmodel13, cmodel14, cmodel15, dmodel11, dmodel12, dmodel13, dmodel14, dmodel15, emodel11, emodel12, emodel13, emodel14, emodel15, fmodel11, fmodel12, fmodel13, fmodel14, fmodel15,
amodel16, amodel17, amodel18, amodel19, amodel20, bmodel16, bmodel17, bmodel18, bmodel19, bmodel20, cmodel16, cmodel17, cmodel18, cmodel19, cmodel20, dmodel16, dmodel17, dmodel18, dmodel19, dmodel20, emodel16, emodel17, emodel18, emodel19, emodel20, fmodel16, fmodel17, fmodel18, fmodel19, fmodel20,
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

        elim1 = emodel1.mainsequence()
        elim2 = emodel2.mainsequence()
        elim3 = emodel3.mainsequence()
        elim4 = emodel4.mainsequence()
        elim5 = emodel5.mainsequence()
        elim6 = emodel6.mainsequence()
        elim7 = emodel7.mainsequence()
        elim8 = emodel8.mainsequence()
        elim9 = emodel9.mainsequence()
        elim10 = emodel10.mainsequence()
        elim11 = emodel11.mainsequence()
        elim12 = emodel12.mainsequence()
        elim13 = emodel13.mainsequence()
        elim14 = emodel14.mainsequence()
        elim15 = emodel15.mainsequence()
        elim16 = emodel16.mainsequence()
        elim17 = emodel17.mainsequence()
        elim18 = emodel18.mainsequence()
        elim19 = emodel19.mainsequence()
        elim20 = emodel20.mainsequence()

        flim1 = fmodel1.mainsequence()
        flim2 = fmodel2.mainsequence()
        flim3 = fmodel3.mainsequence()
        flim4 = fmodel4.mainsequence()
        flim5 = fmodel5.mainsequence()
        flim6 = fmodel6.mainsequence()
        flim7 = fmodel7.mainsequence()
        flim8 = fmodel8.mainsequence()
        flim9 = fmodel9.mainsequence()
        flim10 = fmodel10.mainsequence()
        flim11 = fmodel11.mainsequence()
        flim12 = fmodel12.mainsequence()
        flim13 = fmodel13.mainsequence()
        flim14 = fmodel14.mainsequence()  
        flim15 = fmodel15.mainsequence()
        flim16 = fmodel16.mainsequence()
        flim17 = fmodel17.mainsequence()
        flim18 = fmodel18.mainsequence()
        flim19 = fmodel19.mainsequence()
        flim20 = fmodel20.mainsequence()
        
        # limit colorbar
        min1 = 6.5
        max1 = 9

        limit = '_ms'
        folder = 'MainSequence'
    else:
        # full simulation
        alim1 = amodel1.end()
        alim2 = amodel2.end()
        alim3 = amodel3.end()
        alim4 = amodel4.end()
        alim5 = amodel5.end()
        alim6 = amodel6.end()
        alim7 = amodel7.end()
        alim8 = amodel8.end()
        alim9 = amodel9.end()
        alim10 = amodel10.end()
        alim11 = amodel11.end()
        alim12 = amodel12.end()
        alim13 = amodel13.end()
        alim14 = amodel14.end()
        alim15 = amodel15.end()
        alim16 = amodel16.end()
        alim17 = amodel17.end()
        alim18 = amodel18.end()
        alim19 = amodel19.end()
        alim20 = amodel20.end()

        blim1 = bmodel1.end()
        blim2 = bmodel2.end()
        blim3 = bmodel3.end()
        blim4 = bmodel4.end()
        blim5 = bmodel5.end()
        blim6 = bmodel6.end()
        blim7 = bmodel7.end()
        blim8 = bmodel8.end()
        blim9 = bmodel9.end()
        blim10 = bmodel10.end()
        blim11 = bmodel11.end()
        blim12 = bmodel12.end()
        blim13 = bmodel13.end()
        blim14 = bmodel14.end()
        blim15 = bmodel15.end()
        blim16 = bmodel16.end()
        blim17 = bmodel17.end()
        blim18 = bmodel18.end()
        blim19 = bmodel19.end()
        blim20 = bmodel20.end()

        clim1 = cmodel1.end()
        clim2 = cmodel2.end()
        clim3 = cmodel3.end()
        clim4 = cmodel4.end()
        clim5 = cmodel5.end()
        clim6 = cmodel6.end()
        clim7 = cmodel7.end()
        clim8 = cmodel8.end()
        clim9 = cmodel9.end()
        clim10 = cmodel10.end()
        clim11 = cmodel11.end()
        clim12 = cmodel12.end()
        clim13 = cmodel13.end()
        clim14 = cmodel14.end()
        clim15 = cmodel15.end()
        clim16 = cmodel16.end()
        clim17 = cmodel17.end()
        clim18 = cmodel18.end()
        clim19 = cmodel19.end()
        clim20 = cmodel20.end()

        dlim1 = dmodel1.end()
        dlim2 = dmodel2.end()
        dlim3 = dmodel3.end()
        dlim4 = dmodel4.end()
        dlim5 = dmodel5.end()
        dlim6 = dmodel6.end()
        dlim7 = dmodel7.end()
        dlim8 = dmodel8.end()
        dlim9 = dmodel9.end()
        dlim10 = dmodel10.end()
        dlim11 = dmodel11.end()
        dlim12 = dmodel12.end()
        dlim13 = dmodel13.end()
        dlim14 = dmodel14.end()
        dlim15 = dmodel15.end()
        dlim16 = dmodel16.end()
        dlim17 = dmodel17.end()
        dlim18 = dmodel18.end()
        dlim19 = dmodel19.end()
        dlim20 = dmodel20.end()

        elim1 = emodel1.end()
        elim2 = emodel2.end()
        elim3 = emodel3.end()
        elim4 = emodel4.end()
        elim5 = emodel5.end()
        elim6 = emodel6.end()
        elim7 = emodel7.end()
        elim8 = emodel8.end()
        elim9 = emodel9.end()
        elim10 = emodel10.end()
        elim11 = emodel11.end()
        elim12 = emodel12.end()
        elim13 = emodel13.end()
        elim14 = emodel14.end()
        elim15 = emodel15.end()
        elim16 = emodel16.end()
        elim17 = emodel17.end()
        elim18 = emodel18.end()
        elim19 = emodel19.end()
        elim20 = emodel20.end()

        flim1 = fmodel1.end()
        flim2 = fmodel2.end()
        flim3 = fmodel3.end()
        flim4 = fmodel4.end()
        flim5 = fmodel5.end()
        flim6 = fmodel6.end()
        flim7 = fmodel7.end()
        flim8 = fmodel8.end()
        flim9 = fmodel9.end()
        flim10 = fmodel10.end()
        flim11 = fmodel11.end()
        flim12 = fmodel12.end()
        flim13 = fmodel13.end()
        flim14 = fmodel14.end()
        flim15 = fmodel15.end()
        flim16 = fmodel16.end()
        flim17 = fmodel17.end()
        flim18 = fmodel18.end()
        flim19 = fmodel19.end()
        flim20 = fmodel20.end()

         # limit colorbar
        min1 = 6.5
        max1 = 9.5

        limit = ''
        folder = 'FullSimulation'


    # ------ Set Plot Style ------
    default_style()
    fig, ax1, ax2, ax3, ax4, colormap = N_mass(ms)
    
    # ------ Set Legend ------
    circle = mlines.Line2D([], [], color = 'grey',  marker='o', linestyle='None',
                          markersize=5, label='SMC')
    square = mlines.Line2D([], [], color = 'grey', marker='s', linestyle='None',
                          markersize=5, label='GAL')
    triangle = mlines.Line2D([], [], color = 'grey', marker='^', linestyle='None',
                          markersize=5, label='LMC')
    
     # ====== 1 ======
    # plot colors
    ims1 = ax1.scatter(amodel1.M[0], amodel1.vrot[0], c= amodel1.lognit[alim1], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel2.M[0], amodel2.vrot[0], c= amodel2.lognit[alim2], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel3.M[0], amodel3.vrot[0], c= amodel3.lognit[alim3], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel4.M[0], amodel4.vrot[0], c= amodel4.lognit[alim4], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(amodel5.M[0], amodel5.vrot[0], c= amodel5.lognit[alim5], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(bmodel1.M[0], bmodel1.vrot[0], c= bmodel1.lognit[blim1], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel2.M[0], bmodel2.vrot[0], c= bmodel2.lognit[blim2], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel3.M[0], bmodel3.vrot[0], c= bmodel3.lognit[blim3], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel4.M[0], bmodel4.vrot[0], c= bmodel4.lognit[blim4], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(bmodel5.M[0], bmodel5.vrot[0], c= bmodel5.lognit[blim5], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(cmodel1.M[0], cmodel1.vrot[0], c= cmodel1.lognit[clim1], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel2.M[0], cmodel2.vrot[0], c= cmodel2.lognit[clim2], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel3.M[0], cmodel3.vrot[0], c= cmodel3.lognit[clim3], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel4.M[0], cmodel4.vrot[0], c= cmodel4.lognit[clim4], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(cmodel5.M[0], cmodel5.vrot[0], c= cmodel5.lognit[clim5], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(dmodel1.M[0], dmodel1.vrot[0], c= dmodel1.lognit[dlim1], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel2.M[0], dmodel2.vrot[0], c= dmodel2.lognit[dlim2], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel3.M[0], dmodel3.vrot[0], c= dmodel3.lognit[dlim3], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel4.M[0], dmodel4.vrot[0], c= dmodel4.lognit[dlim4], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(dmodel5.M[0], dmodel5.vrot[0], c= dmodel5.lognit[dlim5], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(emodel1.M[0], emodel1.vrot[0], c= emodel1.lognit[elim1], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(emodel2.M[0], emodel2.vrot[0], c= emodel2.lognit[elim2], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(emodel3.M[0], emodel3.vrot[0], c= emodel3.lognit[elim3], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(emodel4.M[0], emodel4.vrot[0], c= emodel4.lognit[elim4], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(emodel5.M[0], emodel5.vrot[0], c= emodel5.lognit[elim5], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax1.scatter(fmodel1.M[0], fmodel1.vrot[0], c= fmodel1.lognit[flim1], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(fmodel2.M[0], fmodel2.vrot[0], c= fmodel2.lognit[flim2], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(fmodel3.M[0], fmodel3.vrot[0], c= fmodel3.lognit[flim3], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(fmodel4.M[0], fmodel4.vrot[0], c= fmodel4.lognit[flim4], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax1.scatter(fmodel5.M[0], fmodel5.vrot[0], c= fmodel5.lognit[flim5], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    
    ax1.legend(handles=[circle, triangle, square], loc='center left')

    # cbar = fig.colorbar(ims1, ax = ax1)
    # cbar.set_label('Final Mass / Initial Mass')

    # ====== 2 ======
    # plot colors
    ims2 = ax2.scatter(amodel6.M[0], amodel6.vrot[0], c= amodel6.lognit[alim6], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel7.M[0], amodel7.vrot[0], c= amodel7.lognit[alim7], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel8.M[0], amodel8.vrot[0], c= amodel8.lognit[alim8], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel9.M[0], amodel9.vrot[0], c= amodel9.lognit[alim9], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(amodel10.M[0], amodel10.vrot[0], c= amodel10.lognit[alim10], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(bmodel6.M[0], bmodel6.vrot[0], c= bmodel6.lognit[blim6], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel7.M[0], bmodel7.vrot[0], c= bmodel7.lognit[blim7], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel8.M[0], bmodel8.vrot[0], c= bmodel8.lognit[blim8], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel9.M[0], bmodel9.vrot[0], c= bmodel9.lognit[blim9], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(bmodel10.M[0], bmodel10.vrot[0], c= bmodel10.lognit[blim10], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(cmodel6.M[0], cmodel6.vrot[0], c= cmodel6.lognit[clim6], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel7.M[0], cmodel7.vrot[0], c= cmodel7.lognit[clim7], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel8.M[0], cmodel8.vrot[0], c= cmodel8.lognit[clim8], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel9.M[0], cmodel9.vrot[0], c= cmodel9.lognit[clim9], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(cmodel10.M[0], cmodel10.vrot[0], c= cmodel10.lognit[clim10], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(dmodel6.M[0], dmodel6.vrot[0], c= dmodel6.lognit[dlim6], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel7.M[0], dmodel7.vrot[0], c= dmodel7.lognit[dlim7], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel8.M[0], dmodel8.vrot[0], c= dmodel8.lognit[dlim8], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel9.M[0], dmodel9.vrot[0], c= dmodel9.lognit[dlim9], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(dmodel10.M[0], dmodel10.vrot[0], c= dmodel10.lognit[dlim10], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(emodel6.M[0], emodel6.vrot[0], c= emodel6.lognit[elim6], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(emodel7.M[0], emodel7.vrot[0], c= emodel7.lognit[elim7], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(emodel8.M[0], emodel8.vrot[0], c= emodel8.lognit[elim8], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(emodel9.M[0], emodel9.vrot[0], c= emodel9.lognit[elim9], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(emodel10.M[0], emodel10.vrot[0], c= emodel10.lognit[elim10], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax2.scatter(fmodel6.M[0], fmodel6.vrot[0], c= fmodel6.lognit[flim6], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(fmodel7.M[0], fmodel7.vrot[0], c= fmodel7.lognit[flim7], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(fmodel8.M[0], fmodel8.vrot[0], c= fmodel8.lognit[flim8], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(fmodel9.M[0], fmodel9.vrot[0], c= fmodel9.lognit[flim9], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax2.scatter(fmodel10.M[0], fmodel10.vrot[0], c= fmodel10.lognit[flim10], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    
    cbar2 = fig.colorbar(ims2, ax = ax2)
    cbar2.set_label('Nitrogen Abundance')

    ax2.legend(handles=[circle, triangle, square], loc='center left')

    # ====== 3 ======
    # plot colors
    ims3 = ax3.scatter(amodel11.M[0], amodel11.vrot[0], c= amodel11.lognit[alim11], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel12.M[0], amodel12.vrot[0], c= amodel12.lognit[alim12], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel13.M[0], amodel13.vrot[0], c= amodel13.lognit[alim13], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel14.M[0], amodel14.vrot[0], c= amodel14.lognit[alim14], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(amodel15.M[0], amodel15.vrot[0], c= amodel15.lognit[alim15], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    #ax3.scatter(bmodel11.M[0], bmodel11.vrot[0], c= bmodel11.lognit[130], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel12.M[0], bmodel12.vrot[0], c= bmodel12.lognit[blim12], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel13.M[0], bmodel13.vrot[0], c= bmodel13.lognit[blim13], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel14.M[0], bmodel14.vrot[0], c= bmodel14.lognit[blim14], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(bmodel15.M[0], bmodel15.vrot[0], c= bmodel15.lognit[blim15], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(cmodel11.M[0], cmodel11.vrot[0], c= cmodel11.lognit[clim11], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel12.M[0], cmodel12.vrot[0], c= cmodel12.lognit[clim12], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel13.M[0], cmodel13.vrot[0], c= cmodel13.lognit[clim13], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel14.M[0], cmodel14.vrot[0], c= cmodel14.lognit[clim14], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(cmodel15.M[0], cmodel15.vrot[0], c= cmodel15.lognit[clim15], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(dmodel11.M[0], dmodel11.vrot[0], c= dmodel11.lognit[dlim11], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel12.M[0], dmodel12.vrot[0], c= dmodel12.lognit[dlim12], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel13.M[0], dmodel13.vrot[0], c= dmodel13.lognit[dlim13], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel14.M[0], dmodel14.vrot[0], c= dmodel14.lognit[dlim14], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(dmodel15.M[0], dmodel15.vrot[0], c= dmodel15.lognit[dlim15], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(emodel11.M[0], emodel11.vrot[0], c= emodel11.lognit[elim11], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(emodel12.M[0], emodel12.vrot[0], c= emodel12.lognit[elim12], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(emodel13.M[0], emodel13.vrot[0], c= emodel13.lognit[elim13], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(emodel14.M[0], emodel14.vrot[0], c= emodel14.lognit[elim14], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(emodel15.M[0], emodel15.vrot[0], c= emodel15.lognit[elim15], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax3.scatter(fmodel11.M[0], fmodel11.vrot[0], c= fmodel11.lognit[flim11], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(fmodel12.M[0], fmodel12.vrot[0], c= fmodel12.lognit[flim12], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(fmodel13.M[0], fmodel13.vrot[0], c= fmodel13.lognit[flim13], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(fmodel14.M[0], fmodel14.vrot[0], c= fmodel14.lognit[flim14], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax3.scatter(fmodel15.M[0], fmodel15.vrot[0], c= fmodel15.lognit[flim15], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    
    # cbar3 = fig.colorbar(ims3, ax = ax3)
    # cbar3.set_label('Final Mass / Initial Mass')

    ax3.legend(handles=[circle, triangle, square], loc='center left')

    # ====== 4 ======
    # plot colors
    ims4 = ax4.scatter(amodel16.M[0], amodel16.vrot[0], c= amodel16.lognit[alim16], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel17.M[0], amodel17.vrot[0], c= amodel17.lognit[alim17], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel18.M[0], amodel18.vrot[0], c= amodel18.lognit[alim18], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel19.M[0], amodel19.vrot[0], c= amodel19.lognit[alim19], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(amodel20.M[0], amodel20.vrot[0], c= amodel20.lognit[alim20], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(bmodel16.M[0], bmodel16.vrot[0], c= bmodel16.lognit[blim16], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel17.M[0], bmodel17.vrot[0], c= bmodel17.lognit[blim17], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel18.M[0], bmodel18.vrot[0], c= bmodel18.lognit[blim18], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel19.M[0], bmodel19.vrot[0], c= bmodel19.lognit[blim19], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(bmodel20.M[0], bmodel20.vrot[0], c= bmodel20.lognit[blim20], marker='s', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(cmodel16.M[0], cmodel16.vrot[0], c= cmodel16.lognit[clim16], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel17.M[0], cmodel17.vrot[0], c= cmodel17.lognit[clim17], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel18.M[0], cmodel18.vrot[0], c= cmodel18.lognit[clim18], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel19.M[0], cmodel19.vrot[0], c= cmodel19.lognit[clim19], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(cmodel20.M[0], cmodel20.vrot[0], c= cmodel20.lognit[clim20], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(dmodel16.M[0], dmodel16.vrot[0], c= dmodel16.lognit[dlim16], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel17.M[0], dmodel17.vrot[0], c= dmodel17.lognit[dlim17], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel18.M[0], dmodel18.vrot[0], c= dmodel18.lognit[dlim18], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel19.M[0], dmodel19.vrot[0], c= dmodel19.lognit[dlim19], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(dmodel20.M[0], dmodel20.vrot[0], c= dmodel20.lognit[dlim20], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(emodel16.M[0], emodel16.vrot[0], c= emodel16.lognit[elim16], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(emodel17.M[0], emodel17.vrot[0], c= emodel17.lognit[elim17], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(emodel18.M[0], emodel18.vrot[0], c= emodel18.lognit[elim18], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(emodel19.M[0], emodel19.vrot[0], c= emodel19.lognit[elim19], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(emodel20.M[0], emodel20.vrot[0], c= emodel20.lognit[elim20], marker='o', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    ax4.scatter(fmodel16.M[0], fmodel16.vrot[0], c= fmodel16.lognit[flim16], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(fmodel17.M[0], fmodel17.vrot[0], c= fmodel17.lognit[flim17], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(fmodel18.M[0], fmodel18.vrot[0], c= fmodel18.lognit[flim18], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(fmodel19.M[0], fmodel19.vrot[0], c= fmodel19.lognit[flim19], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)
    ax4.scatter(fmodel20.M[0], fmodel20.vrot[0], c= fmodel20.lognit[flim20], marker='^', edgecolors='none', s=50, cmap=colormap, vmin = min1, vmax = max1)

    cbar4 = fig.colorbar(ims4, ax = ax4)
    cbar4.set_label('Nitrogen Abundance')

    ax4.legend(handles=[circle, triangle, square], loc='center left')

    fig.tight_layout()
    plt.savefig(f'Plots/Overview/{folder}/Nmass{limit}.png')


Nmass(avink01_20, avink01_30, avink01_40, avink01_50, avink01_60, bvink01_20, bvink01_30, bvink01_40, bvink01_50, bvink01_60, cvink01_20, cvink01_30, cvink01_40, cvink01_50, cvink01_60, dvink01_20, dvink01_30, dvink01_40, dvink01_50, dvink01_60, evink01_20, evink01_30, evink01_40, evink01_50, evink01_60, fvink01_20, fvink01_30, fvink01_40, fvink01_50, fvink01_60,
avink18_20, avink18_30, avink18_40, avink18_50, avink18_60, bvink18_20, bvink18_30, bvink18_40, bvink18_50, bvink18_60, cvink18_20, cvink18_30, cvink18_40, cvink18_50, cvink18_60, dvink18_20, dvink18_30, dvink18_40, dvink18_50, dvink18_60, evink18_20, evink18_30, evink18_40, evink18_50, evink18_60, fvink18_20, fvink18_30, fvink18_40, fvink18_50, fvink18_60,
aleuven_20, aleuven_30, aleuven_40, aleuven_50, aleuven_60, bleuven_20, bleuven_30, bleuven_40, bleuven_50, bleuven_60, cleuven_20, cleuven_30, cleuven_40, cleuven_50, cleuven_60, dleuven_20, dleuven_30, dleuven_40, dleuven_50, dleuven_60, eleuven_20, eleuven_30, eleuven_40, eleuven_50, eleuven_60, fleuven_20, fleuven_30, fleuven_40, fleuven_50, fleuven_60,
akrticka_20, akrticka_30, akrticka_40, akrticka_50, akrticka_60, bkrticka_20, bkrticka_30, bkrticka_40, bkrticka_50, bkrticka_60, ckrticka_20, ckrticka_30, ckrticka_40, ckrticka_50, ckrticka_60, dkrticka_20, dkrticka_30, dkrticka_40, dkrticka_50, dkrticka_60, ekrticka_20, ekrticka_30, ekrticka_40, ekrticka_50, ekrticka_60, fkrticka_20, fkrticka_30, fkrticka_40, fkrticka_50, fkrticka_60,
ms)

# ================================================================
