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

file1 = open('parameters_Nenkova.dat','w+')
############################Nenkova08############################
print >>file1, 'chi2','dof','incl', 'min', 'max', 'N0', 'min', 'max', 'sigma', 'min', 'max', 'Y', 'min', 'max', 'q', 'min', 'max', 'tau', 'min', 'max'
chi2_3c120_2, dof_3c120_2, incl_3c120_Nenkova08, min_incl_3c120, max_incl_3c120, N0_3c120_Nenkova08,min_N0_3c120, max_N0_3c120, sigma_3c120_Nenkova08, min_sigma_3c120, max_sigma_3c120, Y_3c120_Nenkova08, min_Y_3c120, max_Y_3c120, q_3c120_Nenkova08, min_q_3c120, max_q_3c120, tau_3c120_Nenkova08, min_tau_3c120, max_tau_3c120, norm, min, max = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/3c120_Nenkova08_2_of_1s_ebv.txt', unpack='True')
if max_incl_3c120==0.0:
    max_incl_3c120=90.0
if min_sigma_3c120==0.0:
    min_sigma_3c120=15.0
if max_sigma_3c120==0.0:
    max_sigma_3c120=70.0
if min_N0_3c120==0.0:
    min_N0_3c120=1.0
if max_N0_3c120==0.0:
    max_N0_3c120=15.0
if min_Y_3c120==0.0:
    min_Y_3c120=5.0
if max_Y_3c120==0.0:
    max_Y_3c120=100.0
if max_q_3c120==0.0:
    max_q_3c120=2.5
if min_tau_3c120==0.0:
    min_tau_3c120=10.0
if max_tau_3c120==0.0:
    max_tau_3c120=300.0
print >>file1, chi2_3c120_2, dof_3c120_2, incl_3c120_Nenkova08, min_incl_3c120, max_incl_3c120, N0_3c120_Nenkova08,min_N0_3c120, max_N0_3c120, sigma_3c120_Nenkova08, min_sigma_3c120, max_sigma_3c120, Y_3c120_Nenkova08, min_Y_3c120, max_Y_3c120, q_3c120_Nenkova08, min_q_3c120, max_q_3c120, tau_3c120_Nenkova08, min_tau_3c120, max_tau_3c120, norm, min, max, '#3c120'

chi2_3c445_2, dof_3c445_2, incl_3c445_Nenkova08, min_incl_3c445, max_incl_3c445, N0_3c445_Nenkova08,min_N0_3c445, max_N0_3c445, sigma_3c445_Nenkova08, min_sigma_3c445, max_sigma_3c445, Y_3c445_Nenkova08, min_Y_3c445, max_Y_3c445, q_3c445_Nenkova08, min_q_3c445, max_q_3c445, tau_3c445_Nenkova08, min_tau_3c445, max_tau_3c445, norm, min, max = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/3c445_Nenkova08_2_of_1s_ebv.txt', unpack='True')
if max_incl_3c445==0.0:
    max_incl_3c445=90.0
if min_sigma_3c445==0.0:
    min_sigma_3c445=15.0
if max_sigma_3c445==0.0:
    max_sigma_3c445=70.0
if min_N0_3c445==0.0:
    min_N0_3c445=1.0
if max_N0_3c445==0.0:
    max_N0_3c445=15.0
if min_Y_3c445==0.0:
    min_Y_3c445=5.0
if max_Y_3c445==0.0:
    max_Y_3c445=100.0
if max_q_3c445==0.0:
    max_q_3c445=2.5
if min_tau_3c445==0.0:
    min_tau_3c445=10.0
if max_tau_3c445==0.0:
    max_tau_3c445=300.0
print >>file1, chi2_3c445_2, dof_3c445_2, incl_3c445_Nenkova08, min_incl_3c445, max_incl_3c445, N0_3c445_Nenkova08,min_N0_3c445, max_N0_3c445, sigma_3c445_Nenkova08, min_sigma_3c445, max_sigma_3c445, Y_3c445_Nenkova08, min_Y_3c445, max_Y_3c445, q_3c445_Nenkova08, min_q_3c445, max_q_3c445, tau_3c445_Nenkova08, min_tau_3c445, max_tau_3c445, norm, min, max, '#3c445'

chi2_AKN120_2, dof_AKN120_2, incl_AKN120_Nenkova08, min_incl_AKN120, max_incl_AKN120, N0_AKN120_Nenkova08,min_N0_AKN120, max_N0_AKN120, sigma_AKN120_Nenkova08, min_sigma_AKN120, max_sigma_AKN120, Y_AKN120_Nenkova08, min_Y_AKN120, max_Y_AKN120, q_AKN120_Nenkova08, min_q_AKN120, max_q_AKN120, tau_AKN120_Nenkova08, min_tau_AKN120, max_tau_AKN120, norm, min, max = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/AKN120_Nenkova08_2_of_1s_ebv.txt', unpack='True')
if max_incl_AKN120==0.0:
    max_incl_AKN120=90.0
if min_sigma_AKN120==0.0:
    min_sigma_AKN120=15.0
if max_sigma_AKN120==0.0:
    max_sigma_AKN120=70.0
if min_N0_AKN120==0.0:
    min_N0_AKN120=1.0
if max_N0_AKN120==0.0:
    max_N0_AKN120=15.0
if min_Y_AKN120==0.0:
    min_Y_AKN120=5.0
if max_Y_AKN120==0.0:
    max_Y_AKN120=100.0
if max_q_AKN120==0.0:
    max_q_AKN120=2.5
if min_tau_AKN120==0.0:
    min_tau_AKN120=10.0
if max_tau_AKN120==0.0:
    max_tau_AKN120=300.0
print >>file1, chi2_AKN120_2, dof_AKN120_2, incl_AKN120_Nenkova08, min_incl_AKN120, max_incl_AKN120, N0_AKN120_Nenkova08,min_N0_AKN120, max_N0_AKN120, sigma_AKN120_Nenkova08, min_sigma_AKN120, max_sigma_AKN120, Y_AKN120_Nenkova08, min_Y_AKN120, max_Y_AKN120, q_AKN120_Nenkova08, min_q_AKN120, max_q_AKN120, tau_AKN120_Nenkova08, min_tau_AKN120, max_tau_AKN120, norm, min, max, '#AKN120'

chi2_OQ208_4, dof_OQ208_4, incl_OQ208_Nenkova08, min_incl_OQ208, max_incl_OQ208, N0_OQ208_Nenkova08,min_N0_OQ208, max_N0_OQ208, sigma_OQ208_Nenkova08, min_sigma_OQ208, max_sigma_OQ208, Y_OQ208_Nenkova08, min_Y_OQ208, max_Y_OQ208, q_OQ208_Nenkova08, min_q_OQ208, max_q_OQ208, tau_OQ208_Nenkova08, min_tau_OQ208, max_tau_OQ208, norm, min, max= loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/OQ208_Nenkova08_4_of_1s_ebv.txt', unpack='True')
if max_incl_OQ208==0.0:
    max_incl_OQ208=90.0
if min_sigma_OQ208==0.0:
    min_sigma_OQ208=15.0
if max_sigma_OQ208==0.0:
    max_sigma_OQ208=70.0
if min_N0_OQ208==0.0:
    min_N0_OQ208=1.0
if max_N0_OQ208==0.0:
    max_N0_OQ208=15.0
if min_Y_OQ208==0.0:
    min_Y_OQ208=5.0
if max_Y_OQ208==0.0:
    max_Y_OQ208=100.0
if max_q_OQ208==0.0:
    max_q_OQ208=2.5
if min_tau_OQ208==0.0:
    min_tau_OQ208=10.0
if max_tau_OQ208==0.0:
    max_tau_OQ208=300.0
print >>file1, chi2_OQ208_4, dof_OQ208_4, incl_OQ208_Nenkova08, min_incl_OQ208, max_incl_OQ208, N0_OQ208_Nenkova08,min_N0_OQ208, max_N0_OQ208, sigma_OQ208_Nenkova08, min_sigma_OQ208, max_sigma_OQ208, Y_OQ208_Nenkova08, min_Y_OQ208, max_Y_OQ208, q_OQ208_Nenkova08, min_q_OQ208, max_q_OQ208, tau_OQ208_Nenkova08, min_tau_OQ208, max_tau_OQ208, norm, min, max, '#OQ208'

chi2_ESO198_2, dof_ESO198_2, incl_ESO198_Nenkova08, min_incl_ESO198, max_incl_ESO198, N0_ESO198_Nenkova08,min_N0_ESO198, max_N0_ESO198, sigma_ESO198_Nenkova08, min_sigma_ESO198, max_sigma_ESO198, Y_ESO198_Nenkova08, min_Y_ESO198, max_Y_ESO198, q_ESO198_Nenkova08, min_q_ESO198, max_q_ESO198, tau_ESO198_Nenkova08, min_tau_ESO198, max_tau_ESO198, norm, min, max = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ESO198_Nenkova08_2_of_1s_ebv.txt', unpack='True')
if max_incl_ESO198==0.0:
    max_incl_ESO198=90.0
if min_sigma_ESO198==0.0:
    min_sigma_ESO198=15.0
if max_sigma_ESO198==0.0:
    max_sigma_ESO198=70.0
if min_N0_ESO198==0.0:
    min_N0_ESO198=1.0
if max_N0_ESO198==0.0:
    max_N0_ESO198=15.0
if min_Y_ESO198==0.0:
    min_Y_ESO198=5.0
if max_Y_ESO198==0.0:
    max_Y_ESO198=100.0
if max_q_ESO198==0.0:
    max_q_ESO198=2.5
if min_tau_ESO198==0.0:
    min_tau_ESO198=10.0
if max_tau_ESO198==0.0:
    max_tau_ESO198=300.0
print >>file1, chi2_ESO198_2, dof_ESO198_2, incl_ESO198_Nenkova08, min_incl_ESO198, max_incl_ESO198, N0_ESO198_Nenkova08,min_N0_ESO198, max_N0_ESO198, sigma_ESO198_Nenkova08, min_sigma_ESO198, max_sigma_ESO198, Y_ESO198_Nenkova08, min_Y_ESO198, max_Y_ESO198, q_ESO198_Nenkova08, min_q_ESO198, max_q_ESO198, tau_ESO198_Nenkova08, min_tau_ESO198, max_tau_ESO198, norm, min, max, '#ESO198'

chi2_ESO548_2, dof_ESO548_2, incl_ESO548_Nenkova08, min_incl_ESO548, max_incl_ESO548, N0_ESO548_Nenkova08,min_N0_ESO548, max_N0_ESO548, sigma_ESO548_Nenkova08, min_sigma_ESO548, max_sigma_ESO548, Y_ESO548_Nenkova08, min_Y_ESO548, max_Y_ESO548, q_ESO548_Nenkova08, min_q_ESO548, max_q_ESO548, tau_ESO548_Nenkova08, min_tau_ESO548, max_tau_ESO548, norm, min, max = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ESO548_Nenkova08_2_of_1s_ebv.txt', unpack='True')
if max_incl_ESO548==0.0:
    max_incl_ESO548=90.0
if min_sigma_ESO548==0.0:
    min_sigma_ESO548=15.0
if max_sigma_ESO548==0.0:
    max_sigma_ESO548=70.0
if min_N0_ESO548==0.0:
    min_N0_ESO548=1.0
if max_N0_ESO548==0.0:
    max_N0_ESO548=15.0
if min_Y_ESO548==0.0:
    min_Y_ESO548=5.0
if max_Y_ESO548==0.0:
    max_Y_ESO548=100.0
if max_q_ESO548==0.0:
    max_q_ESO548=2.5
if min_tau_ESO548==0.0:
    min_tau_ESO548=10.0
if max_tau_ESO548==0.0:
    max_tau_ESO548=300.0
print >>file1, chi2_ESO548_2, dof_ESO548_2, incl_ESO548_Nenkova08, min_incl_ESO548, max_incl_ESO548, N0_ESO548_Nenkova08,min_N0_ESO548, max_N0_ESO548, sigma_ESO548_Nenkova08, min_sigma_ESO548, max_sigma_ESO548, Y_ESO548_Nenkova08, min_Y_ESO548, max_Y_ESO548, q_ESO548_Nenkova08, min_q_ESO548, max_q_ESO548, tau_ESO548_Nenkova08, min_tau_ESO548, max_tau_ESO548, norm, min, max, '#ESO548'

chi2_Mrk1018_2, dof_Mrk1018_2, incl_Mrk1018_Nenkova08, min_incl_Mrk1018, max_incl_Mrk1018, N0_Mrk1018_Nenkova08,min_N0_Mrk1018, max_N0_Mrk1018, sigma_Mrk1018_Nenkova08, min_sigma_Mrk1018, max_sigma_Mrk1018, Y_Mrk1018_Nenkova08, min_Y_Mrk1018, max_Y_Mrk1018, q_Mrk1018_Nenkova08, min_q_Mrk1018, max_q_Mrk1018, tau_Mrk1018_Nenkova08, min_tau_Mrk1018, max_tau_Mrk1018, norm, min, max = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/Mrk1018_Nenkova08_2_of_1s_ebv.txt', unpack='True')
if max_incl_Mrk1018==0.0:
    max_incl_Mrk1018=90.0
if min_sigma_Mrk1018==0.0:
    min_sigma_Mrk1018=15.0
if max_sigma_Mrk1018==0.0:
    max_sigma_Mrk1018=70.0
if min_N0_Mrk1018==0.0:
    min_N0_Mrk1018=1.0
if max_N0_Mrk1018==0.0:
    max_N0_Mrk1018=15.0
if min_Y_Mrk1018==0.0:
    min_Y_Mrk1018=5.0
if max_Y_Mrk1018==0.0:
    max_Y_Mrk1018=100.0
if max_q_Mrk1018==0.0:
    max_q_Mrk1018=2.5
if min_tau_Mrk1018==0.0:
    min_tau_Mrk1018=10.0
if max_tau_Mrk1018==0.0:
    max_tau_Mrk1018=300.0
print >>file1, chi2_Mrk1018_2, dof_Mrk1018_2, incl_Mrk1018_Nenkova08, min_incl_Mrk1018, max_incl_Mrk1018, N0_Mrk1018_Nenkova08,min_N0_Mrk1018, max_N0_Mrk1018, sigma_Mrk1018_Nenkova08, min_sigma_Mrk1018, max_sigma_Mrk1018, Y_Mrk1018_Nenkova08, min_Y_Mrk1018, max_Y_Mrk1018, q_Mrk1018_Nenkova08, min_q_Mrk1018, max_q_Mrk1018, tau_Mrk1018_Nenkova08, min_tau_Mrk1018, max_tau_Mrk1018, norm, min, max, '#Mrk1018'

chi2_ngc1275_1, dof_ngc1275_1, incl_ngc1275_Nenkova08, min_incl_ngc1275, max_incl_ngc1275, N0_ngc1275_Nenkova08,min_N0_ngc1275, max_N0_ngc1275, sigma_ngc1275_Nenkova08, min_sigma_ngc1275, max_sigma_ngc1275, Y_ngc1275_Nenkova08, min_Y_ngc1275, max_Y_ngc1275, q_ngc1275_Nenkova08, min_q_ngc1275, max_q_ngc1275, tau_ngc1275_Nenkova08, min_tau_ngc1275, max_tau_ngc1275, norm, min, max = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ngc1275_Nenkova08_1_of_1s_ebv.txt', unpack='True')
if max_incl_ngc1275==0.0:
    max_incl_ngc1275=90.0
if min_sigma_ngc1275==0.0:
    min_sigma_ngc1275=15.0
if max_sigma_ngc1275==0.0:
    max_sigma_ngc1275=70.0
if min_N0_ngc1275==0.0:
    min_N0_ngc1275=1.0
if max_N0_ngc1275==0.0:
    max_N0_ngc1275=15.0
if min_Y_ngc1275==0.0:
    min_Y_ngc1275=5.0
if max_Y_ngc1275==0.0:
    max_Y_ngc1275=100.0
if max_q_ngc1275==0.0:
    max_q_ngc1275=2.5
if min_tau_ngc1275==0.0:
    min_tau_ngc1275=10.0
if max_tau_ngc1275==0.0:
    max_tau_ngc1275=300.0
print >>file1, chi2_ngc1275_1, dof_ngc1275_1, incl_ngc1275_Nenkova08, min_incl_ngc1275, max_incl_ngc1275, N0_ngc1275_Nenkova08,min_N0_ngc1275, max_N0_ngc1275, sigma_ngc1275_Nenkova08, min_sigma_ngc1275, max_sigma_ngc1275, Y_ngc1275_Nenkova08, min_Y_ngc1275, max_Y_ngc1275, q_ngc1275_Nenkova08, min_q_ngc1275, max_q_ngc1275, tau_ngc1275_Nenkova08, min_tau_ngc1275, max_tau_ngc1275, norm, min, max, '#NGC1275'

chi2_ngc2110_4, dof_ngc2110_4, incl_ngc2110_Nenkova08, min_incl_ngc2110, max_incl_ngc2110, N0_ngc2110_Nenkova08,min_N0_ngc2110, max_N0_ngc2110, sigma_ngc2110_Nenkova08, min_sigma_ngc2110, max_sigma_ngc2110, Y_ngc2110_Nenkova08, min_Y_ngc2110, max_Y_ngc2110, q_ngc2110_Nenkova08, min_q_ngc2110, max_q_ngc2110, tau_ngc2110_Nenkova08, min_tau_ngc2110, max_tau_ngc2110, norm, min, max = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ngc2110_Nenkova08_4_of_1s_ebv.txt', unpack='True')
if max_incl_ngc2110==0.0:
    max_incl_ngc2110=90.0
if min_sigma_ngc2110==0.0:
    min_sigma_ngc2110=15.0
if max_sigma_ngc2110==0.0:
    max_sigma_ngc2110=70.0
if min_N0_ngc2110==0.0:
    min_N0_ngc2110=1.0
if max_N0_ngc2110==0.0:
    max_N0_ngc2110=15.0
if min_Y_ngc2110==0.0:
    min_Y_ngc2110=5.0
if max_Y_ngc2110==0.0:
    max_Y_ngc2110=100.0
if max_q_ngc2110==0.0:
    max_q_ngc2110=2.5
if min_tau_ngc2110==0.0:
    min_tau_ngc2110=10.0
if max_tau_ngc2110==0.0:
    max_tau_ngc2110=300.0
print >>file1, chi2_ngc2110_4, dof_ngc2110_4, incl_ngc2110_Nenkova08, min_incl_ngc2110, max_incl_ngc2110, N0_ngc2110_Nenkova08,min_N0_ngc2110, max_N0_ngc2110, sigma_ngc2110_Nenkova08, min_sigma_ngc2110, max_sigma_ngc2110, Y_ngc2110_Nenkova08, min_Y_ngc2110, max_Y_ngc2110, q_ngc2110_Nenkova08, min_q_ngc2110, max_q_ngc2110, tau_ngc2110_Nenkova08, min_tau_ngc2110, max_tau_ngc2110, norm, min, max, '#NGC2110'

chi2_ngc4258_4, dof_ngc4258_4, incl_ngc4258_Nenkova08, min_incl_ngc4258, max_incl_ngc4258, N0_ngc4258_Nenkova08,min_N0_ngc4258, max_N0_ngc4258, sigma_ngc4258_Nenkova08, min_sigma_ngc4258, max_sigma_ngc4258, Y_ngc4258_Nenkova08, min_Y_ngc4258, max_Y_ngc4258, q_ngc4258_Nenkova08, min_q_ngc4258, max_q_ngc4258, tau_ngc4258_Nenkova08, min_tau_ngc4258, max_tau_ngc4258, norm, min, max = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ngc4258_Nenkova08_4_of_1s_ebv.txt', unpack='True')
if max_incl_ngc4258==0.0:
    max_incl_ngc4258=90.0
if min_sigma_ngc4258==0.0:
    min_sigma_ngc4258=15.0
if max_sigma_ngc4258==0.0:
    max_sigma_ngc4258=70.0
if min_N0_ngc4258==0.0:
    min_N0_ngc4258=1.0
if max_N0_ngc4258==0.0:
    max_N0_ngc4258=15.0
if min_Y_ngc4258==0.0:
    min_Y_ngc4258=5.0
if max_Y_ngc4258==0.0:
    max_Y_ngc4258=100.0
if max_q_ngc4258==0.0:
    max_q_ngc4258=2.5
if min_tau_ngc4258==0.0:
    min_tau_ngc4258=10.0
if max_tau_ngc4258==0.0:
    max_tau_ngc4258=300.0
print >>file1, chi2_ngc4258_4, dof_ngc4258_4, incl_ngc4258_Nenkova08, min_incl_ngc4258, max_incl_ngc4258, N0_ngc4258_Nenkova08,min_N0_ngc4258, max_N0_ngc4258, sigma_ngc4258_Nenkova08, min_sigma_ngc4258, max_sigma_ngc4258, Y_ngc4258_Nenkova08, min_Y_ngc4258, max_Y_ngc4258, q_ngc4258_Nenkova08, min_q_ngc4258, max_q_ngc4258, tau_ngc4258_Nenkova08, min_tau_ngc4258, max_tau_ngc4258, norm, min, max, '#NGC4258'

chi2_pg0804_2, dof_pg0804_2, incl_pg0804_Nenkova08, min_incl_pg0804, max_incl_pg0804, N0_pg0804_Nenkova08,min_N0_pg0804, max_N0_pg0804, sigma_pg0804_Nenkova08, min_sigma_pg0804, max_sigma_pg0804, Y_pg0804_Nenkova08, min_Y_pg0804, max_Y_pg0804, q_pg0804_Nenkova08, min_q_pg0804, max_q_pg0804, tau_pg0804_Nenkova08, min_tau_pg0804, max_tau_pg0804, norm, min, max= loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg0804_Nenkova08_2_of_1s_ebv.txt', unpack='True')
if max_incl_pg0804==0.0:
    max_incl_pg0804=90.0
if min_sigma_pg0804==0.0:
    min_sigma_pg0804=15.0
if max_sigma_pg0804==0.0:
    max_sigma_pg0804=70.0
if min_N0_pg0804==0.0:
    min_N0_pg0804=1.0
if max_N0_pg0804==0.0:
    max_N0_pg0804=15.0
if min_Y_pg0804==0.0:
    min_Y_pg0804=5.0
if max_Y_pg0804==0.0:
    max_Y_pg0804=100.0
if max_q_pg0804==0.0:
    max_q_pg0804=2.5
if min_tau_pg0804==0.0:
    min_tau_pg0804=10.0
if max_tau_pg0804==0.0:
    max_tau_pg0804=300.0
print >>file1, chi2_pg0804_2, dof_pg0804_2, incl_pg0804_Nenkova08, min_incl_pg0804, max_incl_pg0804, N0_pg0804_Nenkova08,min_N0_pg0804, max_N0_pg0804, sigma_pg0804_Nenkova08, min_sigma_pg0804, max_sigma_pg0804, Y_pg0804_Nenkova08, min_Y_pg0804, max_Y_pg0804, q_pg0804_Nenkova08, min_q_pg0804, max_q_pg0804, tau_pg0804_Nenkova08, min_tau_pg0804, max_tau_pg0804, norm, min, max, '#PG0804+'

chi2_pg0844_2, dof_pg0844_2, incl_pg0844_Nenkova08, min_incl_pg0844, max_incl_pg0844, N0_pg0844_Nenkova08,min_N0_pg0844, max_N0_pg0844, sigma_pg0844_Nenkova08, min_sigma_pg0844, max_sigma_pg0844, Y_pg0844_Nenkova08, min_Y_pg0844, max_Y_pg0844, q_pg0844_Nenkova08, min_q_pg0844, max_q_pg0844, tau_pg0844_Nenkova08, min_tau_pg0844, max_tau_pg0844, norm, min, max = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg0844_Nenkova08_2_of_1s_ebv.txt', unpack='True')
if max_incl_pg0844==0.0:
    max_incl_pg0844=90.0
if min_sigma_pg0844==0.0:
    min_sigma_pg0844=15.0
if max_sigma_pg0844==0.0:
    max_sigma_pg0844=70.0
if min_N0_pg0844==0.0:
    min_N0_pg0844=1.0
if max_N0_pg0844==0.0:
    max_N0_pg0844=15.0
if min_Y_pg0844==0.0:
    min_Y_pg0844=5.0
if max_Y_pg0844==0.0:
    max_Y_pg0844=100.0
if max_q_pg0844==0.0:
    max_q_pg0844=2.5
if min_tau_pg0844==0.0:
    min_tau_pg0844=10.0
if max_tau_pg0844==0.0:
    max_tau_pg0844=300.0
print >>file1, chi2_pg0844_2, dof_pg0844_2, incl_pg0844_Nenkova08, min_incl_pg0844, max_incl_pg0844, N0_pg0844_Nenkova08,min_N0_pg0844, max_N0_pg0844, sigma_pg0844_Nenkova08, min_sigma_pg0844, max_sigma_pg0844, Y_pg0844_Nenkova08, min_Y_pg0844, max_Y_pg0844, q_pg0844_Nenkova08, min_q_pg0844, max_q_pg0844, tau_pg0844_Nenkova08, min_tau_pg0844, max_tau_pg0844, norm, min, max, '#PG0844+'

chi2_pg1011_2, dof_pg1011_2, incl_pg1011_Nenkova08, min_incl_pg1011, max_incl_pg1011, N0_pg1011_Nenkova08,min_N0_pg1011, max_N0_pg1011, sigma_pg1011_Nenkova08, min_sigma_pg1011, max_sigma_pg1011, Y_pg1011_Nenkova08, min_Y_pg1011, max_Y_pg1011, q_pg1011_Nenkova08, min_q_pg1011, max_q_pg1011, tau_pg1011_Nenkova08, min_tau_pg1011, max_tau_pg1011, norm, min, max = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1011_Nenkova08_2_of_1s_ebv.txt', unpack='True')
if max_incl_pg1011==0.0:
    max_incl_pg1011=90.0
if min_sigma_pg1011==0.0:
    min_sigma_pg1011=15.0
if max_sigma_pg1011==0.0:
    max_sigma_pg1011=70.0
if min_N0_pg1011==0.0:
    min_N0_pg1011=1.0
if max_N0_pg1011==0.0:
    max_N0_pg1011=15.0
if min_Y_pg1011==0.0:
    min_Y_pg1011=5.0
if max_Y_pg1011==0.0:
    max_Y_pg1011=100.0
if max_q_pg1011==0.0:
    max_q_pg1011=2.5
if min_tau_pg1011==0.0:
    min_tau_pg1011=10.0
if max_tau_pg1011==0.0:
    max_tau_pg1011=300.0
print >>file1, chi2_pg1011_2, dof_pg1011_2, incl_pg1011_Nenkova08, min_incl_pg1011, max_incl_pg1011, N0_pg1011_Nenkova08,min_N0_pg1011, max_N0_pg1011, sigma_pg1011_Nenkova08, min_sigma_pg1011, max_sigma_pg1011, Y_pg1011_Nenkova08, min_Y_pg1011, max_Y_pg1011, q_pg1011_Nenkova08, min_q_pg1011, max_q_pg1011, tau_pg1011_Nenkova08, min_tau_pg1011, max_tau_pg1011, norm, min, max, '#PG1011+'

chi2_pg1211_2, dof_pg1211_2, incl_pg1211_Nenkova08, min_incl_pg1211, max_incl_pg1211, N0_pg1211_Nenkova08,min_N0_pg1211, max_N0_pg1211, sigma_pg1211_Nenkova08, min_sigma_pg1211, max_sigma_pg1211, Y_pg1211_Nenkova08, min_Y_pg1211, max_Y_pg1211, q_pg1211_Nenkova08, min_q_pg1211, max_q_pg1211, tau_pg1211_Nenkova08, min_tau_pg1211, max_tau_pg1211, norm, min, max = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1211_Nenkova08_2_of_1s_ebv.txt', unpack='True')
if max_incl_pg1211==0.0:
    max_incl_pg1211=90.0
if min_sigma_pg1211==0.0:
    min_sigma_pg1211=15.0
if max_sigma_pg1211==0.0:
    max_sigma_pg1211=70.0
if min_N0_pg1211==0.0:
    min_N0_pg1211=1.0
if max_N0_pg1211==0.0:
    max_N0_pg1211=15.0
if min_Y_pg1211==0.0:
    min_Y_pg1211=5.0
if max_Y_pg1211==0.0:
    max_Y_pg1211=100.0
if max_q_pg1211==0.0:
    max_q_pg1211=2.5
if min_tau_pg1211==0.0:
    min_tau_pg1211=10.0
if max_tau_pg1211==0.0:
    max_tau_pg1211=300.0
print >>file1, chi2_pg1211_2, dof_pg1211_2, incl_pg1211_Nenkova08, min_incl_pg1211, max_incl_pg1211, N0_pg1211_Nenkova08,min_N0_pg1211, max_N0_pg1211, sigma_pg1211_Nenkova08, min_sigma_pg1211, max_sigma_pg1211, Y_pg1211_Nenkova08, min_Y_pg1211, max_Y_pg1211, q_pg1211_Nenkova08, min_q_pg1211, max_q_pg1211, tau_pg1211_Nenkova08, min_tau_pg1211, max_tau_pg1211, norm, min, max, '#PG1211+'

chi2_pg1411_2, dof_pg1411_2, incl_pg1411_Nenkova08, min_incl_pg1411, max_incl_pg1411, N0_pg1411_Nenkova08,min_N0_pg1411, max_N0_pg1411, sigma_pg1411_Nenkova08, min_sigma_pg1411, max_sigma_pg1411, Y_pg1411_Nenkova08, min_Y_pg1411, max_Y_pg1411, q_pg1411_Nenkova08, min_q_pg1411, max_q_pg1411, tau_pg1411_Nenkova08, min_tau_pg1411, max_tau_pg1411, norm, min, max = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1411_Nenkova08_2_of_1s_ebv.txt', unpack='True')
if max_incl_pg1411==0.0:
    max_incl_pg1411=90.0
if min_sigma_pg1411==0.0:
    min_sigma_pg1411=15.0
if max_sigma_pg1411==0.0:
    max_sigma_pg1411=70.0
if min_N0_pg1411==0.0:
    min_N0_pg1411=1.0
if max_N0_pg1411==0.0:
    max_N0_pg1411=15.0
if min_Y_pg1411==0.0:
    min_Y_pg1411=5.0
if max_Y_pg1411==0.0:
    max_Y_pg1411=100.0
if max_q_pg1411==0.0:
    max_q_pg1411=2.5
if min_tau_pg1411==0.0:
    min_tau_pg1411=10.0
if max_tau_pg1411==0.0:
    max_tau_pg1411=300.0
print >>file1, chi2_pg1411_2, dof_pg1411_2, incl_pg1411_Nenkova08, min_incl_pg1411, max_incl_pg1411, N0_pg1411_Nenkova08,min_N0_pg1411, max_N0_pg1411, sigma_pg1411_Nenkova08, min_sigma_pg1411, max_sigma_pg1411, Y_pg1411_Nenkova08, min_Y_pg1411, max_Y_pg1411, q_pg1411_Nenkova08, min_q_pg1411, max_q_pg1411, tau_pg1411_Nenkova08, min_tau_pg1411, max_tau_pg1411, norm, min, max, '#PG1411+'

chi2_pg1535_2, dof_pg1535_2, incl_pg1535_Nenkova08, min_incl_pg1535, max_incl_pg1535, N0_pg1535_Nenkova08,min_N0_pg1535, max_N0_pg1535, sigma_pg1535_Nenkova08, min_sigma_pg1535, max_sigma_pg1535, Y_pg1535_Nenkova08, min_Y_pg1535, max_Y_pg1535, q_pg1535_Nenkova08, min_q_pg1535, max_q_pg1535, tau_pg1535_Nenkova08, min_tau_pg1535, max_tau_pg1535, norm, min, max = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1535_Nenkova08_2_of_1s_ebv.txt', unpack='True')
if max_incl_pg1535==0.0:
    max_incl_pg1535=90.0
if min_sigma_pg1535==0.0:
    min_sigma_pg1535=15.0
if max_sigma_pg1535==0.0:
    max_sigma_pg1535=70.0
if min_N0_pg1535==0.0:
    min_N0_pg1535=1.0
if max_N0_pg1535==0.0:
    max_N0_pg1535=15.0
if min_Y_pg1535==0.0:
    min_Y_pg1535=5.0
if max_Y_pg1535==0.0:
    max_Y_pg1535=100.0
if max_q_pg1535==0.0:
    max_q_pg1535=2.5
if min_tau_pg1535==0.0:
    min_tau_pg1535=10.0
if max_tau_pg1535==0.0:
    max_tau_pg1535=300.0
print >>file1, chi2_pg1535_2, dof_pg1535_2, incl_pg1535_Nenkova08, min_incl_pg1535, max_incl_pg1535, N0_pg1535_Nenkova08,min_N0_pg1535, max_N0_pg1535, sigma_pg1535_Nenkova08, min_sigma_pg1535, max_sigma_pg1535, Y_pg1535_Nenkova08, min_Y_pg1535, max_Y_pg1535, q_pg1535_Nenkova08, min_q_pg1535, max_q_pg1535, tau_pg1535_Nenkova08, min_tau_pg1535, max_tau_pg1535, norm, min, max, '#PG1535+'

chi2_pg2214_2, dof_pg2214_2, incl_pg2214_Nenkova08, min_incl_pg2214, max_incl_pg2214, N0_pg2214_Nenkova08,min_N0_pg2214, max_N0_pg2214, sigma_pg2214_Nenkova08, min_sigma_pg2214, max_sigma_pg2214, Y_pg2214_Nenkova08, min_Y_pg2214, max_Y_pg2214, q_pg2214_Nenkova08, min_q_pg2214, max_q_pg2214, tau_pg2214_Nenkova08, min_tau_pg2214, max_tau_pg2214, norm, min, max = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg2214_Nenkova08_2_of_1s_ebv.txt', unpack='True')
if max_incl_pg2214==0.0:
    max_incl_pg2214=90.0
if min_sigma_pg2214==0.0:
    min_sigma_pg2214=15.0
if max_sigma_pg2214==0.0:
    max_sigma_pg2214=70.0
if min_N0_pg2214==0.0:
    min_N0_pg2214=1.0
if max_N0_pg2214==0.0:
    max_N0_pg2214=15.0
if min_Y_pg2214==0.0:
    min_Y_pg2214=5.0
if max_Y_pg2214==0.0:
    max_Y_pg2214=100.0
if max_q_pg2214==0.0:
    max_q_pg2214=2.5
if min_tau_pg2214==0.0:
    min_tau_pg2214=10.0
if max_tau_pg2214==0.0:
    max_tau_pg2214=300.0
print >>file1, chi2_pg2214_2, dof_pg2214_2, incl_pg2214_Nenkova08, min_incl_pg2214, max_incl_pg2214, N0_pg2214_Nenkova08,min_N0_pg2214, max_N0_pg2214, sigma_pg2214_Nenkova08, min_sigma_pg2214, max_sigma_pg2214, Y_pg2214_Nenkova08, min_Y_pg2214, max_Y_pg2214, q_pg2214_Nenkova08, min_q_pg2214, max_q_pg2214, tau_pg2214_Nenkova08, min_tau_pg2214, max_tau_pg2214, norm, min, max, '#PG2214+'

file1.close()


