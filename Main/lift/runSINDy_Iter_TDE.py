
import numpy as np
import pysindy as ps
import json

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from LoadData_lift import fnc_LoadData_lift
from raiseDim_lift import fnc_raiseDim_lift
from runSINDy import fnc_runSINDy
from saveDirectory import fnc_saveDirectory
from saveData import fnc_saveData


def fnc_runSINDy_Iter_TDE():
	

	###  Create the unique output directory
	save_dir = fnc_saveDirectory()
	

	###  Load the the configuration file with all analysis settings and parameters
	with open('Lift-config.json', 'r') as f:
	    config = json.load(f)
	globals().update(config)
	n_terms = np.math.comb(poly_order + 2, 2)


	###  Load data
	t , C_l , C_d , dt = fnc_LoadData_lift( Re , t_trm_1 , t_trm_2 )


	TDE_num = iterations
	TDE_vec = np.linspace( 0 , TD_Embed , num=TDE_num )
	print('\n\nIterating from tau = ' + str(0) + ' to tau = ' + str(TD_Embed) + '\n')


	NRMSE_1_TDE = np.zeros(( TDE_num , ))
	NRMSE_2_TDE = np.zeros(( TDE_num , ))
	NRMSE_sys_TDE = np.zeros(( TDE_num , ))

	Coefs_u1_TDE = np.zeros(( TDE_num , n_terms ))
	Coefs_u2_TDE = np.zeros(( TDE_num , n_terms ))


	for i_TDE in range( TDE_num ):

		TDE_sub = TDE_vec[i_TDE]

		###  Raise dimension of system by either time-delay embedding or time-differentiating
		t_PS , data_1 , data_2 = fnc_raiseDim_lift( TDE_or_ddt , t , TDE_sub, C_l , C_d , l_d_flag , should_normalize)




		if np.mod(i_TDE , TDE_num//10) == 0: 
			print('Iteration  =  '+str(i_TDE)+'  /  '+str(TDE_num-1) + '  |  tau  =  ' + str(TDE_sub) )


		model , coefs , x_test_sim , error_1 , error_2 , NRMSE_1 , NRMSE_2 , NRMSE_sys = \
		fnc_runSINDy( data_1 , data_2 , t_PS , dt , diff_order , poly_order , threshold )



		Coefs_u1_TDE[i_TDE , :] = coefs[0,:]
		Coefs_u2_TDE[i_TDE , :] = coefs[1,:]


		NRMSE_1_TDE[i_TDE] = np.sqrt( np.sum(error_1**2) / np.sum(data_1**2) )
		NRMSE_2_TDE[i_TDE] = np.sqrt( np.sum(error_2**2) / np.sum(data_2**2) )


	NRMSE_sys_TDE = np.sqrt( NRMSE_1_TDE**2 + NRMSE_2_TDE**2 )


	###  Save the data
	save_arrays = [ TDE_vec , Coefs_u1_TDE , Coefs_u2_TDE , NRMSE_1_TDE , NRMSE_2_TDE , NRMSE_sys_TDE ]
	save_names = [ 'TDE_vec.npy' , 'Coefs_u1.npy' , 'Coefs_u2.npy' , 'NRMSE_1.npy' , 'NRMSE_2.npy' , 'NRMSE_sys.npy' ]
	fnc_saveData(save_dir , save_arrays , save_names)


	return save_dir , model , TDE_vec , Coefs_u1_TDE , Coefs_u2_TDE , NRMSE_1_TDE , NRMSE_2_TDE , NRMSE_sys_TDE

