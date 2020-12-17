
from inputs import *
import numpy as np

# Initialize:

phi_dl_an_0 = phi_an_0 - phi_sep_0
phi_dl_ca_0 = phi_ca_0 - phi_sep_0




t_final = charge_frac*3600./C_rate

SV_0 = np.array([phi_dl_an_0, phi_dl_ca_0]) #how to account for two different phis? weighted average?

# Load inputs and other parameters into 'pars' class:
class pars:
    eps_gr_r = np.divide(W_gr_list[6], density_gr * H_an * A_an)
    eps_si_r = np.divide(W_si_list[1], density_si * H_an * A_an)
    eps_gr_list_W = np.divide(W_gr_list, density_gr * (H_an * A_an))
    eps_si_list_W =  np.divide(W_si_list, density_si * (H_an * A_an))

    capacity_anode_r = H_an * (capacity_gr*eps_gr_r*density_gr + capacity_si*eps_si_r*density_si)
    capacity_anode_list_W = H_an * (capacity_gr*eps_gr_list_W*density_gr + capacity_si*eps_si_list_W*density_si)
    capacity_cathode = capacity_nmc*H_ca*eps_nmc*density_nmc
    
    capacity_area_r = min(capacity_anode_r,capacity_cathode)
    capacity_area_W = np.zeros_like(capacity_anode_list_W)
    for i in np.arange(len(capacity_anode_list_W)):    
        capacity_area_W[i] = min(capacity_anode_list_W[i],capacity_cathode)

    T = T

    dPhi_eq_gr = dPhi_eq_gr
    dPhi_eq_si = dPhi_eq_si
    dPhi_eq_ca = dPhi_eq_ca

    i_o_gr = i_o_gr
    n_gr = n_gr
    beta_gr = beta_gr
    i_o_si = i_o_si
    n_si = n_si
    beta_si = beta_si

    i_o_ca = i_o_ca
    n_ca = n_ca
    beta_ca = beta_ca

    C_dl_an_inv = 1/C_dl_an
    C_dl_ca_inv = 1/C_dl_ca

    i_ext_list_W = C_rate*capacity_area_W
    i_ext_r = C_rate*capacity_area_r

    A_fac_gr_r = np.divide(r_gr, 3*H_an*eps_gr_r)
    A_fac_si_r = np.divide(r_si, 3*H_an*eps_si_r)
    A_fac_gr_list_W = np.divide(r_gr[0], 3*H_an*eps_gr_list_W)
    A_fac_si_list_W = np.divide(r_si[3], 3*H_an*eps_si_list_W)
    A_fac_ca = r_nmc/3/H_ca/eps_nmc


