import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import sys
import math
import scipy as scipy
import scipy.integrate as scii
from pylab import *
import uncertainties as u
from uncertainties import unumpy
from uncertainties import ufloat
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
from matplotlib.collections import LineCollection
from matplotlib.ticker import AutoMinorLocator
#----------------------------------------------
#### SETUP PLOTS HERE +++++++++++++++++++++++++++++++++++++++++++++++
rc('axes', linewidth=10)
###rc('ticks', which = 'minor', width = 3, length = 12)

# HRD
fig1, ax1 = plt.subplots(1,1, figsize=(20,20))
ax1.set_xlim(51,2)
#ax.set_xlim(4.75,4.0)
#ax1.set_ylim(4.15,4.99)
ax1.set_xlabel('T$_{\mathrm{eff}}$ [kK]', size=60 )
#ax.set_ylabel('$\mathrm{\log (L/L_{\odot}) }$', size=44)
ax1.set_ylabel('log (L / L$_{\odot}$)', size=60 )
#ax.set_ylabel('$\mathrm{\log N/N_{ini}}$', size=44)
ax1.tick_params(labelsize=54, width = 12, length = 22)
ax1.xaxis.set_major_locator(ticker.MultipleLocator(5)) # 2))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.yaxis.set_minor_locator(AutoMinorLocator(5))
ax1.tick_params(which = 'minor', width = 3, length = 12)
#ax1.set_title('secondary diagnostic', fontsize = 60, fontweight='bold', pad = 60)

# sHRD
fig11, ax11 = plt.subplots(1,1, figsize=(20,20))
ax11.set_xlim(51,2)
#ax.set_xlim(4.75,4.0)
#ax11.set_ylim(4.15,4.85)
ax11.set_xlabel('T$_{\mathrm{eff}}$ [kK]', size=60 )
#ax.set_ylabel('$\mathrm{\log (L/L_{\odot}) }$', size=44)
ax11.set_ylabel('log $( T_{\mathrm{eff}}^{4}/g_{\mathrm{eff}}$ / $T_{\mathrm{eff, \odot}}^{4}/g_{\mathrm{eff, \odot}} ) $', size=60 )
#ax.set_ylabel('$\mathrm{\log N/N_{ini}}$', size=44)
ax11.tick_params(labelsize=54, width = 12, length = 22)
ax11.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax11.xaxis.set_minor_locator(AutoMinorLocator(5))
ax11.yaxis.set_minor_locator(AutoMinorLocator(5))
ax11.tick_params(which = 'minor', width = 3, length = 12)

# Kiel d.
fig111, ax111 = plt.subplots(1,1, figsize=(20,20))
ax111.set_xlim(51,2)
ax111.invert_yaxis()
#ax.set_xlim(4.75,4.0)
#ax111.set_ylim(4.4,2.9)
ax111.set_xlabel('T$_{\mathrm{eff}}$ [kK]', size=60 )
#ax.set_ylabel('$\mathrm{\log (L/L_{\odot}) }$', size=44)
ax111.set_ylabel('log g [cm s$^{-2}$]', size=60 )
#ax.set_ylabel('$\mathrm{\log N/N_{ini}}$', size=44)
ax111.tick_params(labelsize=54, width = 12, length = 22)
ax111.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax111.xaxis.set_minor_locator(AutoMinorLocator(5))
ax111.yaxis.set_minor_locator(AutoMinorLocator(5))
ax111.tick_params(which = 'minor', width = 3, length = 12)

# Hunter - P 
fig2, ax2 = plt.subplots(1,1, figsize=(20,20))
#ax3.set_xlim(-20,615)
ax2.set_ylim(7.5,9.3)
ax2.invert_xaxis()
ax2.set_xlabel('log P$_{rot}$ [d]',  size=60)
ax2.set_ylabel('log $[N/H] + 12$',  size=60)
ax2.tick_params(labelsize=54, width = 12, length = 22)
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
ax2.yaxis.set_minor_locator(AutoMinorLocator(4))
ax2.tick_params(which = 'minor', width = 3, length = 12)
#ax2.set_title('primary diagnostic', fontsize = 60, fontweight='bold', pad = 60)

# Hunter
fig3, ax3 = plt.subplots(1,1, figsize=(20,20))
ax3.set_xlim(-20,400)
ax3.set_ylim(7.5,9.3)
#ax8.invert_xaxis()
ax3.set_xlabel('$v_{\mathrm{eq}}$  [km s$^{-1}$]',  size=60)
ax3.set_ylabel('log $[N/H] + 12$',  size=60)
ax3.tick_params(labelsize=44, width = 9, length = 22)
ax3.xaxis.set_minor_locator(AutoMinorLocator(4))
ax3.yaxis.set_minor_locator(AutoMinorLocator(5))
ax3.tick_params(which = 'minor', width = 3, length = 12)
#ax3.set_title('primary diagnostic', fontsize = 60, fontweight='bold', pad = 60)

# Bp 
fig4, ax4 = plt.subplots(1,1, figsize=(20,20))
#ax4.set_xlim(4.4,3.2)
#ax4.set_ylim(-0.8,5.4)
### ax4.invert_xaxis()
ax4.set_xlabel('Age [Myr]', size=60)
#ax4.set_ylabel('log P$\mathbf{_{rot}}$ [d]', size=48)
ax4.set_ylabel('log $B_p$ [G]', size=60)
#:::ax4444 = ax4.twinx()   # mirror them
#:::ax4444.set_ylabel('R [$R_\odot$]', size=48, color = 'orange')
### ax4.set_ylabel('v sin $\mathbf{i}$  [km s$^\mathbf{{-1}}$]', size=48, fontweight = 'bold')
ax4.tick_params(labelsize=44, width = 9, length = 22)
ax4.xaxis.set_minor_locator(AutoMinorLocator(4))
ax4.yaxis.set_minor_locator(AutoMinorLocator(5))
ax4.tick_params(which = 'minor', width = 3, length = 12)
#:::ax4444.tick_params(labelsize=44, width = 9, length = 22, color = 'orange')
#ax444.xaxis.set_minor_locator(AutoMinorLocator(4))
#:::ax4444.yaxis.set_minor_locator(AutoMinorLocator(5))
#:::ax4444.tick_params(which = 'minor', width = 3, length = 12, color = 'orange')

# Prot 
fig44, ax44 = plt.subplots(1,1, figsize=(20,20))
#ax4.set_xlim(4.4,3.2)
#ax4.set_ylim(-0.8,5.4)
### ax4.invert_xaxis()
ax44.set_xlabel('Age [Myr]', size=60)
ax44.set_ylabel('log P$\mathbf{_{rot}}$ [d]', size=60)
ax444 = ax44.twinx()   # mirror them
#ax444.set_ylabel('v$_{eq}$ [km s$^\mathbf{{-1}}$]', size=48)
ax444.set_ylabel('$\Omega / \Omega_{crit}$', size=48, color = 'orange')

#ax4.set_ylabel('Bp [G]', size=48)
### ax4.set_ylabel('v sin $\mathbf{i}$  [km s$^\mathbf{{-1}}$]', size=48, fontweight = 'bold')
ax44.tick_params(labelsize=44, width = 9, length = 22)
ax44.xaxis.set_minor_locator(AutoMinorLocator(4))
ax44.yaxis.set_minor_locator(AutoMinorLocator(5))
ax44.tick_params(which = 'minor', width = 3, length = 12)
ax444.tick_params(labelsize=44, width = 9, length = 22, color = 'orange')
#ax444.xaxis.set_minor_locator(AutoMinorLocator(4))
ax444.yaxis.set_minor_locator(AutoMinorLocator(5))
ax444.tick_params(which = 'minor', width = 3, length = 12, color = 'orange')

# Omega
fig5, ax5 = plt.subplots(1,1, figsize=(20,20))
ax5.set_xlim(4.4,-0.2)
#ax4.set_ylim(-0.8,5.4)
### ax4.invert_xaxis()
ax5.set_xlabel('log g [cm s$^{-2}$]', size=60)
ax5.set_ylabel('log $\Omega$ [s$^{-1}]$', size=60)
### ax4.set_ylabel('v sin $\mathbf{i}$  [km s$^\mathbf{{-1}}$]', size=48, fontweight = 'bold')
ax5.tick_params(labelsize=44, width = 9, length = 22)
ax5.xaxis.set_minor_locator(AutoMinorLocator(4))
ax5.yaxis.set_minor_locator(AutoMinorLocator(5))
ax5.tick_params(which = 'minor', width = 3, length = 12)

fig6, ax6 = plt.subplots(1,1, figsize=(20,25))
#rc('axes', linewidth=2)
ax6.tick_params(labelsize=44, width = 9, length = 22)
ax6.xaxis.set_minor_locator(AutoMinorLocator(4))
ax6.yaxis.set_minor_locator(AutoMinorLocator(5))
ax6.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
ax6.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
ax6.tick_params(which = 'minor', width = 3, length = 12)
#plt.ylim(300,-0.5) # inverted
ax6.set_xlim(0.,2.)
ax6.set_ylim(-0.05,4.5)
ax6.set_xlabel('log (R$\mathbf{_A}$ / R$\mathbf{_\star}$)', size=48, fontweight = 'bold')
ax6.set_ylabel('log (R$\mathbf{_K}$ / R$\mathbf{_\star}$)', size=48, fontweight = 'bold')
ax6.invert_yaxis()

# Mdot
fig7, ax7 = plt.subplots(1,1, figsize=(20,20))
ax7.set_xlim(51, 2)
ax7.set_xlabel('T$_{\mathrm{eff}}$ [kK]', size=60)
ax7.set_ylabel('log $\dot{M}$ [M$_\odot$ yr$^{-1}$]', size=60)
### ax4.set_ylabel('v sin $\mathbf{i}$  [km s$^\mathbf{{-1}}$]', size=48, fontweight = 'bold')
ax7.tick_params(labelsize=44, width = 9, length = 22)
ax7.xaxis.set_minor_locator(AutoMinorLocator(4))
ax7.yaxis.set_minor_locator(AutoMinorLocator(5))
ax7.tick_params(which = 'minor', width = 3, length = 12)

# Abundance
fig77, ax77 = plt.subplots(1,1, figsize=(20,20))
ax77.set_ylim(-3.1,-2.2)
ax77.set_xlabel('Age [Myr]', size=60)
ax77.set_ylabel('log N/H mass fraction', size=60)
### ax4.set_ylabel('v sin $\mathbf{i}$  [km s$^\mathbf{{-1}}$]', size=48, fontweight = 'bold')
ax77.tick_params(labelsize=44, width = 9, length = 22)
ax77.xaxis.set_minor_locator(AutoMinorLocator(4))
ax77.yaxis.set_minor_locator(AutoMinorLocator(5))
ax77.tick_params(which = 'minor', width = 3, length = 12)

# Abundance
fig777, ax777 = plt.subplots(1,1, figsize=(20,20))
#ax777.set_ylim(-3.1,-2.2)
ax777.set_xlabel('Age [Myr]', size=60)
ax777.set_ylabel('He mass fraction', size=60)
### ax4.set_ylabel('v sin $\mathbf{i}$  [km s$^\mathbf{{-1}}$]', size=48, fontweight = 'bold')
ax777.tick_params(labelsize=44, width = 9, length = 22)
ax777.xaxis.set_minor_locator(AutoMinorLocator(4))
ax777.yaxis.set_minor_locator(AutoMinorLocator(5))
ax777.tick_params(which = 'minor', width = 3, length = 12)
