# read data and test

from ClassData import Data
#from plotset import *
import matplotlib.pyplot as plt

import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np

vink01 = Data('../Data/40M_Vink01_out.data')
vink18 = Data('../Data/40M_Vink18_out.data')

def simulation(model1, model2):

    xlist = []
    ylist = []
    xlist2 = []
    ylist2 = []

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
            plt.legend()
        plt.ion()
        plt.draw()
        plt.pause(0.0000001)
        #plt.close()

#simulation(vink01,vink18)

def circles(model1,model2):

    for i in range(0,len(model1.age),20):

        circle1 = plt.Circle((1600, 1800), model1.R[i], alpha=0.2, lw=3, color = 'red', edgecolor='r', label = 'Model 1')
        circle2 = plt.Circle((4600, 1800), model2.R[i], alpha=0.2, lw=3, color = 'darkred', edgecolor='r', label = 'Model 2')

        fig, ax = plt.subplots() 
        ax.set_xlim(0,6200)
        ax.set_ylim(0,4000)
        ax.set_ylabel('Distance R$_{\odot}$')
        ax.set_xlabel('Distance R$_{\odot}$')
        ax.set_title('Compare Radius of 2 Models')

        ax.add_patch(circle1)
        ax.add_patch(circle2)

        plt.text(4800,3200, f'Age: {round(model1.age[i],2)} [M/y]')
        plt.legend(loc = 'upper right')

        #plt.show()

        plt.draw()
        plt.pause(0.0000001)
        plt.close()
        #print(i)


    #fig.savefig('Plots/plotcircles.png')

circles(vink01, vink18)