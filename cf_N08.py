import pylab as pyla
import numpy as np
from numpy import *
import random
from os import sys
import matplotlib.ticker as ticker
import matplotlib as mat
from matplotlib import *
from matplotlib.ticker import FuncFormatter, MaxNLocator
from scipy.stats import distributions
#from PlottingXspecSpectrum import *
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from scipy import stats
from math import *
from scipy import integrate
from scipy.integrate import quad,nquad
from time import time
import scipy

#chi2, dof, incl, min_incl, max_incl, N0,min_N0, max_N0, sigma, min_sigma, max_sigma, Y, min_Y, max_Y, q, min_q, max_q, tau, min_tau, max_tau, norm, min_norm, max_norm = loadtxt('parameters_Nenkova.dat', unpack='True')
#chi2, dof, incl, min_incl, max_incl, N0,min_N0, max_N0, sigma, min_sigma, max_sigma, Y, min, max, q, min_q, max_q, tau, min, max, norm, min, max = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/3c120_Nenkova08_2_of_1s_ebv.txt', unpack='True')
incl = input('Enter inclination value:')
sigma = input('Enter sigma value:')
N0 = input('Enter N0 value:')

tetha =90.-incl
tetha0 = sigma
################################################
#####             [Nenkova08]              #####
################################################
def PescNenkova08(tetha, tetha0, N0):
    
    Nt = N0 * exp(-1.*power(tetha,2.)/pow(tetha0,2.) )
    return exp(-1.*Nt)*cos(tetha)

    #def Infer_Rout_Nenkova08(Y0,LogLbol):
    
    #Rin = 1.3*sqrt(pow(10.,LogLbol-46.))
    #Rout = Y0*Rin
#return Rin,Rout

def Infer_fcov_Nenkova08(N0,tetha0,tetha):
    
    tethadisk0 = tetha0*pi/180.
    fcov = 1. - quad(PescNenkova08,0.,pi/2., args=(tethadisk0,N0))[0]
    return fcov

################################################
#file1 = open('CF_Nenkova.dat','w+')

#for i in range(0,len(dof)):
#   print >>file1, Infer_fcov_Nenkova08(N0[i],tetha0[i],tetha[i])
#file1.close()

print 'Covering Factor=', Infer_fcov_Nenkova08(N0,tetha0,tetha)
