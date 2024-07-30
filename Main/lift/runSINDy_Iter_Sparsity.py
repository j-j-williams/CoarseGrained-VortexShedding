
from runSINDy import fnc_runSINDy
import numpy as np
import pysindy as ps

import warnings
warnings.filterwarnings("ignore", category=UserWarning)


def fnc_runSINDy_Iter_Sparsity( data_1 , data_2 , t_PS , dt , diff_order , poly_order , threshold ):
	
	n_terms = 10


	threshold_num = 21
	threshold_vec = np.linspace( 0 , threshold , num=threshold_num )
	print('Iterating from lambda = ' + str(0) + ' to lambda = ' + str(threshold))


	NRMSE_1_thresh = np.zeros(( threshold_num , ))
	NRMSE_2_thresh = np.zeros(( threshold_num , ))
	NRMSE_sys_thresh = np.zeros(( threshold_num , ))

	Coefs_u1_thresh = np.zeros(( threshold_num , n_terms ))
	Coefs_u2_thresh = np.zeros(( threshold_num , n_terms ))


	
	for i_threshold in range( threshold_num ):

	    threshold_sub = threshold_vec[i_threshold]

	    if np.mod(i_threshold , threshold_num//10) == 0: 
	    	print('Iteration  =  '+str(i_threshold)+'  /  '+str(threshold_num-1) + '  |  lambda  =  ' + str(threshold_sub) )


	    model , coefs , x_test_sim , error_1 , error_2 , NRMSE_1 , NRMSE_2 , NRMSE_sys = \
	    fnc_runSINDy( data_1 , data_2 , t_PS , dt , diff_order , poly_order , threshold_sub)



	    Coefs_u1_thresh[i_threshold , :] = coefs[0,:]
	    Coefs_u2_thresh[i_threshold , :] = coefs[1,:]


	    NRMSE_1_thresh[i_threshold] = np.sqrt( np.sum(error_1**2) / np.sum(data_1**2) )
	    NRMSE_2_thresh[i_threshold] = np.sqrt( np.sum(error_2**2) / np.sum(data_2**2) )


	NRMSE_sys_thresh = np.sqrt( NRMSE_1_thresh**2 + NRMSE_2_thresh**2 )


	return threshold_vec , Coefs_u1_thresh , Coefs_u2_thresh , NRMSE_1_thresh , NRMSE_2_thresh , NRMSE_sys_thresh

