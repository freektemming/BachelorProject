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

simulation(vink01,vink18)

# ------ Plot 2 stars ------
def circles(model1,model2):

    length = len(model1.age)
    for i in range(0,length,20):

        colormap = plt.cm.plasma
        colorX = length * [1600]
        colorY = length * [4000]
        colorX2 = length * [4600]
        colorY2 = length * [4000]

        #circle1 = plt.Circle((1600, 3000), model1.R[i], alpha=0.2, lw=3, color = 'red', edgecolor='r', label = 'Model 1')
        #circle2 = plt.Circle((4600, 3000), model2.R[i], alpha=0.2, lw=3, color = 'red', edgecolor='r', label = 'Model 2')

        fig, ax = plt.subplots() 
        ax.set_xlim(0,6200)
        ax.set_ylim(0,6200)
        ax.set_ylabel('Distance R$_{\odot}$')
        ax.set_xlabel('Distance R$_{\odot}$')
        ax.set_title('Compare Radius of 2 Models')

        #ax.add_patch(circle1)
        #ax.add_patch(circle2)

        # plot colors
        ims1 = ax.scatter(colorX[i], colorY[i], c= model1.age[i], marker='o', edgecolors='none', s=int(model1.R[i]**1.3), cmap=colormap, vmin = 4.5, vmax = model1.get_max_bar())
        ims2 = ax.scatter(colorX2[i], colorY2[i], c= model2.age[i], marker='o', edgecolors='none', s=int(model2.R[i]**1.3), cmap=colormap, vmin = 4.5, vmax = model2.get_max_bar())
        cbar1 = fig.colorbar(ims1, ax = ax)
        cbar1.set_label('Age [Myr]')

        plt.text(1000,1500, f'Age: {round(model1.age[i],2)} [My]')
        plt.text(4000,1500, f'Age: {round(model2.age[i],2)} [My]')

        plt.text(1000,1000, f'Mass: {round(model1.M[i],2)} M_sun')
        plt.text(4000,1000, f'Mass: {round(model2.M[i],2)} M_sun')


        plt.text(1000,500, f'Core H: {round(model1.HC[i] / max(model1.HC) * 100,2)} %')
        plt.text(4000,500, f'Core H: {round(model2.HC[i] / max(model2.HC) * 100,2)} %')
        #plt.legend(shadow = False, edgecolor = 'k', loc = 'upper right')

        #plt.show()

        plt.draw()
        plt.pause(0.1)
        plt.close()
        #print(i)

circles(vink01, vink18)