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
rc('axes', linewidth=2)

# HRD
fig1, ax1 = plt.subplots(1,1, figsize=(9,6))
ax1.set_xlim(51,2)
ax1.set_xlabel('T$_{\mathrm{eff}}$ [kK]')
ax1.set_ylabel('log (L / L$_{\odot}$)')
ax1.set_title('HRD 40 solar masses',fontweight='bold')

