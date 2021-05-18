# script that contains data import for other scripts

from classData import Data
from classStructure import Structure

# ------ Select Data ------
    
datafolder = '4x4'
#datafolder = 'OmegaCrit06'
#datafolder = 'Z002Om2'
#datafolder = 'Z007Om2'

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

# ------ Structure ------

# # Vink 01
# vink01_20z = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/prof_ZAMS.data')
# vink01_20m = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/prof_midMS.data')
# vink01_20t = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/prof_TAMS.data')
# vink01_30z = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/30/LOGS/prof_ZAMS.data')
# vink01_30m = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/30/LOGS/prof_midMS.data')
# vink01_30t = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/30/LOGS/prof_TAMS.data')
# vink01_40z = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/40/LOGS/prof_ZAMS.data')
# vink01_40m = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/40/LOGS/prof_midMS.data')
# vink01_40t = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/40/LOGS/prof_TAMS.data')
# vink01_50z = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/50/LOGS/prof_ZAMS.data')
# vink01_50m = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/50/LOGS/prof_midMS.data')
# vink01_50t = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/50/LOGS/prof_TAMS.data')
# vink01_60z = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/60/LOGS/prof_ZAMS.data')
# vink01_60m = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/60/LOGS/prof_midMS.data')
# vink01_60t = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/60/LOGS/prof_TAMS.data')

# # Vink 18
# vink18_20z = Structure(f'../../BachelorProjectData/Data/{datafolder}/2/20/LOGS/prof_ZAMS.data')
# vink18_20m = Structure(f'../../BachelorProjectData/Data/{datafolder}/2/20/LOGS/prof_midMS.data')
# vink18_20t = Structure(f'../../BachelorProjectData/Data/{datafolder}/2/20/LOGS/prof_TAMS.data')
# vink18_30z = Structure(f'../../BachelorProjectData/Data/{datafolder}/2/30/LOGS/prof_ZAMS.data')
# vink18_30m = Structure(f'../../BachelorProjectData/Data/{datafolder}/2/30/LOGS/prof_midMS.data')
# vink18_30t = Structure(f'../../BachelorProjectData/Data/{datafolder}/2/30/LOGS/prof_TAMS.data')
# vink18_40z = Structure(f'../../BachelorProjectData/Data/{datafolder}/2/40/LOGS/prof_ZAMS.data')
# vink18_40m = Structure(f'../../BachelorProjectData/Data/{datafolder}/2/40/LOGS/prof_midMS.data')
# vink18_40t = Structure(f'../../BachelorProjectData/Data/{datafolder}/2/40/LOGS/prof_TAMS.data')
# vink18_50z = Structure(f'../../BachelorProjectData/Data/{datafolder}/2/50/LOGS/prof_ZAMS.data')
# vink18_50m = Structure(f'../../BachelorProjectData/Data/{datafolder}/2/50/LOGS/prof_midMS.data')
# vink18_50t = Structure(f'../../BachelorProjectData/Data/{datafolder}/2/50/LOGS/prof_TAMS.data')
# vink18_60z = Structure(f'../../BachelorProjectData/Data/{datafolder}/2/60/LOGS/prof_ZAMS.data')
# vink18_60m = Structure(f'../../BachelorProjectData/Data/{datafolder}/2/60/LOGS/prof_midMS.data')
# vink18_60t = Structure(f'../../BachelorProjectData/Data/{datafolder}/2/60/LOGS/prof_TAMS.data')

# # Leuven
# leuven_20z = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/prof_ZAMS.data')
# leuven_20m = Structure(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/prof_midMS.data')
# leuven_20t = Structure(f'../../BachelorProjectData/Data/{datafolder}/3/20/LOGS/prof_TAMS.data')
# leuven_30z = Structure(f'../../BachelorProjectData/Data/{datafolder}/3/30/LOGS/prof_ZAMS.data')
# leuven_30m = Structure(f'../../BachelorProjectData/Data/{datafolder}/3/30/LOGS/prof_midMS.data')
# leuven_30t = Structure(f'../../BachelorProjectData/Data/{datafolder}/3/30/LOGS/prof_TAMS.data')
# leuven_40z = Structure(f'../../BachelorProjectData/Data/{datafolder}/3/40/LOGS/prof_ZAMS.data')
# leuven_40m = Structure(f'../../BachelorProjectData/Data/{datafolder}/3/40/LOGS/prof_midMS.data')
# leuven_40t = Structure(f'../../BachelorProjectData/Data/{datafolder}/3/40/LOGS/prof_TAMS.data')
# leuven_50z = Structure(f'../../BachelorProjectData/Data/{datafolder}/3/50/LOGS/prof_ZAMS.data')
# leuven_50m = Structure(f'../../BachelorProjectData/Data/{datafolder}/3/50/LOGS/prof_midMS.data')
# leuven_50t = Structure(f'../../BachelorProjectData/Data/{datafolder}/3/50/LOGS/prof_TAMS.data')
# leuven_60z = Structure(f'../../BachelorProjectData/Data/{datafolder}/3/60/LOGS/prof_ZAMS.data')
# leuven_60m = Structure(f'../../BachelorProjectData/Data/{datafolder}/3/60/LOGS/prof_midMS.data')
# leuven_60t = Structure(f'../../BachelorProjectData/Data/{datafolder}/3/60/LOGS/prof_TAMS.data')

# # Krticka
# krticka_20z = Structure(f'../../BachelorProjectData/Data/{datafolder}/4/20/LOGS/prof_ZAMS.data')
# krticka_20m = Structure(f'../../BachelorProjectData/Data/{datafolder}/4/20/LOGS/prof_midMS.data')
# krticka_20t = Structure(f'../../BachelorProjectData/Data/{datafolder}/4/20/LOGS/prof_TAMS.data')
# krticka_30z = Structure(f'../../BachelorProjectData/Data/{datafolder}/4/30/LOGS/prof_ZAMS.data')
# krticka_30m = Structure(f'../../BachelorProjectData/Data/{datafolder}/4/30/LOGS/prof_midMS.data')
# krticka_30t = Structure(f'../../BachelorProjectData/Data/{datafolder}/4/30/LOGS/prof_TAMS.data')
# krticka_40z = Structure(f'../../BachelorProjectData/Data/{datafolder}/4/40/LOGS/prof_ZAMS.data')
# krticka_40m = Structure(f'../../BachelorProjectData/Data/{datafolder}/4/40/LOGS/prof_midMS.data')
# krticka_40t = Structure(f'../../BachelorProjectData/Data/{datafolder}/4/40/LOGS/prof_TAMS.data')
# krticka_50z = Structure(f'../../BachelorProjectData/Data/{datafolder}/4/50/LOGS/prof_ZAMS.data')
# krticka_50m = Structure(f'../../BachelorProjectData/Data/{datafolder}/4/50/LOGS/prof_midMS.data')
# krticka_50t = Structure(f'../../BachelorProjectData/Data/{datafolder}/4/50/LOGS/prof_TAMS.data')
# krticka_60z = Structure(f'../../BachelorProjectData/Data/{datafolder}/4/60/LOGS/prof_ZAMS.data')
# krticka_60m = Structure(f'../../BachelorProjectData/Data/{datafolder}/4/60/LOGS/prof_midMS.data')
# krticka_60t = Structure(f'../../BachelorProjectData/Data/{datafolder}/4/60/LOGS/prof_TAMS.data')

# -----------------------------------------------------------------------------------

datafolder = 'OmegaCrit06'

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