# script that contains data import for other scripts

from classData import Data
from classStructure import Structure

# ------ Models ------
vink01 = Data('../Data/40M_Vink01_out.data')
vink18 = Data('../Data/40M_Vink18_out.data')

# Vink 01
vink01_20 = Data('../Data/4x4/1/20/LOGS/out.data')
vink01_30 = Data('../Data/4x4/1/30/LOGS/out.data')
vink01_40 = Data('../Data/4x4/1/40/LOGS/out.data')
vink01_50 = Data('../Data/4x4/1/50/LOGS/out.data')
vink01_60 = Data('../Data/4x4/1/60/LOGS/out.data')

# Vink 18
vink18_20 = Data('../Data/4x4/1/20/LOGS/out.data')
vink18_30 = Data('../Data/4x4/1/30/LOGS/out.data')
vink18_40 = Data('../Data/4x4/1/40/LOGS/out.data')
vink18_50 = Data('../Data/4x4/1/50/LOGS/out.data')
vink18_60 = Data('../Data/4x4/1/60/LOGS/out.data')

# Vink 18
vink18_20 = Data('../Data/4x4/2/20/LOGS/out.data')
vink18_30 = Data('../Data/4x4/2/30/LOGS/out.data')
vink18_40 = Data('../Data/4x4/2/40/LOGS/out.data')
vink18_50 = Data('../Data/4x4/2/50/LOGS/out.data')
vink18_60 = Data('../Data/4x4/2/60/LOGS/out.data')

# Leuven
leuven_20 = Data('../Data/4x4/3/20/LOGS/out.data')
leuven_30 = Data('../Data/4x4/3/30/LOGS/out.data')
leuven_40 = Data('../Data/4x4/3/40/LOGS/out.data')
leuven_50 = Data('../Data/4x4/3/50/LOGS/out.data')
leuven_60 = Data('../Data/4x4/3/60/LOGS/out.data')

# Krticka
krticka_20 = Data('../Data/4x4/4/20/LOGS/out.data')
krticka_30 = Data('../Data/4x4/4/30/LOGS/out.data')
krticka_40 = Data('../Data/4x4/4/40/LOGS/out.data')
krticka_50 = Data('../Data/4x4/4/50/LOGS/out.data')
krticka_60 = Data('../Data/4x4/4/60/LOGS/out.data')

# ------ Structure ------
zams = Structure('../Data/prof_ZAMS.data')
mid = Structure('../Data/prof_midMS.data')
tams = Structure('../Data/prof_tams.data')

# Vink 01
vink01_20z = Structure('../Data/4x4/1/20/LOGS/prof_ZAMS.data')
vink01_20m = Structure('../Data/4x4/1/20/LOGS/prof_midMS.data')
vink01_20t = Structure('../Data/4x4/1/20/LOGS/prof_TAMS.data')
vink01_30z = Structure('../Data/4x4/1/30/LOGS/prof_ZAMS.data')
vink01_30m = Structure('../Data/4x4/1/30/LOGS/prof_midMS.data')
vink01_30t = Structure('../Data/4x4/1/30/LOGS/prof_TAMS.data')
vink01_40z = Structure('../Data/4x4/1/40/LOGS/prof_ZAMS.data')
vink01_40m = Structure('../Data/4x4/1/40/LOGS/prof_midMS.data')
vink01_40t = Structure('../Data/4x4/1/40/LOGS/prof_TAMS.data')
vink01_50z = Structure('../Data/4x4/1/50/LOGS/prof_ZAMS.data')
vink01_50m = Structure('../Data/4x4/1/50/LOGS/prof_midMS.data')
vink01_50t = Structure('../Data/4x4/1/50/LOGS/prof_TAMS.data')
vink01_60z = Structure('../Data/4x4/1/60/LOGS/prof_ZAMS.data')
vink01_60m = Structure('../Data/4x4/1/60/LOGS/prof_midMS.data')
vink01_60t = Structure('../Data/4x4/1/60/LOGS/prof_TAMS.data')

# Vink 18
vink18_20z = Structure('../Data/4x4/2/20/LOGS/prof_ZAMS.data')
vink18_20m = Structure('../Data/4x4/2/20/LOGS/prof_midMS.data')
vink18_20t = Structure('../Data/4x4/2/20/LOGS/prof_TAMS.data')
vink18_30z = Structure('../Data/4x4/2/30/LOGS/prof_ZAMS.data')
vink18_30m = Structure('../Data/4x4/2/30/LOGS/prof_midMS.data')
vink18_30t = Structure('../Data/4x4/2/30/LOGS/prof_TAMS.data')
vink18_40z = Structure('../Data/4x4/2/40/LOGS/prof_ZAMS.data')
vink18_40m = Structure('../Data/4x4/2/40/LOGS/prof_midMS.data')
vink18_40t = Structure('../Data/4x4/2/40/LOGS/prof_TAMS.data')
vink18_50z = Structure('../Data/4x4/2/50/LOGS/prof_ZAMS.data')
vink18_50m = Structure('../Data/4x4/2/50/LOGS/prof_midMS.data')
vink18_50t = Structure('../Data/4x4/2/50/LOGS/prof_TAMS.data')
vink18_60z = Structure('../Data/4x4/2/60/LOGS/prof_ZAMS.data')
vink18_60m = Structure('../Data/4x4/2/60/LOGS/prof_midMS.data')
vink18_60t = Structure('../Data/4x4/2/60/LOGS/prof_TAMS.data')

# Leuven
leuven_20z = Structure('../Data/4x4/1/20/LOGS/prof_ZAMS.data')
leuven_20m = Structure('../Data/4x4/1/20/LOGS/prof_midMS.data')
leuven_20t = Structure('../Data/4x4/3/20/LOGS/prof_TAMS.data')
leuven_30z = Structure('../Data/4x4/3/30/LOGS/prof_ZAMS.data')
leuven_30m = Structure('../Data/4x4/3/30/LOGS/prof_midMS.data')
leuven_30t = Structure('../Data/4x4/3/30/LOGS/prof_TAMS.data')
leuven_40z = Structure('../Data/4x4/3/40/LOGS/prof_ZAMS.data')
leuven_40m = Structure('../Data/4x4/3/40/LOGS/prof_midMS.data')
leuven_40t = Structure('../Data/4x4/3/40/LOGS/prof_TAMS.data')
leuven_50z = Structure('../Data/4x4/3/50/LOGS/prof_ZAMS.data')
leuven_50m = Structure('../Data/4x4/3/50/LOGS/prof_midMS.data')
leuven_50t = Structure('../Data/4x4/3/50/LOGS/prof_TAMS.data')
leuven_60z = Structure('../Data/4x4/3/60/LOGS/prof_ZAMS.data')
leuven_60m = Structure('../Data/4x4/3/60/LOGS/prof_midMS.data')
leuven_60t = Structure('../Data/4x4/3/60/LOGS/prof_TAMS.data')

# Krticka
krticka_20z = Structure('../Data/4x4/4/20/LOGS/prof_ZAMS.data')
krticka_20m = Structure('../Data/4x4/4/20/LOGS/prof_midMS.data')
krticka_20t = Structure('../Data/4x4/4/20/LOGS/prof_TAMS.data')
krticka_30z = Structure('../Data/4x4/4/30/LOGS/prof_ZAMS.data')
krticka_30m = Structure('../Data/4x4/4/30/LOGS/prof_midMS.data')
krticka_30t = Structure('../Data/4x4/4/30/LOGS/prof_TAMS.data')
krticka_40z = Structure('../Data/4x4/4/40/LOGS/prof_ZAMS.data')
krticka_40m = Structure('../Data/4x4/4/40/LOGS/prof_midMS.data')
krticka_40t = Structure('../Data/4x4/4/40/LOGS/prof_TAMS.data')
krticka_50z = Structure('../Data/4x4/4/50/LOGS/prof_ZAMS.data')
krticka_50m = Structure('../Data/4x4/4/50/LOGS/prof_midMS.data')
krticka_50t = Structure('../Data/4x4/4/50/LOGS/prof_TAMS.data')
krticka_60z = Structure('../Data/4x4/4/60/LOGS/prof_ZAMS.data')
krticka_60m = Structure('../Data/4x4/4/60/LOGS/prof_midMS.data')
krticka_60t = Structure('../Data/4x4/4/60/LOGS/prof_TAMS.data')