# plotstyles 

import matplotlib.pyplot as plt
import matplotlib as mpl

def default_style():

    plt.style.use('default')
    plt.rc('axes', unicode_minus=False) # using font minus sine
    mpl.rcParams['font.family'] = "Tw Cen MT"
    mpl.rcParams['patch.linewidth'] = .8
    plt.rcParams['xtick.major.size'] = 3.0
    plt.rcParams['xtick.minor.size'] = 3.0
    plt.rcParams['xtick.top'] = True
    plt.rcParams['ytick.major.size'] = 3.0
    plt.rcParams['ytick.minor.size'] = 3.0
    plt.rcParams['ytick.right'] = True
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    #plt.minorticks_on()

def histogramstyle():

    plt.style.use('default')
    plt.rc('axes', unicode_minus=False) # using font minus sine
    mpl.rcParams['font.family'] = "Tw Cen MT"
    mpl.rcParams['patch.linewidth'] = .8
    plt.rcParams['xtick.major.size'] = 3.0
    plt.rcParams['xtick.minor.size'] = 3.0
    plt.rcParams['xtick.top'] = False
    plt.rcParams['ytick.major.size'] = 3.0
    plt.rcParams['ytick.minor.size'] = 3.0
    plt.rcParams['ytick.right'] = False
    plt.rcParams['xtick.direction'] = 'out'
    plt.rcParams['ytick.direction'] = 'out'
    #plt.minorticks_on()



def science_style():

    plt.style.use('default')
    plt.rcParams["axes.labelweight"] = "light"
    plt.rcParams["font.weight"] = "light"
    mpl.rcParams['patch.linewidth'] = .8
    plt.rcParams['text.usetex'] = True # using latex font
    plt.rcParams['font.size'] = 15
    plt.rcParams['legend.fontsize'] = 18
    plt.rcParams['xtick.major.size'] = 5.0
    plt.rcParams['xtick.minor.size'] = 3.0
    plt.rcParams['ytick.major.size'] = 5.0
    plt.rcParams['ytick.minor.size'] = 3.0
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    #plt.minorticks_on()