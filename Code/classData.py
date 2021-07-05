# Class were all the information per model is saved

import numpy as np
from statistics import mean

# constants
sigma = 5.67051 * pow(10,-5)  # cgs
Rsun = 6.957 * pow(10,10)
Lsun = 3.828 * pow(10,33)
pi = np.pi
G = 6.67259e-8 # cgs
Msun = 1.99e33  # cgs
year = 3.154e7  # sec. 
Teffsun = 5.780e3 # K 
loggsun = 4.43775 # cgs
Lscriptsun = pow(Teffsun,4.)/(10**loggsun)

class Data:

    def __init__(self,data):

        # data with six rows skipped
        data = np.genfromtxt(data,skip_header=6)  
        self.coreh = data[:,59]
        self.xd = self.coreh.compress((self.coreh>self.coreh[0]*0.997).flat) 
        self.x = len(self.xd)
        self.coreH = data[self.x:,59]

        self.centerhe = data[self.x:,60]
        self.convective_core = data[self.x:,39]

        # standard parameters
        self.model = data[self.x:,0]
        self.m = len(self.model)
        self.age2 = data[self.x-1:self.m-1,1]
        self.age = data[self.x:,1] / 1e6
        self.M = data[self.x:,2]
        self.logM = np.log10(self.M)
        self.Mdot = data[self.x:,3]
        self.Mdot = - self.Mdot 
        self.logMdot = np.log10(self.Mdot)
        self.logTeff = data[self.x:,6]
        self.Teff = data[self.x:,7] / 1e3 # kK
        self.logL = data[self.x:,11]
        self.R =  data[self.x:,13]
        self.logR = np.log10(self.R)
        self.logg = data[self.x:,14]
        self.g = 10**self.logg

        # ------ Histogram ------
        self.histL = self.logL / self.logL[0]
        self.Vrot = data[self.x:,22]
        self.histVrot = self.Vrot / self.Vrot[0]
        self.histR = self.R / self.R[0]
        self.histM = self.M / self.M[0]
        self.convcore = data[self.x:,37]
        self.histCore = self.convcore / self.convcore[0]
        
        # ------ Convection ------
        self.normR = self.R / np.max(self.R)
        self.nmass = self.M / np.max(self.M)
        self.convcore = data[self.x:,37]
        self.convective_core = data[self.x:,37] / self.M * self.nmass
        self.envelope_mass = self.M - self.convcore
        self.logconvective_core = np.log10(self.convective_core)
        self.mix1 = data[self.x:,40]
        self.czmass = data[self.x:,27] / self.M * self.nmass
        self.czradius = data[self.x:,28] #/ self.R
        self.logczradius = np.log10(self.czradius)
        self.nczradius = data[self.x:,28] / self.R
        self.Hecoremass = data[self.x:,30] / self.M * self.nmass
        
        # Elements
        self.HC = data[self.x:,59] * self.nmass # fraction of core mass
        self.HeC = data[self.x:,60] * self.nmass # fraction of core mass
        self.CC = data[self.x:,61] * self.nmass # fraction of core mass
        self.NC = data[self.x:,62] * self.nmass # fraction of core mass
        self.OC = data[self.x:,63] * self.nmass # fraction of core mass
        
        self.convbot = data[self.x:,39] * self.nmass # conv mix 1 m/Mstar
        self.convtop = data[self.x,38] * self.nmass # conv mix 1 m/Mstar
        self.convtop2 = data[self.x:,40] * self.nmass # conv mix 2 m/Mstar
        self.convbot2 = data[self.x:,41] * self.nmass # conv mix 2 m/Mstar
        self.top = data[self.x:,42] * self.nmass # mix 1 m/Mstar
        self.bot = data[self.x:,43] * self.nmass # mix 1 m/Mstar

        self.logconvbot = np.log10(self.convbot)

        # ------ Elements ------
        self.centerc = data[self.x:,61] # c12
        self.centernit = data[self.x:,62] # N14

        # total mass
        self.toth1 = data[self.x:,71]
        self.ntoth1 = self.toth1 / np.max(self.M) * self.nmass
        self.tothe = data[self.x:,72]
        self.ntothe = self.tothe / np.max(self.M) * self.nmass

        # surface elements
        self.logh1 = data[self.x:,69]
        self.h1 = pow(10,self.logh1)
        self.nh1 = self.h1 / np.max(self.M) * self.nmass
        self.lognh1 = np.log10(self.nh1)
        self.loghe = data[self.x:,70] # He4 surf
        self.he = 10**self.loghe
        self.nhe = self.he / np.max(self.M) * self.nmass
        self.lognhe = np.log10(self.nhe)
        self.nit = data[self.x:,66] # N14
        self.nnit = self.nit / np.max(self.M) * self.nmass
        self.lognnit = np.log10(self.nnit)
        self.ox = data[self.x:,67] # O16
        self.nox = self.ox / np.max(self.M) * self.nmass
        self.lognox = np.log10(self.nox)
        self.car = data[self.x:,65]  # C12
        self.ncar = self.car / np.max(self.M) * self.nmass
        self.logncar = np.log10(self.ncar)

        self.lognit = np.log10(self.nit/(14*self.h1)) + 12
        self.nith = self.nit/self.h1
        self.oxh = self.ox/self.h1
        self.carh = self.car/self.h1

        self.botsurfh1 = self.ntoth1 - self.nh1
        self.botsurfhe = self.ntothe - self.nhe

        # ==================== Kippenhahn
        self.nhemin = []
        for i in range(len(self.nhe)):
            self.nhemin.append(self.nmass[i]-self.nhe[i])

        self.ntotheminsurf = self.ntothe - self.nhe
        self.ntotheminsurfmin = []
        for i in range(len(self.ntotheminsurf)):
            self.ntotheminsurfmin.append(self.nmass[i]-self.ntotheminsurf[i])

        self.surfcartoplim = self.ntoth1 + self.ncar
        self.surfnittoplim = self.surfcartoplim + self.nnit
        self.surfoxtoplim = self.surfnittoplim + self.nox
        # ====================

        # ------ Rotation ------
        self.vrot = data[self.x:,22]
        self.Jtot = data[self.x:,5]
        self.Omega = data[self.x:,19]
        self.Omegac = data[self.x:,58]
        self.omdivomcr = data[self.x:,20]
        self.periods = 2. * pi * (self.R*Rsun) / (self.vrot *1e5)
        self.period = self.periods / (3600. * 24.)
        self.logperiod = np.log10(self.period)

        # ------ wind ------
        self.vesc = data[self.x:,86]
        self.vinf = data[self.x:,87]
        
        # wind models
        self.wvink01 = data[self.x:,88]
        self.usewvink01 = data[self.x:,89]
        self.wvink18 = data[self.x:,90]
        self.usewvink18 = data[self.x:,91]
        self.wleuven = data[self.x:,92]
        self.usewleuven = data[self.x:,93]
        self.wkrticka = data[self.x:,94]
        self.usewkrticka= data[self.x:,95]
        self.wbeasor = data[self.x:,96]
        self.usewbeasor = data[self.x:,97]
        self.wkee = data[self.x:,98]
        self.usewkee = data[self.x:,99]
        self.wsander =  data[self.x:,100]
        self.usewsander = data[self.x:,101]
        
        self.frot = data[self.x:,102]
        self.Mdotorig = data[self.x:,103]
            
        # ------ time ------
        self.time = self.age#/pow(10,6) ???

    # ------ Color Bar ------
    # age
    def get_max_bar(self):
        m = 0
        bar = self.age
        m_temp = bar.max()
        if m_temp > m:
            m = m_temp          
        return m #baz

    def get_min_bar(self):
        n = 0
        bar = self.age
        n_temp = bar.min()
        if n_temp < n:
            n = n_temp          
        return n #meg

    # gravity
    def get_max_grav(self):
        m = 0
        bar = self.logg
        m_temp = bar.max()
        if m_temp > m:
            m = m_temp          
        return m #baz

    def get_min_grav(self):
        n = 0
        bar = self.logg
        n_temp = bar.min()
        if n_temp < n:
            n = n_temp          
        return n #meg

    # ------ Determine main sequence ------
    def mainsequence(self):
        for i in range(len(self.age) - 1):
            if self.Teff[i + 1] - self.Teff[i] > 0:
                return i
    # get maximum age on main sequence
    def get_age(self, i):
        max = self.age[i]
        return max
    
    # get minimum gravitation on main sequence
    def get_grav(self, i):
        min = self.logg[i]
        return min

    # determine eind of simulation, defined by temperature of 10 kK
    def end(self):
        for i in range(len(self.Teff) - 1):
            if self.Teff[i] < 10:
                return i
        # else        
        return -1

    # ------ Determine max of list in certain range ------
    def minlist(self, lim):
        min = np.min(self.logg[0:lim])
        return min