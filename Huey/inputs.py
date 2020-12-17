import numpy as np

# Inputs
C_rate = 0.1 # How many charges per hour?

T = 298 #K

r_gr = [100E-6, 100E-7, 100E-8, 100E-9] #m, Hitatchi
r_si = [100E-6,100E-7,100E-8, 100E-9] #m, from CAMP, Paraclete Energy 
phi_an_0 = 0 #V
C_dl_an = 1e4 #F/m2
i_o_gr = 4.0  #A/m2
i_o_si = 0.5
n_gr = -1
n_si = -3.75
beta_gr = 0.5
beta_si = 0.5
H_an = 30e-6  #m
density_gr = 2260 #kg/m3
capacity_gr = 350 #Ah/kg
W_gr_list = np.linspace(0.1,0.8,8)  #weight frac
density_si = 2330 #kg/m3
capacity_si = 4200 #Ah/kg
W_si_list = 0.9 - W_gr_list #weight frac
dPhi_eq_gr = -0.125
dPhi_eq_si = -1.05 #??
A_an = 1E-4 #m2, total surface of anode (x*y), for calculating volume fractions

phi_sep_0 = 1.8  #V

r_nmc = 0.3e-6 #m, from CAMP
phi_ca_0 = 4.6  #V
C_dl_ca = 1e4 #F/m2
i_o_ca = 100 #A/m2
n_ca = -1
beta_ca = 0.5
H_ca = 50e-6  #m
density_nmc = 2200  #kg/m3, from Targray NMC 811
capacity_nmc = 185  #Ah/kg
eps_nmc = 0.65
dPhi_eq_ca = 4.07

# How deep do we want to charge/discharge?
charge_frac = 0.9