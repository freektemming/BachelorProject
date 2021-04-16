# Script to make simulation

from classData import Data
#from plotset import *
import matplotlib.pyplot as plt

import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import math

# ------ Models ------
vink01 = Data('../Data/40M_Vink01_out.data')
vink18 = Data('../Data/40M_Vink18_out.data')

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

# ------ Plot 2 stars ------
def circles(model1,model2):

    xlist = []
    ylist = []
    xlist2 = []
    ylist2 = []

    ylist3 = []
    ylist4 = []
    ylist5 = []
    ylist6 = []

    length = len(model1.age) - 1200
    counter = 0
    for i in range(0,length,8):
        
        # after H burning fase: make simulation faster (skip steps)
        counter += 1
        if model1.age[i] > 4.6:
            if counter % 2 == 0:
                continue

        # ------ Plot 1 ------
        colormap = plt.cm.plasma
        colorX = length * [1600]
        colorY = length * [4000]
        colorX2 = length * [4600]
        colorY2 = length * [4000]

        #circle1 = plt.Circle((1600, 3000), model1.R[i], alpha=0.2, lw=3, color = 'red', edgecolor='r', label = 'Model 1')
        #circle2 = plt.Circle((4600, 3000), model2.R[i], alpha=0.2, lw=3, color = 'red', edgecolor='r', label = 'Model 2')

        fig, (ax1, ax2) = plt.subplots(2, figsize=(9,6.5)) 
        ax1.set_xlim(0,6200)
        ax1.set_ylim(0,6200)
        ax1.set_ylabel('Radius R$_{\odot}$')
        ax1.set_xlabel('Radius R$_{\odot}$')
        ax1.set_title('Radius of 2 Models', fontweight = 'bold')

        #ax.add_patch(circle1)
        #ax.add_patch(circle2)

        # plot colors
        ims1 = ax1.scatter(colorX[i], colorY[i], c= model1.age[i], marker='o', edgecolors='none', s=int(model1.R[i]**1.3), cmap=colormap, vmin = 4.5, vmax = model1.get_max_bar())
        ims2 = ax1.scatter(colorX2[i], colorY2[i], c= model2.age[i], marker='o', edgecolors='none', s=int(model2.R[i]**1.3), cmap=colormap, vmin = 4.5, vmax = model2.get_max_bar())
        cbar1 = fig.colorbar(ims1, ax = ax1)
        cbar1.set_label('Age [Myr]')

        ax1.text(1000,1500, f'Age: {round(model1.age[i],2)} [My]')
        ax1.text(4000,1500, f'Age: {round(model2.age[i],2)} [My]')

        ax1.text(1000,1000, f'Mass: {round(model1.M[i],2)} M_sun')
        ax1.text(4000,1000, f'Mass: {round(model2.M[i],2)} M_sun')


        # ax1.text(1000,500, f'Core H: {round(model1.HC[i] / max(model1.HC) * 100,2)} %')
        # ax1.text(4000,500, f'Core H: {round(model2.HC[i] / max(model2.HC) * 100,2)} %')

        # ------ Plot 2 ------

        xlist.append(model1.age[i])
        ylist.append(model1.HC[i])
        xlist2.append(model2.age[i])
        ylist2.append(model2.HC[i])

        ylist3.append(model1.HeC[i])
        ylist4.append(model2.HeC[i])

        ylist5.append(model1.CC[i])
        ylist6.append(model2.CC[i])
            
        ax2.plot(xlist, ylist, label='Vink 01', linewidth=2, color = 'navy')
        ax2.plot(xlist2, ylist2, label='Vink 18', linewidth=2, color = 'darkred')
        ax2.plot(xlist, ylist3, linewidth=2, color = 'navy')
        ax2.plot(xlist2, ylist4, linewidth=2, color = 'darkred')
        ax2.plot(xlist, ylist5, linewidth=2, color = 'navy')
        ax2.plot(xlist2, ylist6, linewidth=2, color = 'darkred')

        ax2.set_xlim(0,6)
        ax2.set_ylim(0,1)
        ax2.set_ylabel('m / M$_{\odot}$')
        ax2.set_xlabel('Age [My]')
        ax2.set_title('Core Elements', fontweight = 'bold')

        ax2.text(0.05,0.75, 'Hydrogen')
        ax2.text(0.05,0.35, 'Helium')
        if model1.CC[i] > 0.16:
            ax2.text(4.3,0.15, 'Carbon ->')

        plt.legend(shadow = False, edgecolor = 'k')

        fig.tight_layout()
        plt.draw()
        plt.pause(0.00001)
        plt.close()
        #print(i)

circles(vink01, vink18)