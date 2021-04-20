# Script to make simulation

from classData import Data
#from plotset import *
import matplotlib.pyplot as plt

import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import math
from scipy import interpolate
import os
import imageio

# ------ Models ------
vink01 = Data('../Data/40M_Vink01_out.data')
vink18 = Data('../Data/40M_Vink18_out.data')

# ------ Interpolate model to same age list so steps are equal ------
# model = model from which variables are checked
# varX = x variable to wich it has to be interpolated
# varY = y variable that you want to plot
def interpol(model, varX, varY):
    
    x = model.age
    y = varY
    f = interpolate.interp1d(x, y, fill_value='extrapolate')

    xnew = varX
    ynew = f(xnew)

    return xnew, ynew


# ------ Plot 2 stars ------
def circles(model1,model2):

    # ------ Files for GIF ------
    files = []

    # ------ Get Interpolation ------
    # model 1
    xInterpol1 = interpol(model1, model1.age, model1.Teff)[0]
    yInterpol11 = interpol(model1, model1.age, model1.Teff)[1]
    yInterpol12 = interpol(model1, model1.age, model1.R)[1]
    yInterpol13 = interpol(model1, model1.age, model1.M)[1]
    yInterpol14 = interpol(model1, model1.age, model1.HC)[1]
    yInterpol15 = interpol(model1, model1.age, model1.HeC)[1]
    yInterpol16 = interpol(model1, model1.age, model1.CC)[1]

    # model 2
    xInterpol2 = interpol(model2, model1.age, model2.Teff)[0]
    yInterpol21 = interpol(model2, model1.age, model2.Teff)[1]
    yInterpol22 = interpol(model2, model1.age, model2.R)[1]
    yInterpol23 = interpol(model2, model1.age, model2.M)[1]
    yInterpol24 = interpol(model2, model1.age, model2.HC)[1]
    yInterpol25 = interpol(model2, model1.age, model2.HeC)[1]
    yInterpol26 = interpol(model2, model1.age, model2.CC)[1]

    # ------ Get Lists For Second Plot ------
    xlist = []
    ylist = []
    xlist2 = []
    ylist2 = []

    ylist3 = []
    ylist4 = []
    ylist5 = []
    ylist6 = []


    # ------ Loop Over Data ------
    length = len(xInterpol1)
    counter = 0
    for i in range(0,length,5):
        
        # after H burning fase: make simulation faster (skip steps)
        counter += 1
        if model1.age[i] > 4.5:
            if counter % 2 == 0:
                continue

        # ------ Plot 1 ------
        colormap = plt.cm.plasma_r

        # coordinates where circels are located in diagram
        colorX = length * [1600]
        colorY = length * [4000]
        colorX2 = length * [4600]
        colorY2 = length * [4000]

        #circle1 = plt.Circle((1600, 3000), model1.R[i], alpha=0.2, lw=3, color = 'red', edgecolor='r', label = 'Model 1')
        #circle2 = plt.Circle((4600, 3000), model2.R[i], alpha=0.2, lw=3, color = 'red', edgecolor='r', label = 'Model 2')

        # set figure
        fig, (ax1, ax2) = plt.subplots(2, figsize=(9,6.5)) 
        ax1.set_xlim(0,6200)
        ax1.set_ylim(0,6200)
        ax1.set_ylabel('Radius R$_{\odot}$')
        ax1.set_xlabel('Radius R$_{\odot}$')
        ax1.set_title('2 Models 40M$_{\odot}$', fontweight = 'bold')

        #ax.add_patch(circle1)
        #ax.add_patch(circle2)

        # plot colors
        ims1 = ax1.scatter(colorX[i], colorY[i], c= yInterpol11[i], marker='o', edgecolors='none', s=int(yInterpol12[i]**1.3), cmap=colormap, vmin = 0, vmax = 50)
        ims2 = ax1.scatter(colorX2[i], colorY2[i], c= yInterpol21[i], marker='o', edgecolors='none', s=int(yInterpol22[i]**1.3), cmap=colormap, vmin = 0, vmax = 50)
        cbar1 = fig.colorbar(ims1, ax = ax1)
        cbar1.set_label('Teff [kK]')

        # plot text
        ax1.text(1000,1500, f'Age: {round(xInterpol1[i],2)} [My]')
        ax1.text(4000,1500, f'Age: {round(xInterpol2[i],2)} [My]')
        ax1.text(1000,1000, f'Mass: {round(yInterpol13[i],2)} [M_sun]')
        ax1.text(4000,1000, f'Mass: {round(yInterpol23[i],2)} [M_sun]')
        ax1.text(1000,500, f'Teff: {round(yInterpol11[i],2)} [kK]')
        ax1.text(4000,500, f'Teff: {round(yInterpol21[i],2)} [kK]')

        # ------ Plot 2 ------
        xlist.append(xInterpol1[i])
        ylist.append(yInterpol14[i])
        xlist2.append(xInterpol2[i])
        ylist2.append(yInterpol24[i])

        ylist3.append(yInterpol15[i])
        ylist4.append(yInterpol25[i])

        ylist5.append(yInterpol16[i])
        ylist6.append(yInterpol26[i])

        # plot lines    
        ax2.plot(xlist, ylist, label='Vink 01', linewidth=2, color = 'navy')
        ax2.plot(xlist2, ylist2, label='Vink 18', linewidth=2, color = 'darkred')
        ax2.plot(xlist, ylist3, linewidth=2, color = 'navy')
        ax2.plot(xlist2, ylist4, linewidth=2, color = 'darkred')
        ax2.plot(xlist, ylist5, linewidth=2, color = 'navy')
        ax2.plot(xlist2, ylist6, linewidth=2, color = 'darkred')

        # set axis
        ax2.set_xlim(0,6)
        ax2.set_ylim(0,1)
        ax2.set_ylabel('m / M$_{\star}$')
        ax2.set_xlabel('Age [My]')
        ax2.set_title('Core Elements', fontweight = 'bold')

        # set text
        ax2.text(0.05,0.75, 'Hydrogen')
        ax2.text(0.05,0.35, 'Helium')
        if model1.CC[i] > 0.16:
            ax2.text(4.3,0.15, 'Carbon ->')

        # ------ Show ------
        plt.legend(shadow = False, edgecolor = 'k')
        fig.tight_layout()
        plt.draw()
        plt.pause(0.00001)
        plt.close()

        # ------ GIF ------
        filename = f'Plots/GIF/{i}.png'
        files.append(filename)
        plt.savefig(f'{filename}')
        
        plt.close()
        print(xInterpol1[i])

    # ------ Make GIF From Saved Files ------
    # with imageio.get_writer('Plots/simulation.gif', mode='I') as writer:
    #     for filename in files:
    #         image = imageio.imread(filename)
    #         writer.append_data(image)


circles(vink01, vink18)


def simulation(model1, model2):

    xlist = []
    ylist = []
    xlist2 = []
    ylist2 = []

    # ------ Loop over model steps ------
    for i in range(0,len(model1.model),15):

        xlist.append(model1.model[i])
        ylist.append(model1.R[i])
        xlist2.append(model2.model[i])
        ylist2.append(model2.R[i])
            
        plt.plot(xlist, ylist, label='Model 1', linewidth=2, color = 'navy')
        plt.plot(xlist2, ylist2, label='Model 2', linewidth=2, color = 'darkred')
        plt.xlim(0,4000)
        plt.ylim(0,1500)
        plt.ylabel('Radius R$_{\odot}$')
        plt.xlabel('Age [M/y]')
        plt.title('Compare Radius of 2 Models')
        if i == 0:
            plt.legend(shadow = False, edgecolor = 'k')
        plt.ion()
        plt.draw()
        plt.pause(0.0000001)
        #plt.close()

#simulation(vink01,vink18)
