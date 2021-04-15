# Script that tests

from classData import Data
from classStructure import Structure
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np

# ------ Models ------
#vink01 = Data('../Data/40M_Vink01_out.data')
#vink18 = Data('../Data/40M_Vink18_out.data')
zams = Structure('../Data/prof_ZAMS.data')

plt.plot(zams.normR, zams.mlt)
plt.show()

