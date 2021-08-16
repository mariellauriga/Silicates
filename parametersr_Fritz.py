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

file1 = open('parameters_Fritz.dat','w+')
print >>file1, '#chi2', 'dof', 'incl', 'min', 'max', 'sigma','min', 'max', 'gamma', 'min', 'max', 'beta', 'min', 'max', 'Y', 'min', 'max', 'tau', 'min', 'max', 'norm', 'min', 'max', 'name'
chi2_3c120, dof_3c120, incl_3c120_fritz06,min_incl_3c120, max_incl_3c120, sigma_3c120_fritz06,min_sigma_3c120, max_sigma_3c120, gamma_3c120_fritz06, min_gamma_3c120, max_gamma_3c120, beta_3c120_fritz06, min_beta_3c120, max_beta_3c120, Y_3c120_fritz06, min_Y_3c120, max_Y_3c120, tau_3c120_fritz06, min_tau_3c120, max_tau_3c120, norm_3c120, min_norm_3c120, max_norm_3c120  = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/3c120_Fritz06_4_of_1s_ebv.txt', unpack='True')
if max_incl_3c120==0.0:
    max_incl_3c120=90.0
if min_sigma_3c120==0.0:
    min_sigma_3c120=20.0
if max_sigma_3c120==0.0:
    max_sigma_3c120=60.0
if max_gamma_3c120==0.0:
    max_gamma_3c120=6.0
if min_beta_3c120==0.0:
    min_beta_3c120=-1.0
if max_beta_3c120==0.0:
    max_beta_3c120=-0.01
if min_Y_3c120==0.0:
    min_Y_3c120=10.0
if max_Y_3c120==0.0:
    max_Y_3c120=150.0
if min_tau_3c120==0.0:
    min_tau_3c120=0.1
if max_tau_3c120==0.0:
    max_tau_3c120=10.0
print >>file1,chi2_3c120, dof_3c120, incl_3c120_fritz06,min_incl_3c120, max_incl_3c120, sigma_3c120_fritz06,min_sigma_3c120, max_sigma_3c120, gamma_3c120_fritz06, min_gamma_3c120, max_gamma_3c120, beta_3c120_fritz06, min_beta_3c120, max_beta_3c120, Y_3c120_fritz06, min_Y_3c120, max_Y_3c120, tau_3c120_fritz06, min_tau_3c120, max_tau_3c120, norm_3c120, min_norm_3c120, max_norm_3c120, '#3c120'

chi2_OQ208_1, dof_OQ208_1, incl_OQ208_fritz06,min_incl_OQ208, max_incl_OQ208, sigma_OQ208_fritz06,min_sigma_OQ208, max_sigma_OQ208, gamma_OQ208_fritz06, min_gamma_OQ208, max_gamma_OQ208, beta_OQ208_fritz06, min_beta_OQ208, max_beta_OQ208, Y_OQ208_fritz06, min_Y_OQ208, max_Y_OQ208, tau_OQ208_fritz06, min_tau_OQ208, max_tau_OQ208, norm_OQ208, min_norm_OQ208, max_norm_OQ208 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/OQ208_Fritz06_1_of_1s_ebv.txt', unpack='True')
if max_incl_OQ208==0.0:
    max_incl_OQ208=90.0
if min_sigma_OQ208==0.0:
    min_sigma_OQ208=20.0
if max_sigma_OQ208==0.0:
    max_sigma_OQ208=60.0
if max_gamma_OQ208==0.0:
    max_gamma_OQ208=6.0
if min_beta_OQ208==0.0:
    min_beta_OQ208=-1.0
if max_beta_OQ208==0.0:
    max_beta_OQ208=-0.01
if min_Y_OQ208==0.0:
    min_Y_OQ208=10.0
if max_Y_OQ208==0.0:
    max_Y_OQ208=150.0
if min_tau_OQ208==0.0:
    min_tau_OQ208=0.1
if max_tau_OQ208==0.0:
    max_tau_OQ208=10.0
print >>file1, chi2_OQ208_1, dof_OQ208_1, incl_OQ208_fritz06,min_incl_OQ208, max_incl_OQ208, sigma_OQ208_fritz06,min_sigma_OQ208, max_sigma_OQ208, gamma_OQ208_fritz06, min_gamma_OQ208, max_gamma_OQ208, beta_OQ208_fritz06, min_beta_OQ208, max_beta_OQ208, Y_OQ208_fritz06, min_Y_OQ208, max_Y_OQ208, tau_OQ208_fritz06, min_tau_OQ208, max_tau_OQ208, norm_OQ208, min_norm_OQ208, max_norm_OQ208, '#OQ208'

chi2_Mrk1018_1, dof_Mrk1018_1, incl_Mrk1018_fritz06,min_incl_Mrk1018, max_incl_Mrk1018, sigma_Mrk1018_fritz06,min_sigma_Mrk1018, max_sigma_Mrk1018, gamma_Mrk1018_fritz06, min_gamma_Mrk1018, max_gamma_Mrk1018, beta_Mrk1018_fritz06, min_beta_Mrk1018, max_beta_Mrk1018, Y_Mrk1018_fritz06, min_Y_Mrk1018, max_Y_Mrk1018, tau_Mrk1018_fritz06, min_tau_Mrk1018, max_tau_Mrk1018, norm_Mrk1018, min_norm_Mrk1018, max_norm_Mrk1018  = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/Mrk1018_Fritz06_1_of_1s_ebv.txt', unpack='True')
if max_incl_Mrk1018==0.0:
    max_incl_Mrk1018=90.0
if min_sigma_Mrk1018==0.0:
    min_sigma_Mrk1018=20.0
if max_sigma_Mrk1018==0.0:
    max_sigma_Mrk1018=60.0
if max_gamma_Mrk1018==0.0:
    max_gamma_Mrk1018=6.0
if min_beta_Mrk1018==0.0:
    min_beta_Mrk1018=-1.0
if max_beta_Mrk1018==0.0:
    max_beta_Mrk1018=-0.01
if min_Y_Mrk1018==0.0:
    min_Y_Mrk1018=10.0
if max_Y_Mrk1018==0.0:
    max_Y_Mrk1018=150.0
if min_tau_Mrk1018==0.0:
    min_tau_Mrk1018=0.1
if max_tau_Mrk1018==0.0:
    max_tau_Mrk1018=10.0
print >>file1, chi2_Mrk1018_1, dof_Mrk1018_1, incl_Mrk1018_fritz06,min_incl_Mrk1018, max_incl_Mrk1018, sigma_Mrk1018_fritz06,min_sigma_Mrk1018, max_sigma_Mrk1018, gamma_Mrk1018_fritz06, min_gamma_Mrk1018, max_gamma_Mrk1018, beta_Mrk1018_fritz06, min_beta_Mrk1018, max_beta_Mrk1018, Y_Mrk1018_fritz06, min_Y_Mrk1018, max_Y_Mrk1018, tau_Mrk1018_fritz06, min_tau_Mrk1018, max_tau_Mrk1018, norm_Mrk1018, min_norm_Mrk1018, max_norm_Mrk1018, '#Mrk1018'

chi2_ngc4258_3, dof_ngc4258_3, incl_ngc4258_fritz06,min_incl_ngc4258, max_incl_ngc4258, sigma_ngc4258_fritz06,min_sigma_ngc4258, max_sigma_ngc4258, gamma_ngc4258_fritz06, min_gamma_ngc4258, max_gamma_ngc4258, beta_ngc4258_fritz06, min_beta_ngc4258, max_beta_ngc4258, Y_ngc4258_fritz06, min_Y_ngc4258, max_Y_ngc4258, tau_ngc4258_fritz06, min_tau_ngc4258, max_tau_ngc4258, norm_ngc4258, min_norm_ngc4258, max_norm_ngc4258 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ngc4258_Fritz06_3_of_1s_ebv.txt', unpack='True')
if max_incl_ngc4258==0.0:
    max_incl_ngc4258=90.0
if min_sigma_ngc4258==0.0:
    min_sigma_ngc4258=20.0
if max_sigma_ngc4258==0.0:
    max_sigma_ngc4258=60.0
if max_gamma_ngc4258==0.0:
    max_gamma_ngc4258=6.0
if min_beta_ngc4258==0.0:
    min_beta_ngc4258=-1.0
if max_beta_ngc4258==0.0:
    max_beta_ngc4258=-0.01
if min_Y_ngc4258==0.0:
    min_Y_ngc4258=10.0
if max_Y_ngc4258==0.0:
    max_Y_ngc4258=150.0
if min_tau_ngc4258==0.0:
    min_tau_ngc4258=0.1
if max_tau_ngc4258==0.0:
    max_tau_ngc4258=10.0
print >>file1, chi2_ngc4258_3, dof_ngc4258_3, incl_ngc4258_fritz06,min_incl_ngc4258, max_incl_ngc4258, sigma_ngc4258_fritz06,min_sigma_ngc4258, max_sigma_ngc4258, gamma_ngc4258_fritz06, min_gamma_ngc4258, max_gamma_ngc4258, beta_ngc4258_fritz06, min_beta_ngc4258, max_beta_ngc4258, Y_ngc4258_fritz06, min_Y_ngc4258, max_Y_ngc4258, tau_ngc4258_fritz06, min_tau_ngc4258, max_tau_ngc4258, norm_ngc4258, min_norm_ngc4258, max_norm_ngc4258, '#NGC4258'

chi2_pg0804_2, dof_pg0804_2, incl_pg0804_fritz06,min_incl_pg0804, max_incl_pg0804, sigma_pg0804_fritz06,min_sigma_pg0804, max_sigma_pg0804, gamma_pg0804_fritz06, min_gamma_pg0804, max_gamma_pg0804, beta_pg0804_fritz06, min_beta_pg0804, max_beta_pg0804, Y_pg0804_fritz06, min_Y_pg0804, max_Y_pg0804, tau_pg0804_fritz06, min_tau_pg0804, max_tau_pg0804, norm_pg0804, min_norm_pg0804, max_norm_pg0804  = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg0804_Fritz06_2_of_1s_ebv.txt', unpack='True')
if max_incl_pg0804==0.0:
    max_incl_pg0804=90.0
if min_sigma_pg0804==0.0:
    min_sigma_pg0804=20.0
if max_sigma_pg0804==0.0:
    max_sigma_pg0804=60.0
if max_gamma_pg0804==0.0:
    max_gamma_pg0804=6.0
if min_beta_pg0804==0.0:
    min_beta_pg0804=-1.0
if max_beta_pg0804==0.0:
    max_beta_pg0804=-0.01
if min_Y_pg0804==0.0:
    min_Y_pg0804=10.0
if max_Y_pg0804==0.0:
    max_Y_pg0804=150.0
if min_tau_pg0804==0.0:
    min_tau_pg0804=0.1
if max_tau_pg0804==0.0:
    max_tau_pg0804=10.0
print >>file1, chi2_pg0804_2, dof_pg0804_2, incl_pg0804_fritz06,min_incl_pg0804, max_incl_pg0804, sigma_pg0804_fritz06,min_sigma_pg0804, max_sigma_pg0804, gamma_pg0804_fritz06, min_gamma_pg0804, max_gamma_pg0804, beta_pg0804_fritz06, min_beta_pg0804, max_beta_pg0804, Y_pg0804_fritz06, min_Y_pg0804, max_Y_pg0804, tau_pg0804_fritz06, min_tau_pg0804, max_tau_pg0804, norm_pg0804, min_norm_pg0804, max_norm_pg0804, '#PG0804+'

chi2_pg0844_2, dof_pg0844_2, incl_pg0844_fritz06,min_incl_pg0844, max_incl_pg0844, sigma_pg0844_fritz06,min_sigma_pg0844, max_sigma_pg0844, gamma_pg0844_fritz06, min_gamma_pg0844, max_gamma_pg0844, beta_pg0844_fritz06, min_beta_pg0844, max_beta_pg0844, Y_pg0844_fritz06, min_Y_pg0844, max_Y_pg0844, tau_pg0844_fritz06, min_tau_pg0844, max_tau_pg0844, norm_pg0844, min_norm_pg0844, max_norm_pg0844  = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg0844_Fritz06_2_of_1s_ebv.txt', unpack='True')
if max_incl_pg0844==0.0:
    max_incl_pg0844=90.0
if min_sigma_pg0844==0.0:
    min_sigma_pg0844=20.0
if max_sigma_pg0844==0.0:
    max_sigma_pg0844=60.0
if max_gamma_pg0844==0.0:
    max_gamma_pg0844=6.0
if min_beta_pg0844==0.0:
    min_beta_pg0844=-1.0
if max_beta_pg0844==0.0:
    max_beta_pg0844=-0.01
if min_Y_pg0844==0.0:
    min_Y_pg0844=10.0
if max_Y_pg0844==0.0:
    max_Y_pg0844=150.0
if min_tau_pg0844==0.0:
    min_tau_pg0844=0.1
if max_tau_pg0844==0.0:
    max_tau_pg0844=10.0
print >>file1, chi2_pg0844_2, dof_pg0844_2, incl_pg0844_fritz06,min_incl_pg0844, max_incl_pg0844, sigma_pg0844_fritz06,min_sigma_pg0844, max_sigma_pg0844, gamma_pg0844_fritz06, min_gamma_pg0844, max_gamma_pg0844, beta_pg0844_fritz06, min_beta_pg0844, max_beta_pg0844, Y_pg0844_fritz06, min_Y_pg0844, max_Y_pg0844, tau_pg0844_fritz06, min_tau_pg0844, max_tau_pg0844, norm_pg0844, min_norm_pg0844, max_norm_pg0844, '#PG0844+'

chi2_pg1011_1, dof_pg1011_1, incl_pg1011_fritz06,min_incl_pg1011, max_incl_pg1011, sigma_pg1011_fritz06,min_sigma_pg1011, max_sigma_pg1011, gamma_pg1011_fritz06, min_gamma_pg1011, max_gamma_pg1011, beta_pg1011_fritz06, min_beta_pg1011, max_beta_pg1011, Y_pg1011_fritz06, min_Y_pg1011, max_Y_pg1011, tau_pg1011_fritz06, min_tau_pg1011, max_tau_pg1011, norm_pg1011, min_norm_pg1011, max_norm_pg1011  = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1011_Fritz06_1_of_1s_ebv.txt', unpack='True')
if max_incl_pg1011==0.0:
    max_incl_pg1011=90.0
if min_sigma_pg1011==0.0:
    min_sigma_pg1011=20.0
if max_sigma_pg1011==0.0:
    max_sigma_pg1011=60.0
if max_gamma_pg1011==0.0:
    max_gamma_pg1011=6.0
if min_beta_pg1011==0.0:
    min_beta_pg1011=-1.0
if max_beta_pg1011==0.0:
    max_beta_pg1011=-0.01
if min_Y_pg1011==0.0:
    min_Y_pg1011=10.0
if max_Y_pg1011==0.0:
    max_Y_pg1011=150.0
if min_tau_pg1011==0.0:
    min_tau_pg1011=0.1
if max_tau_pg1011==0.0:
    max_tau_pg1011=10.0
print >>file1, chi2_pg1011_1, dof_pg1011_1, incl_pg1011_fritz06,min_incl_pg1011, max_incl_pg1011, sigma_pg1011_fritz06,min_sigma_pg1011, max_sigma_pg1011, gamma_pg1011_fritz06, min_gamma_pg1011, max_gamma_pg1011, beta_pg1011_fritz06, min_beta_pg1011, max_beta_pg1011, Y_pg1011_fritz06, min_Y_pg1011, max_Y_pg1011, tau_pg1011_fritz06, min_tau_pg1011, max_tau_pg1011, norm_pg1011, min_norm_pg1011, max_norm_pg1011, '#PG1011+'

chi2_pg1211_4, dof_pg1211_4, incl_pg1211_fritz06,min_incl_pg1211, max_incl_pg1211, sigma_pg1211_fritz06,min_sigma_pg1211, max_sigma_pg1211, gamma_pg1211_fritz06, min_gamma_pg1211, max_gamma_pg1211, beta_pg1211_fritz06, min_beta_pg1211, max_beta_pg1211, Y_pg1211_fritz06, min_Y_pg1211, max_Y_pg1211, tau_pg1211_fritz06, min_tau_pg1211, max_tau_pg1211, norm_pg1211, min_norm_pg1211, max_norm_pg1211  = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1211_Fritz06_4_of_1s_ebv.txt', unpack='True')
if max_incl_pg1211==0.0:
    max_incl_pg1211=90.0
if min_sigma_pg1211==0.0:
    min_sigma_pg1211=20.0
if max_sigma_pg1211==0.0:
    max_sigma_pg1211=60.0
if max_gamma_pg1211==0.0:
    max_gamma_pg1211=6.0
if min_beta_pg1211==0.0:
    min_beta_pg1211=-1.0
if max_beta_pg1211==0.0:
    max_beta_pg1211=-0.01
if min_Y_pg1211==0.0:
    min_Y_pg1211=10.0
if max_Y_pg1211==0.0:
    max_Y_pg1211=150.0
if min_tau_pg1211==0.0:
    min_tau_pg1211=0.1
if max_tau_pg1211==0.0:
    max_tau_pg1211=10.0
print >>file1, chi2_pg1211_4, dof_pg1211_4, incl_pg1211_fritz06,min_incl_pg1211, max_incl_pg1211, sigma_pg1211_fritz06,min_sigma_pg1211, max_sigma_pg1211, gamma_pg1211_fritz06, min_gamma_pg1211, max_gamma_pg1211, beta_pg1211_fritz06, min_beta_pg1211, max_beta_pg1211, Y_pg1211_fritz06, min_Y_pg1211, max_Y_pg1211, tau_pg1211_fritz06, min_tau_pg1211, max_tau_pg1211, norm_pg1211, min_norm_pg1211, max_norm_pg1211, '#PG1211+'

chi2_pg1535_2, dof_pg1535_2, incl_pg1535_fritz06,min_incl_pg1535, max_incl_pg1535, sigma_pg1535_fritz06,min_sigma_pg1535, max_sigma_pg1535, gamma_pg1535_fritz06, min_gamma_pg1535, max_gamma_pg1535, beta_pg1535_fritz06, min_beta_pg1535, max_beta_pg1535, Y_pg1535_fritz06, min_Y_pg1535, max_Y_pg1535, tau_pg1535_fritz06, min_tau_pg1535, max_tau_pg1535, norm_pg1535, min_norm_pg1535, max_norm_pg1535 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1535_Fritz06_2_of_1s_ebv.txt', unpack='True')
if max_incl_pg1535==0.0:
    max_incl_pg1535=90.0
if min_sigma_pg1535==0.0:
    min_sigma_pg1535=20.0
if max_sigma_pg1535==0.0:
    max_sigma_pg1535=60.0
if max_gamma_pg1535==0.0:
    max_gamma_pg1535=6.0
if min_beta_pg1535==0.0:
    min_beta_pg1535=-1.0
if max_beta_pg1535==0.0:
    max_beta_pg1535=-0.01
if min_Y_pg1535==0.0:
    min_Y_pg1535=10.0
if max_Y_pg1535==0.0:
    max_Y_pg1535=150.0
if min_tau_pg1535==0.0:
    min_tau_pg1535=0.1
if max_tau_pg1535==0.0:
    max_tau_pg1535=10.0
print >>file1, chi2_pg1535_2, dof_pg1535_2, incl_pg1535_fritz06,min_incl_pg1535, max_incl_pg1535, sigma_pg1535_fritz06,min_sigma_pg1535, max_sigma_pg1535, gamma_pg1535_fritz06, min_gamma_pg1535, max_gamma_pg1535, beta_pg1535_fritz06, min_beta_pg1535, max_beta_pg1535, Y_pg1535_fritz06, min_Y_pg1535, max_Y_pg1535, tau_pg1535_fritz06, min_tau_pg1535, max_tau_pg1535, norm_pg1535, min_norm_pg1535, max_norm_pg1535, '#PG1535+'

chi2_pg2214_2, dof_pg2214_2, incl_pg2214_fritz06,min_incl_pg2214, max_incl_pg2214, sigma_pg2214_fritz06,min_sigma_pg2214, max_sigma_pg2214, gamma_pg2214_fritz06, min_gamma_pg2214, max_gamma_pg2214, beta_pg2214_fritz06, min_beta_pg2214, max_beta_pg2214, Y_pg2214_fritz06, min_Y_pg2214, max_Y_pg2214, tau_pg2214_fritz06, min_tau_pg2214, max_tau_pg2214, norm_pg2214, min_norm_pg2214, max_norm_pg2214  = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg2214_Fritz06_4_of_1s_ebv.txt', unpack='True')
if max_incl_pg2214==0.0:
    max_incl_pg2214=90.0
if min_sigma_pg2214==0.0:
    min_sigma_pg2214=20.0
if max_sigma_pg2214==0.0:
    max_sigma_pg2214=60.0
if max_gamma_pg2214==0.0:
    max_gamma_pg2214=6.0
if min_beta_pg2214==0.0:
    min_beta_pg2214=-1.0
if max_beta_pg2214==0.0:
    max_beta_pg2214=-0.01
if min_Y_pg2214==0.0:
    min_Y_pg2214=10.0
if max_Y_pg2214==0.0:
    max_Y_pg2214=150.0
if min_tau_pg2214==0.0:
    min_tau_pg2214=0.1
if max_tau_pg2214==0.0:
    max_tau_pg2214=10.0
print >>file1, chi2_pg2214_2, dof_pg2214_2, incl_pg2214_fritz06,min_incl_pg2214, max_incl_pg2214, sigma_pg2214_fritz06,min_sigma_pg2214, max_sigma_pg2214, gamma_pg2214_fritz06, min_gamma_pg2214, max_gamma_pg2214, beta_pg2214_fritz06, min_beta_pg2214, max_beta_pg2214, Y_pg2214_fritz06, min_Y_pg2214, max_Y_pg2214, tau_pg2214_fritz06, min_tau_pg2214, max_tau_pg2214, norm_pg2214, min_norm_pg2214, max_norm_pg2214, '#PG2214+'

file1.close()


