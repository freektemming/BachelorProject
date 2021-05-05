# Script that contains setup for plots

from data import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np

def HRD(model):

    colormap = plt.cm.plasma
    fig, ax = plt.subplots(1,1)

    ax.set_xlim(60,2)
    ax.set_xlabel('T$_{\mathregular{eff}}$ [kK]')
    ax.set_ylabel('log (L / L$_{\odot}$)')
    ax.set_title(f'Herzsprung Russell Diagram: {model}')

    return fig, ax, colormap

def subHRD():

    colormap = plt.cm.plasma
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)
    fig.suptitle('Herzsprung Russell Diagram')

    ax1.set_xlim(60,2)
    ax1.set_xlabel('T$_{\mathrm{eff}}$ [kK]')
    ax1.set_ylabel('log (L / L$_{\odot}$)')
    ax1.set_title('Vink 01')

    ax2.set_xlim(60,2)
    ax2.set_xlabel('T$_{\mathrm{eff}}$ [kK]')
    ax2.set_ylabel('log (L / L$_{\odot}$)')
    ax2.set_title('Vink 18')

    ax3.set_xlim(60,2)
    ax3.set_xlabel('T$_{\mathrm{eff}}$ [kK]')
    ax3.set_ylabel('log (L / L$_{\odot}$)')
    ax3.set_title('Leuven')

    ax4.set_xlim(60,2)
    ax4.set_xlabel('T$_{\mathrm{eff}}$ [kK]')
    ax4.set_ylabel('log (L / L$_{\odot}$)')
    ax4.set_title('Krticka')

    return fig, ((ax1, ax2), (ax3, ax4)), colormap

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

def hunterNH(mass):

    colormap = plt.cm.plasma_r
    fig, ax = plt.subplots(1,1)
    
    ax.set_xlabel('V$_{\mathregular{rot}}$ [km / s]')
    ax.set_ylabel('log (N / H) + 12')
    ax.set_title(f'Hunter Diagram of {mass} Solar Mass Stars')

    return fig, ax, colormap

def hunter(mass):

    colormap = plt.cm.plasma_r
    fig, ax = plt.subplots(1,1)
    
    ax.set_xlabel('V$_{\mathregular{rot}}$ [km / s]')
    ax.set_ylabel('log (N/N$_{\star}$)')
    ax.set_title(f'Surface Nitrogen of {mass} Solar Mass Stars')

    return fig, ax, colormap
    
def kippenhahn(number, mass):
    
    colormap = plt.cm.cividis_r
    colormap = plt.cm.cubehelix
    fig, ax = plt.subplots(1,1)

    if number == '1':
        model = 'Vink 01 Model'
    if number == '2':
        model = 'Vink 18 Model'
    if number == '3':
        model = 'Leuven Model'
    if number == '4':
        model = 'Krticka Model'

    ax.set_ylabel('m / M$_{\star}$')
    ax.set_title(f'Mass Fractions {model}: {mass}M''$_{\odot}$')

    #ax.set_xticks([0.0648,3.12,4.76])
    #ax.set_xticklabels(['Zams', 'Mid','Tams'])
    ax.set_xlabel('Time [Myr]')

    return fig, ax, colormap

def HHe():

    colormap = plt.cm.plasma
    fig, ax = plt.subplots(1,1)

    ax.set_xlabel('Core Hydrogen')
    ax.set_ylabel('Core Helium')
    ax.set_title('Hydrogen and Helium')

    return fig, ax, colormap

def HeC():

    colormap = plt.cm.plasma
    fig, ax = plt.subplots(1,1)

    ax.set_xlabel('Core Helium')
    ax.set_ylabel('Core Carbon')
    ax.set_title('Helium and Carbon')

    return fig, ax, colormap

def vrotmdot(plottype, model):
    
    colormap = plt.cm.plasma_r
    fig, ax = plt.subplots(1,1)

    if plottype == 'Mdot':
        ax.set_xlim(55,2)
        ax.set_xlabel('T$_{\mathregular{eff}}$ [kK]')
        ax.set_ylabel('log ($\dot{M}$) [M$_{\odot}$ / yr]')
        ax.set_title(f'Mass Loss: {model} Stars')

    if plottype == 'Vrot':
        ax.set_xlim(55,2)
        ax.set_xlabel('T$_{\mathregular{eff}}$ [kK]')
        ax.set_ylabel('V$_{\mathregular{rot}}$ [km / s]')
        ax.set_title(f'Rotational Velocity: {model} Stars')

    return fig, ax, colormap

def Core(model):

    fig, ax = plt.subplots(1,1)
    colormap = plt.cm.cividis

    ax.set_ylabel('log (m / M$_{\star}$)')
    ax.set_xlabel('Time [Myr]')
    ax.set_title(f'Core Mass of {model} Stars')

    return fig, ax, colormap

def mid(model):

    fig, ax = plt.subplots(1,1)

    ax.set_ylabel('log (m / M$_{\star}$)')
    ax.set_xlabel('m / M$_{\star}$')
    ax.set_title(f'Structure of MID MS {model} Star')

    return fig, ax