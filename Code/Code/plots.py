# Script that contains setup for plots

from classData import Data
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np

# ------ Models ------
vink01 = Data('../Data/40M_Vink01_out.data')
vink18 = Data('../Data/40M_Vink18_out.data')

def vescape():
    print('hoi')
    
    colormap = plt.cm.plasma
    fig, ax = plt.subplots(1,1, figsize=(9,6.5))

    ax.set_xlabel('V$_{\mathrm{esc}}$')
    ax.set_ylabel('M$_{\mathrm{dot}}$')
    ax.set_title('V$_{\mathrm{esc}}$ vs M$_{\mathrm{dot}}$',fontweight='bold')

def LvsMdot():

    colormap = plt.cm.plasma
    fig, ax = plt.subplots(1,1, figsize=(9,6.5))
    
    ax.set_xlabel('log (L / L$_{\odot}$)')
    ax.set_ylabel('M$_{\mathrm{dot}}$')
    ax.set_title('L vs Mdot',fontweight='bold')

def hunterNH():

    colormap = plt.cm.plasma
    fig, ax = plt.subplots(1,1, figsize=(9,6.5))
    
    ax.set_xlabel('V$_{\mathrm{rot}}$')
    ax.set_ylabel('log (N / H) + 12')
    ax.set_title('Hunter',fontweight='bold')

def hunter():

    colormap = plt.cm.plasma
    fig, ax = plt.subplots(1,1, figsize=(9,6.5))
    
    ax.set_xlabel('V$_{\mathrm{rot}}$')
    ax.set_ylabel('N/N$_{\star}$')
    ax.set_title('Hunter',fontweight='bold')
    
