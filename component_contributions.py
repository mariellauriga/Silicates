from pylab import *
############################Fritz06############################
chi2_3c120_4, dof_3c120_4, ft_3c120_4, min_3c120_4, max_3c120_4, f1_3c120_4, f2_3c120_4, f3_3c120_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/3c120_Fritz06_4_fluxes_ebv.txt', unpack='True')
frac_torus_3c120_fritz06 = f1_3c120_4[0]/ft_3c120_4[0]
frac_ste_3c120_fritz06 = f2_3c120_4[0]/ft_3c120_4[0]
frac_Hii_3c120_fritz06 = f3_3c120_4[0]/ft_3c120_4[0]

chi2_OQ208_1, dof_OQ208_1, ft_OQ208_1, min_OQ208_1, max_OQ208_1, f1_OQ208_1, f2_OQ208_1, f3_OQ208_1 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/OQ208_Fritz06_1_fluxes_ebv.txt', unpack='True')
frac_torus_OQ208_fritz06 = f1_OQ208_1/ft_OQ208_1
frac_ste_OQ208_fritz06 = f2_OQ208_1/ft_OQ208_1
frac_Hii_OQ208_fritz06 = f3_OQ208_1/ft_OQ208_1

chi2_Mrk1018_1, dof_Mrk1018_1, ft_Mrk1018_1, min_Mrk1018_1, max_Mrk1018_1, f1_Mrk1018_1, f2_Mrk1018_1, f3_Mrk1018_1 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/Mrk1018_Fritz06_1_fluxes_ebv.txt', unpack='True')
frac_torus_Mrk1018_fritz06 = f1_Mrk1018_1/ft_Mrk1018_1
frac_ste_Mrk1018_fritz06 = f2_Mrk1018_1/ft_Mrk1018_1
frac_Hii_Mrk1018_fritz06 = f3_Mrk1018_1/ft_Mrk1018_1

chi2_ngc4258_3, dof_ngc4258_3, ft_ngc4258_3, min_ngc4258_3, max_ngc4258_3, f1_ngc4258_3, f2_ngc4258_3, f3_ngc4258_3 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ngc4258_Fritz06_3_fluxes_ebv.txt', unpack='True')
frac_torus_ngc4258_fritz06 = f1_ngc4258_3/ft_ngc4258_3
frac_ste_ngc4258_fritz06 = f2_ngc4258_3/ft_ngc4258_3
frac_Hii_ngc4258_fritz06 = f3_ngc4258_3/ft_ngc4258_3

chi2_pg0804_2, dof_pg0804_2, ft_pg0804_2, min_pg0804_2, max_pg0804_2, f1_pg0804_2, f2_pg0804_2, f3_pg0804_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg0804_Fritz06_2_fluxes_ebv.txt', unpack='True')
frac_torus_pg0804_fritz06 = f1_pg0804_2/ft_pg0804_2
frac_ste_pg0804_fritz06 = f2_pg0804_2/ft_pg0804_2
frac_Hii_pg0804_fritz06 = f3_pg0804_2/ft_pg0804_2

chi2_pg0844_2, dof_pg0844_2, ft_pg0844_2, min_pg0844_2, max_pg0844_2, f1_pg0844_2, f2_pg0844_2, f3_pg0844_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg0844_Fritz06_2_fluxes_ebv.txt', unpack='True')
frac_torus_pg0844_fritz06 = f1_pg0844_2/ft_pg0844_2
frac_ste_pg0844_fritz06 = f2_pg0844_2/ft_pg0844_2
frac_Hii_pg0844_fritz06 = f3_pg0844_2/ft_pg0844_2

chi2_pg1011_1, dof_pg1011_1, ft_pg1011_1, min_pg1011_1, max_pg1011_1, f1_pg1011_1, f2_pg1011_1, f3_pg1011_1 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1011_Fritz06_1_fluxes_ebv.txt', unpack='True')
frac_torus_pg1011_fritz06 = f1_pg1011_1/ft_pg1011_1
frac_ste_pg1011_fritz06 = f2_pg1011_1/ft_pg1011_1
frac_Hii_pg1011_fritz06 = f3_pg1011_1/ft_pg1011_1

chi2_pg1211_4, dof_pg1211_4, ft_pg1211_4, min_pg1211_4, max_pg1211_4, f1_pg1211_4, f2_pg1211_4, f3_pg1211_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1211_Fritz06_4_fluxes_ebv.txt', unpack='True')
frac_torus_pg1211_fritz06 = f1_pg1211_4/ft_pg1211_4
frac_ste_pg1211_fritz06 = f2_pg1211_4/ft_pg1211_4
frac_Hii_pg1211_fritz06 = f3_pg1211_4/ft_pg1211_4

chi2_pg1535_2, dof_pg1535_2, ft_pg1535_2, min_pg1535_2, max_pg1535_2, f1_pg1535_2, f2_pg1535_2, f3_pg1535_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1535_Fritz06_2_fluxes_ebv.txt', unpack='True')
frac_torus_pg1535_fritz06 = f1_pg1535_2/ft_pg1535_2
frac_ste_pg1535_fritz06 = f2_pg1535_2/ft_pg1535_2
frac_Hii_pg1535_fritz06 = f3_pg1535_2/ft_pg1535_2

chi2_pg2214_2, dof_pg2214_2, ft_pg2214_2, min_pg2214_2, max_pg2214_2, f1_pg2214_2, f2_pg2214_2, f3_pg2214_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg2214_Fritz06_2_fluxes_ebv.txt', unpack='True')
frac_torus_pg2214_fritz06 = f1_pg2214_2/ft_pg2214_2
frac_ste_pg2214_fritz06 = f2_pg2214_2/ft_pg2214_2
frac_Hii_pg2214_fritz06 = f3_pg2214_2/ft_pg2214_2

frac_torus_fritz06 = (frac_torus_3c120_fritz06, frac_torus_OQ208_fritz06, frac_torus_Mrk1018_fritz06, frac_torus_ngc4258_fritz06, frac_torus_pg0804_fritz06, frac_torus_pg0844_fritz06, frac_torus_pg1011_fritz06, frac_torus_pg1211_fritz06, frac_torus_pg1535_fritz06, frac_torus_pg2214_fritz06)

frac_ste_fritz06 = (frac_ste_3c120_fritz06, frac_ste_OQ208_fritz06, frac_ste_Mrk1018_fritz06, frac_ste_ngc4258_fritz06, frac_ste_pg0804_fritz06, frac_ste_pg0844_fritz06, frac_ste_pg1011_fritz06, frac_ste_pg1211_fritz06, frac_ste_pg1535_fritz06, frac_ste_pg2214_fritz06)

frac_Hii_fritz06 = (frac_Hii_3c120_fritz06, frac_Hii_OQ208_fritz06, frac_Hii_Mrk1018_fritz06, frac_Hii_ngc4258_fritz06, frac_Hii_pg0804_fritz06, frac_Hii_pg0844_fritz06, frac_Hii_pg1011_fritz06, frac_Hii_pg1211_fritz06, frac_Hii_pg1535_fritz06, frac_Hii_pg2214_fritz06)

############################Nenkova08############################

chi2_3c120_2, dof_3c120_2, ft_3c120_2, min_3c120_2, max_3c120_2, f1_3c120_2, f2_3c120_2, f3_3c120_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/3c120_Nenkova08_2_fluxes_ebv.txt', unpack='True')
frac_torus_3c120_Nenkova08 = f1_3c120_2[0]/ft_3c120_2[0]
frac_ste_3c120_Nenkova08 = f2_3c120_2[0]/ft_3c120_2[0]
frac_Hii_3c120_Nenkova08 = f3_3c120_2[0]/ft_3c120_2[0]

chi2_3c445_2, dof_3c445_2, ft_3c445_2, min_3c445_2, max_3c445_2, f1_3c445_2, f2_3c445_2, f3_3c445_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/3c445_Nenkova08_2_fluxes_ebv.txt', unpack='True')
frac_torus_3c445_Nenkova08 = f1_3c445_2/ft_3c445_2
frac_ste_3c445_Nenkova08 = f2_3c445_2/ft_3c445_2
frac_Hii_3c445_Nenkova08 = f3_3c445_2/ft_3c445_2

chi2_AKN120_2, dof_AKN120_2, ft_AKN120_2, min_AKN120_2, max_AKN120_2, f1_AKN120_2, f2_AKN120_2, f3_AKN120_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/AKN120_Nenkova08_2_fluxes_ebv.txt', unpack='True')
frac_torus_AKN120_Nenkova08 = f1_AKN120_2/ft_AKN120_2
frac_ste_AKN120_Nenkova08 = f2_AKN120_2/ft_AKN120_2
frac_Hii_AKN120_Nenkova08 = f3_AKN120_2/ft_AKN120_2

chi2_OQ208_4, dof_OQ208_4, ft_OQ208_4, min_OQ208_4, max_OQ208_4, f1_OQ208_4, f2_OQ208_4, f3_OQ208_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/OQ208_Nenkova08_4_fluxes_ebv.txt', unpack='True')
frac_torus_OQ208_Nenkova08 = f1_OQ208_4/ft_OQ208_4
frac_ste_OQ208_Nenkova08 = f2_OQ208_4/ft_OQ208_4
frac_Hii_OQ208_Nenkova08 = f3_OQ208_4/ft_OQ208_4

chi2_ESO198_2, dof_ESO198_2, ft_ESO198_2, min_ESO198_2, max_ESO198_2, f1_ESO198_2, f2_ESO198_2, f3_ESO198_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ESO198_Nenkova08_2_fluxes_ebv.txt', unpack='True')
frac_torus_ESO198_Nenkova08 = f1_ESO198_2/ft_ESO198_2
frac_ste_ESO198_Nenkova08 = f2_ESO198_2/ft_ESO198_2
frac_Hii_ESO198_Nenkova08 = f3_ESO198_2/ft_ESO198_2

chi2_ESO548_2, dof_ESO548_2, ft_ESO548_2, min_ESO548_2, max_ESO548_2, f1_ESO548_2, f2_ESO548_2, f3_ESO548_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ESO548_Nenkova08_2_fluxes_ebv.txt', unpack='True')
frac_torus_ESO548_Nenkova08 = f1_ESO548_2/ft_ESO548_2
frac_ste_ESO548_Nenkova08 = f2_ESO548_2/ft_ESO548_2
frac_Hii_ESO548_Nenkova08 = f3_ESO548_2/ft_ESO548_2

chi2_Mrk1018_2, dof_Mrk1018_2, ft_Mrk1018_2, min_Mrk1018_2, max_Mrk1018_2, f1_Mrk1018_2, f2_Mrk1018_2, f3_Mrk1018_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/Mrk1018_Nenkova08_2_fluxes_ebv.txt', unpack='True')
frac_torus_Mrk1018_Nenkova08 = f1_Mrk1018_2/ft_Mrk1018_2
frac_ste_Mrk1018_Nenkova08 = f2_Mrk1018_2/ft_Mrk1018_2
frac_Hii_Mrk1018_Nenkova08 = f3_Mrk1018_2/ft_Mrk1018_2

chi2_ngc1275_1, dof_ngc1275_1, ft_ngc1275_1, min_ngc1275_1, max_ngc1275_1, f1_ngc1275_1, f2_ngc1275_1, f3_ngc1275_1 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ngc1275_Nenkova08_1_fluxes_ebv.txt', unpack='True')
frac_torus_ngc1275_Nenkova08 = f1_ngc1275_1/ft_ngc1275_1
frac_ste_ngc1275_Nenkova08 = f2_ngc1275_1/ft_ngc1275_1
frac_Hii_ngc1275_Nenkova08 = f3_ngc1275_1/ft_ngc1275_1

chi2_ngc2110_4, dof_ngc2110_4, ft_ngc2110_4, min_ngc2110_4, max_ngc2110_4, f1_ngc2110_4, f2_ngc2110_4, f3_ngc2110_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ngc2110_Nenkova08_4_fluxes_ebv.txt', unpack='True')
frac_torus_ngc2110_Nenkova08 = f1_ngc2110_4/ft_ngc2110_4
frac_ste_ngc2110_Nenkova08 = f2_ngc2110_4/ft_ngc2110_4
frac_Hii_ngc2110_Nenkova08 = f3_ngc2110_4/ft_ngc2110_4

chi2_ngc4258_4, dof_ngc4258_4, ft_ngc4258_4, min_ngc4258_4, max_ngc4258_4, f1_ngc4258_4, f2_ngc4258_4, f3_ngc4258_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ngc4258_Nenkova08_4_fluxes_ebv.txt', unpack='True')
frac_torus_ngc4258_Nenkova08 = f1_ngc4258_4/ft_ngc4258_4
frac_ste_ngc4258_Nenkova08 = f2_ngc4258_4/ft_ngc4258_4
frac_Hii_ngc4258_Nenkova08 = f3_ngc4258_4/ft_ngc4258_4

chi2_pg0804_2, dof_pg0804_2, ft_pg0804_2, min_pg0804_2, max_pg0804_2, f1_pg0804_2, f2_pg0804_2, f3_pg0804_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg0804_Nenkova08_2_fluxes_ebv.txt', unpack='True')
frac_torus_pg0804_Nenkova08 = f1_pg0804_2/ft_pg0804_2
frac_ste_pg0804_Nenkova08 = f2_pg0804_2/ft_pg0804_2
frac_Hii_pg0804_Nenkova08 = f3_pg0804_2/ft_pg0804_2

chi2_pg0844_2, dof_pg0844_2, ft_pg0844_2, min_pg0844_2, max_pg0844_2, f1_pg0844_2, f2_pg0844_2, f3_pg0844_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg0844_Nenkova08_2_fluxes_ebv.txt', unpack='True')
frac_torus_pg0844_Nenkova08 = f1_pg0844_2/ft_pg0844_2
frac_ste_pg0844_Nenkova08 = f2_pg0844_2/ft_pg0844_2
frac_Hii_pg0844_Nenkova08 = f3_pg0844_2/ft_pg0844_2

chi2_pg1011_2, dof_pg1011_2, ft_pg1011_2, min_pg1011_2, max_pg1011_2, f1_pg1011_2, f2_pg1011_2, f3_pg1011_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1011_Nenkova08_2_fluxes_ebv.txt', unpack='True')
frac_torus_pg1011_Nenkova08 = f1_pg1011_2/ft_pg1011_2
frac_ste_pg1011_Nenkova08 = f2_pg1011_2/ft_pg1011_2
frac_Hii_pg1011_Nenkova08 = f3_pg1011_2/ft_pg1011_2

chi2_pg1211_2, dof_pg1211_2, ft_pg1211_2, min_pg1211_2, max_pg1211_2, f1_pg1211_2, f2_pg1211_2, f3_pg1211_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1211_Nenkova08_2_fluxes_ebv.txt', unpack='True')
frac_torus_pg1211_Nenkova08 = f1_pg1211_2/ft_pg1211_2
frac_ste_pg1211_Nenkova08 = f2_pg1211_2/ft_pg1211_2
frac_Hii_pg1211_Nenkova08 = f3_pg1211_2/ft_pg1211_2

chi2_pg1411_2, dof_pg1411_2, ft_pg1411_2, min_pg1411_2, max_pg1411_2, f1_pg1411_2, f2_pg1411_2, f3_pg1411_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1411_Nenkova08_2_fluxes_ebv.txt', unpack='True')
frac_torus_pg1411_Nenkova08 = f1_pg1411_2/ft_pg1411_2
frac_ste_pg1411_Nenkova08 = f2_pg1411_2/ft_pg1411_2
frac_Hii_pg1411_Nenkova08 = f3_pg1411_2/ft_pg1411_2

chi2_pg1535_2, dof_pg1535_2, ft_pg1535_2, min_pg1535_2, max_pg1535_2, f1_pg1535_2, f2_pg1535_2, f3_pg1535_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1535_Nenkova08_2_fluxes_ebv.txt', unpack='True')
frac_torus_pg1535_Nenkova08 = f1_pg1535_2/ft_pg1535_2
frac_ste_pg1535_Nenkova08 = f2_pg1535_2/ft_pg1535_2
frac_Hii_pg1535_Nenkova08 = f3_pg1535_2/ft_pg1535_2

chi2_pg2214_2, dof_pg2214_2, ft_pg2214_2, min_pg2214_2, max_pg2214_2, f1_pg2214_2, f2_pg2214_2, f3_pg2214_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg2214_Nenkova08_2_fluxes_ebv.txt', unpack='True')
frac_torus_pg2214_Nenkova08 = f1_pg2214_2/ft_pg2214_2
frac_ste_pg2214_Nenkova08 = f2_pg2214_2/ft_pg2214_2
frac_Hii_pg2214_Nenkova08 = f3_pg2214_2/ft_pg2214_2

frac_torus_Nenkova08 = (frac_torus_3c120_Nenkova08, frac_torus_3c445_Nenkova08, frac_torus_AKN120_Nenkova08, frac_torus_OQ208_Nenkova08, frac_torus_ESO198_Nenkova08, frac_torus_ESO548_Nenkova08, frac_torus_Mrk1018_Nenkova08, frac_torus_ngc1275_Nenkova08, frac_torus_ngc2110_Nenkova08, frac_torus_ngc4258_Nenkova08, frac_torus_pg0804_Nenkova08, frac_torus_pg0844_Nenkova08, frac_torus_pg1011_Nenkova08, frac_torus_pg1211_Nenkova08, frac_torus_pg1411_Nenkova08, frac_torus_pg1535_Nenkova08, frac_torus_pg2214_Nenkova08)

frac_ste_Nenkova08 = (frac_ste_3c120_Nenkova08, frac_ste_3c445_Nenkova08, frac_ste_AKN120_Nenkova08, frac_ste_OQ208_Nenkova08, frac_ste_ESO198_Nenkova08, frac_ste_ESO548_Nenkova08, frac_ste_Mrk1018_Nenkova08, frac_ste_ngc1275_Nenkova08, frac_ste_ngc2110_Nenkova08, frac_ste_ngc4258_Nenkova08, frac_ste_pg0804_Nenkova08, frac_ste_pg0844_Nenkova08, frac_ste_pg1011_Nenkova08, frac_ste_pg1211_Nenkova08, frac_ste_pg1411_Nenkova08, frac_ste_pg1535_Nenkova08, frac_ste_pg2214_Nenkova08)

frac_Hii_Nenkova08 = (frac_Hii_3c120_Nenkova08, frac_Hii_3c445_Nenkova08, frac_Hii_AKN120_Nenkova08, frac_Hii_OQ208_Nenkova08, frac_Hii_ESO198_Nenkova08, frac_Hii_ESO548_Nenkova08, frac_Hii_Mrk1018_Nenkova08, frac_Hii_ngc1275_Nenkova08, frac_Hii_ngc2110_Nenkova08, frac_Hii_ngc4258_Nenkova08, frac_Hii_pg0804_Nenkova08, frac_Hii_pg0844_Nenkova08, frac_Hii_pg1011_Nenkova08, frac_Hii_pg1211_Nenkova08, frac_Hii_pg1411_Nenkova08, frac_Hii_pg1535_Nenkova08, frac_Hii_pg2214_Nenkova08)

############################Hoenig10############################
chi2_3c120_4, dof_3c120_4, ft_3c120_4, min_3c120_4, max_3c120_4, f1_3c120_4, f2_3c120_4, f3_3c120_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/3c120_Hoenig10_4_fluxes_ebv.txt', unpack='True')
frac_torus_3c120_Hoenig10 = f1_3c120_4[0]/ft_3c120_4[0]
frac_ste_3c120_Hoenig10 = f2_3c120_4[0]/ft_3c120_4[0]
frac_Hii_3c120_Hoenig10 = f3_3c120_4[0]/ft_3c120_4[0]

chi2_3c382_4, dof_3c382_4, ft_3c382_4, min_3c382_4, max_3c382_4, f1_3c382_4, f2_3c382_4, f3_3c382_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/3c382_Hoenig10_4_fluxes_ebv.txt', unpack='True')
frac_torus_3c382_Hoenig10 = f1_3c382_4/ft_3c382_4
frac_ste_3c382_Hoenig10 = f2_3c382_4/ft_3c382_4
frac_Hii_3c382_Hoenig10 = f3_3c382_4/ft_3c382_4

chi2_3c445_2, dof_3c445_2, ft_3c445_2, min_3c445_2, max_3c445_2, f1_3c445_2, f2_3c445_2, f3_3c445_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/3c445_Hoenig10_2_fluxes_ebv.txt', unpack='True')
frac_torus_3c445_Hoenig10 = f1_3c445_2/ft_3c445_2
frac_ste_3c445_Hoenig10 = f2_3c445_2/ft_3c445_2
frac_Hii_3c445_Hoenig10 = f3_3c445_2/ft_3c445_2

chi2_AKN120_4, dof_AKN120_4, ft_AKN120_4, min_AKN120_4, max_AKN120_4, f1_AKN120_4, f2_AKN120_4, f3_AKN120_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/AKN120_Hoenig10_4_fluxes_ebv.txt', unpack='True')
frac_torus_AKN120_Hoenig10 = f1_AKN120_4/ft_AKN120_4
frac_ste_AKN120_Hoenig10 = f2_AKN120_4/ft_AKN120_4
frac_Hii_AKN120_Hoenig10 = f3_AKN120_4/ft_AKN120_4

chi2_OQ208_4, dof_OQ208_4, ft_OQ208_4, min_OQ208_4, max_OQ208_4, f1_OQ208_4, f2_OQ208_4, f3_OQ208_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/OQ208_Hoenig10_4_fluxes_ebv.txt', unpack='True')
frac_torus_OQ208_Hoenig10 = f1_OQ208_4/ft_OQ208_4
frac_ste_OQ208_Hoenig10 = f2_OQ208_4/ft_OQ208_4
frac_Hii_OQ208_Hoenig10 = f3_OQ208_4/ft_OQ208_4

chi2_ESO548_4, dof_ESO548_4, ft_ESO548_4, min_ESO548_4, max_ESO548_4, f1_ESO548_4, f2_ESO548_4, f3_ESO548_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ESO548_Hoenig10_4_fluxes_ebv.txt', unpack='True')
frac_torus_ESO548_Hoenig10 = f1_ESO548_4/ft_ESO548_4
frac_ste_ESO548_Hoenig10 = f2_ESO548_4/ft_ESO548_4
frac_Hii_ESO548_Hoenig10 = f3_ESO548_4/ft_ESO548_4

chi2_Mrk1018_4, dof_Mrk1018_4, ft_Mrk1018_4, min_Mrk1018_4, max_Mrk1018_4, f1_Mrk1018_4, f2_Mrk1018_4, f3_Mrk1018_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/Mrk1018_Hoenig10_4_fluxes_ebv.txt', unpack='True')
frac_torus_Mrk1018_Hoenig10 = f1_Mrk1018_4/ft_Mrk1018_4
frac_ste_Mrk1018_Hoenig10 = f2_Mrk1018_4/ft_Mrk1018_4
frac_Hii_Mrk1018_Hoenig10 = f3_Mrk1018_4/ft_Mrk1018_4

chi2_ngc4258_3, dof_ngc4258_3, ft_ngc4258_3, min_ngc4258_3, max_ngc4258_3, f1_ngc4258_3, f2_ngc4258_3, f3_ngc4258_3 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ngc4258_Hoenig10_3_fluxes_ebv.txt', unpack='True')
frac_torus_ngc4258_Hoenig10 = f1_ngc4258_3/ft_ngc4258_3
frac_ste_ngc4258_Hoenig10 = f2_ngc4258_3/ft_ngc4258_3
frac_Hii_ngc4258_Hoenig10 = f3_ngc4258_3/ft_ngc4258_3

chi2_pg0844_4, dof_pg0844_4, ft_pg0844_4, min_pg0844_4, max_pg0844_4, f1_pg0844_4, f2_pg0844_4, f3_pg0844_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg0844_Hoenig10_4_fluxes_ebv.txt', unpack='True')
frac_torus_pg0844_Hoenig10 = f1_pg0844_4/ft_pg0844_4
frac_ste_pg0844_Hoenig10 = f2_pg0844_4/ft_pg0844_4
frac_Hii_pg0844_Hoenig10 = f3_pg0844_4/ft_pg0844_4

chi2_pg1011_2, dof_pg1011_2, ft_pg1011_2, min_pg1011_2, max_pg1011_2, f1_pg1011_2, f2_pg1011_2, f3_pg1011_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1011_Hoenig10_2_fluxes_ebv.txt', unpack='True')
frac_torus_pg1011_Hoenig10 = f1_pg1011_2/ft_pg1011_2
frac_ste_pg1011_Hoenig10 = f2_pg1011_2/ft_pg1011_2
frac_Hii_pg1011_Hoenig10 = f3_pg1011_2/ft_pg1011_2

chi2_pg1211_4, dof_pg1211_4, ft_pg1211_4, min_pg1211_4, max_pg1211_4, f1_pg1211_4, f2_pg1211_4, f3_pg1211_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1211_Hoenig10_4_fluxes_ebv.txt', unpack='True')
frac_torus_pg1211_Hoenig10 = f1_pg1211_4/ft_pg1211_4
frac_ste_pg1211_Hoenig10 = f2_pg1211_4/ft_pg1211_4
frac_Hii_pg1211_Hoenig10 = f3_pg1211_4/ft_pg1211_4

chi2_pg1411_4, dof_pg1411_4, ft_pg1411_4, min_pg1411_4, max_pg1411_4, f1_pg1411_4, f2_pg1411_4, f3_pg1411_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1411_Hoenig10_4_fluxes_ebv.txt', unpack='True')
frac_torus_pg1411_Hoenig10 = f1_pg1411_4/ft_pg1411_4
frac_ste_pg1411_Hoenig10 = f2_pg1411_4/ft_pg1411_4
frac_Hii_pg1411_Hoenig10 = f3_pg1411_4/ft_pg1411_4

chi2_pg1535_4, dof_pg1535_4, ft_pg1535_4, min_pg1535_4, max_pg1535_4, f1_pg1535_4, f2_pg1535_4, f3_pg1535_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1535_Hoenig10_4_fluxes_ebv.txt', unpack='True')
frac_torus_pg1535_Hoenig10 = f1_pg1535_4/ft_pg1535_4
frac_ste_pg1535_Hoenig10 = f2_pg1535_4/ft_pg1535_4
frac_Hii_pg1535_Hoenig10 = f3_pg1535_4/ft_pg1535_4

chi2_pg2214_4, dof_pg2214_4, ft_pg2214_4, min_pg2214_4, max_pg2214_4, f1_pg2214_4, f2_pg2214_4, f3_pg2214_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg2214_Hoenig10_4_fluxes_ebv.txt', unpack='True')
frac_torus_pg2214_Hoenig10 = f1_pg2214_4/ft_pg2214_4
frac_ste_pg2214_Hoenig10 = f2_pg2214_4/ft_pg2214_4
frac_Hii_pg2214_Hoenig10 = f3_pg2214_4/ft_pg2214_4

frac_torus_Hoenig10 = (frac_torus_3c120_Hoenig10, frac_torus_3c382_Hoenig10, frac_torus_3c445_Hoenig10, frac_torus_AKN120_Hoenig10, frac_torus_OQ208_Hoenig10, frac_torus_ESO548_Hoenig10, frac_torus_Mrk1018_Hoenig10, frac_torus_ngc4258_Hoenig10, frac_torus_pg0844_Hoenig10, frac_torus_pg1011_Hoenig10, frac_torus_pg1211_Hoenig10, frac_torus_pg1411_Hoenig10, frac_torus_pg1535_Hoenig10, frac_torus_pg2214_Hoenig10)

frac_ste_Hoenig10 = (frac_ste_3c120_Hoenig10, frac_ste_3c382_Hoenig10, frac_ste_3c445_Hoenig10, frac_ste_AKN120_Hoenig10, frac_ste_OQ208_Hoenig10, frac_ste_ESO548_Hoenig10, frac_ste_Mrk1018_Hoenig10, frac_ste_ngc4258_Hoenig10, frac_ste_pg0844_Hoenig10, frac_ste_pg1011_Hoenig10, frac_ste_pg1211_Hoenig10, frac_ste_pg1411_Hoenig10, frac_ste_pg1535_Hoenig10, frac_ste_pg2214_Hoenig10)

frac_Hii_Hoenig10 = (frac_Hii_3c120_Hoenig10, frac_Hii_3c382_Hoenig10, frac_Hii_3c445_Hoenig10, frac_Hii_AKN120_Hoenig10, frac_Hii_OQ208_Hoenig10, frac_Hii_ESO548_Hoenig10, frac_Hii_Mrk1018_Hoenig10, frac_Hii_ngc4258_Hoenig10, frac_Hii_pg0844_Hoenig10, frac_Hii_pg1011_Hoenig10, frac_Hii_pg1211_Hoenig10, frac_Hii_pg1411_Hoenig10, frac_Hii_pg1535_Hoenig10, frac_Hii_pg2214_Hoenig10)

############################Hoenig17############################
chi2_3c120_4, dof_3c120_4, ft_3c120_4, min_3c120_4, max_3c120_4, f1_3c120_4, f2_3c120_4, f3_3c120_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/3c120_Hoenig17_4_fluxes_ebv.txt', unpack='True')
frac_torus_3c120_Hoenig17 = f1_3c120_4[0]/ft_3c120_4[0]
frac_ste_3c120_Hoenig17 = f2_3c120_4[0]/ft_3c120_4[0]
frac_Hii_3c120_Hoenig17 = f3_3c120_4[0]/ft_3c120_4[0]

chi2_3c382_2, dof_3c382_2, ft_3c382_2, min_3c382_2, max_3c382_2, f1_3c382_2, f2_3c382_2, f3_3c382_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/3c382_Hoenig17_2_fluxes_ebv.txt', unpack='True')
frac_torus_3c382_Hoenig17 = f1_3c382_2/ft_3c382_2
frac_ste_3c382_Hoenig17 = f2_3c382_2/ft_3c382_2
frac_Hii_3c382_Hoenig17 = f3_3c382_2/ft_3c382_2

chi2_3c445_1, dof_3c445_1, ft_3c445_1, min_3c445_1, max_3c445_1, f1_3c445_1, f2_3c445_1, f3_3c445_1 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/3c445_Hoenig17_1_fluxes_ebv.txt', unpack='True')
frac_torus_3c445_Hoenig17 = f1_3c445_1/ft_3c445_1
frac_ste_3c445_Hoenig17 = f2_3c445_1/ft_3c445_1
frac_Hii_3c445_Hoenig17 = f3_3c445_1/ft_3c445_1

chi2_AKN120_2, dof_AKN120_2, ft_AKN120_2, min_AKN120_2, max_AKN120_2, f1_AKN120_2, f2_AKN120_2, f3_AKN120_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/AKN120_Hoenig17_2_fluxes_ebv.txt', unpack='True')
frac_torus_AKN120_Hoenig17 = f1_AKN120_2/ft_AKN120_2
frac_ste_AKN120_Hoenig17 = f2_AKN120_2/ft_AKN120_2
frac_Hii_AKN120_Hoenig17 = f3_AKN120_2/ft_AKN120_2

chi2_OQ208_3, dof_OQ208_3, ft_OQ208_3, min_OQ208_3, max_OQ208_3, f1_OQ208_3, f2_OQ208_3, f3_OQ208_3 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/OQ208_Hoenig17_3_fluxes_ebv.txt', unpack='True')
frac_torus_OQ208_Hoenig17 = f1_OQ208_3/ft_OQ208_3
frac_ste_OQ208_Hoenig17 = f2_OQ208_3/ft_OQ208_3
frac_Hii_OQ208_Hoenig17 = f3_OQ208_3/ft_OQ208_3

chi2_ESO198_1, dof_ESO198_1, ft_ESO198_1, min_ESO198_1, max_ESO198_1, f1_ESO198_1, f2_ESO198_1, f3_ESO198_1 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ESO198_Hoenig17_1_fluxes_ebv.txt', unpack='True')
frac_torus_ESO198_Hoenig17 = f1_ESO198_1/ft_ESO198_1
frac_ste_ESO198_Hoenig17 = f2_ESO198_1/ft_ESO198_1
frac_Hii_ESO198_Hoenig17 = f3_ESO198_1/ft_ESO198_1

chi2_ESO548_2, dof_ESO548_2, ft_ESO548_2, min_ESO548_2, max_ESO548_2, f1_ESO548_2, f2_ESO548_2, f3_ESO548_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ESO548_Hoenig17_2_fluxes_ebv.txt', unpack='True')
frac_torus_ESO548_Hoenig17 = f1_ESO548_2/ft_ESO548_2
frac_ste_ESO548_Hoenig17 = f2_ESO548_2/ft_ESO548_2
frac_Hii_ESO548_Hoenig17 = f3_ESO548_2/ft_ESO548_2

chi2_Mrk1018_1, dof_Mrk1018_1, ft_Mrk1018_1, min_Mrk1018_1, max_Mrk1018_1, f1_Mrk1018_1, f2_Mrk1018_1, f3_Mrk1018_1 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/Mrk1018_Hoenig17_1_fluxes_ebv.txt', unpack='True')
frac_torus_Mrk1018_Hoenig17 = f1_Mrk1018_1/ft_Mrk1018_1
frac_ste_Mrk1018_Hoenig17 = f2_Mrk1018_1/ft_Mrk1018_1
frac_Hii_Mrk1018_Hoenig17 = f3_Mrk1018_1/ft_Mrk1018_1

chi2_ngc4258_3, dof_ngc4258_3, ft_ngc4258_3, min_ngc4258_3, max_ngc4258_3, f1_ngc4258_3, f2_ngc4258_3, f3_ngc4258_3 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ngc4258_Hoenig17_3_fluxes_ebv.txt', unpack='True')
frac_torus_ngc4258_Hoenig17 = f1_ngc4258_3/ft_ngc4258_3
frac_ste_ngc4258_Hoenig17 = f2_ngc4258_3/ft_ngc4258_3
frac_Hii_ngc4258_Hoenig17 = f3_ngc4258_3/ft_ngc4258_3

chi2_ngc7603_3, dof_ngc7603_3, ft_ngc7603_3, min_ngc7603_3, max_ngc7603_3, f1_ngc7603_3, f2_ngc7603_3, f3_ngc7603_3 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/ngc7603_Hoenig17_3_fluxes_ebv.txt', unpack='True')
frac_torus_ngc7603_Hoenig17 = f1_ngc7603_3[0]/ft_ngc7603_3[0]
frac_ste_ngc7603_Hoenig17 = f2_ngc7603_3[0]/ft_ngc7603_3[0]
frac_Hii_ngc7603_Hoenig17 = f3_ngc7603_3[0]/ft_ngc7603_3[0]

chi2_pg0804_1, dof_pg0804_1, ft_pg0804_1, min_pg0804_1, max_pg0804_1, f1_pg0804_1, f2_pg0804_1, f3_pg0804_1 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg0804_Hoenig17_1_fluxes_ebv.txt', unpack='True')
frac_torus_pg0804_Hoenig17 = f1_pg0804_1/ft_pg0804_1
frac_ste_pg0804_Hoenig17 = f2_pg0804_1/ft_pg0804_1
frac_Hii_pg0804_Hoenig17 = f3_pg0804_1/ft_pg0804_1

chi2_pg0844_2, dof_pg0844_2, ft_pg0844_2, min_pg0844_2, max_pg0844_2, f1_pg0844_2, f2_pg0844_2, f3_pg0844_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg0844_Hoenig17_2_fluxes_ebv.txt', unpack='True')
frac_torus_pg0844_Hoenig17 = f1_pg0844_2/ft_pg0844_2
frac_ste_pg0844_Hoenig17 = f2_pg0844_2/ft_pg0844_2
frac_Hii_pg0844_Hoenig17 = f3_pg0844_2/ft_pg0844_2

chi2_pg1011_1, dof_pg1011_1, ft_pg1011_1, min_pg1011_1, max_pg1011_1, f1_pg1011_1, f2_pg1011_1, f3_pg1011_1 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1011_Hoenig17_1_fluxes_ebv.txt', unpack='True')
frac_torus_pg1011_Hoenig17 = f1_pg1011_1/ft_pg1011_1
frac_ste_pg1011_Hoenig17 = f2_pg1011_1/ft_pg1011_1
frac_Hii_pg1011_Hoenig17 = f3_pg1011_1/ft_pg1011_1

chi2_pg1211_1, dof_pg1211_1, ft_pg1211_1, min_pg1211_1, max_pg1211_1, f1_pg1211_1, f2_pg1211_1, f3_pg1211_1 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1211_Hoenig17_1_fluxes_ebv.txt', unpack='True')
frac_torus_pg1211_Hoenig17 = f1_pg1211_1/ft_pg1211_1
frac_ste_pg1211_Hoenig17 = f2_pg1211_1/ft_pg1211_1
frac_Hii_pg1211_Hoenig17 = f3_pg1211_1/ft_pg1211_1

chi2_pg1411_4, dof_pg1411_4, ft_pg1411_4, min_pg1411_4, max_pg1411_4, f1_pg1411_4, f2_pg1411_4, f3_pg1411_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1411_Hoenig17_4_fluxes_ebv.txt', unpack='True')
frac_torus_pg1411_Hoenig17 = f1_pg1411_4/ft_pg1411_4
frac_ste_pg1411_Hoenig17 = f2_pg1411_4/ft_pg1411_4
frac_Hii_pg1411_Hoenig17 = f3_pg1411_4/ft_pg1411_4

chi2_pg1535_4, dof_pg1535_4, ft_pg1535_4, min_pg1535_4, max_pg1535_4, f1_pg1535_4, f2_pg1535_4, f3_pg1535_4 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg1535_Hoenig17_4_fluxes_ebv.txt', unpack='True')
frac_torus_pg1535_Hoenig17 = f1_pg1535_4/ft_pg1535_4
frac_ste_pg1535_Hoenig17 = f2_pg1535_4/ft_pg1535_4
frac_Hii_pg1535_Hoenig17 = f3_pg1535_4/ft_pg1535_4

chi2_pg2214_2, dof_pg2214_2, ft_pg2214_2, min_pg2214_2, max_pg2214_2, f1_pg2214_2, f2_pg2214_2, f3_pg2214_2 = loadtxt('/Users/mariela/Documents/projects/silicates/AGN-Spitzer-spectrum/final-sample/modeling/archivostexto/pg2214_Hoenig17_2_fluxes_ebv.txt', unpack='True')
frac_torus_pg2214_Hoenig17 = f1_pg2214_2/ft_pg2214_2
frac_ste_pg2214_Hoenig17 = f2_pg2214_2/ft_pg2214_2
frac_Hii_pg2214_Hoenig17 = f3_pg2214_2/ft_pg2214_2

frac_torus_Hoenig17 = (frac_torus_3c120_Hoenig17, frac_torus_3c382_Hoenig17, frac_torus_3c445_Hoenig17, frac_torus_AKN120_Hoenig17,frac_torus_OQ208_Hoenig17,frac_torus_ESO198_Hoenig17,frac_torus_ESO548_Hoenig17,frac_torus_Mrk1018_Hoenig17,frac_torus_ngc4258_Hoenig17,frac_torus_ngc7603_Hoenig17,frac_torus_pg0804_Hoenig17,frac_torus_pg0844_Hoenig17, frac_torus_pg1011_Hoenig17, frac_torus_pg1211_Hoenig17, frac_torus_pg1411_Hoenig17, frac_torus_pg1535_Hoenig17, frac_torus_pg2214_Hoenig17)

frac_ste_Hoenig17 = (frac_ste_3c120_Hoenig17, frac_ste_3c382_Hoenig17, frac_ste_3c445_Hoenig17, frac_ste_AKN120_Hoenig17,frac_ste_OQ208_Hoenig17,frac_ste_ESO198_Hoenig17,frac_ste_ESO548_Hoenig17,frac_ste_Mrk1018_Hoenig17,frac_ste_ngc4258_Hoenig17,frac_ste_ngc7603_Hoenig17,frac_ste_pg0804_Hoenig17,frac_ste_pg0844_Hoenig17, frac_ste_pg1011_Hoenig17, frac_ste_pg1211_Hoenig17, frac_ste_pg1411_Hoenig17, frac_ste_pg1535_Hoenig17, frac_ste_pg2214_Hoenig17)

frac_Hii_Hoenig17 = (frac_Hii_3c120_Hoenig17, frac_Hii_3c382_Hoenig17, frac_Hii_3c445_Hoenig17, frac_Hii_AKN120_Hoenig17,frac_Hii_OQ208_Hoenig17,frac_Hii_ESO198_Hoenig17,frac_Hii_ESO548_Hoenig17,frac_Hii_Mrk1018_Hoenig17,frac_Hii_ngc4258_Hoenig17,frac_Hii_ngc7603_Hoenig17,frac_Hii_pg0804_Hoenig17,frac_Hii_pg0844_Hoenig17, frac_Hii_pg1011_Hoenig17, frac_Hii_pg1211_Hoenig17, frac_Hii_pg1411_Hoenig17, frac_Hii_pg1535_Hoenig17, frac_Hii_pg2214_Hoenig17)

plt.figure('fraction_components')

plt.subplot(221)

hist(frac_torus_fritz06, 5, histtype='step',color='brown', stacked=True, fill=False, linewidth = 4, label='Torus')
hist(frac_ste_fritz06, 5, histtype='step',color='green', stacked=True, fill=False, linewidth = 4, label='Stellar')
hist(frac_Hii_fritz06, 5, histtype='step',color='blue', stacked=True, fill=False, linewidth = 4, label='Torus')
plt.title('Fritz et al. (2006): smooth torus', fontsize=16)
plt.ylabel(r'N',fontsize=20)
#plt.xlabel(r'Fraction',fontsize=16)
plt.legend(loc = 'best', numpoints=1, prop={'size':16})

tick_params(axis='x', labelsize=16)
tick_params(axis='y', labelsize=16)

plt.subplot(222)

hist(frac_torus_Nenkova08, 5, histtype='step',color='brown', stacked=True, fill=False, linewidth = 4, label='Torus')
hist(frac_ste_Nenkova08, 5, histtype='step',color='green', stacked=True, fill=False, linewidth = 4, label='Stellar')
hist(frac_Hii_Nenkova08, 5, histtype='step',color='blue', stacked=True, fill=False, linewidth = 4, label='Torus')

plt.title('Nenkova et al. (2008a, b): clumpy torus', fontsize=18)
plt.ylabel(r'N',fontsize=20)
#plt.xlabel(r'Fraction',fontsize=16)
#plt.legend(loc = 'best', numpoints=1, prop={'size':16})
tick_params(axis='x', labelsize=16)
tick_params(axis='y', labelsize=16)

plt.subplot(223)
hist(frac_torus_Hoenig10, 5, histtype='step',color='brown', stacked=True, fill=False, linewidth = 4, label='Torus')
hist(frac_ste_Hoenig10, 5, histtype='step',color='green', stacked=True, fill=False, linewidth = 4, label='Stellar')
hist(frac_Hii_Hoenig10, 5, histtype='step',color='blue', stacked=True, fill=False, linewidth = 4, label='Torus')

plt.title('Hoenig et al. (2010): clumpy torus', fontsize=18)
plt.ylabel(r'N',fontsize=20)
plt.xlabel(r'Fraction',fontsize=16)
#plt.legend(loc = 'best', numpoints=1, prop={'size':16})

tick_params(axis='x', labelsize=16)
tick_params(axis='y', labelsize=16)

plt.subplot(224)
hist(frac_torus_Hoenig17, 5, histtype='step',color='brown', stacked=True, fill=False, linewidth = 4, label='Torus')
hist(frac_ste_Hoenig17, 5, histtype='step',color='green', stacked=True, fill=False, linewidth = 4, label='Stellar')
hist(frac_Hii_Hoenig17, 5, histtype='step',color='blue', stacked=True, fill=False, linewidth = 4, label='Torus')

plt.title('Hoenig et al. (2017): clumpy torus', fontsize=18)
plt.ylabel(r'N',fontsize=20)
plt.xlabel(r'Fraction',fontsize=16)
#plt.legend(loc = 'best', numpoints=1, prop={'size':16})

tick_params(axis='x', labelsize=16)
tick_params(axis='y', labelsize=16)

plt.show()

