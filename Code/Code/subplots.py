# Multiple supblots / histograms to compare variables from different models

from ClassData import Data
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np

# ------ Models ------
vink01 = Data('../Data/40M_Vink01_out.data')
vink18 = Data('../Data/40M_Vink18_out.data')

# ------ Compare 4 variables ------
def star(model1, model2):

    # ------ Figure ------
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(9,6.5))
    fig.suptitle('Comparison Models', fontweight='bold')

    # ------ Plot 1 ------
    ax1.plot(model1.age, model1.M, label = 'Vink01', color = 'navy')
    ax1.plot(model2.age, model2.M, label = 'Vink18', color = 'darkred')
    ax1.legend(fancybox = True, scatterpoints = 1, labelspacing = 1, shadow=True)
    ax1.set_xlabel('Age [Myr]')
    ax1.set_ylabel('Mass [M$_{\odot}$]')
    ax1.set_title('Mass')
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    # ------ Plot 2 ------
    ax2.plot(model1.age, model1.logL, label = 'Vink01', color = 'navy')
    ax2.plot(model2.age, model2.logL, label = 'Vink18', color = 'darkred')
    ax2.set_xlabel('Age [Myr]')
    ax2.set_ylabel('log (L / L$_{\odot}$)')
    ax2.set_title('Luminosity')
    ax2.legend(fancybox = True, scatterpoints = 1, labelspacing = 1, shadow=True)

    # ------ Plot 3 ------
    ax3.plot(model1.age, model1.Teff, label = 'Vink01', color = 'navy')
    ax3.plot(model2.age, model2.Teff, label = 'Vink18', color = 'darkred')
    ax3.legend(fancybox = True, scatterpoints = 1, labelspacing = 1, shadow=True)
    ax3.set_xlabel('Age [Myr]')
    ax3.set_ylabel('Teff [kK]')
    ax3.set_title('Effective Temperature')

    # ------ Plot 4 ------
    ax4.plot(model1.age, model1.R, label = 'Vink01', color = 'navy')
    ax4.plot(model2.age, model2.R, label = 'Vink18', color = 'darkred')
    ax4.legend(fancybox = True, scatterpoints = 1, labelspacing = 1, shadow=True)
    ax4.set_xlabel('Age [Myr]')
    ax4.set_ylabel('Radius [R$_{\odot}$]')
    ax4.set_title('Radius')
    
    plt.tight_layout()
    plt.savefig('Plots/subplot.png')

star(vink01, vink18)

# ------ Elements ------
def elements(model1, model2):

    # ------ Figure ------
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(9,6.5))
    fig.suptitle('Comparison Models', fontweight='bold')

    # ------ Plot 1 ------
    ax1.plot(model1.age, model1.car, label = 'Vink01', color = 'navy')
    ax1.plot(model2.age, model2.car, label = 'Vink18', color = 'darkred')
    ax1.legend(fancybox = True, scatterpoints = 1, labelspacing = 1, shadow=True)
    ax1.set_xlabel('Age [Myr]')
    ax1.set_ylabel('')
    ax1.set_title('Carbon')
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    # ------ Plot 2 ------
    ax2.plot(model1.age, model1.nit, label = 'Vink01', color = 'navy')
    ax2.plot(model2.age, model2.nit, label = 'Vink18', color = 'darkred')
    ax2.set_xlabel('Age [Myr]')
    ax2.set_ylabel('')
    ax2.set_title('Nitrogen')
    ax2.legend(fancybox = True, scatterpoints = 1, labelspacing = 1, shadow=True)

    # ------ Plot 3 ------
    ax3.plot(model1.age, model1.ox, label = 'Vink01', color = 'navy')
    ax3.plot(model2.age, model2.ox, label = 'Vink18', color = 'darkred')
    ax3.legend(fancybox = True, scatterpoints = 1, labelspacing = 1, shadow=True)
    ax3.set_xlabel('Age [Myr]')
    ax3.set_ylabel('')
    ax3.set_title('Oxigen')

    # ------ Plot 4 ------
    ax4.plot(model1.age, model1.surfh1, label = 'Vink01', color = 'navy')
    ax4.plot(model2.age, model2.surfh1, label = 'Vink18', color = 'darkred')
    ax4.legend(fancybox = True, scatterpoints = 1, labelspacing = 1, shadow=True)
    ax4.set_xlabel('Age [Myr]')
    ax4.set_ylabel('')
    ax4.set_title('Surface H')
    
    plt.tight_layout()
    plt.savefig('Plots/elements.png')

elements(vink01, vink18)

# ------ Rotation ------
def rotation(model1, model2):

    # ------ Figure ------
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(9,6.5))
    fig.suptitle('Comparison Models', fontweight='bold')

    # ------ Plot 1 ------
    ax1.plot(model1.age, model1.vrot, label = 'Vink01', color = 'navy')
    ax1.plot(model2.age, model2.vrot, label = 'Vink18', color = 'darkred')
    ax1.legend(fancybox = True, scatterpoints = 1, labelspacing = 1, shadow=True)
    ax1.set_xlabel('Age [Myr]')
    ax1.set_ylabel('')
    ax1.set_title('Rotational Velocity')
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    # ------ Plot 2 ------
    ax2.plot(model1.age, model1.Jtot, label = 'Vink01', color = 'navy')
    ax2.plot(model2.age, model2.Jtot, label = 'Vink18', color = 'darkred')
    ax2.set_xlabel('Age [Myr]')
    ax2.set_ylabel('')
    ax2.set_title('Total Angular Momentum')
    ax2.legend(fancybox = True, scatterpoints = 1, labelspacing = 1, shadow=True)

    # ------ Plot 3 ------
    ax3.plot(model1.age, model1.Omega, label = 'Vink01', color = 'navy')
    ax3.plot(model2.age, model2.Omega, label = 'Vink18', color = 'darkred')
    ax3.legend(fancybox = True, scatterpoints = 1, labelspacing = 1, shadow=True)
    ax3.set_xlabel('Age [Myr]')
    ax3.set_ylabel('')
    ax3.set_title('Omega')

    # ------ Plot 4 ------
    ax4.plot(model1.age, model1.period, label = 'Vink01', color = 'navy')
    ax4.plot(model2.age, model2.period, label = 'Vink18', color = 'darkred')
    ax4.legend(fancybox = True, scatterpoints = 1, labelspacing = 1, shadow=True)
    ax4.set_xlabel('Age [Myr]')
    ax4.set_ylabel('')
    ax4.set_title('Period')
    
    plt.tight_layout()
    plt.savefig('Plots/rotation.png')

rotation(vink01, vink18)

# ------ Histograms ------
def histogram(model1, model2):

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

    # ------ Hist 1 ------
    ax1.bar(2, model1.M[len(model1.M)-1], 1, label='vink01', color = 'navy')
    ax1.bar(3, model2.M[len(model2.M)-1], 1, label='vink18', color = 'darkred')
    ax1.set_xlim(0,7)
    ax1.set_xticks([2,3])
    ax1.set_xticklabels(['', ''])
    ax1.set_ylabel('Mass M$_{\odot}$')
    ax1.set_title('Mass')
    ax1.legend()

    # ------ Hist 2 ------
    ax2.bar(2, model1.R[len(model1.R)-1], 1, label='vink01', color = 'navy')
    ax2.bar(3, model2.R[len(model2.R)-1], 1, label='vink18', color = 'darkred')
    ax2.set_xlim(0,7)
    ax2.set_xticks([2,3])
    ax2.set_xticklabels(['', ''])
    ax2.set_ylabel('Radius R$_{\odot}$')
    ax2.set_title('Radius')
    ax2.legend()

    # ------ Hist 3 ------
    ax3.bar(2, model1.Teff[len(model1.Teff)-1], 1, label='vink01', color = 'navy')
    ax3.bar(3, model2.Teff[len(model2.Teff)-1], 1, label='vink18', color = 'darkred')
    ax3.set_xlim(0,7)
    ax3.set_xticks([2,3])
    ax3.set_xticklabels(['', ''])
    ax3.set_ylabel('Teff')
    ax3.set_title('Effective Temperature')
    ax3.legend()

    # ------ Hist 4 ------
    ax4.bar(2, model1.logL[len(model1.logL)-1], 1, label='vink01', color = 'navy')
    ax4.bar(3, model2.logL[len(model2.logL)-1], 1, label='vink18', color = 'darkred')
    ax4.set_xlim(0,7)
    ax4.set_xticks([2,3])
    ax4.set_xticklabels(['', ''])
    ax4.set_ylabel('LogL')
    ax4.set_title('Luminosity')
    ax4.legend()

    fig.tight_layout()
    plt.savefig('Plots/histogram.png')

histogram(vink01, vink18)

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
        variable1 = model1.surfh1
        variable2 = model2.surfh1

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
    plt.savefig('Plots/difference.png')

difplot(vink01,vink18)