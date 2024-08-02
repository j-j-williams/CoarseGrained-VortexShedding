

from datetime import datetime
import os
import shutil
import numpy as np


def fnc_saveDirectory_vorticity( Re , data_choice_string , y_CG_1 , y_CG_2 , x_trnc_pt_a , x_trnc_pt_b , TD_Embed ):
	str_datetime = datetime.now().strftime("%Y_%m_%d_%H%M%S")
	# save_dir = 'Output/'  + str_datetime + '__Re' + str(Re) + '_' + data_choice_string+ '_y' + str(y_CG_1) + '_y' + str(y_CG_2) +'_x' + str(np.round(x[1+x_trnc_pt_a],1)) + '_x' + str(np.round(x[1+x_trnc_pt_b],1)) + '_TD' + str(TD_Embed)
	save_dir = 'Output/'  + str_datetime + '__Re' + str(Re) + '_' + data_choice_string+ '_y' + str(y_CG_1) + '_y' + str(y_CG_2) +'_x' + str(x_trnc_pt_a) + '_x' + str(x_trnc_pt_b) + '_TD' + str(TD_Embed) + '/'
	os.mkdir(save_dir)
	os.makedirs(save_dir + 'Data/')
	os.makedirs(save_dir + 'Plots/')

	config_filename = 'config-vorticity.json'
	if os.path.exists(config_filename):  shutil.copy(config_filename, save_dir)

	return save_dir

