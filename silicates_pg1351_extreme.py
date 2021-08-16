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
nx1 = pr.x2
ny1 = pr.y2
ney1 = pr.ey2
z = pr.z_2

print 'spec=',nx1[0], nx1[-1]
f1 = interp1d(nx1,ny1, 'slinear')
ferr = interp1d(nx1,ney1)
#####################
s01 = arange(5.52,5.98,0.1,dtype=float)
s0 = arange(6.48,7.34,0.1,dtype=float)
s1 = arange(7.94,8.0,0.1,dtype=float)
s2 = arange(8.15,8.87,0.1,dtype=float)
s3 = arange(9.25,10.28,0.1,dtype=float)
s4 = arange(10.68,11.02,0.1,dtype=float)
s5 = arange(11.52,12.65,0.1,dtype=float)
s6 = arange(13.5,14.0,0.1,dtype=float)
s7 = arange(14.6,15.27,0.1,dtype=float)
s8 = arange(15.87,16.71,0.1,dtype=float)
s9 = arange(17.4,18.45,0.1,dtype=float)
s10 = arange(19.1, 19.43,0.1,dtype=float)
s11 = arange(21.22, 22.21,0.1,dtype=float)
s12 = arange(22.89,23.30,0.1,dtype=float)
s13 = arange(24.09,31.5,0.1,dtype=float)
l9um=concatenate((s01,s0,s1,s2,s3,s4,s5,s6,s7), axis=0)
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
file1 = open('silicates_files_all/spec_resampled_9um_pg1351.dat','w+')
count = 0
k = 0
j = 2
while count < 80:  
   f9um = np.mean(spec_noLines9um[k:j])
   ef9um = sqrt((np.std(spec_noLines9um[k:j]))**(2)+np.mean(e_spec_noLines9um[k:j])**(2))
   x9um = np.mean(l9um[k:j])
   print >>file1, x9um, f9um, ef9um 
   k = j + 1
   j = j + 3
   count =count + 1
file1.close()    
x9um_res, f9um_res,  ef9um_res = loadtxt('silicates_files_all/spec_resampled_9um_pg1351.dat', unpack=True)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
func_Nirs = interp1d(x9um_res, f9um_res, 'slinear')
f10um_irs =  func_Nirs(10.) #mJy
f10um_irs = f10um_irs/1000. #Jy
f10um_irs = f10um_irs*1.e-23 #erg s-1 cm-2 Hz-1
nu_irs = (3.e14)/10. #Hz or s-1
f10um_irs = f10um_irs*nu_irs #erg s-1 cm-2
d = (123.4e6)*(3.086e18) #cm
L10um_irs = f10um_irs*4*3.14*d**(2)

func_eNirs = interp1d(x9um_res, ef9um_res, 'slinear')
ef10um_irs =  func_eNirs(10.) #mJy
ef10um_irs = ef10um_irs/1000. #Jy
ef10um_irs = ef10um_irs*1.e-23 #erg s-1 cm-2 Hz-1
ef10um_irs = ef10um_irs*nu_irs #erg s-1 cm-2

eL10um_irs = L10um_irs*(ef10um_irs/f10um_irs)
print 'L10um_irs=', log10(L10um_irs), '+/-',eL10um_irs/(log(10)*L10um_irs)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

file2 = open('silicates_files_all/spec_resampled_18um_pg1351.dat','w+')
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
x18um_res,  f18um_res,  ef18um_res = loadtxt('silicates_files_all/spec_resampled_18um_pg1351.dat', unpack=True)

########Continuum-bands to feature at 9um########
file3 = open('band1_9um.dat', 'w+')
file4 = open('band2_9um.dat', 'w+')
for i in range(0,100):
###Imprime las bandas###
    l1 = np.random.uniform(7.0, 8.0, 100)
    fc1 = f2_9um(l1)
    efc1 = ferr2_9um(l1)
    pfc1 = mean(fc1)
    epfc1 = mean(efc1)
    pl1 = mean(l1)    
    print >>file3, pl1, pfc1, pfc1+epfc1, pfc1-epfc1

    l2 = np.random.uniform(14.0, 14.50, 100)
    fc2 = f2_9um(l2)
    efc2 = ferr2_9um(l2)
    pfc2 = mean(fc2)
    epfc2 = mean(efc2)
    pl2 = mean(l2)
    print >>file4, pl2, pfc2, pfc2+epfc2, pfc2-epfc2
##############################
file3.close()
file4.close()
plt.fill([7.0,8.0,8.0,7.0],[0,0,1800,1800], color='pink',fill=False, hatch='\\',linewidth=2)
plt.fill([14.0,14.50,14.50,14.0],[0,0,1800,1800], color='pink',fill=False, hatch='\\',linewidth=2)


xpl1_9um, ypfc1_9um, up_pfc1_9um, low_pfc1_9um = loadtxt('band1_9um.dat', unpack=True)
xpl2_9um, ypfc2_9um, up_pfc2_9um, low_pfc2_9um = loadtxt('band2_9um.dat', unpack=True)

l3_9um = arange(8.10,13.99,0.1,dtype=float)
########Continuum-bands to feature at 18um########
file5 = open('band1_18um.dat', 'w+')
file6 = open('band2_18um.dat', 'w+')
for i in range(0,100):
###Imprime las bandas###
    l1 = np.random.uniform(14.0, 14.50, 100)
    fc1 = f2_18um(l1)
    efc1 = ferr2_18um(l1)
    pfc1 = mean(fc1)
    epfc1 = mean(efc1)
    pl1 = mean(l1)    
    print >>file5, pl1, pfc1, pfc1+epfc1, pfc1-epfc1

    l2 = np.random.uniform(20.0, 21.0, 100)
    fc2 = f2_18um(l2)
    efc2 = ferr2_18um(l2)
    pfc2 = mean(fc2)
    epfc2 = mean(efc2)
    pl2 = mean(l2)
    print >>file6, pl2, pfc2, pfc2+epfc2, pfc2-epfc2
##############################
file5.close()
file6.close()
plt.fill([14.0,14.50,14.50,14.0],[0,0,1800,1800], color='pink',fill=False, hatch='\\',linewidth=2)
plt.fill([20.0,21.0,21.0,20.0],[0,0,1800,1800], color='pink',fill=False, hatch='\\',linewidth=2)

xpl1_18um, ypfc1_18um, up_pfc1_18um, low_pfc1_18um = loadtxt('band1_18um.dat', unpack=True)
xpl2_18um, ypfc2_18um, up_pfc2_18um, low_pfc2_18um = loadtxt('band2_18um.dat', unpack=True)
############################################################
l3_18um = arange(14.60,19.99,0.1,dtype=float)
########Continuum########
fintp9 = interp1d(x9um_res, f9um_res, 'slinear')
spec_inBlue9um = fintp9(l3_9um)
err_fintp9 = interp1d(x9um_res, ef9um_res, 'slinear')  ###########1
espec_inBlue9um = err_fintp9(l3_9um)                   ###########2

file7 = open('sil9um.dat', 'w+')
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

    fsil9um = log(spec_inBlue9um) - log(fcont_9um)
    sil9um = max(fsil9um)
    idsil9um = where(fsil9um == fsil9um.max())[0]
    err9 = float(espec_inBlue9um[idsil9um])/float(spec_inBlue9um[idsil9um])###########3
    print >>file7, float(l3_9um[idsil9um]), sil9um, err9                   ###########4
file7.close()    
lsilicate9um, silicato9um, esilicato9um  = loadtxt('sil9um.dat', unpack=True)  ###########5
print 'lambda_max=',mean(lsilicate9um),'std=', std(lsilicate9um), 'silicato9um=', mean(silicato9um), 'std=', sqrt((std(silicato9um))**(2)+(mean(esilicato9um))**(2))                                                        ###########6

x9 =(mean(lsilicate9um),mean(lsilicate9um))
y9 = (0,800)
plt.plot(x9,y9, 'k:', color='red', linewidth=4)

fintp18 = interp1d(x18um_res, f18um_res, 'slinear')
spec_inBlue18 = fintp18(l3_18um)
err_fintp18 = interp1d(x18um_res, ef18um_res, 'slinear')             ###########7
espec_inBlue18um = err_fintp18(l3_18um)                              ###########8

file8 = open('sil18um.dat', 'w+')     
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

    fsil18um = log(spec_inBlue18) - log(fcont_18um)
    sil18um = max(fsil18um)
    idsil18um = where(fsil18um == fsil18um.max())[0]
    lsil_max18 = np.where(l3_18um == float(l3_18um[idsil18um]))    
    err18 = float(espec_inBlue18um[idsil18um])/float(spec_inBlue18[idsil18um]) ###########9   
    print >>file8, float(l3_18um[idsil18um]), sil18um, err18                   ###########10
file8.close()
lsilicate18um, silicato18um, esilicato18um = loadtxt('sil18um.dat', unpack=True)
print 'lambda_max=',mean(lsilicate18um),'std=',std(lsilicate18um), 'silicato18um=', mean(silicato18um), 'std=', sqrt((std(silicato18um))**(2)+(mean(esilicato18um))**(2))                                                   ###########11

x18 =(mean(lsilicate18um),mean(lsilicate18um))
y18 = (0,800)
plt.plot(x18,y18, 'k:', color='red', linewidth=4)


plt.plot(x9um_res,f9um_res, color='orange', linewidth=4)
plt.plot(x18um_res,f18um_res, color='orange', linewidth=4)

plt.plot(nx1, ny1, color='black')
plt.fill_between(nx1, ny1,(ny1+ney1), color='grey')
plt.fill_between(nx1, ny1,(ny1-ney1), color='grey') 

siv=(10.5,10.5)
text(10.6, 50,'[S IV]',fontsize=18)
Neii=(12.8,12.8)
text(12.9, 50,'[Ne II]',fontsize=18)
Nev_14=(14.3,14.3)
text(14.4, 80,'[Ne V]',fontsize=18)
Neiii=(15.5,15.5)
text(15.6, 50,'[Ne III]',fontsize=18)
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

tick_params(axis='x', labelsize=18)
tick_params(axis='y', labelsize=18)
plt.ylabel(r" $f_{\nu}$(mJy)",fontsize=22)
plt.xlabel("Rest-frame wavelength ($\mu$m)",fontsize=22)


plt.show()
