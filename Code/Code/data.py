# script that contains data import for other scripts

from classData import Data
from classStructure import Structure

# ------ Models ------
vink01 = Data('../Data/40M_Vink01_out.data')
vink18 = Data('../Data/40M_Vink18_out.data')

# ------ Structure ------
zams = Structure('../Data/prof_ZAMS.data')
mid = Structure('../Data/prof_midMS.data')
tams = Structure('../Data/prof_tams.data')