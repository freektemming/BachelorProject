# Class were all the information of star structure is saved

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

class Structure:

    def __init__(self,data):
        
        # data with six rows skipped
        data2 = np.genfromtxt(data,skip_header=6)

        self.logR = data2[:,4]
        self.normlogR = self.logR / np.max(self.logR)
        self.R = data2[:,18]
        self.normR = self.R / np.max(self.R)
        self.M = data2[:,62]
        self.normM = self.M / np.max(self.M)

        self.mixtype = data2[:,8]
        self.zone = data2[:,0]
        self.mlt = data2[:,35]

        self.datatest = data

    # open data again (first rows) and get age of star
    def age(self):
        # data with third row
        data_top = np.genfromtxt(self.datatest, max_rows=3)
        self.age = data_top[2,4] / 10**6
        self.age = float(self.age)
        self.age = round(self.age,2)
        return self.age
    
    # open data again (first rows) and get model number of star
    def model(self):
        # data with third row
        data_top = np.genfromtxt(self.datatest, max_rows=3)
        self.model = data_top[2,0]
        self.model = int(self.model)
        return self.model