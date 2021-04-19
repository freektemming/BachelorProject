# Script that tests

from classData import Data
from classStructure import Structure
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np

# ------ Models ------
vink01 = Data('../Data/40M_Vink01_out.data')
vink18 = Data('../Data/40M_Vink18_out.data')
zams = Structure('../Data/prof_ZAMS.data')

import matplotlib.pyplot as plt
from scipy import interpolate

def interpol(model1, model2):
    
    x1 = model1.age
    y1 = model1.Teff
    f1 = interpolate.interp1d(x1, y1)

    xnew1 = model1.age
    ynew1 = f1(xnew1)   # use interpolation function returned by `interp1d`


    x2 = model2.age
    y2 = model2.Teff
    f2 = interpolate.interp1d(x2, y2)

    xnew2 = model2.age
    ynew2 = f2(xnew2)   # use interpolation function returned by `interp1d`

    print(len(model1.age))
    print(len(xnew1))
    print(len(model2.age))
    print(len(xnew2))
    plt.plot(xnew1, ynew1, 'o')
    plt.plot(xnew2, ynew2, 'o')
    plt.show()

interpol(vink01, vink18)