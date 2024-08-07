
import numpy as np
import pysindy as ps
import json

import warnings
warnings.filterwarnings("ignore")

from loadData_lift import fnc_loadData_lift
from raiseDim_lift import fnc_raiseDim_lift
from runSINDy import fnc_runSINDy
from saveDirectory import fnc_saveDirectory
from saveData import fnc_saveData


def fnc_runSINDy_Iter_Sparsity():
	

	###  Create the unique output directory
	save_dir = fnc_saveDirectory()


	###  Load the the configuration file with all analysis settings and parameters
	with open('config-lift.json', 'r') as f:
	    config = json.load(f)
	globals().update(config)
	n_terms = np.math.comb(poly_order + 2, 2)


	###  Load data
	t , C_l , C_d , dt = fnc_loadData_lift( Re , t_trm_1 , t_trm_2 , regime )


	###  Raise dimension of system by either time-delay embedding or time-differentiating
	from raiseDim_lift import fnc_raiseDim_lift
	t_PS , data_1 , data_2 = \
	fnc_raiseDim_lift( TDE_or_ddt , t , TD_Embed, C_l , C_d , l_d_flag , should_normalize )


	###  Prepare to iterative on sparsity
	threshold_num = iterations
	threshold_vec = np.linspace( 0 , threshold , num=threshold_num )
	print('\n\nIterating from lambda = ' + str(0) + ' to lambda = ' + str(threshold) + '\n')

	NRMSE_1_thresh = np.zeros(( threshold_num , ))
	NRMSE_2_thresh = np.zeros(( threshold_num , ))
	NRMSE_sys_thresh = np.zeros(( threshold_num , ))

	Coefs_u1_thresh = np.zeros(( threshold_num , n_terms ))
	Coefs_u2_thresh = np.zeros(( threshold_num , n_terms ))

	
	for i_threshold in range( threshold_num ):

	    threshold_sub = threshold_vec[i_threshold]

	    if np.mod(i_threshold , threshold_num//10) == 0:  print('Iteration  =  '+str(i_threshold)+'  /  '+str(threshold_num-1) + '  |  lambda  =  ' + str(threshold_sub) )


    	###  Run SINDy
	    model , coefs , x_test_sim , error_1 , error_2 , NRMSE_1 , NRMSE_2 , NRMSE_sys = \
	    fnc_runSINDy( data_1 , data_2 , t_PS , dt , diff_order , poly_order , threshold_sub)


	    Coefs_u1_thresh[i_threshold , :] = coefs[0,:]
	    Coefs_u2_thresh[i_threshold , :] = coefs[1,:]


	    NRMSE_1_thresh[i_threshold] = np.sqrt( np.sum(error_1**2) / np.sum(data_1**2) )
	    NRMSE_2_thresh[i_threshold] = np.sqrt( np.sum(error_2**2) / np.sum(data_2**2) )


	NRMSE_sys_thresh = np.sqrt( NRMSE_1_thresh**2 + NRMSE_2_thresh**2 )


	###  Save the data
	save_arrays = [ threshold_vec , Coefs_u1_thresh , Coefs_u2_thresh , NRMSE_1_thresh , NRMSE_2_thresh , NRMSE_sys_thresh ]
	save_names = [ 'threshold_vec.npy' , 'Coefs_u1.npy' , 'Coefs_u2.npy' , 'NRMSE_1.npy' , 'NRMSE_2.npy' , 'NRMSE_sys.npy' ]
	fnc_saveData(save_dir , save_arrays , save_names)


	return save_dir , model , threshold_vec , Coefs_u1_thresh , Coefs_u2_thresh , NRMSE_1_thresh , NRMSE_2_thresh , NRMSE_sys_thresh

