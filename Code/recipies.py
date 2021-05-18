# Script that makes multiple HRD plots

from data import *
from plots import *
from plotstyles import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np

# limit: True for main sequense
lim = False

# ------ plot normal HRD 1 Model All Masses------
def recipe(model1, model2, model3, model4, model5, number, ms):

    # plot name of model in legend
    if number == '1':
        model = 'Vink 01 Model'
    if number == '2':
        model = 'Vink 18 Model'
    if number == '3':
        model = 'Leuven Model'
    if number == '4':
        model = 'Krticka Model'

    lim1 = len(model1.age)

    # ------ Set Plot Style ------
    default_style()
    fig, ax, colormap = HRD(model)

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

    if number == '1':   
        for i in range(len(model1.age[0:lim1])):
            if model1.usewvink01[i] == 1:
                vinkx.append(model1.Teff[i])
                vinky.append(model1.logL[i])
                vinkc.append(model1.usewvink01)
            else:
                novinkx.append(model1.Teff[i])
                novinky.append(model1.logL[i])
                novinkc.append(model1.usewvink01)
    if number == '2':   
        for i in range(len(model1.age[0:lim1])):
            if model1.usewvink18[i] == 1:
                vinkx.append(model1.Teff[i])
                vinky.append(model1.logL[i])
                vinkc.append(model1.usewvink01)
            else:
                novinkx.append(model1.Teff[i])
                novinky.append(model1.logL[i])
                novinkc.append(model1.usewvink01)
    if number == '3':   
        for i in range(len(model1.age[0:lim1])):
            if model1.usewleuven[i] == 1:
                vinkx.append(model1.Teff[i])
                vinky.append(model1.logL[i])
                vinkc.append(model1.usewvink01)
            else:
                novinkx.append(model1.Teff[i])
                novinky.append(model1.logL[i])
                novinkc.append(model1.usewvink01)
    if number == '4':   
        for i in range(len(model1.age[0:lim1])):
            if model1.usewkrticka[i] == 1:
                vinkx.append(model1.Teff[i])
                vinky.append(model1.logL[i])
                vinkc.append(model1.usewvink01)
            else:
                novinkx.append(model1.Teff[i])
                novinky.append(model1.logL[i])
                novinkc.append(model1.usewvink01)


    ax.plot(vinkx, vinky, lw = 1, color = 'black', label = model)
    ax.plot(novinkx, novinky, lw = 1, color = 'red', label = 'Other Model')

    # ============ Model 2 =========== 

    vinkx.clear()
    vinky.clear()
    vinkc.clear()
    novinkx.clear()
    novinky.clear()
    novinkc.clear()
    
    if number == '1':   
        for i in range(len(model2.age[0:lim1])):
            if model2.usewvink01[i] == 1:
                vinkx.append(model2.Teff[i])
                vinky.append(model2.logL[i])
                vinkc.append(model2.usewvink01)
            else:
                novinkx.append(model2.Teff[i])
                novinky.append(model2.logL[i])
                novinkc.append(model2.usewvink01)
    if number == '2':   
        for i in range(len(model2.age[0:lim1])):
            if model2.usewvink18[i] == 1:
                vinkx.append(model2.Teff[i])
                vinky.append(model2.logL[i])
                vinkc.append(model2.usewvink01)
            else:
                novinkx.append(model2.Teff[i])
                novinky.append(model2.logL[i])
                novinkc.append(model2.usewvink01)
    if number == '3':   
        for i in range(len(model2.age[0:lim1])):
            if model2.usewleuven[i] == 1:
                vinkx.append(model2.Teff[i])
                vinky.append(model2.logL[i])
                vinkc.append(model2.usewvink01)
            else:
                novinkx.append(model2.Teff[i])
                novinky.append(model2.logL[i])
                novinkc.append(model2.usewvink01)
    if number == '4':   
        for i in range(len(model2.age[0:lim1])):
            if model2.usewkrticka[i] == 1:
                vinkx.append(model2.Teff[i])
                vinky.append(model2.logL[i])
                vinkc.append(model2.usewvink01)
            else:
                novinkx.append(model2.Teff[i])
                novinky.append(model2.logL[i])
                novinkc.append(model2.usewvink01)

    ax.plot(vinkx, vinky, lw = 1, color = 'black')
    ax.plot(novinkx, novinky, lw = 1, color = 'red')

     # ============ Model 3 =========== 

    vinkx.clear()
    vinky.clear()
    vinkc.clear()
    novinkx.clear()
    novinky.clear()
    novinkc.clear()
    
    if number == '1':   
        for i in range(len(model3.age[0:lim1])):
            if model3.usewvink01[i] == 1:
                vinkx.append(model3.Teff[i])
                vinky.append(model3.logL[i])
                vinkc.append(model3.usewvink01)
            else:
                novinkx.append(model3.Teff[i])
                novinky.append(model3.logL[i])
                novinkc.append(model3.usewvink01)
    if number == '2':   
        for i in range(len(model3.age[0:lim1])):
            if model3.usewvink18[i] == 1:
                vinkx.append(model3.Teff[i])
                vinky.append(model3.logL[i])
                vinkc.append(model3.usewvink01)
            else:
                novinkx.append(model3.Teff[i])
                novinky.append(model3.logL[i])
                novinkc.append(model3.usewvink01)
    if number == '3':   
        for i in range(len(model3.age[0:lim1])):
            if model3.usewleuven[i] == 1:
                vinkx.append(model3.Teff[i])
                vinky.append(model3.logL[i])
                vinkc.append(model3.usewvink01)
            else:
                novinkx.append(model3.Teff[i])
                novinky.append(model3.logL[i])
                novinkc.append(model3.usewvink01)
    if number == '4':   
        for i in range(len(model3.age[0:lim1])):
            if model3.usewkrticka[i] == 1:
                vinkx.append(model3.Teff[i])
                vinky.append(model3.logL[i])
                vinkc.append(model3.usewvink01)
            else:
                novinkx.append(model3.Teff[i])
                novinky.append(model3.logL[i])
                novinkc.append(model3.usewvink01)


    ax.plot(vinkx, vinky, lw = 1, color = 'black')
    ax.plot(novinkx, novinky, lw = 1, color = 'red')

     # ============ Model 4 =========== 

    vinkx.clear()
    vinky.clear()
    vinkc.clear()
    novinkx.clear()
    novinky.clear()
    novinkc.clear()
    
    if number == '1':   
        for i in range(len(model4.age[0:lim1])):
            if model4.usewvink01[i] == 1:
                vinkx.append(model4.Teff[i])
                vinky.append(model4.logL[i])
                vinkc.append(model4.usewvink01)
            else:
                novinkx.append(model4.Teff[i])
                novinky.append(model4.logL[i])
                novinkc.append(model4.usewvink01)
    if number == '2':   
        for i in range(len(model4.age[0:lim1])):
            if model4.usewvink18[i] == 1:
                vinkx.append(model4.Teff[i])
                vinky.append(model4.logL[i])
                vinkc.append(model4.usewvink01)
            else:
                novinkx.append(model4.Teff[i])
                novinky.append(model4.logL[i])
                novinkc.append(model4.usewvink01)
    if number == '3':   
        for i in range(len(model4.age[0:lim1])):
            if model4.usewleuven[i] == 1:
                vinkx.append(model4.Teff[i])
                vinky.append(model4.logL[i])
                vinkc.append(model4.usewvink01)
            else:
                novinkx.append(model4.Teff[i])
                novinky.append(model4.logL[i])
                novinkc.append(model4.usewvink01)
    if number == '4':   
        for i in range(len(model4.age[0:lim1])):
            if model4.usewkrticka[i] == 1:
                vinkx.append(model4.Teff[i])
                vinky.append(model4.logL[i])
                vinkc.append(model4.usewvink01)
            else:
                novinkx.append(model4.Teff[i])
                novinky.append(model4.logL[i])
                novinkc.append(model4.usewvink01)


    ax.plot(vinkx, vinky, lw = 1, color = 'black')
    ax.plot(novinkx, novinky, lw = 1, color = 'red')

     # ============ Model 5 =========== 

    vinkx.clear()
    vinky.clear()
    vinkc.clear()
    novinkx.clear()
    novinky.clear()
    novinkc.clear()
    
    if number == '1':   
        for i in range(len(model5.age[0:lim1])):
            if model5.usewvink01[i] == 1:
                vinkx.append(model5.Teff[i])
                vinky.append(model5.logL[i])
                vinkc.append(model5.usewvink01)
            else:
                novinkx.append(model5.Teff[i])
                novinky.append(model5.logL[i])
                novinkc.append(model5.usewvink01)
    if number == '2':   
        for i in range(len(model5.age[0:lim1])):
            if model5.usewvink18[i] == 1:
                vinkx.append(model5.Teff[i])
                vinky.append(model5.logL[i])
                vinkc.append(model5.usewvink01)
            else:
                novinkx.append(model5.Teff[i])
                novinky.append(model5.logL[i])
                novinkc.append(model5.usewvink01)
    if number == '3':   
        for i in range(len(model5.age[0:lim1])):
            if model5.usewleuven[i] == 1:
                vinkx.append(model5.Teff[i])
                vinky.append(model5.logL[i])
                vinkc.append(model5.usewvink01)
            else:
                novinkx.append(model5.Teff[i])
                novinky.append(model5.logL[i])
                novinkc.append(model5.usewvink01)
    if number == '4':   
        for i in range(len(model5.age[0:lim1])):
            if model5.usewkrticka[i] == 1:
                vinkx.append(model5.Teff[i])
                vinky.append(model5.logL[i])
                vinkc.append(model5.usewvink01)
            else:
                novinkx.append(model5.Teff[i])
                novinky.append(model5.logL[i])
                novinkc.append(model5.usewvink01)


    ax.plot(vinkx, vinky, lw = 1, color = 'black')
    ax.plot(novinkx, novinky, lw = 1, color = 'red')
    
    ax.legend(shadow = False, edgecolor = 'k')

    # ------ Text ------
    ax.text(model1.Teff[0] + 5, model1.logL[0], '20M$_{\odot}$', fontweight = 'bold')
    ax.text(model2.Teff[0] + 5, model2.logL[0], '30M$_{\odot}$', fontweight = 'bold')
    ax.text(model3.Teff[0] + 5, model3.logL[0], '40M$_{\odot}$', fontweight = 'bold')
    ax.text(model4.Teff[0] + 5, model4.logL[0], '50M$_{\odot}$', fontweight = 'bold')
    ax.text(model5.Teff[0] + 5, model5.logL[0], '60M$_{\odot}$', fontweight = 'bold')
    
    fig.tight_layout()
    plt.savefig(f'Plots/Recipies/HRD{number}.png')
    #plt.show()

recipe(vink01_20, vink01_30, vink01_40, vink01_50, vink01_60, '1', ms=lim)
recipe(vink18_20, vink18_30, vink18_40, vink18_50, vink18_60, '2', ms=lim)
recipe(leuven_20, leuven_30, leuven_40, leuven_50, leuven_60, '3', ms=lim)
recipe(krticka_20, krticka_30, krticka_40, krticka_50, krticka_60, '4', ms=lim)
