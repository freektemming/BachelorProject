# script that contains data import for other scripts

from classData import Data
from classStructure import Structure

# ------ Select Data ------
    
#datafolder = '4x4'
#datafolder = 'OmegaCrit06'
#datafolder = 'Z002Om2'
#datafolder = 'Z007Om2'

#datafolder = 'TestRunMW'
#datafolder = 'TestRunLMC'
datafolder = 'TestRunSMC'

# -----------------------------------------------------------------------------------

# Vink 01
vink01_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/20/LOGS/out.data')
vink01_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/30/LOGS/out.data')
vink01_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/40/LOGS/out.data')
vink01_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/50/LOGS/out.data')
vink01_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/1/60/LOGS/out.data')

# Vink 18
vink18_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/20/LOGS/out.data')
vink18_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/30/LOGS/out.data')
vink18_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/40/LOGS/out.data')
vink18_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/50/LOGS/out.data')
vink18_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/2/60/LOGS/out.data')

# Leuven
leuven_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/20/LOGS/out.data')
leuven_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/30/LOGS/out.data')
leuven_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/40/LOGS/out.data')
leuven_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/50/LOGS/out.data')
leuven_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/3/60/LOGS/out.data')

# Krticka
krticka_20 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/20/LOGS/out.data')
krticka_30 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/30/LOGS/out.data')
krticka_40 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/40/LOGS/out.data')
krticka_50 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/50/LOGS/out.data')
krticka_60 = Data(f'../../BachelorProjectData/Data/{datafolder}/4/60/LOGS/out.data')

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

