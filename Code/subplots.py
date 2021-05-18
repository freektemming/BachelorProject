# Multiple supblots / histograms to compare variables from different models

from data import *
from plots import *
from plotstyles import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np


# limit: True for main sequense
lim = True

# ------ Compare 4 variables ------
def star(model1, model2, model3, model4, mass, ms):

    # ------ Set Plot Style ------
    default_style()

    if ms == True:
        # main sequence limit
        lim1 = model1.mainsequence()
        lim2 = model2.mainsequence()
        lim3 = model3.mainsequence()
        lim4 = model4.mainsequence()
        folder = 'MainSequence'
    else:
        # full simulation
        lim1 = len(model1.age)
        lim2 = len(model1.age)
        lim3 = len(model1.age)
        lim4 = len(model1.age)
        folder = 'FullSimulation'

    # ------ Figure ------
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(9,6.5))
    
    if ms == True:
        fig.suptitle(f'Main Sequence: {mass}''M$_{\odot}$', fontweight='bold')
        limit = '_ms'
    else:
        fig.suptitle(f'Full Evolution: {mass}''M$_{\odot}$', fontweight='bold')
        limit = ''

    # ------ Plot 1 ------
    ax1.plot(model1.age[0:lim1], model1.M[0:lim1], label = 'Vink 01', color = 'navy')
    ax1.plot(model2.age[0:lim2], model2.M[0:lim2], label = 'Vink 18', color = 'darkred')
    ax1.plot(model3.age[0:lim3], model3.M[0:lim3], label = 'Leuven', color = 'green')
    ax1.plot(model4.age[0:lim4], model4.M[0:lim4], label = 'Krticka', color = 'pink')
    ax1.legend(shadow = False, edgecolor = 'k')
    ax1.set_xlabel('Age [Myr]')
    ax1.set_ylabel('Mass [M$_{\odot}$]')
    ax1.set_title('Mass')
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    # ------ Plot 2 ------
    ax4.plot(model1.age[0:lim1], model1.logL[0:lim1], label = 'Vink 01', color = 'navy')
    ax4.plot(model2.age[0:lim2], model2.logL[0:lim2], label = 'Vink 18', color = 'darkred')
    ax4.plot(model3.age[0:lim3], model3.logL[0:lim3], label = 'Leuven', color = 'green')
    ax4.plot(model4.age[0:lim4], model4.logL[0:lim4], label = 'Krticka', color = 'pink')
    ax4.set_xlabel('Age [Myr]')
    ax4.set_ylabel('log (L / L$_{\odot}$)')
    ax4.set_title('Luminosity')
    ax4.legend(shadow = False, edgecolor = 'k')

    # ------ Plot 3 ------
    ax3.plot(model1.age[0:lim1], model1.vrot[0:lim1], label = 'Vink 01', color = 'navy')
    ax3.plot(model2.age[0:lim2], model2.vrot[0:lim2], label = 'Vink 18', color = 'darkred')
    ax3.plot(model3.age[0:lim3], model3.vrot[0:lim3], label = 'Leuven', color = 'green')
    ax3.plot(model4.age[0:lim4], model4.vrot[0:lim4], label = 'Krticka', color = 'pink')
    ax3.legend(shadow = False, edgecolor = 'k')
    ax3.set_xlabel('Age [Myr]')
    ax3.set_ylabel('V$_{\mathregular{rot}}$ [km / s]')
    ax3.set_title('Rotational Velocity')

    # ------ Plot 4 ------
    ax2.plot(model1.age[0:lim1], model1.logMdot[0:lim1], label = 'Vink 01', color = 'navy')
    ax2.plot(model2.age[0:lim2], model2.logMdot[0:lim2], label = 'Vink 18', color = 'darkred')
    ax2.plot(model3.age[0:lim3], model3.logMdot[0:lim3], label = 'Leuven', color = 'green')
    ax2.plot(model4.age[0:lim4], model4.logMdot[0:lim4], label = 'Krticka', color = 'pink')
    ax2.legend(shadow = False, edgecolor = 'k')
    ax2.set_xlabel('Age [Myr]')
    ax2.set_ylabel('log ($\dot{M}$) [M$_{\odot}$ / yr]')
    ax2.set_title('Mass Loss')
    
    plt.tight_layout()
    plt.savefig(f'Plots/{datafolder}/Subplots/Star/{folder}/star{mass}{limit}.png')

# star(vink01_20, vink18_20, leuven_20, krticka_20, '20', ms = lim)
# star(vink01_30, vink18_30, leuven_30, krticka_30, '30', ms = lim)
# star(vink01_40, vink18_40, leuven_40, krticka_40, '40', ms = lim)
# star(vink01_50, vink18_50, leuven_50, krticka_50, '50', ms = lim)
# star(vink01_60, vink18_60, leuven_60, krticka_60, '60', ms = lim)

# ------ Elements ------
def elements(model1, model2, model3, model4, mass, ms):

    # ------ Set Plot Style ------
    default_style()

    if ms == True:
        # main sequence limit
        lim1 = model1.mainsequence()
        lim2 = model2.mainsequence()
        lim3 = model3.mainsequence()
        lim4 = model4.mainsequence()
        folder = 'MainSequence'
    else:
        # full simulation
        lim1 = len(model1.age)
        lim2 = len(model1.age)
        lim3 = len(model1.age)
        lim4 = len(model1.age)
        folder = 'FullSimulation'

    # ------ Figure ------
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(9,6.5))
    
    if ms == True:
        fig.suptitle(f'Main Sequence: {mass}''M$_{\odot}$', fontweight='bold')
        limit = '_ms'
    else:
        fig.suptitle(f'Full Evolution: {mass}''M$_{\odot}$', fontweight='bold')
        limit = ''

    # ------ Plot 1 ------
    ax1.plot(model1.age[0:lim1], model1.lognh1[0:lim1], label = 'Vink 01', color = 'navy')
    ax1.plot(model2.age[0:lim2], model2.lognh1[0:lim2], label = 'Vink 18', color = 'darkred')
    ax1.plot(model3.age[0:lim3], model3.lognh1[0:lim3], label = 'Leuven', color = 'green')
    ax1.plot(model4.age[0:lim4], model4.lognh1[0:lim4], label = 'Krticka', color = 'pink')
    ax1.legend(shadow = False, edgecolor = 'k')
    ax1.set_xlabel('Age [Myr]')
    ax1.set_ylabel('log (H/H$_{\star}$)')
    ax1.set_title('Surface Hydrogen')
    #ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    # ------ Plot 2 ------
    ax2.plot(model1.age[0:lim1], model1.lognhe[0:lim1], label = 'Vink 01', color = 'navy')
    ax2.plot(model2.age[0:lim2], model2.lognhe[0:lim2], label = 'Vink 18', color = 'darkred')
    ax2.plot(model3.age[0:lim3], model3.lognhe[0:lim3], label = 'Leuven', color = 'green')
    ax2.plot(model4.age[0:lim4], model4.lognhe[0:lim4], label = 'Krticka', color = 'pink')
    ax2.set_xlabel('Age [Myr]')
    ax2.set_ylabel('log (He/He$_{\star}$)')
    ax2.set_title('Surface Helium')
    ax2.legend(shadow = False, edgecolor = 'k')

    # ------ Plot 3 ------
    ax3.plot(model1.age[0:lim1], model1.logncar[0:lim1], label = 'Vink 01', color = 'navy')
    ax3.plot(model2.age[0:lim2], model2.logncar[0:lim2], label = 'Vink 18', color = 'darkred')
    ax3.plot(model3.age[0:lim3], model3.logncar[0:lim3], label = 'Leuven', color = 'green')
    ax3.plot(model4.age[0:lim4], model4.logncar[0:lim4], label = 'Krticka', color = 'pink')
    ax3.legend(shadow = False, edgecolor = 'k')
    ax3.set_xlabel('Age [Myr]')
    ax3.set_ylabel('log (C/C$_{\star}$)')
    ax3.set_title('Surface Carbon')

    # ------ Plot 4 ------
    ax4.plot(model1.age[0:lim1], model1.lognnit[0:lim1], label = 'Vink 01', color = 'navy')
    ax4.plot(model2.age[0:lim2], model2.lognnit[0:lim2], label = 'Vink 18', color = 'darkred')
    ax4.plot(model3.age[0:lim3], model3.lognnit[0:lim3], label = 'Leuven', color = 'green')
    ax4.plot(model4.age[0:lim4], model4.lognnit[0:lim4], label = 'Krticka', color = 'pink')
    ax4.legend(shadow = False, edgecolor = 'k')
    ax4.set_xlabel('Age [Myr]')
    ax4.set_ylabel('log (N/N$_{\star}$)')
    ax4.set_title('Surface Nitrogen')
    
    plt.tight_layout()
    plt.savefig(f'Plots/{datafolder}/Subplots/Elements/{folder}/elem{mass}{limit}.png')

elements(vink01_20, vink18_20, leuven_20, krticka_20, '20', ms = lim)
elements(vink01_30, vink18_30, leuven_30, krticka_30, '30', ms = lim)
elements(vink01_40, vink18_40, leuven_40, krticka_40, '40', ms = lim)
elements(vink01_50, vink18_50, leuven_50, krticka_50, '50', ms = lim)
elements(vink01_60, vink18_60, leuven_60, krticka_60, '60', ms = lim)



# ------ Histograms ------
def histogram(model1, model2, model3, model4, mass, ms):

    # ------ Set Plot Style ------
    histogramstyle()

    if ms == True:
        # main sequence limit
        lim1 = model1.mainsequence()
        lim2 = model2.mainsequence()
        lim3 = model3.mainsequence()
        lim4 = model4.mainsequence()
        folder = 'MainSequence'
    else:
        # full simulation
        lim1 = len(model1.age)
        lim2 = len(model1.age)
        lim3 = len(model1.age)
        lim4 = len(model1.age)
        folder = 'FullSimulation'

    # ------ Figure ------
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(9,6.5))
    
    if ms == True:
        fig.suptitle(f'Main Sequence: {mass}''M$_{\odot}$', fontweight='bold')
        limit = '_ms'
    else:
        fig.suptitle(f'Full Evolution: {mass}''M$_{\odot}$', fontweight='bold')
        limit = ''

    # ------ Hist 1 ------
    ax1.bar(2, model1.histM[len(model1.M[0:lim1])-1], 1, label='Vink 01', color = 'navy')
    ax1.bar(3, model2.histM[len(model2.M[0:lim2])-1], 1, label='Vink 18', color = 'darkred')
    ax1.bar(4, model3.histM[len(model3.M[0:lim3])-1], 1, label='Leuven', color = 'green')
    ax1.bar(5, model4.histM[len(model4.M[0:lim4])-1], 1, label='Krticka', color = 'pink')
    ax1.set_xlim(0,7)
    ax1.set_ylim(0.6)
    ax1.set_xticks([2,3,4,5])
    ax1.set_xticklabels(['Vink 01','Vink 18','Leuven','Krticka'])
    ax1.set_ylabel('Mass [M / M$_{\mathregular{start}}$]')
    ax1.set_title('Mass')
    #ax1.legend(shadow = False, edgecolor = 'k')

    # ------ Hist 2 ------
    ax2.bar(2, model1.histR[len(model1.M[0:lim1])-1], 1, label='Vink 01', color = 'navy')
    ax2.bar(3, model2.histR[len(model2.M[0:lim2])-1], 1, label='Vink 18', color = 'darkred')
    ax2.bar(4, model3.histR[len(model3.M[0:lim3])-1], 1, label='Leuven', color = 'green')
    ax2.bar(5, model4.histR[len(model4.M[0:lim4])-1], 1, label='Krticka', color = 'pink')
    ax2.set_xlim(0,7)
    ax2.set_xticks([2,3,4,5])
    ax2.set_xticklabels(['Vink 01','Vink 18','Leuven','Krticka'])
    ax2.set_ylabel('Radius [R / R$_{\mathregular{start}}$]')
    ax2.set_title('Radius')
    #ax2.legend(shadow = False, edgecolor = 'k')

    # ------ Hist 3 ------
    ax3.bar(2, model1.histVrot[len(model1.M[0:lim1])-1], 1, label='Vink 01', color = 'navy')
    ax3.bar(3, model2.histVrot[len(model2.M[0:lim2])-1], 1, label='Vink 18', color = 'darkred')
    ax3.bar(4, model3.histVrot[len(model3.M[0:lim3])-1], 1, label='Leuven', color = 'green')
    ax3.bar(5, model4.histVrot[len(model4.M[0:lim4])-1], 1, label='Krticka', color = 'pink')
    ax3.set_xlim(0,7)
    ax3.set_xticks([2,3,4,5])
    ax3.set_xticklabels(['Vink 01','Vink 18','Leuven','Krticka'])
    ax3.set_ylabel('V$_{\mathregular{rot}}$ [V / V$_{\mathregular{start}}$]')
    ax3.set_title('Rotational Velocity')
    #ax3.legend(shadow = False, edgecolor = 'k')

    # ------ Hist 4 ------
    ax4.bar(2, model1.histL[len(model1.M[0:lim1])-1], 1, label='Vink 01', color = 'navy')
    ax4.bar(3, model2.histL[len(model2.M[0:lim2])-1], 1, label='Vink 18', color = 'darkred')
    ax4.bar(4, model3.histL[len(model3.M[0:lim3])-1], 1, label='Leuven', color = 'green')
    ax4.bar(5, model4.histL[len(model4.M[0:lim4])-1], 1, label='Krticka', color = 'pink')
    ax4.set_xlim(0,7)
    ax4.set_ylim(1)
    ax4.set_xticks([2,3,4,5])
    ax4.set_xticklabels(['Vink 01','Vink 18','Leuven','Krticka'])
    ax4.set_ylabel('Luminosity [L / L$_{\mathregular{start}}$]')
    ax4.set_title('Luminosity')
    #ax4.legend(shadow = False, edgecolor = 'k')

    fig.tight_layout()
    #plt.show()
    plt.savefig(f'Plots/{datafolder}/Subplots/Histogram/{folder}/hist{mass}{limit}.png')

# histogram(vink01_20, vink18_20, leuven_20, krticka_20, '20', ms = lim)
# histogram(vink01_30, vink18_30, leuven_30, krticka_30, '30', ms = lim)
# histogram(vink01_40, vink18_40, leuven_40, krticka_40, '40', ms = lim)
# histogram(vink01_50, vink18_50, leuven_50, krticka_50, '50', ms = lim)
# histogram(vink01_60, vink18_60, leuven_60, krticka_60, '60', ms = lim)
# lim = True
# histogram(vink01_20, vink18_20, leuven_20, krticka_20, '20', ms = lim)
# histogram(vink01_30, vink18_30, leuven_30, krticka_30, '30', ms = lim)
# histogram(vink01_40, vink18_40, leuven_40, krticka_40, '40', ms = lim)
# histogram(vink01_50, vink18_50, leuven_50, krticka_50, '50', ms = lim)
# histogram(vink01_60, vink18_60, leuven_60, krticka_60, '60', ms = lim)


# ------ Plot difference between 2 variables ------
def difference(model1,model2, var):

    # choose variables to call
    if var == 1:
        variable1 = model1.M
        variable2 = model2.M

    if var == 2:
        variable1 = model1.vrot
        variable2 = model2.vrot

    if var == 3:
        variable1 = model1.h1
        variable2 = model2.h1

    if var == 4:
        variable1 = model1.R
        variable2 = model2.R

    length = 0
    DifferenceList = []
    steps = []

    # pick shortest model to loop over
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
    
    # list for x axis
    for i in range(length):
        steps.append(i)

    return DifferenceList, steps
    
def difplot(model1,model2):

    # ------ Set Plot Style ------
    default_style()

    # get x-lists and differences
    dif1, steps1 = difference(model1,model2,1)
    dif2, steps2 = difference(model1,model2,2)
    dif3, steps3 = difference(model1,model2,3)
    dif4, steps4 = difference(model1,model2,4)

    # ------ Figure ------
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(9,6.5))
    fig.suptitle('Difference Between Models', fontweight='bold')

    # ------ Plot 1 ------
    ax1.plot(steps1, dif1, color = 'navy')
    ax1.set_xlabel('Model [steps]')
    ax1.set_ylabel('Mass [M$_{\odot}$]')
    ax1.set_title('Mass')
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    # ------ Plot 2 ------
    ax2.plot(steps2, dif2, color = 'navy')
    ax2.set_xlabel('Model [steps]')
    ax2.set_ylabel('Vrot')
    ax2.set_title('Rotational Velocity')
    ax2.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    # ------ Plot 3 ------
    ax3.plot(steps3, dif3, color = 'navy')
    ax3.set_xlabel('Model [steps]')
    ax3.set_ylabel('')
    ax3.set_title('Surface H')
    ax3.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    # ------ Plot 4 ------
    ax4.plot(steps4, dif4, color = 'navy')
    ax4.set_xlabel('Model [steps]')
    ax4.set_ylabel('Radius R$_{\odot}$')
    ax4.set_title('Radius')
    ax4.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    fig.tight_layout()
    plt.savefig('Plots/Week1/Subplots/difference.png')

#difplot(vink01,vink18)


# ------ Rotation ------
def rotation(model1, model2, ms):

    # ------ Set Plot Style ------
    default_style()

    if ms == True:
        # main sequence limit
        lim1 = model1.mainsequence()
        lim2 = model2.mainsequence()
    else:
        # full simulation
        lim1 = len(model1.age)
        lim2 = len(model1.age)

    # ------ Figure ------
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(9,6.5))

    if ms == True:
        fig.suptitle('Main Sequence Results', fontweight='bold')
        limit = '_ms'
    else:
        fig.suptitle('Full Evolution Results', fontweight='bold')
        limit = ''

    # ------ Plot 1 ------
    ax1.plot(model1.age[0:lim1], model1.vrot[0:lim1], label = 'Vink01', color = 'navy')
    ax1.plot(model2.age[0:lim2], model2.vrot[0:lim2], label = 'Vink18', color = 'darkred')
    ax1.legend(shadow = False, edgecolor = 'k')
    ax1.set_xlabel('Age [Myr]')
    ax1.set_ylabel('')
    ax1.set_title('Rotational Velocity')
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    # ------ Plot 2 ------
    ax2.plot(model1.age[0:lim1], model1.Jtot[0:lim1], label = 'Vink01', color = 'navy')
    ax2.plot(model2.age[0:lim2], model2.Jtot[0:lim2], label = 'Vink18', color = 'darkred')
    ax2.set_xlabel('Age [Myr]')
    ax2.set_ylabel('')
    ax2.set_title('Total Angular Momentum')
    ax2.legend(shadow = False, edgecolor = 'k')

    # ------ Plot 3 ------
    ax3.plot(model1.age[0:lim1], model1.Omega[0:lim1], label = 'Vink01', color = 'navy')
    ax3.plot(model2.age[0:lim2], model2.Omega[0:lim2], label = 'Vink18', color = 'darkred')
    ax3.legend(shadow = False, edgecolor = 'k')
    ax3.set_xlabel('Age [Myr]')
    ax3.set_ylabel('')
    ax3.set_title('Omega')

    # ------ Plot 4 ------
    ax4.plot(model1.age[0:lim1], model1.period[0:lim1], label = 'Vink01', color = 'navy')
    ax4.plot(model2.age[0:lim2], model2.period[0:lim2], label = 'Vink18', color = 'darkred')
    ax4.legend(shadow = False, edgecolor = 'k')
    ax4.set_xlabel('Age [Myr]')
    ax4.set_ylabel('')
    ax4.set_title('Period')
    
    plt.tight_layout()
    plt.savefig(f'Plots/Week1/Subplots/rotation{limit}.png')

#rotation(vink01, vink18, ms = lim)