
import numpy as np
import pysindy as ps

import warnings
warnings.filterwarnings("ignore", category=UserWarning)


def fnc_runSINDy( data_1 , data_2 , t_PS , dt, diff_order , poly_order , threshold ):


	zeta_dt = ps.FiniteDifference(axis=0)._differentiate(data_1  , dt)
	eta_dt  = ps.FiniteDifference(axis=0)._differentiate(data_2  , dt)
	# return zeta_t , eta_t

	X = np.asarray([data_1, data_2]).T
	feature_names = ["x", "y"]

	model = ps.SINDy(
	    differentiation_method = ps.FiniteDifference(order   	= diff_order ) ,
	    feature_library        = ps.PolynomialLibrary(degree	= poly_order ) , 
	    optimizer              = ps.STLSQ(threshold			 	= threshold),
	    feature_names          = feature_names,)


	###  Generate SINDy fit

	model.fit(X, t=t_PS, quiet=True)


	coefs = model.coefficients()
    

	X0 = X[0,:]
	x_test_sim = model.simulate(X0, t_PS)
	error_1 = data_1 - x_test_sim[:,0]
	error_2 = data_2 - x_test_sim[:,1]

	NRMSE_1 = np.sqrt( np.sum(error_1**2) / np.sum(data_1**2) )
	NRMSE_2 = np.sqrt( np.sum(error_2**2) / np.sum(data_2**2) )

	NRMSE_sys = np.sqrt( NRMSE_1**2 + NRMSE_2**2 )


	return model , coefs , x_test_sim , error_1 , error_2 , NRMSE_1 , NRMSE_2 , NRMSE_sys




