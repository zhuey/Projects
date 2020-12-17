from scipy.integrate import solve_ivp
import numpy as np
from function import residual
from inputs import *

from init import SV_0, t_final, pars

time_span = np.array([0,t_final])



for i in np.arange(len(W_gr_list)): 
    pars.eps_gr = pars.eps_gr_list_W[i]
    pars.eps_si = pars.eps_si_list_W[i]
    pars.i_ext = pars.i_ext_list_W[i]
    pars.A_fac_gr = pars.A_fac_gr_list_W[i]
    pars.A_fac_si = pars.A_fac_si_list_W[i]

    solution = solve_ivp(lambda t, y: residual(t, y, pars), time_span, SV_0, method='BDF',
        rtol=1e-6, atol=1e-8)
    
    from matplotlib import pyplot as plt
    #for var in solution.y:
    # plt.plot(solution.t,var)
    plt.plot(solution.t,solution.y[1]-solution.y[0])
plt.xlabel('Time (s)',fontsize=14)
plt.ylabel('Voltage (V)',fontsize=14)
plt.savefig('composition.pdf',dpi=350)
plt.legend(['Si-Gr 0.8-0.1','Si-Gr 0.7-0.2','Si-Gr 0.6-0.3','Si-Gr 0.5-0.4','Si-Gr 0.4-0.5','Si-Gr 0.3-0.6','Si-Gr 0.2-0.7','Si-Gr 0.1-0.8',], ncol=2)
plt.show()

plt.plot(W_si_list,np.ones(len(W_si_list))*pars.capacity_cathode, color='darkcyan')
plt.plot(W_si_list,pars.capacity_anode_list_W, color='magenta')
plt.xlabel('Weight fraction Si', fontsize=14)
plt.ylabel('Capacity, $Ah\ kg^{-1}$',fontsize=14)
plt.legend(['Cathode capacity','Anode capacity'])
plt.savefig('capacity.jpg',dpi=350)
plt.show()

