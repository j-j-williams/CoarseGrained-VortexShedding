import numpy as np
import pysindy as ps


def fnc_raiseDim_ddt_lift( t , TD_Embed , data , should_normalize ):

	# Retaining this code from the TDE function ensures that under both TDE and d/dt,
	# the time interval and length is the same – assuming we are careful enough to
	# input a good/correct tau for TDE even when doing d/dt

	t_1 = t
	t_2 = t+TD_Embed
	TD_Embed_Index = np.argmin( np.abs(t - TD_Embed) )
	TD_Embed_backendIndex = np.argmin( np.abs( t_2 - np.max(t_1) ) ) 
	data_1 = data[TD_Embed_Index:-1 ]


	if should_normalize == 1: 
		# Only normalize the original signal when time-differentiating
		data_1 = data_1 / np.max(np.abs(data_1));


	dt = t[1]-t[0]
	
	data_2 = ps.FiniteDifference(axis=0)._differentiate(data_1  , dt)
	t_Ovlp = t[TD_Embed_Index:-1]

	return t_Ovlp , data_1 , data_2

