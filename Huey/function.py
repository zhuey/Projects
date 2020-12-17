import numpy as np
from math import exp

# Constants
F = 96485
R = 8.3145

def residual(t, SV, pars):

    RTinv = 1/R/pars.T
    dSV_dt = np.zeros_like(SV)
    
    eta_gr = SV[0] - pars.dPhi_eq_gr
    i_Far_gr = pars.i_o_gr*(exp(-pars.n_gr*F*pars.beta_gr*eta_gr*RTinv) - exp(pars.n_gr*F*(1-pars.beta_gr)*eta_gr*RTinv))
    i_dl_gr = pars.i_ext*pars.eps_gr*pars.A_fac_gr - i_Far_gr
    
    eta_si = SV[0] - pars.dPhi_eq_si
    i_Far_si = pars.i_o_si*(exp(-pars.n_si*F*pars.beta_si*eta_si*RTinv) - exp(pars.n_si*F*(1-pars.beta_si)*eta_si*RTinv))
    i_dl_si = pars.i_ext*pars.eps_si*pars.A_fac_si - i_Far_si

    i_dl_an = i_dl_gr * pars.eps_gr + i_dl_si * pars.eps_si

    dSV_dt[0] = i_dl_an*pars.C_dl_an_inv
    
    eta_ca = SV[1] - pars.dPhi_eq_ca
    i_Far_ca = pars.i_o_ca*(exp(-pars.n_ca*F*pars.beta_ca*eta_ca*RTinv)
                      - exp(pars.n_ca*F*(1-pars.beta_ca)*eta_ca*RTinv))
    i_dl_ca = -pars.i_ext*pars.A_fac_ca - i_Far_ca
    
    
    dSV_dt[1] = i_dl_ca*pars.C_dl_ca_inv
    
    return dSV_dt