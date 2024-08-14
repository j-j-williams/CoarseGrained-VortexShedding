
import numpy as np


def fnc_loadData_vorticity( Re , data_choice_string , y_CG_1 , y_CG_2 , regime ):

	###  Set loading strings
	if   regime == "trans":   stem = '../../Vortex Shedding Data/Transient/'
	elif regime == "steady":  stem = '../../Vortex Shedding Data/Steady State/'

	stem = stem + 'Re' + str(Re) + '/'

	###  Load data
	data = np.load( stem + 'CoarseGrained-Data/' + data_choice_string + '_y' + str(y_CG_1) + '_y' + str(y_CG_2) + '.npy' )

	###  Load parameters
	x  = np.load( stem + 'Parameters/x.npy' )
	t  = np.load( stem + 'Parameters/t.npy' )
	dx = np.load( stem + 'Parameters/dx.npy' )[0][0]
	dt = np.load( stem + 'Parameters/dt.npy' )[0][0]


	return data , x , t , dx , dt