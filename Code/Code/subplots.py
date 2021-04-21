# Multiple supblots / histograms to compare variables from different models

from data import *
from plots import *
from plotstyles import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np


# limit: True for main sequense
lim = False

# ------ Compare 4 variables ------
def star(model1, model2, ms):

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
    
    if ms == 'ms':
        fig.suptitle('Main Sequence Results', fontweight='bold')
        limit = '_ms'
    else:
        fig.suptitle('Full Evolution Results', fontweight='bold')
        limit = ''

    # ------ Plot 1 ------
    ax1.plot(model1.age[0:lim1], model1.M[0:lim1], label = 'Vink01', color = 'navy')
    ax1.plot(model2.age[0:lim2], model2.M[0:lim2], label = 'Vink18', color = 'darkred')
    ax1.legend(shadow = False, edgecolor = 'k')
    ax1.set_xlabel('Age [Myr]')
    ax1.set_ylabel('Mass [M$_{\odot}$]')
    ax1.set_title('Mass')
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    # ------ Plot 2 ------
    ax2.plot(model1.age[0:lim1], model1.logL[0:lim1], label = 'Vink01', color = 'navy')
    ax2.plot(model2.age[0:lim2], model2.logL[0:lim2], label = 'Vink18', color = 'darkred')
    ax2.set_xlabel('Age [Myr]')
    ax2.set_ylabel('log (L / L$_{\odot}$)')
    ax2.set_title('Luminosity')
    ax2.legend(shadow = False, edgecolor = 'k')

    # ------ Plot 3 ------
    ax3.plot(model1.age[0:lim1], model1.Teff[0:lim1], label = 'Vink01', color = 'navy')
    ax3.plot(model2.age[0:lim2], model2.Teff[0:lim2], label = 'Vink18', color = 'darkred')
    ax3.legend(shadow = False, edgecolor = 'k')
    ax3.set_xlabel('Age [Myr]')
    ax3.set_ylabel('Teff [kK]')
    ax3.set_title('Effective Temperature')

    # ------ Plot 4 ------
    ax4.plot(model1.age[0:lim1], model1.R[0:lim1], label = 'Vink01', color = 'navy')
    ax4.plot(model2.age[0:lim2], model2.R[0:lim2], label = 'Vink18', color = 'darkred')
    ax4.legend(shadow = False, edgecolor = 'k')
    ax4.set_xlabel('Age [Myr]')
    ax4.set_ylabel('Radius [R$_{\odot}$]')
    ax4.set_title('Radius')
    
    plt.tight_layout()
    plt.savefig(f'Plots/Week1/Subplots/subplot{limit}.png')

star(vink01, vink18, ms = lim)

# ------ Elements ------
def elements(model1, model2, ms):

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
    ax1.plot(model1.age[0:lim1], model1.nh1[0:lim1], label = 'Vink01', color = 'navy')
    ax1.plot(model2.age[0:lim2], model2.nh1[0:lim2], label = 'Vink18', color = 'darkred')
    ax1.legend(shadow = False, edgecolor = 'k')
    ax1.set_xlabel('Age [Myr]')
    ax1.set_ylabel('H/H$_{\star}$')
    ax1.set_title('Surface Hydrogen')
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    # ------ Plot 2 ------
    ax2.plot(model1.age[0:lim1], model1.ncar[0:lim1], label = 'Vink01', color = 'navy')
    ax2.plot(model2.age[0:lim2], model2.ncar[0:lim2], label = 'Vink18', color = 'darkred')
    ax2.set_xlabel('Age [Myr]')
    ax2.set_ylabel('C/C$_{\star}$')
    ax2.set_title('Surface Carbon')
    ax2.legend(shadow = False, edgecolor = 'k')

    # ------ Plot 3 ------
    ax3.plot(model1.age[0:lim1], model1.nnit[0:lim1], label = 'Vink01', color = 'navy')
    ax3.plot(model2.age[0:lim2], model2.nnit[0:lim2], label = 'Vink18', color = 'darkred')
    ax3.legend(shadow = False, edgecolor = 'k')
    ax3.set_xlabel('Age [Myr]')
    ax3.set_ylabel('N/N$_{\star}$')
    ax3.set_title('Surface Nitrogen')

    # ------ Plot 4 ------
    ax4.plot(model1.age[0:lim1], model1.nox[0:lim1], label = 'Vink01', color = 'navy')
    ax4.plot(model2.age[0:lim2], model2.nox[0:lim2], label = 'Vink18', color = 'darkred')
    ax4.legend(shadow = False, edgecolor = 'k')
    ax4.set_xlabel('Age [Myr]')
    ax4.set_ylabel('O/O$_{\star}$')
    ax4.set_title('Surface Oxigen')
    
    plt.tight_layout()
    plt.savefig(f'Plots/Week1/Subplots/elements{limit}.png')

elements(vink01, vink18, ms = lim)

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

rotation(vink01, vink18, ms = lim)

# ------ Histograms ------
def histogram(model1, model2, ms):

    # ------ Set Plot Style ------
    histogramstyle()

    if ms == True:
        # main sequence limit
        lim1 = model1.mainsequence()
        lim2 = model2.mainsequence()
    else:
        # full simulation
        lim1 = len(model1.age)
        lim2 = len(model1.age)


    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)
    
    if ms == True:
        fig.suptitle('Main Sequence Results', fontweight='bold')
        limit = '_ms'
    else:
        fig.suptitle('Full Evolution Results', fontweight='bold')
        limit = ''

    # ------ Hist 1 ------
    ax1.bar(2, model1.M[len(model1.M[0:lim1])-1], 1, label='vink01', color = 'navy')
    ax1.bar(3, model2.M[len(model2.M[0:lim2])-1], 1, label='vink18', color = 'darkred')
    ax1.set_xlim(0,7)
    ax1.set_xticks([2,3])
    ax1.set_xticklabels(['', ''])
    ax1.set_ylabel('Mass M$_{\odot}$')
    ax1.set_title('Mass')
    ax1.legend(shadow = False, edgecolor = 'k')

    # ------ Hist 2 ------
    ax2.bar(2, model1.R[len(model1.R[0:lim1])-1], 1, label='vink01', color = 'navy')
    ax2.bar(3, model2.R[len(model2.R[0:lim2])-1], 1, label='vink18', color = 'darkred')
    ax2.set_xlim(0,7)
    ax2.set_xticks([2,3])
    ax2.set_xticklabels(['', ''])
    ax2.set_ylabel('Radius R$_{\odot}$')
    ax2.set_title('Radius')
    ax2.legend(shadow = False, edgecolor = 'k')

    # ------ Hist 3 ------
    ax3.bar(2, model1.Teff[len(model1.Teff[0:lim1])-1], 1, label='vink01', color = 'navy')
    ax3.bar(3, model2.Teff[len(model2.Teff[0:lim2])-1], 1, label='vink18', color = 'darkred')
    ax3.set_xlim(0,7)
    ax3.set_xticks([2,3])
    ax3.set_xticklabels(['', ''])
    ax3.set_ylabel('Teff')
    ax3.set_title('Effective Temperature')
    ax3.legend(shadow = False, edgecolor = 'k')

    # ------ Hist 4 ------
    ax4.bar(2, model1.logL[len(model1.logL[0:lim1])-1], 1, label='vink01', color = 'navy')
    ax4.bar(3, model2.logL[len(model2.logL[0:lim2])-1], 1, label='vink18', color = 'darkred')
    ax4.set_xlim(0,7)
    ax4.set_xticks([2,3])
    ax4.set_xticklabels(['', ''])
    ax4.set_ylabel('LogL')
    ax4.set_title('Luminosity')
    ax4.legend(shadow = False, edgecolor = 'k')

    fig.tight_layout()
    plt.savefig(f'Plots/Week1/Subplots/histogram{limit}.png')

histogram(vink01, vink18, ms = lim)

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

difplot(vink01,vink18)