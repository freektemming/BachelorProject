#--------------------------------------------------------------------------
# Kippenhahn Diagram plotting the very unevenly distributed data along
# the time axis using the NonUniformImage method by mapping the 
# physical quantity to be shown onto a regular grid along the mass axis 
#
# Coding: afg/23.VIII.2012
#--------------------------------------------------------------------------
from scipy import interpolate as ip
import numpy as np
import mesa as ms

#-matplotlib specifics
from matplotlib.pyplot import figure, show
from matplotlib.image  import NonUniformImage
#--------------------------------------------------
#...Allow for using TeX mode in matplotlib Figures
#--------------------------------------------------
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
#--------------------------------------------------
#...Defintions
#==============
eps = 1.e-3   # mass boundary to avoid interpolation problems: see q_base
nq  = 512     # number of gridpoints on regular mass mesh

                       # problem specific, used when script was tested
myr = 1.e+6            # units to measure time in
tp1_max = 4522060464.5 # epoch of maximum of initial He-flash  
                       

q_crit = 0.45                             # maximum relative mass to be shown 
                                          # in "Kippenhahn diagram"
q_base = np.linspace(0+eps,q_crit-eps,nq) # define the uniform mass grid 
                                          # which applies to all models


models = np.arange(13200,15000,5) # how to step through profile-file sequence

# initialize lists 
zdat = []   # for z data; the values of the physical quantity, 
            # defined over the q,t plane, which shall be plotted
agel = []   # time-axis

for mod_no in models:
    prof=ms.mesa_profile('.',mod_no,num_type='model')

    age = prof.header_attr.get('star_age')

    lgone_m_q = prof.get('logxq')
    epsnuc    = prof.get('eps_nuc')

    q = 1.0 - 10**(lgone_m_q)

    # prepare for linear interpolation along q axis
    # N.B. xx must be an monotonically increasing x!!
    #      since vectors in profiles start at the surface
    #      they have to be inverted for the interpolation

    xx = q[::-1]
    yy = np.minimum(np.maximum(np.log10(epsnuc[::-1]),0.0),2.0)

    fieps = ip.interp1d(xx,yy)

    # interpolate yy and y2 to the q_base points
    eps_ip = fieps(q_base)   

    agel.append(age)
    zdat.append(list(eps_ip))

#...appropriately normalize x-axis 
#   and transform lists to arrays
time = (np.array(agel) - tp1_max)/myr 
z    = np.array(zdat).transpose()

tmin = time.min() 
tmax = time.max()
qmin = q_base.min()
qmax = q_base.max()

# interpolate data on the nonuniform grid
#interp='nearest'
interp = 'bilinear'

fig = figure()
ax = fig.add_subplot(111)
im = NonUniformImage(ax,cmap='Oranges',interpolation=interp,extent=(tmin,tmax,qmin,qmax))
im.set_data(time, q_base, z)
ax.images.append(im)
ax.set_xlim(tmin,tmax)
ax.set_ylim(qmin,qmax)

# labeling the plot
ax.set_title('Nuclear Burning ' r'$1.3 M_\odot$ Red Giant' )
ax.set_xlabel(r'$t^\ast$ / Myrs')
ax.set_ylabel(r'$q$')      

show()
