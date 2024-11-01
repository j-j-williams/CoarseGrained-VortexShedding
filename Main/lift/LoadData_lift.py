
import numpy as np


def fnc_loadData_lift( Re , t_trm_1 , t_trm_2, regime ):

    ###  Set loading strings
    if   regime == "trans":   stem = '../../Vortex Shedding Data/Transient/'
    elif regime == "steady":  stem = '../../Vortex Shedding Data/Steady State/'

    filename = stem + 'Re' + str(Re) + '/ibpm.force'

    ###  Load data
    full_simulation_data = np.genfromtxt(filename, dtype="f8", delimiter=" ")
    t =   full_simulation_data[t_trm_1 : t_trm_2, 1]
    C_l = full_simulation_data[t_trm_1 : t_trm_2, 3]
    C_d = full_simulation_data[t_trm_1 : t_trm_2, 2]

    # adjust t
    t = t-t[0]

    # Derived quantites
    dt = t[1]-t[0]


    return t , C_l , C_d , dt