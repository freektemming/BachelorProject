import numpy as np

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
        data = np.genfromtxt(data,skip_header=6)  
        self.coreh = data[:,59]
        self.xd = self.coreh.compress((self.coreh>self.coreh[0]*0.997).flat) 
        self.x = len(self.xd)

        self.model = data[:,0]
        self.m = len(self.model)
        self.age2 = data[self.x-1:self.m-1,1]
        self.age = data[self.x:,1] / 1e6
        self.M = data[self.x:,2]
        self.logM = np.log10(self.M)
        self.Mdot = data[self.x:,3]
        self.Mdot = - self.Mdot 
        self.logMdot = np.log10(self.Mdot)
        self.logTeff = data[self.x:,6]
        self.Teff = data[self.x:,7]
        self.logL = data[self.x:,11]
        self.R =  data[self.x:,13]
        self.logg = data[self.x:,14]
        self.g = 10**self.logg
        self.centernit = data[self.x:,62] # N14
        self.logsurfh1 = data[self.x:,69]
        self.surfh1 = pow(10,self.logsurfh1)
        self.nit = data[self.x:,66] # N14
        self.ox = data[self.x:,67] # O16
        self.car = data[self.x:,65]  # C12
        self.lognit = np.log10(self.nit/(14*self.surfh1)) + 12
        self.logsurfhe = data[self.x:,70] # He4 surf
        self.surfhe = 10**self.logsurfhe

        self.nith = self.nit/self.surfh1
        self.oxh = self.ox/self.surfh1
        self.carh = self.car/self.surfh1

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
        self.time = self.age/pow(10,6)

    # ------ Color Bar ------
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