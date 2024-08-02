
import numpy as np

def fnc_loadData_vorticity( Re , data_choice_string , y_CG_1 , y_CG_2 ):

	stem = '../../Vortex Shedding Data/'


	data = np.load( stem + 'Coarse-Grained Flowfield Data/y-avg/Re' + str(Re) + '/' + data_choice_string + '/' + data_choice_string + '_y' + str(y_CG_1) + '_y' + str(y_CG_2) + '.npy' )


	x  = np.load( stem + 'Parameters/Re' + str(Re) + '/x.npy' )
	t  = np.load( stem + 'Parameters/Re' + str(Re) + '/t.npy' )
	dx = np.load( stem + 'Parameters/Re' + str(Re) + '/dx.npy' )[0][0]
	dt = np.load( stem + 'Parameters/Re' + str(Re) + '/dt.npy' )[0][0]


	return data , x , t , dx , dt