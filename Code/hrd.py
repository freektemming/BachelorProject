# Script that makes multiple HRD plots

from classData import Data
#from data import *
from plots import *
from plotstyles import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np

# ------ plot normal HRD 1 Model All Masses------
def hrd(model1, model2, model3, model4, model5, number, ms):

    # plot name of model in legend
    if number == '1':
        model = 'Vink 01 Model'
    if number == '2':
        model = 'Vink 18 Model'
    if number == '3':
        model = 'Leuven Model'
    if number == '4':
        model = 'Krticka Model'

    if ms == True:
        # main sequence limit
        lim1 = model1.mainsequence()
        lim2 = model2.mainsequence()
        lim3 = model3.mainsequence()
        lim4 = model4.mainsequence()
        lim5 = model5.mainsequence()

        # age limit colorbar
        min1 = model1.get_min_bar()
        max1 = model1.get_age(lim1)
        limit = '_ms'
        folder = 'MainSequence'
    else:
        # full simulation
        lim1 = model1.end()
        lim2 = model2.end()
        lim3 = model3.end()
        lim4 = model4.end()
        lim5 = model5.end()

        min1 = model1.get_min_bar()
        max1 = model1.get_max_bar()
        limit = ''
        folder = 'FullSimulation'

    # ------ Set Plot Style ------
    default_style()
    fig, ax, colormap = HRD(model)

    # plot line
    ax.plot(model1.Teff[0:lim1], model1.logL[0:lim1], lw = 1, color = 'black')
    ax.plot(model2.Teff[0:lim2], model2.logL[0:lim2], lw = 1, color = 'black')
    ax.plot(model3.Teff[0:lim3], model3.logL[0:lim3], lw = 1, color = 'black')
    ax.plot(model4.Teff[0:lim4], model4.logL[0:lim4], lw = 1, color = 'black')
    ax.plot(model5.Teff[0:lim5], model5.logL[0:lim5], lw = 1, color = 'black')

    # plot colors
    ims1 = ax.scatter(model1.Teff[0:lim1], model1.logL[0:lim1], c= model1.age[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims2 = ax.scatter(model2.Teff[0:lim2], model2.logL[0:lim2], c= model2.age[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims3 = ax.scatter(model3.Teff[0:lim3], model3.logL[0:lim3], c= model3.age[0:lim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims4 = ax.scatter(model4.Teff[0:lim4], model4.logL[0:lim4], c= model4.age[0:lim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims5 = ax.scatter(model5.Teff[0:lim5], model5.logL[0:lim5], c= model5.age[0:lim5], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    #ax.legend(shadow = False, edgecolor = 'k')

    # ------ Text ------
    ax.text(model1.Teff[0] + 5, model1.logL[0], '20M$_{\odot}$', fontweight = 'bold')
    ax.text(model2.Teff[0] + 5, model2.logL[0], '30M$_{\odot}$', fontweight = 'bold')
    ax.text(model3.Teff[0] + 5, model3.logL[0], '40M$_{\odot}$', fontweight = 'bold')
    ax.text(model4.Teff[0] + 5, model4.logL[0], '50M$_{\odot}$', fontweight = 'bold')
    ax.text(model5.Teff[0] + 5, model5.logL[0], '60M$_{\odot}$', fontweight = 'bold')
    
    fig.tight_layout()
    plt.savefig(f'Plots/{datafolder}/HRDmodels/{folder}/HRD{number}{limit}.png', dpi=200)


# ------ plot normal HRD 4 Models 1 Mass ------
def hrdmass(model1, model2, model3, model4, number, ms):

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
        lim1 = model1.end()
        lim2 = model2.end()
        lim3 = model3.end()
        lim4 = model4.end()

        min1 = model1.get_min_bar()
        max1 = model1.get_max_bar()
        limit = ''
        folder = 'FullSimulation'

    # ------ Set Plot Style ------
    default_style()
    fig, ax, colormap = HRD(model)

    # plot line
    ax.plot(model1.Teff[0:lim1], model1.logL[0:lim1], lw = 1, color = 'black', linestyle = 'solid', label = 'Vink 01')
    ax.plot(model2.Teff[0:lim2], model2.logL[0:lim2], lw = 1, color = 'black', linestyle = 'dashed', label = 'Vink 18')
    ax.plot(model3.Teff[0:lim3], model3.logL[0:lim3], lw = 1, color = 'black', linestyle = 'dashdot', label = 'Leuven')
    ax.plot(model4.Teff[0:lim4], model4.logL[0:lim4], lw = 1, color = 'black', linestyle = 'dotted', label = 'Krticka')
    
    # plot colors
    ims1 = ax.scatter(model1.Teff[0:lim1], model1.logL[0:lim1], c= model1.age[0:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims2 = ax.scatter(model2.Teff[0:lim2], model2.logL[0:lim2], c= model2.age[0:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims3 = ax.scatter(model3.Teff[0:lim3], model3.logL[0:lim3], c= model3.age[0:lim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims4 = ax.scatter(model4.Teff[0:lim4], model4.logL[0:lim4], c= model4.age[0:lim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    ax.legend(shadow = False, edgecolor = 'k')

    fig.tight_layout()
    plt.savefig(f'Plots/{datafolder}/HRDmass/{folder}/HRD{mass}{limit}.png', dpi=200)
 

# ------ Plot multiple HRD 4 Models Main Sequence------
def subhrd(model11, model12, model13, model14, model15, model21, model22, model23, model24, model25, model31, model32, model33, model34, model35, model41, model42, model43, model44, model45, ms):
    
    # distance of text in plot
    txt = 11

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

        # colorbar limits
        min1 = model11.get_min_bar()
        max1 = model11.get_age(lim11)

        min2 = model21.get_min_bar()
        max2 = model21.get_age(lim21)

        min3 = model31.get_min_bar()
        max3 = model31.get_age(lim31)

        min4 = model31.get_min_bar()
        max4 = model31.get_age(lim41)

        limit = '_ms'
    else:
        # full simulation
        lim1 = len(model11.age)
        lim2 = len(model11.age)
        min1 = model11.get_min_bar()
        max1 = model11.get_max_bar()
        limit = ''

    # ------ Set Plot Style ------
    default_style()
    fig, ((ax1, ax2), (ax3, ax4)), colormap = subHRD()

    # ------ first plot ------
    # plot line
    ax1.plot(model11.Teff[0:lim11], model11.logL[0:lim11], lw = 1, color = 'black')
    ax1.plot(model12.Teff[0:lim12], model12.logL[0:lim12], lw = 1, color = 'black')
    ax1.plot(model13.Teff[0:lim13], model13.logL[0:lim13], lw = 1, color = 'black')
    ax1.plot(model14.Teff[0:lim14], model14.logL[0:lim14], lw = 1, color = 'black')
    ax1.plot(model15.Teff[0:lim15], model15.logL[0:lim15], lw = 1, color = 'black')

    # plot colors
    ims11 = ax1.scatter(model11.Teff[0:lim11], model11.logL[0:lim11], c= model11.age[0:lim11], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims12 = ax1.scatter(model12.Teff[0:lim12], model12.logL[0:lim12], c= model12.age[0:lim12], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims13 = ax1.scatter(model13.Teff[0:lim13], model13.logL[0:lim13], c= model13.age[0:lim13], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims14 = ax1.scatter(model14.Teff[0:lim14], model14.logL[0:lim14], c= model14.age[0:lim14], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims15 = ax1.scatter(model15.Teff[0:lim15], model15.logL[0:lim15], c= model15.age[0:lim15], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    cbar1 = fig.colorbar(ims11, ax = ax1)
    cbar1.set_label('Age [Myr]')
    #ax1.legend(shadow = False, edgecolor = 'k')

    # plot text
    ax1.text(model11.Teff[0] + txt, model11.logL[0], '20M$_{\odot}$', fontweight = 'bold', fontsize=8)
    ax1.text(model12.Teff[0] + txt, model12.logL[0], '30M$_{\odot}$', fontweight = 'bold', fontsize=8)
    ax1.text(model13.Teff[0] + txt, model13.logL[0], '40M$_{\odot}$', fontweight = 'bold', fontsize=8)
    ax1.text(model14.Teff[0] + txt, model14.logL[0], '50M$_{\odot}$', fontweight = 'bold', fontsize=8)
    ax1.text(model15.Teff[0] + txt, model15.logL[0], '60M$_{\odot}$', fontweight = 'bold', fontsize=8)
    

    # ----- Second plot ------
    # plot line
    ax2.plot(model21.Teff[0:lim21], model21.logL[0:lim21], lw = 1, color = 'black')
    ax2.plot(model22.Teff[0:lim22], model22.logL[0:lim22], lw = 1, color = 'black')
    ax2.plot(model23.Teff[0:lim23], model23.logL[0:lim23], lw = 1, color = 'black')
    ax2.plot(model24.Teff[0:lim24], model24.logL[0:lim24], lw = 1, color = 'black')
    ax2.plot(model25.Teff[0:lim25], model25.logL[0:lim25], lw = 1, color = 'black')

    # plot colors
    ims21 = ax2.scatter(model21.Teff[0:lim21], model21.logL[0:lim21], c= model21.age[0:lim21], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min2, vmax = max2)
    ims22 = ax2.scatter(model22.Teff[0:lim22], model22.logL[0:lim22], c= model22.age[0:lim22], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min2, vmax = max2)
    ims23 = ax2.scatter(model23.Teff[0:lim23], model23.logL[0:lim23], c= model23.age[0:lim23], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min2, vmax = max2)
    ims24 = ax2.scatter(model24.Teff[0:lim24], model24.logL[0:lim24], c= model24.age[0:lim24], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min2, vmax = max2)
    ims25 = ax2.scatter(model25.Teff[0:lim25], model25.logL[0:lim25], c= model25.age[0:lim25], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min2, vmax = max2)
    cbar2 = fig.colorbar(ims21, ax = ax2)
    cbar2.set_label('Age [Myr]')
    #ax2.legend(shadow = False, edgecolor = 'k')

    # plot text
    ax2.text(model21.Teff[0] + txt, model21.logL[0], '20M$_{\odot}$', fontweight = 'bold', fontsize=8)
    ax2.text(model22.Teff[0] + txt, model22.logL[0], '30M$_{\odot}$', fontweight = 'bold', fontsize=8)
    ax2.text(model23.Teff[0] + txt, model23.logL[0], '40M$_{\odot}$', fontweight = 'bold', fontsize=8)
    ax2.text(model24.Teff[0] + txt, model24.logL[0], '50M$_{\odot}$', fontweight = 'bold', fontsize=8)
    ax2.text(model25.Teff[0] + txt, model25.logL[0], '60M$_{\odot}$', fontweight = 'bold', fontsize=8)
    
    # ------ Third Plot ------
    ax3.plot(model31.Teff[0:lim31], model31.logL[0:lim31], lw = 1, color = 'black')
    ax3.plot(model32.Teff[0:lim32], model32.logL[0:lim32], lw = 1, color = 'black')
    ax3.plot(model33.Teff[0:lim33], model33.logL[0:lim33], lw = 1, color = 'black')
    ax3.plot(model34.Teff[0:lim34], model34.logL[0:lim34], lw = 1, color = 'black')
    ax3.plot(model35.Teff[0:lim35], model35.logL[0:lim35], lw = 1, color = 'black')

    # plot colors
    ims31 = ax3.scatter(model31.Teff[0:lim31], model31.logL[0:lim31], c= model31.age[0:lim31], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min3, vmax = max3)
    ims32 = ax3.scatter(model32.Teff[0:lim32], model32.logL[0:lim32], c= model32.age[0:lim32], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min3, vmax = max3)
    ims33 = ax3.scatter(model33.Teff[0:lim33], model33.logL[0:lim33], c= model33.age[0:lim33], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min3, vmax = max3)
    ims34 = ax3.scatter(model34.Teff[0:lim34], model34.logL[0:lim34], c= model34.age[0:lim34], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min3, vmax = max3)
    ims35 = ax3.scatter(model35.Teff[0:lim35], model35.logL[0:lim35], c= model35.age[0:lim35], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min3, vmax = max3)
    cbar3 = fig.colorbar(ims31, ax = ax3)
    cbar3.set_label('Age [Myr]')
    #ax3.legend(shadow = False, edgecolor = 'k')

    # plot text
    ax3.text(model31.Teff[0] + txt, model31.logL[0], '20M$_{\odot}$', fontweight = 'bold', fontsize=8)
    ax3.text(model32.Teff[0] + txt, model32.logL[0], '30M$_{\odot}$', fontweight = 'bold', fontsize=8)
    ax3.text(model33.Teff[0] + txt, model33.logL[0], '40M$_{\odot}$', fontweight = 'bold', fontsize=8)
    ax3.text(model34.Teff[0] + txt, model34.logL[0], '50M$_{\odot}$', fontweight = 'bold', fontsize=8)
    ax3.text(model35.Teff[0] + txt, model35.logL[0], '60M$_{\odot}$', fontweight = 'bold', fontsize=8)
    
     # ------ Fourth Plot ------
    ax4.plot(model41.Teff[0:lim41], model41.logL[0:lim41], lw = 1, color = 'black')
    ax4.plot(model42.Teff[0:lim42], model42.logL[0:lim42], lw = 1, color = 'black')
    ax4.plot(model43.Teff[0:lim43], model43.logL[0:lim43], lw = 1, color = 'black')
    ax4.plot(model44.Teff[0:lim44], model44.logL[0:lim44], lw = 1, color = 'black')
    ax4.plot(model45.Teff[0:lim45], model45.logL[0:lim45], lw = 1, color = 'black')

    # plot colors
    ims41 = ax4.scatter(model41.Teff[0:lim41], model41.logL[0:lim41], c= model41.age[0:lim41], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min4, vmax = max4)
    ims42 = ax4.scatter(model42.Teff[0:lim42], model42.logL[0:lim42], c= model42.age[0:lim42], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min4, vmax = max4)
    ims43 = ax4.scatter(model43.Teff[0:lim43], model43.logL[0:lim43], c= model43.age[0:lim43], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min4, vmax = max4)
    ims44 = ax4.scatter(model44.Teff[0:lim44], model44.logL[0:lim44], c= model44.age[0:lim44], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min4, vmax = max4)
    ims45 = ax4.scatter(model45.Teff[0:lim45], model45.logL[0:lim45], c= model45.age[0:lim45], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min4, vmax = max4)
    cbar4 = fig.colorbar(ims41, ax = ax4)
    cbar4.set_label('Age [Myr]')
    #ax4.legend(shadow = False, edgecolor = 'k')

    # plot text
    ax4.text(model41.Teff[0] + txt, model41.logL[0], '20M$_{\odot}$', fontweight = 'bold', fontsize=8)
    ax4.text(model42.Teff[0] + txt, model42.logL[0], '30M$_{\odot}$', fontweight = 'bold', fontsize=8)
    ax4.text(model43.Teff[0] + txt, model43.logL[0], '40M$_{\odot}$', fontweight = 'bold', fontsize=8)
    ax4.text(model44.Teff[0] + txt, model44.logL[0], '50M$_{\odot}$', fontweight = 'bold', fontsize=8)
    ax4.text(model45.Teff[0] + txt, model45.logL[0], '60M$_{\odot}$', fontweight = 'bold', fontsize=8)
    
    fig.tight_layout()
    plt.savefig('Plots/4x4/HRDmodels/sub.png')

#subhrd(vink01_20, vink01_30, vink01_40, vink01_50, vink01_60, vink18_20, vink18_30, vink18_40, vink18_50, vink18_60, leuven_20, leuven_30, leuven_40, leuven_50, leuven_60, krticka_20, krticka_30, krticka_40, krticka_50, krticka_60, ms=lim)


# both main sequence and full simulation, all datafolders
datalist = ['Z014Om2','Z014Om4','Z014Om6','Z002Om2','Z002Om4','Z002Om6','Z007Om2','Z007Om4','Z007Om6']
for datafolder in datalist:

    print(datafolder)

    # Vink 01
    vink01_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/out.data')
    vink01_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/30/LOGS/out.data')
    vink01_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/40/LOGS/out.data')
    vink01_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/50/LOGS/out.data')
    vink01_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/60/LOGS/out.data')

    # Vink 18
    vink18_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/20/LOGS/out.data')
    vink18_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/30/LOGS/out.data')
    vink18_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/40/LOGS/out.data')
    vink18_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/50/LOGS/out.data')
    vink18_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/60/LOGS/out.data')

    # Leuven
    leuven_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/20/LOGS/out.data')
    leuven_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/30/LOGS/out.data')
    leuven_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/40/LOGS/out.data')
    leuven_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/50/LOGS/out.data')
    leuven_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/60/LOGS/out.data')

    # Krticka
    krticka_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/20/LOGS/out.data')
    krticka_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/30/LOGS/out.data')
    krticka_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/40/LOGS/out.data')
    krticka_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/50/LOGS/out.data')
    krticka_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/60/LOGS/out.data')
        
    # both main sequence and full simulation
    for i in range(2):
        if i == 0:
            lim = False
        if i == 1:
            lim = True

        hrd(vink01_20, vink01_30, vink01_40, vink01_50, vink01_60, '1', ms=lim)
        hrd(vink18_20, vink18_30, vink18_40, vink18_50, vink18_60, '2', ms=lim)
        hrd(leuven_20, leuven_30, leuven_40, leuven_50, leuven_60, '3', ms=lim)
        hrd(krticka_20, krticka_30, krticka_40, krticka_50, krticka_60, '4', ms=lim)
        hrdmass(vink01_20, vink18_20, leuven_20, krticka_20, '20', ms=lim)
        hrdmass(vink01_30, vink18_30, leuven_30, krticka_30, '30', ms=lim)
        hrdmass(vink01_40, vink18_40, leuven_40, krticka_40, '40', ms=lim)
        hrdmass(vink01_50, vink18_50, leuven_50, krticka_50, '50', ms=lim)
        hrdmass(vink01_60, vink18_60, leuven_60, krticka_60, '60', ms=lim)