import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import sys
import math
import scipy as scipy
import scipy.integrate as scii
from pylab import *
import uncertainties as u
from uncertainties import unumpy
from uncertainties import ufloat
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
from matplotlib.collections import LineCollection
from matplotlib.ticker import AutoMinorLocator
#----------------------------------------------
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
#=========================================
from plotsetup import *    # and plotsetup
#=========================================

#
#==== MODELS

mod = ['20','30','40','50','60']

path = '../data/Z014Om2/3/'
mes = '/LOGS/out.data'

# for testing local
#:path = '../data/'
#:mod = ['local/']
#:mes ='/LOGS/out.data'

num = len(mod)

k = ['navy','grey','green','yellow','blue','navy','grey','green','yellow','blue','navy','grey','green','yellow','blue','navy','grey','green','yellow','blue','navy','grey','green','yellow','blue']
j = [':','--','-.','-',':','--','-.','-','--','-.','-','--','-.']
lww = [6,6,6,12,12,12,18,18,18]

# This is for the colour bar:
#:::::::;;
#
def get_max_bar_value():
    m = 0
    for i in range(0,num):
        data = np.genfromtxt(path+mod[i]+mes, skip_header = 6)
        coreh = data[:,59]    # center H1
        xd = coreh.compress((coreh>coreh[0]*0.997).flat) 
        x = len(xd)
        #logg =  data[x:,14]
        #bar = logg
        age = data[x:,1]
        bar = age/1e6###/max(age/1e6)
        #omdivomcr = data[x:,20]
        #logsurfh1 = data[x:,69]
        #surfh1 = pow(10,logsurfh1)
        #bar = surfh1
        m_temp = bar.max()
        if m_temp > m:
            m = m_temp          
    return m
m = get_max_bar_value()
baz = m

def get_min_bar_value():
    n = 0
    for i in range(0,num):
        data = np.genfromtxt(path+mod[i]+mes, skip_header = 6)
        coreh = data[:,59]    # center H1
        xd = coreh.compress((coreh>coreh[0]*0.997).flat) 
        x = len(xd)
        age = data[x:,1]
        bar = age/1e6###/max(age/1e6)
        #logg =  data[x:,14]
        #bar = logg
        #omdivomcr = data[x:,20]
        #logsurfh1 = data[x:,69]
        #surfh1 = pow(10,logsurfh1)
        #bar = surfh1
        n_temp = bar.min()
        if n_temp < n:   # direction < for age, > for log g, and < with n = large number otherwise
            n = n_temp          
    return n
n = get_min_bar_value()
meg = n 

print baz 
print meg


##### MESA files input ###### 
#
#
for i in range(0,num) : 
 data = np.genfromtxt(path+mod[i]+mes,skip_header=6)  
 #-----------------------------------------------
 coreh = data[:,59]
 xd = coreh.compress((coreh>coreh[0]*0.997).flat) 
 x = len(xd)

 model = data[:,0]
 m = len(model)
 age2 = data[x-1:m-1,1]
 age = data[x:,1]
 M = data[x:,2]
 logM = np.log10(M)
 Mdot = data[x:,3]
 Mdot = - Mdot 
 logMdot = np.log10(Mdot)
 logTeff = data[x:,6]
 Teff = data[x:,7]
 logL = data[x:,11]
 R =  data[x:,13]
 logg =  data[x:,14]
 g = 10**logg
 centernit = data[x:,62] # N14
 logsurfh1 = data[x:,69]
 surfh1 = pow(10,logsurfh1)
 nit = data[x:,66] # N14
 ox = data[x:,67] # O16
 car = data[x:,65]  # C12
 lognit = np.log10(nit/(14*surfh1)) + 12
 logsurfhe = data[x:,70] # He4 surf
 surfhe = 10**logsurfhe
 #:::print surfhe[-1]
 
 nith = nit/surfh1
 oxh = ox/surfh1
 carh = car/surfh1

 #-- rot
 vrot = data[x:,22]
 Jtot = data[x:,5]
 Omega = data[x:,19]
 Omegac = data[x:,58]
 omdivomcr = data[x:,20]
 periods = 2. * pi * (R*Rsun) / (vrot *1e5)
 period = periods / (3600. * 24.)
 logperiod = np.log10(period)
#-- wind 

 vesc = data[x:,86]
 vinf = data[x:,87]
 wvink01 = data[x:,88]
 usewvink01 = data[x:,89]
 wvink18 = data[x:,90]
 usewvink18 = data[x:,91]
 wleuven = data[x:,92]
 usewleuven = data[x:,93]
 wkrticka = data[x:,94]
 usewkrticka= data[x:,95]
 wbeasor = data[x:,96]
 usewbeasor = data[x:,97]
 wkee = data[x:,98]
 usewkee = data[x:,99]
 wsander =  data[x:,100]
 usewsander = data[x:,101]
 frot = data[x:,102]
 Mdotorig = data[x:,103]
        
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 time = age/pow(10,6)
 time2 = age2/pow(10,6)
 #dt = age - age2
 #dt = dt * year   ### year to seconds 
#=========  END of MESA file input ==============================================================
 #dd = Teff.compress(((age/1e6)<5).flat)
 #da = len(dd)

 dd1 = Teff.compress(((age/1e6)<2.).flat) # show 2 Myr
 da1 = len(dd1)
 dd2 = Teff.compress(((age/1e6)<4.).flat) # show 4 Myr
 da2 = len(dd2)
 dd3 = Teff.compress(((age/1e6)<6.).flat) # show 6 Myr
 da3 = len(dd3)
 dd4 = Teff.compress(((age/1e6)<8.).flat) # show 8 Myr
 da4 = len(dd4)
 dd5 = Teff.compress(((age/1e6)<10.).flat) # show 10 Myr
 da5 = len(dd5)

 Mini = "{:1.0f}".format(M[0])
 #print '============'
 #print vrot[0], max(vrotwtf), vrotwtf[0]
 #print Bp[0]
 #print '============'
#
#
#
# === IN LOOP PLOTS ===    
#
#
 ax1.plot(Teff/1e3, logL, lw = 6, linestyle = '-', color = 'black', zorder=6)
 #:for p in (da1,da2,da3,da4,da5):
 #:   ax1.plot(Teff[p]/1e3, logL[p], linestyle = '', marker = 'X', markersize = 42, color = 'black', zorder=1)
 ims1 = ax1.scatter(Teff/1e3, logL,c= age/1e6, marker='o', edgecolors='none', s=1000, cmap=plt.cm.magma_r, vmin = meg, vmax = baz)

 ax11.plot(Teff/1e3, np.log10(pow(Teff,4.)/g/Lscriptsun), lw = 6, linestyle = '-', color = 'black', zorder=1)
 ims11 = ax11.scatter(Teff/1e3, np.log10(pow(Teff,4.)/g/Lscriptsun),c= age/1e6, marker='o', edgecolors='none', s=1000, cmap=plt.cm.coolwarm, vmin = meg, vmax = baz)
 
 ax111.plot(Teff/1e3, logg, lw = 6, linestyle = '-', color = 'black', zorder=2)
 #ims111 = ax111.scatter(Teff/1e3,logg,c= age/1e6, marker='o', edgecolors='none', s=1000, cmap=plt.cm.magma_r, vmin = meg, vmax = baz, zorder=1)
 #::ax111.plot(Teff[da3]/1e3, logg[da3], linestyle = '', marker = 'X', markersize = 32, color = 'yellow', zorder=5)
 
 ax2.plot(logperiod, lognit, lw=6, linestyle = '-', color =  'black' )
 ims2 = ax2.scatter(logperiod, lognit,c= age/1e6, marker='o', edgecolors='none', s=1000, cmap=plt.cm.magma_r, vmin = meg, vmax = baz)
 #::ax2.plot(logperiod[da3], lognit[da3], linestyle = '', marker = 'X', markersize = 32, color = 'yellow', zorder=5)

 ax3.plot(vrot, lognit, lw=6, linestyle = '-', color =  'black')
 ims3 = ax3.scatter(vrot, lognit,c= age/1e6, marker='o', edgecolors='none', s=1000, cmap=plt.cm.magma_r, vmin = meg, vmax = baz)
 ax444.plot(time, omdivomcr, lw=14, linestyle = '-', color = 'orange')
 ax44.plot(time, logperiod, lw=14, linestyle = '-', color = 'black' )
 #ax4444.plot(time, R, lw=14, linestyle = j[i], color = 'orange')

 ax4.plot(time, time, lw=14, linestyle = '-')
 #ims4 = ax4.scatter(time, np.log10(Bp),c= age/1e6, marker='o', edgecolors='none', s=1000, cmap=plt.cm.coolwarm, vmin = meg, vmax = baz)
 #ax4.plot(time[da3], np.log10(Bp[da3]), linestyle = '', marker = 'X', markersize = 32, color = 'yellow', zorder=5)

 ax5.plot(logg, np.log10(Omega), lw=16, linestyle = '-' )
 ax5.plot(logg, np.log10(Omegac), lw=16, linestyle = ':' )


 ax7.plot(Teff/1e3, logMdot, lw=16, linestyle = '-', color =  'black' )
 ax7.plot(Teff/1e3, np.log10(frot * Mdotorig), lw=16, linestyle = '--', color =  'grey' )

 dw1 = Teff.compress((usewvink01<1).flat) #
 daww1 = len(dw1)
 db = Teff.compress((usewbeasor<1).flat) #
 dab = len(db)
 ds = Teff.compress((usewsander<1).flat) #
 das = len(ds)

 ax7.plot(Teff[:daww1]/1e3, np.log10(frot[:daww1] * wvink01[:daww1]), lw=16, linestyle = ':', color =  'green' )

 ax7.plot(Teff[dab:]/1e3, np.log10(frot[dab:] * wbeasor[dab:]), lw=16, linestyle = ':', color =  'red' ) 
 ax7.plot(Teff[das:]/1e3, np.log10(frot[das:] * wsander[das:]), lw=16, linestyle = ':', color =  'yellow' )


 #ax7.plot(time,np.log10(nith), lw=16, linestyle = j[i], color =  'red')
 #ax7.plot(time,np.log10(oxh), lw=16, linestyle = j[i], color =  'blue')
 ax77.plot(time,np.log10(nith), lw=16, linestyle = '-', color =  'black' )
 ax777.plot(time,surfhe, lw=16, linestyle = '-', color =  'black' )


cbar = fig1.colorbar(ims1)
cbar.ax.tick_params(labelsize=54) 
cbar.set_label('age [Myr]', size = 54)
#cbar.set_label('$\Omega / \Omega_{crit}$', size = 54)
#cbar.set_label('surf. H [mass frac.]', size = 54)
#cbar = fig11.colorbar(ims11)
#cbar.ax.tick_params(labelsize=54) 
#cbar.set_label('age [Myr]', size = 54)

#cbar = fig111.colorbar(ims111)
#cbar.ax.tick_params(labelsize=54) 
#cbar.set_label('age [Myr]', size = 54)
#cbar.set_label('age', size = 54)

cbar = fig2.colorbar(ims2)
cbar.ax.tick_params(labelsize=54) 
#cbar.set_label('age [Myr]', size = 54)
#cbar.set_label('$\Omega / \Omega_{crit}$', size = 54)
cbar.set_label('surf. H [mass frac.]', size = 54)

#cbar = fig3.colorbar(ims3)
#cbar.ax.tick_params(labelsize=54) 
#cbar.set_label('age [Myr]', size = 54)
#cbar = fig6.colorbar(ims6)
#cbar.ax.tick_params(labelsize=54) 
#cbar.set_label('age [Myr]', size = 54)
#cbar = fig4.colorbar(ims4)
#cbar.ax.tick_params(labelsize=54) 
#cbar.set_label('age [Myr]', size = 54)

#ax1.text(33., 4.99, strg, bbox=dict(facecolor='grey', alpha=0.2, boxstyle='round'), fontsize = 54)
#ax2.text(-1, 2, strg, bbox=dict(facecolor='grey', alpha=0.2, boxstyle='round'), fontsize = 34)

#ax1.annotate("non-magnetic", xy=(23.8, 4.46), xytext=(26.9, 4.3),
 #   arrowprops=dict(arrowstyle="->", linewidth = 10), size = 44, fontsize = 44)
#ax1.annotate("magnetic", xy=(28., 4.64), xytext=(33.2, 4.48),
  #  arrowprops=dict(arrowstyle="->", linewidth = 10), size = 44, fontsize = 44)


#:::legend = ax1.legend(fancybox = True, scatterpoints =1, labelspacing = 1, loc='upper left', shadow=True, fontsize=34, handlelength = 5)
legend = ax11.legend(fancybox = True, scatterpoints =1, labelspacing = 1, loc='upper left', shadow=True, fontsize=34, handlelength = 5)
legend = ax111.legend(fancybox = True, scatterpoints =1, labelspacing = 1, loc='upper left', shadow=True, fontsize=34, handlelength = 5)
legend = ax2.legend(fancybox = True, scatterpoints =1, labelspacing = 1, loc='upper right', shadow=True, fontsize=34, handlelength = 5)
legend = ax3.legend(fancybox = True, scatterpoints =1, labelspacing = 1, loc='upper right', shadow=True, fontsize=34, handlelength = 5)
legend = ax4.legend(fancybox = True, scatterpoints =1, labelspacing = 1, loc='lower right', shadow=True, fontsize=34, handlelength = 5)
legend = ax44.legend(fancybox = True, scatterpoints =1, labelspacing = 1, loc='lower right', shadow=True, fontsize=34, handlelength = 5)
#legend = ax6.legend(fancybox = True, scatterpoints =1, labelspacing = 1, loc='lower right', shadow=True, fontsize=34, handlelength = 5)
legend = ax7.legend(fancybox = True, scatterpoints =1, labelspacing = 1, loc='lower left', shadow=True, fontsize=34, handlelength = 5)
legend = ax77.legend(fancybox = True, scatterpoints =1, labelspacing = 1, loc='upper left', shadow=True, fontsize=34, handlelength = 5)
legend = ax777.legend(fancybox = True, scatterpoints =1, labelspacing = 1, loc='upper left', shadow=True, fontsize=34, handlelength = 5)


fig1.tight_layout()
fig11.tight_layout()
fig111.tight_layout()
fig2.tight_layout()
fig3.tight_layout()
fig4.tight_layout()
fig44.tight_layout()
fig5.tight_layout()
#fig6.tight_layout()
fig7.tight_layout()
fig77.tight_layout()
fig777.tight_layout()

fig1.savefig('test/hrd.png')
#fig11.savefig('test/shrd.png')
fig111.savefig('test/kiel.png')
fig2.savefig('test/hunterp.png')
fig3.savefig('test/hunter.png')
#fig4.savefig('test/bp.png')
fig44.savefig('test/prot.png')
fig5.savefig('test/om.png')
#fig6.savefig('test/rark.png')
fig7.savefig('test/Mdot.png')
fig77.savefig('test/n.png')
fig777.savefig('test/he.png')

#plt.show()
sys.exit()




