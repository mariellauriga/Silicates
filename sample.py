import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import scipy as scipy
import matplotlib.lines as mlines
import itertools
from scipy.interpolate import interp1d
from sklearn.cluster import AffinityPropagation 
from sklearn import metrics 
from sklearn.datasets.samples_generator import make_blobs 
from itertools import cycle
from scipy import stats
############################

#Reading data
z_sample, agn_sample = loadtxt('sample_z_Fx_IRS.dat', unpack=True)
z_Subsample, agn_Subsample = loadtxt('sub_sample_z_Fx_IRS.dat', unpack=True)

ks_z, pv_z = stats.ks_2samp(z_sample, z_Subsample)
ks_agn, pv_agn = stats.ks_2samp(agn_sample, agn_Subsample)


print 'By Redshift:',ks_z, pv_z
if pv_z*100 > 40:
    print 'They are the same'
print 'By AGN contribution:',ks_agn, pv_agn
if pv_agn*100 > 40:
    print 'They are the same'

#####################

plt.subplot(121)

hist(z_sample, 5, histtype='step',color='black', stacked=True, fill=False, linewidth = 4, label='Full sample')
hist(z_Subsample, 5, histtype='step',color='blue', stacked=True, fill=False, linewidth = 4, label='S-S sample')

plt.ylabel(r'N',fontsize=20)
plt.xlabel(r'redshift $z$',fontsize=20)
plt.legend(loc = 'best', numpoints=1, prop={'size':16})

tick_params(axis='x', labelsize=20)
tick_params(axis='y', labelsize=20)


plt.subplot(122)
hist(agn_sample, 5, histtype='step',color='black', stacked=True, fill=False, linewidth = 4, label='Full sample')
hist(agn_Subsample, 2, histtype='step',color='blue', stacked=True, fill=False, linewidth = 4, label='S-S sample')

plt.ylabel(r'N',fontsize=16)
plt.xlabel(r'AGN contribution (per cent)',fontsize=16)
#plt.legend(loc = 2, numpoints=1, prop={'size':16})

tick_params(axis='x', labelsize=20)
tick_params(axis='y', labelsize=20)

plt.show()
