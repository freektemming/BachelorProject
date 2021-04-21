# Script that contains setup for plots

from data import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np

def HRD():

    colormap = plt.cm.plasma
    fig, ax = plt.subplots(1,1)

    ax.set_xlim(51,2)
    ax.set_xlabel('T$_{\mathregular{eff}}$ [kK]')
    ax.set_ylabel('log (L / L$_{\odot}$)')
    ax.set_title('Both Models')

    return fig, ax, colormap

def subHRD():

    colormap = plt.cm.plasma
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('HRD 2 Models')

    ax1.set_xlim(51,2)
    ax1.set_xlabel('T$_{\mathrm{eff}}$ [kK]')
    ax1.set_ylabel('log (L / L$_{\odot}$)')
    ax1.set_title('Vink01')

    ax2.set_xlim(51,2)
    ax2.set_xlabel('T$_{\mathrm{eff}}$ [kK]')
    ax2.set_ylabel('log (L / L$_{\odot}$)')
    ax2.set_title('Vink18')

    return fig, ax1, ax2, colormap

def vescape():
    
    colormap = plt.cm.plasma
    fig, ax = plt.subplots(1,1)

    ax.set_xlabel('V$_{\mathregular{esc}}$')
    ax.set_ylabel('M$_{\mathregular{dot}}$')
    ax.set_title('V$_{\mathregular{esc}}$ vs M$_{\mathregular{dot}}$')

    return fig, ax, colormap

def LvsMdot():

    colormap = plt.cm.plasma
    fig, ax = plt.subplots(1,1)
    
    ax.set_xlabel('log (L / L$_{\odot}$)')
    ax.set_ylabel('M$_{\mathregular{dot}}$')
    ax.set_title('L vs M$_{\mathregular{dot}}$')

    return fig, ax, colormap

def hunterNH():

    colormap = plt.cm.plasma
    fig, ax = plt.subplots(1,1)
    
    ax.set_xlabel('V$_{\mathregular{rot}}$')
    ax.set_ylabel('log (N / H) + 12')
    ax.set_title('Hunter')

    return fig, ax, colormap

def hunter():

    colormap = plt.cm.plasma
    fig, ax = plt.subplots(1,1)
    
    ax.set_xlabel('V$_{\mathregular{rot}}$')
    ax.set_ylabel('N/N$_{\star}$')
    ax.set_title('Hunter')

    return fig, ax, colormap
    
def kippenhahn():
    
    colormap = plt.cm.cividis_r
    colormap = plt.cm.cubehelix
    fig, ax = plt.subplots(1,1)


    ax.set_ylabel('m / M$_{\star}$')
    ax.set_title('Kippenhahn Diagram Mass')

    #ax.set_xticks([0.0648,3.12,4.76])
    #ax.set_xticklabels(['Zams', 'Mid','Tams'])
    ax.set_xlabel('Time [Myr]')

    return fig, ax, colormap
