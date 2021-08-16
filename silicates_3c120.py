import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import scipy as scipy
import matplotlib.lines as mlines
import itertools
from scipy.interpolate import interp1d

##########Names###########
# Look at the excel table in drive "AGN sample"
#Defining the resolution of nuclear spectrum
############################
#Reading the spectra
import prep as pr
nx1 = pr.x12
ny1 = pr.y12
ney1 = pr.ey12
z = pr.z_12

print 'spec=',nx1[0], nx1[-1]
f1 = interp1d(nx1,ny1, 'slinear')
ferr = interp1d(nx1,ney1)
#####################
s1 = arange(6.,7.,0.1,dtype=float)
s2 = arange(8.15,8.87,0.1,dtype=float)
s3 = arange(9.25,10.14,0.1,dtype=float)
s4 = arange(10.73,11.02,0.1,dtype=float)
s5 = arange(11.52,12.65,0.1,dtype=float)
s6 = arange(13.5,14.0,0.1,dtype=float)
s7 = arange(14.6,15.27,0.1,dtype=float)
s8 = arange(15.87,16.71,0.1,dtype=float)
s9 = arange(17.4,18.45,0.1,dtype=float)
s10 = arange(19.1, 19.43,0.1,dtype=float)
s11 = arange(21.22, 22.21,0.1,dtype=float)
s12 = arange(22.89,23.68,0.1,dtype=float)
s13 = arange(26.5,31.5,0.1,dtype=float)
l9um=concatenate((s1,s2,s3,s4,s5,s6,s7), axis=0)
l18um=concatenate((s6,s7,s8,s9,s10,s11,s12,s13), axis=0)

########Spectrum without lines########
spec_noLines9um = f1(l9um)
e_spec_noLines9um = ferr(l9um)
spec_noLines18um = f1(l18um)
e_spec_noLines18um = ferr(l18um)

f2_9um = interp1d(l9um, spec_noLines9um, 'slinear')
ferr2_9um = interp1d(l9um, e_spec_noLines9um, 'slinear')

f2_18um = interp1d(l18um, spec_noLines18um, 'slinear')
ferr2_18um = interp1d(l18um, e_spec_noLines18um, 'slinear')

########Spectrum resampled########
file1 = open('silicates_files_all/spec_resampled_9um_3c120.dat','w+')
count = 0
k = 0
j = 2
while count < 80:  
   f9um = np.mean(spec_noLines9um[k:j])
   ef9um = sqrt((np.std(spec_noLines9um[k:j]))**(2)+np.mean(e_spec_noLines9um[k:j])**(2))
   x9um = np.mean(l9um[k:j])
   ex9um = sqrt((np.std(l9um[k:j]))**(2)+ 0.1**(2))
   print x9um, '' ,ex9um
   print >>file1, x9um, f9um, ef9um 
   k = j + 1
   j = j + 3
   count =count + 1
file1.close()

x9um_res, f9um_res,  ef9um_res = loadtxt('silicates_files_all/spec_resampled_9um_3c120.dat', unpack=True)

file2 = open('silicates_files_all/spec_resampled_18um_3c120.dat','w+')
count = 0
k = 0
j = 2
while count < 80:  
   f18um = np.mean(spec_noLines18um[k:j])
   ef18um = sqrt((np.std(spec_noLines18um[k:j]))**(2)+np.mean(e_spec_noLines18um[k:j])**(2))
   x18um = np.mean(l18um[k:j])
   print >>file2, x18um, f18um, ef18um 
   k = j + 1
   j = j + 3
   count =count + 1
file2.close()    
x18um_res,  f18um_res,  ef18um_res = loadtxt('silicates_files_all/spec_resampled_18um_3c120.dat', unpack=True)

########Continuum-bands to feature at 9um########
file3 = open('band1_9um.dat', 'w+')
file4 = open('band2_9um.dat', 'w+')
for i in range(0,100):
###Imprime las bandas###
    l1 = np.random.uniform(8.2, 8.9, 100)
    fc1 = f2_9um(l1)
    efc1 = ferr2_9um(l1)
    pfc1 = mean(fc1)
    epfc1 = mean(efc1)
    pl1 = mean(l1)    
    print >>file3, pl1, pfc1, pfc1+epfc1, pfc1-epfc1

    l2 = np.random.uniform(13.5, 14., 100)
    fc2 = f2_9um(l2)
    efc2 = ferr2_9um(l2)
    pfc2 = mean(fc2)
    epfc2 = mean(efc2)
    pl2 = mean(l2)
    print >>file4, pl2, pfc2, pfc2+epfc2, pfc2-epfc2
##############################
file3.close()
file4.close()
plt.fill([8.2,8.9,8.9,8.2],[0,0,1800,1800], color='pink',fill=False, hatch='\\',linewidth=2)
plt.fill([13.5,14.,14.,13.5],[0,0,1800,1800], color='pink',fill=False, hatch='\\',linewidth=2)

xpl1_9um, ypfc1_9um, up_pfc1_9um, low_pfc1_9um = loadtxt('band1_9um.dat', unpack=True)
xpl2_9um, ypfc2_9um, up_pfc2_9um, low_pfc2_9um = loadtxt('band2_9um.dat', unpack=True)

l3_9um = arange(9.0,13.7,0.1,dtype=float)
########Continuum-bands to feature at 18um########
file5 = open('band1_18um.dat', 'w+')
file6 = open('band2_18um.dat', 'w+')
for i in range(0,100):
###Imprime las bandas###
    l1 = np.random.uniform(13.5, 14.0, 100)
    fc1 = f2_18um(l1)
    efc1 = ferr2_18um(l1)
    pfc1 = mean(fc1)
    epfc1 = mean(efc1)
    pl1 = mean(l1)    
    print >>file5, pl1, pfc1, pfc1+epfc1, pfc1-epfc1

    l2 = np.random.uniform(26.8, 28.0, 100)
    fc2 = f2_18um(l2)
    efc2 = ferr2_18um(l2)
    pfc2 = mean(fc2)
    epfc2 = mean(efc2)
    pl2 = mean(l2)
    print >>file6, pl2, pfc2, pfc2+epfc2, pfc2-epfc2
##############################
file5.close()
file6.close()
plt.fill([13.5,14.,14.,13.5],[0,0,1800,1800], color='pink',fill=False, hatch='\\',linewidth=2)
plt.fill([26.8,28.,28.,26.8],[0,0,1800,1800], color='pink',fill=False, hatch='\\',linewidth=2)

xpl1_18um, ypfc1_18um, up_pfc1_18um, low_pfc1_18um = loadtxt('band1_18um.dat', unpack=True)
xpl2_18um, ypfc2_18um, up_pfc2_18um, low_pfc2_18um = loadtxt('band2_18um.dat', unpack=True)
############################################################
l3_18um = arange(14.1,26.7,0.1,dtype=float)
########Continuum########
for i in range(0,100):
    s1_9um = np.random.uniform(low_pfc1_9um[i], up_pfc1_9um[i], 100)
    s1_m_9um = mean(s1_9um)

    s2_9um = np.random.uniform(low_pfc2_9um[i], up_pfc2_9um[i], 100)
    s2_m_9um = mean(s2_9um)
    
    l1_2_9um = (xpl1_9um[i],xpl2_9um[i])
    f1_2_9um = (s1_m_9um, s2_m_9um)
    
    f3 = interp1d(l1_2_9um, f1_2_9um)
    fcont_9um = f3(l3_9um)
    plt.plot(l3_9um,fcont_9um, color='blue')
for i in range(0,100):
    s1_18um = np.random.uniform(low_pfc1_18um[i], up_pfc1_18um[i], 100)
    s1_m_18um = mean(s1_18um)

    s2_18um = np.random.uniform(low_pfc2_18um[i], up_pfc2_18um[i], 100)
    s2_m_18um = mean(s2_18um)
    
    l1_2_18um = (xpl1_18um[i],xpl2_18um[i])
    f1_2_18um = (s1_m_18um, s2_m_18um)
    
    f4 = interp1d(l1_2_18um, f1_2_18um)
    fcont_18um = f4(l3_18um)
    plt.plot(l3_18um,fcont_18um, color='blue')    


plt.plot(x9um_res,f9um_res, color='orange', linewidth=4)
plt.plot(x18um_res,f18um_res, color='orange', linewidth=4)

plt.plot(nx1, ny1, color='black')
plt.fill_between(nx1, ny1,(ny1+ney1), color='grey')
plt.fill_between(nx1, ny1,(ny1-ney1), color='grey') 

#plt.plot(l9um, spec_noLines9um, color='red')
#plt.plot(l18um, spec_noLines18um, color='red')


siv=(10.5,10.5)
text(10.6, 80,'[S IV]',fontsize=18)
Neii=(12.8,12.8)
text(12.9, 120,'[Ne II]',fontsize=18)
Nev_14=(14.3,14.3)
text(14.4, 80,'[Ne V]',fontsize=18)
Neiii=(15.5,15.5)
text(15.6, 120,'[Ne III]',fontsize=18)
Siii_18=(18.7,18.7)
text(18.8, 80,'[S III]',fontsize=18)
Nev_24=(24.3,24.3)
text(24.4, 120,'[Ne V]',fontsize=18)
Oiv=(25.9,25.9)
text(26.0, 80,'[O IV]',fontsize=18)
Feii=(26.0,26.0)
text(26.1, 120,'[Fe II]',fontsize=18)
Siii_33=(33.5,33.5)
text(33.6, 80,'[S III]',fontsize=18)

y=(0,max(f9um_res)*5)
plt.plot(siv,y,'k--')
plt.plot(Neii,y,'k--')
plt.plot(Nev_14,y,'k--')
plt.plot(Nev_24,y,'k--')
plt.plot(Neiii,y,'k--')
plt.plot(Siii_18,y,'k--')
plt.plot(Siii_33,y,'k--')
plt.plot(Oiv,y,'k--')
plt.plot(Feii,y,'k--')

plt.errorbar(12/(1+0.033), 266., 7.0, marker='o', markersize=10, color='green',label='Asmus et al. 2014')

tick_params(axis='x', labelsize=18)
tick_params(axis='y', labelsize=18)
plt.ylabel(r" $f_{\nu}$(mJy)",fontsize=22)
plt.xlabel("Rest-frame wavelength ($\mu$m)",fontsize=22)


plt.show()
