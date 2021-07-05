# script that contains data import for other scripts (all 180 simulations)

from classData import Data
from classStructure import Structure

# ------ Select Data ------
    
datafolder = 'Z014Om2'

# -----------------------------------------------------------------------------------

# Vink 01
avink01_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/out.data')
avink01_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/30/LOGS/out.data')
avink01_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/40/LOGS/out.data')
avink01_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/50/LOGS/out.data')
avink01_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/60/LOGS/out.data')

# Vink 18
avink18_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/20/LOGS/out.data')
avink18_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/30/LOGS/out.data')
avink18_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/40/LOGS/out.data')
avink18_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/50/LOGS/out.data')
avink18_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/60/LOGS/out.data')

# Leuven
aleuven_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/20/LOGS/out.data')
aleuven_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/30/LOGS/out.data')
aleuven_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/40/LOGS/out.data')
aleuven_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/50/LOGS/out.data')
aleuven_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/60/LOGS/out.data')

# Krticka
akrticka_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/20/LOGS/out.data')
akrticka_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/30/LOGS/out.data')
akrticka_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/40/LOGS/out.data')
akrticka_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/50/LOGS/out.data')
akrticka_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/60/LOGS/out.data')

# -----------------------------------------------------------------------------------

datafolder = 'Z014Om6'

# Vink 01
bvink01_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/out.data')
bvink01_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/30/LOGS/out.data')
bvink01_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/40/LOGS/out.data')
bvink01_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/50/LOGS/out.data')
bvink01_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/60/LOGS/out.data')

# Vink 18
bvink18_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/20/LOGS/out.data')
bvink18_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/30/LOGS/out.data')
bvink18_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/40/LOGS/out.data')
bvink18_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/50/LOGS/out.data')
bvink18_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/60/LOGS/out.data')

# Leuven
bleuven_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/20/LOGS/out.data')
bleuven_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/30/LOGS/out.data')
bleuven_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/40/LOGS/out.data')
bleuven_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/50/LOGS/out.data')
bleuven_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/60/LOGS/out.data')

# Krticka
bkrticka_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/20/LOGS/out.data')
bkrticka_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/30/LOGS/out.data')
bkrticka_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/40/LOGS/out.data')
bkrticka_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/50/LOGS/out.data')
bkrticka_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/60/LOGS/out.data')

# -----------------------------------------------------------------------------------

datafolder = 'Z002Om2'

# Vink 01
cvink01_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/out.data')
cvink01_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/30/LOGS/out.data')
cvink01_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/40/LOGS/out.data')
cvink01_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/50/LOGS/out.data')
cvink01_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/60/LOGS/out.data')

# Vink 18
cvink18_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/20/LOGS/out.data')
cvink18_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/30/LOGS/out.data')
cvink18_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/40/LOGS/out.data')
cvink18_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/50/LOGS/out.data')
cvink18_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/60/LOGS/out.data')

# Leuven
cleuven_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/20/LOGS/out.data')
cleuven_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/30/LOGS/out.data')
cleuven_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/40/LOGS/out.data')
cleuven_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/50/LOGS/out.data')
cleuven_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/60/LOGS/out.data')

# Krticka
ckrticka_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/20/LOGS/out.data')
ckrticka_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/30/LOGS/out.data')
ckrticka_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/40/LOGS/out.data')
ckrticka_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/50/LOGS/out.data')
ckrticka_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/60/LOGS/out.data')

# -----------------------------------------------------------------------------------

datafolder = 'Z007Om2'

# Vink 01
dvink01_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/out.data')
dvink01_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/30/LOGS/out.data')
dvink01_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/40/LOGS/out.data')
dvink01_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/50/LOGS/out.data')
dvink01_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/60/LOGS/out.data')

# Vink 18
dvink18_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/20/LOGS/out.data')
dvink18_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/30/LOGS/out.data')
dvink18_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/40/LOGS/out.data')
dvink18_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/50/LOGS/out.data')
dvink18_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/60/LOGS/out.data')

# Leuven
dleuven_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/20/LOGS/out.data')
dleuven_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/30/LOGS/out.data')
dleuven_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/40/LOGS/out.data')
dleuven_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/50/LOGS/out.data')
dleuven_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/60/LOGS/out.data')

# Krticka
dkrticka_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/20/LOGS/out.data')
dkrticka_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/30/LOGS/out.data')
dkrticka_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/40/LOGS/out.data')
dkrticka_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/50/LOGS/out.data')
dkrticka_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/60/LOGS/out.data')

# -----------------------------------------------------------------------------------

datafolder = 'Z002Om6'

# Vink 01
evink01_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/out.data')
evink01_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/30/LOGS/out.data')
evink01_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/40/LOGS/out.data')
evink01_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/50/LOGS/out.data')
evink01_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/60/LOGS/out.data')

# Vink 18
evink18_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/20/LOGS/out.data')
evink18_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/30/LOGS/out.data')
evink18_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/40/LOGS/out.data')
evink18_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/50/LOGS/out.data')
evink18_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/60/LOGS/out.data')

# Leuven
eleuven_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/20/LOGS/out.data')
eleuven_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/30/LOGS/out.data')
eleuven_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/40/LOGS/out.data')
eleuven_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/50/LOGS/out.data')
eleuven_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/60/LOGS/out.data')

# Krticka
ekrticka_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/20/LOGS/out.data')
ekrticka_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/30/LOGS/out.data')
ekrticka_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/40/LOGS/out.data')
ekrticka_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/50/LOGS/out.data')
ekrticka_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/60/LOGS/out.data')

# -----------------------------------------------------------------------------------

datafolder = 'Z007Om6'

# Vink 01
fvink01_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/out.data')
fvink01_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/30/LOGS/out.data')
fvink01_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/40/LOGS/out.data')
fvink01_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/50/LOGS/out.data')
fvink01_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/60/LOGS/out.data')

# Vink 18
fvink18_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/20/LOGS/out.data')
fvink18_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/30/LOGS/out.data')
fvink18_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/40/LOGS/out.data')
fvink18_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/50/LOGS/out.data')
fvink18_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/60/LOGS/out.data')

# Leuven
fleuven_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/20/LOGS/out.data')
fleuven_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/30/LOGS/out.data')
fleuven_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/40/LOGS/out.data')
fleuven_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/50/LOGS/out.data')
fleuven_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/60/LOGS/out.data')

# Krticka
fkrticka_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/20/LOGS/out.data')
fkrticka_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/30/LOGS/out.data')
fkrticka_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/40/LOGS/out.data')
fkrticka_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/50/LOGS/out.data')
fkrticka_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/60/LOGS/out.data')

# -----------------------------------------------------------------------------------

datafolder = 'Z014Om4'

# Vink 01
gvink01_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/out.data')
gvink01_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/30/LOGS/out.data')
gvink01_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/40/LOGS/out.data')
gvink01_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/50/LOGS/out.data')
gvink01_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/60/LOGS/out.data')

# Vink 18
gvink18_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/20/LOGS/out.data')
gvink18_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/30/LOGS/out.data')
gvink18_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/40/LOGS/out.data')
gvink18_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/50/LOGS/out.data')
gvink18_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/60/LOGS/out.data')

# Leuven
gleuven_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/20/LOGS/out.data')
gleuven_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/30/LOGS/out.data')
gleuven_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/40/LOGS/out.data')
gleuven_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/50/LOGS/out.data')
gleuven_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/60/LOGS/out.data')

# Krticka
gkrticka_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/20/LOGS/out.data')
gkrticka_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/30/LOGS/out.data')
gkrticka_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/40/LOGS/out.data')
gkrticka_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/50/LOGS/out.data')
gkrticka_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/60/LOGS/out.data')

# -----------------------------------------------------------------------------------

datafolder = 'Z007Om4'

# Vink 01
hvink01_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/out.data')
hvink01_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/30/LOGS/out.data')
hvink01_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/40/LOGS/out.data')
hvink01_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/50/LOGS/out.data')
hvink01_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/60/LOGS/out.data')

# Vink 18
hvink18_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/20/LOGS/out.data')
hvink18_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/30/LOGS/out.data')
hvink18_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/40/LOGS/out.data')
hvink18_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/50/LOGS/out.data')
hvink18_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/60/LOGS/out.data')

# Leuven
hleuven_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/20/LOGS/out.data')
hleuven_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/30/LOGS/out.data')
hleuven_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/40/LOGS/out.data')
hleuven_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/50/LOGS/out.data')
hleuven_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/60/LOGS/out.data')

# Krticka
hkrticka_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/20/LOGS/out.data')
hkrticka_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/30/LOGS/out.data')
hkrticka_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/40/LOGS/out.data')
hkrticka_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/50/LOGS/out.data')
hkrticka_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/60/LOGS/out.data')

# -----------------------------------------------------------------------------------

datafolder = 'Z002Om4'

# Vink 01
ivink01_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/out.data')
ivink01_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/30/LOGS/out.data')
ivink01_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/40/LOGS/out.data')
ivink01_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/50/LOGS/out.data')
ivink01_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/60/LOGS/out.data')

# Vink 18
ivink18_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/20/LOGS/out.data')
ivink18_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/30/LOGS/out.data')
ivink18_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/40/LOGS/out.data')
ivink18_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/50/LOGS/out.data')
ivink18_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/60/LOGS/out.data')

# Leuven
ileuven_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/20/LOGS/out.data')
ileuven_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/30/LOGS/out.data')
ileuven_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/40/LOGS/out.data')
ileuven_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/50/LOGS/out.data')
ileuven_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/60/LOGS/out.data')

# Krticka
ikrticka_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/20/LOGS/out.data')
ikrticka_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/30/LOGS/out.data')
ikrticka_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/40/LOGS/out.data')
ikrticka_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/50/LOGS/out.data')
ikrticka_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/60/LOGS/out.data')