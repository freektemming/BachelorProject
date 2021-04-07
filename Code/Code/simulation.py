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

    for i in range(0,len(model1.model),10):

        xlist.append(model1.model[i])
        ylist.append(model1.R[i])
        xlist2.append(model2.model[i])
        ylist2.append(model2.R[i])
            
        plt.plot(xlist, ylist, label='line 1', linewidth=2, color = 'navy')
        plt.plot(xlist2, ylist2, label='line 1', linewidth=2, color = 'darkred')
        plt.xlim(0,4000)
        plt.ylim(0,1500)
        plt.ion()
        plt.draw()
        plt.pause(0.0000001)

#simulation(vink01,vink18)
