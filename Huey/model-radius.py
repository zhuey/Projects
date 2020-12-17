from scipy.integrate import solve_ivp
import numpy as np
from function import residual
from inputs import *

from init import SV_0, t_final, pars

time_span = np.array([0,t_final])

#solution = np.zeros_like(pars.A_fac_si_list)
pars.A_fac_gr = pars.A_fac_gr_r[0]
pars.i_ext = pars.i_ext_r
pars.eps_gr = pars.eps_gr_r
pars.eps_si = pars.eps_si_r
for i in np.arange(len(pars.A_fac_si_r)):

    pars.A_fac_si = pars.A_fac_si_r[i] 
      
    solution = solve_ivp(lambda t, y: residual(t, y, pars), time_span, SV_0, method='BDF',
        rtol=1e-6, atol=1e-8)
    
    from matplotlib import pyplot as plt
    
    plt.plot(solution.t,solution.y[1]-solution.y[0])
plt.xlabel('Time (s)',fontsize=14)
plt.ylabel('Voltage (V)',fontsize=14)

plt.legend(['100 $\mu m$','10 $\mu m$', '1 $\mu m$', '100 $nm$'])
plt.savefig('silicon radius.jpg',dpi=350)
plt.show()

pars.A_fac_si = pars.A_fac_si_r[0]
for i in np.arange(len(pars.A_fac_si_r)):

    pars.A_fac_gr = pars.A_fac_gr_r[i] 
      

    solution = solve_ivp(lambda t, y: residual(t, y, pars), time_span, SV_0, method='BDF',
        rtol=1e-6, atol=1e-8)

    from matplotlib import pyplot as plt
    
    plt.plot(solution.t,solution.y[1]-solution.y[0])
plt.xlabel('Time (s)',fontsize=14)
plt.ylabel('Voltage (V)',fontsize=14)

plt.legend(['100 $\mu m$','10 $\mu m$', '1 $\mu m$', '100 $nm$'])
plt.savefig('graphite radius.jpg',dpi=350)
plt.show()