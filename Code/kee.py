# Script that tests
from classData import Data
from plots import *
from plotstyles import *

beasor1 = Data('../../BachelorProjectData/Data/TryMWkee/1/40/LOGS/out.data')
beasor2 = Data('../../BachelorProjectData/Data/TryMWkee/2/40/LOGS/out.data')
beasor3 = Data('../../BachelorProjectData/Data/TryMWkee/3/40/LOGS/out.data')
beasor4 = Data('../../BachelorProjectData/Data/TryMWkee/4/40/LOGS/out.data')
kee1 = Data('../../BachelorProjectData/Data/TryMWkee/5/40/LOGS/out.data')
kee2 = Data('../../BachelorProjectData/Data/TryMWkee/6/40/LOGS/out.data')
kee3 = Data('../../BachelorProjectData/Data/TryMWkee/7/40/LOGS/out.data')
kee4 = Data('../../BachelorProjectData/Data/TryMWkee/8/40/LOGS/out.data')


# ------ plot normal HRD 4 Models 1 Mass ------
def hrdmass(model1, model2, model3, model4, number, ms):

    # plot name of model in legend
    if number == '20':
        model = '20 M$_{\odot}$'
        mass = '20'
    if number == '30':
        model = '30 M$_{\odot}$'
        mass = '30'
    if number == '40':
        model = '40 M$_{\odot}$'
        mass = '40'
    if number == '50':
        model = '50 M$_{\odot}$'
        mass = '50'
    if number == '60':
        model = '60 M$_{\odot}$'
        mass = '60'

    if ms == True:
        # main sequence limit
        lim1 = model1.mainsequence()
        lim2 = model2.mainsequence()
        # lim3 = model3.mainsequence()
        # lim4 = model4.mainsequence()

        # age limit colorbar
        min1 = model1.get_min_bar()
        max1 = model1.get_age(lim1)
        limit = '_ms'
        folder = 'MainSequence'
    else:
        # full simulation
        lim1 = len(model1.age)
        lim2 = len(model2.age)
        lim3 = len(model3.age)
        lim4 = len(model4.age)
        
        start1 = model1.end()
        start2 = model2.end()
        start3 = model3.end()
        start4 = model4.end()

        # start1 = 0
        # start2 = 0
        # start3 = 0
        # start4 = 0

        # lim3 = model3.end()
        # lim4 = model4.end()

        min1 = model1.get_min_bar()
        max1 = model1.get_max_bar()
        limit = ''
        folder = 'FullSimulation'

    # ------ Set Plot Style ------
    default_style()
    fig, ax, colormap = HRD(model)

    # plot line
    ax.plot(model1.Teff[start1:lim1], model1.logL[start1:lim1], lw = 1, color = 'black', linestyle = 'solid', label = 'vink 01')
    ax.plot(model2.Teff[start2:lim2], model2.logL[start2:lim2], lw = 1, color = 'blue', linestyle = 'solid', label = 'vink 18')
    ax.plot(model3.Teff[start3:lim3], model3.logL[start3:lim3], lw = 1, color = 'green', linestyle = 'solid', label = 'Leuven')
    ax.plot(model4.Teff[start4:lim4], model4.logL[start4:lim4], lw = 1, color = 'pink', linestyle = 'solid', label = 'Krticka')
    
    # plot colors
    ims1 = ax.scatter(model1.Teff[start1:lim1], model1.logL[start1:lim1], c= model1.age[start1:lim1], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims2 = ax.scatter(model2.Teff[start2:lim2], model2.logL[start2:lim2], c= model2.age[start2:lim2], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims3 = ax.scatter(model3.Teff[start3:lim3], model3.logL[start3:lim3], c= model3.age[start3:lim3], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    ims4 = ax.scatter(model4.Teff[start4:lim4], model4.logL[start4:lim4], c= model4.age[start4:lim4], marker='o', edgecolors='none', s=100, cmap=colormap, vmin = min1, vmax = max1)
    
    cbar1 = fig.colorbar(ims1, ax = ax)
    cbar1.set_label('Age [Myr]')
    ax.legend(shadow = False, edgecolor = 'k')

    fig.tight_layout()
    plt.show()
    #plt.savefig(f'Plots/{datafolder}/HRDmass/{folder}/HRD{mass}{limit}.png', dpi=200)

# hrdmass(beasor1,beasor2,beasor3,beasor4,'40', False)
# hrdmass(kee1,kee2,kee3,kee4,'40', False)


# ======================================================================================

# ------ plot normal HRD 1 Model All Masses------
def recipe(model1, model2):

    lim1 = len(model1.age)
    lim2 = len(model2.age)

    # ------ Set Plot Style ------
    default_style()
    fig, (ax1, ax2), colormap = HRDRSG()

    # self.wvink01 = data[self.x:,88]
    # self.usewvink01 = data[self.x:,89]
    # self.wvink18 = data[self.x:,90]
    # self.usewvink18 = data[self.x:,91]
    # self.wleuven = data[self.x:,92]
    # self.usewleuven = data[self.x:,93]
    # self.wkrticka = data[self.x:,94]
    # self.usewkrticka= data[self.x:,95]
    # self.wbeasor = data[self.x:,96]
    # self.usewbeasor = data[self.x:,97]
    # self.wkee = data[self.x:,98]
    # self.usewkee = data[self.x:,99]
    # self.wsander =  data[self.x:,100]
    # self.usewsander = data[self.x:,101]

    # ============ Model 1 ===========

    vinkx = []
    vinky = []
    vinkc = []
    novinkx = []
    novinky = []
    novinkc = []
    recipe = []

 
    for i in range(len(model1.age[0:lim1])):
        if model1.usewvink01[i] == 1:
            vinkx.append(model1.Teff[i])
            vinky.append(model1.logL[i])
        else:
            novinkx.append(model1.Teff[i])
            novinky.append(model1.logL[i])

    #ax.plot(vinkx, vinky, lw = 1, color = 'black', label = 'Original Model')
    #ax.plot(novinkx, novinky, lw = 1, color = 'red', label = model)

    # ============ Model 2 =========== 

    vinkx.clear()
    vinky.clear()
    vinkc.clear()
    novinkx.clear()
    novinky.clear()
    novinkc.clear()
    
 
    for i in range(len(model2.age[0:lim1])):
        if model2.usewvink18[i] == 1:
            vinkx.append(model2.Teff[i])
            vinky.append(model2.logL[i])
        else:
            novinkx.append(model2.Teff[i])
            novinky.append(model2.logL[i])
   
    #ax.plot(vinkx, vinky, lw = 1, color = 'black')
    #ax.plot(novinkx, novinky, lw = 1, color = 'red')

     # ============ Model 3 =========== 

    vinkx.clear()
    vinky.clear()
    vinkc.clear()
    novinkx.clear()
    novinky.clear()
    novinkc.clear()
    
    for i in range(len(model1.age[0:lim1])):
        if model1.usewkrticka[i] == 1:
            vinkx.append(model1.Teff[i])
            vinky.append(model1.logL[i])
        else:
            novinkx.append(model1.Teff[i])
            novinky.append(model1.logL[i])

    #ax1.plot(vinkx, vinky, lw = 1, color = 'green', label='Krticka')
    ax1.plot(novinkx, novinky, lw = 1, color = 'black', label='Beasor')

     # ============ Model 4 =========== 

    vinkx.clear()
    vinky.clear()
    vinkc.clear()
    novinkx.clear()
    novinky.clear()
    novinkc.clear()
    
    
    for i in range(len(model2.age[0:lim2])):
        if model2.usewkrticka[i] == 1:
            vinkx.append(model2.Teff[i])
            vinky.append(model2.logL[i])
        else:
            novinkx.append(model2.Teff[i])
            novinky.append(model2.logL[i])

    ax1.plot(novinkx, novinky, lw = 1, color = 'red', label='Kee')
    #ax1.plot(vinkx, vinky, lw = 1, color = 'green')
    
    ax1.legend(shadow = False, edgecolor = 'k')

    # ----- SECOND PLOT ----------
    # full simulation
    lim1 = len(model1.age)
    lim2 = len(model2.age)
    start1 = model1.end()
    start2 = model2.end()

    # plot line
    ax2.plot(model1.age[start1:lim1], model1.logMdot[start1:lim1], lw = 1, color = 'black', label = 'Beasor')
    ax2.plot(model2.age[start2:lim2], model2.logMdot[start2:lim2], lw = 1, color = 'red', label = 'Kee')

    ax2.legend(shadow = False, edgecolor = 'k')

    # # ------ Text ------
    # ax.text(model1.Teff[0] + 5, model1.logL[0], '20M$_{\odot}$', fontweight = 'bold')
    # ax.text(model2.Teff[0] + 5, model2.logL[0], '30M$_{\odot}$', fontweight = 'bold')
    # ax.text(model3.Teff[0] + 5, model3.logL[0], '40M$_{\odot}$', fontweight = 'bold')
    # ax.text(model4.Teff[0] + 5, model4.logL[0], '50M$_{\odot}$', fontweight = 'bold')
    # ax.text(model5.Teff[0] + 5, model5.logL[0], '60M$_{\odot}$', fontweight = 'bold')
    
    fig.tight_layout()
    plt.savefig(f'Plots/RSG/BK4.png', dpi=200)
    #plt.show()

recipe(beasor4, kee4) # plot beasor and kee vs krticka (4)
#recipe(kee1,kee2,kee3,kee4, '2')


# ------ Plot multiple HRD 4 Models Main Sequence------
def masslosskee(model1, model2, ms):

    # limits
    if ms == True:
        # main sequence limit
        lim1 = model1.mainsequence()
        lim2 = model2.mainsequence()
        limit = '_ms'
    else:
        # full simulation
        lim1 = len(model1.age)
        lim2 = len(model1.age)

        limit = ''

    # ------ Set Plot Style ------
    default_style()
    fig, ax = plt.subplots(1,1)

    #ax.set_xlim(10,2)
    #ax.set_ylim(-8.7,-4.5)
    #ax.set_xlabel('T$_{\mathrm{eff}}$ [kK]')
    ax.set_xlabel('Time (Myr)')
    ax.set_ylabel('log M$_{\mathregular{dot}}$ [M$_{\odot}$ / yr]')
    ax.set_title('Mass Loss Rates Beasor and Kee')

    # ------ first plot ------
    # plot line
    ax.plot(model1.age[0:lim1], model1.logMdot[0:lim1], lw = 1, color = 'black', label = 'Beasor')
    ax.plot(model2.age[0:lim2], model2.logMdot[0:lim2], lw = 1, color = 'red', label = 'Kee')

    ax.legend(shadow = False, edgecolor = 'k')

    fig.tight_layout()
    #plt.savefig(f'Plots/Overview/Mdot-Teff/{omega}/{region}{limit}.png', dpi=200)
    plt.show()

#masslosskee(beasor4, kee4, ms=False)