

from datetime import datetime
import os
import shutil


def fnc_saveDirectory():
	save_dir = 'Output/' + datetime.now().strftime('%Y_%m_%d-%H_%M_%S') + '/'
	os.makedirs(save_dir)
	os.makedirs(save_dir + 'Data/')
	os.makedirs(save_dir + 'Plots/')
	
	config_filename = 'config-lift.json'
	if os.path.exists(config_filename):  shutil.copy(config_filename, save_dir)

	return save_dir

