#!/usr/bin/env python
# make a horizontal bar chart
from pylab import *
############################
#Reading data
#nF06 = loadtxt('Fritz06.dat', unpack='True')
#nN08 = loadtxt('Nenkova08.dat', unpack='True')
#nH10 = loadtxt('Hoenig10.dat', unpack='True')
#nH17 = loadtxt('Hoenig17.dat', unpack='True')

#####################
plt.figure('models_statistic')
plt.subplot(411)
val_Fritz = (12,4,4,1,2)
val_Fritz_not_modeled = (20,19,22,21)
pos = arange(5)+.1
val_Fritz = array(val_Fritz)*100/23
posx = (20,40,60,80)
barh(pos, val_Fritz, align='center', alpha=0.5, color='blue')
yticks(pos, ('Non-modeled','Torus', 'Torus+Ste.', 'Torus+HII', 'Torus+Ste.+HII'))
xticks(posx, ())
#plt.xlabel(r'Per-cent of objects',fontsize=16)
plt.title('Fritz et al. (2006): smooth torus', fontsize=18)
tick_params(axis='x', labelsize=16)
tick_params(axis='y', labelsize=12)
plt.xlim(0,100)
#plt.figure('Nenkova08')
plt.subplot(412)
val_Nenkova = (6,1,13,0,3)
val_Nenkova_not_modeled = (22,10,23,20)
pos = arange(5)+.1
val_Nenkova = array(val_Nenkova)*100/23
val_Nenkova_not_modeled = array(val_Nenkova_not_modeled)*100/23
#barh(pos, val_Nenkova_not_modeled, align='center', alpha=0.7, color='pink')
barh(pos, val_Nenkova, align='center', alpha=0.5, color='blue')
#plt.ylabel(r'N',fontsize=16)
#yticks(pos, ('', '', '', ''))
yticks(pos, ('Non-modeled','Torus', 'Torus+Ste.', 'Torus+HII', 'Torus+Ste.+HII'))
xticks(posx, ())
#plt.xlabel(r'Per-cent of objects',fontsize=16)
plt.title('Nenkova et al. (2008a, b): clumpy torus', fontsize=18)
tick_params(axis='x', labelsize=16)
tick_params(axis='y', labelsize=12)
plt.xlim(0,100)
#plt.figure('Hoenig10')
plt.subplot(413)
val_Hoenig10 = (8,1,2,1,11)
val_Hoenig10_not_modeled = (23,21,22,12)
pos = arange(5)+.1
val_Hoenig10 = array(val_Hoenig10)*100/23
val_Hoenig10_not_modeled = array(val_Hoenig10_not_modeled)*100/23
#barh(pos, val_Hoenig10_not_modeled, align='center', alpha=0.7, color='pink')
barh(pos, val_Hoenig10, align='center', alpha=0.5, color='blue')
#plt.ylabel(r'N',fontsize=16)
yticks(pos, ('Non-modeled','Torus', 'Torus+Ste.', 'Torus+HII', 'Torus+Ste.+HII'))
xticks(posx, ())
#plt.xlabel(r'Per-cent of objects',fontsize=16)
plt.title('Hoenig et al. (2010): clumpy torus', fontsize=18)
tick_params(axis='x', labelsize=16)
tick_params(axis='y', labelsize=12)
plt.xlim(0,100)
#plt.figure('Hoenig17')
plt.subplot(414)
val_Hoenig17 = (5,7,5,3,3)
val_Hoenig17_not_modeled = (17,18,20,20)
pos = arange(5)+.1
val_Hoenig17=array(val_Hoenig17)*100/23
val_Hoenig17_not_modeled=array(val_Hoenig17_not_modeled)*100/23
#barh(pos, val_Hoenig17_not_modeled, align='center', alpha=0.7, color='pink')
barh(pos, val_Hoenig17, align='center', alpha=0.5, color='blue')
#plt.ylabel(r'N',fontsize=16)
#yticks(pos, ('','', '', '', ''))
yticks(pos, ('Non-modeled','Disk+outflow', 'Disk+outflow+Ste.', 'Disk+outflow+HII', 'Disk+outflow+Ste.+HII'))
plt.xlabel(r'Per-cent of objects',fontsize=16)
plt.title('Hoenig et al. (2017): Clumpy disk+outflow', fontsize=18)
tick_params(axis='x', labelsize=16)
tick_params(axis='y', labelsize=12)
plt.xlim(0,100)
plt.show()
