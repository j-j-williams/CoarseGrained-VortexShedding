
###  Import modules

import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import os


###  Set parameter 

plot_U = 1
plot_V = 1
plot_W = 1

str_runTitle = 'Re100-prd'

plt_start = 0
plt_stop  = 501


###  Set  loading string

stem = '/Users/stevebrunton/Documents/ibpm-master/Lab iMac Sims/Production Runs/' +str_runTitle+ '/Data/'


directory = stem + 'U/'
N_plt = len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])


###  Plot full colormaps of the data

for i_plt in range( plt_start , plt_stop  ):
    
	if np.mod( i_plt , N_plt//10 ) == 0: print('i  =  ' +str(i_plt) + '  /  ' +str(N_plt-1) )

	U = np.load( stem + 'U/' + 'U_' + str(i_plt) + '.npy' )
	V = np.load( stem + 'V/' + 'V_' + str(i_plt) + '.npy' )
	W = np.load( stem + 'W/' + 'W_' + str(i_plt) + '.npy' )

	if plot_U == 1:
		# Plot  x-velocity
		plt.figure(figsize=(12,6))
		plt.pcolormesh(U.T , cmap='coolwarm' , vmin = -0.2 , vmax = 1.2 )
		plt.xlabel('x' , fontsize=16)
		plt.ylabel('y' , fontsize=16)
		ttl_str = 'U(x,y ; t = ' + str(i_plt) + ')'
		plt.title(ttl_str , fontsize=16)
		plt.xticks(fontsize=14)
		plt.yticks(fontsize=14)
		plt.colorbar()
		plt.savefig(str_runTitle + '/U/Flowfield-U-' + str(i_plt) + '.png')
		plt.close()

	if plot_V == 1:
		# Plot  y-velocity
		plt.figure(figsize=(12,6))
		plt.pcolormesh(V.T , cmap='coolwarm' , vmin = -0.5 , vmax = 0.5 )
		plt.xlabel('x' , fontsize=16)
		plt.ylabel('y' , fontsize=16)
		ttl_str = 'V(x,y ; t = ' + str(i_plt) + ')'
		plt.title(ttl_str , fontsize=16)
		plt.xticks(fontsize=14)
		plt.yticks(fontsize=14)
		plt.colorbar()
		plt.savefig(str_runTitle + '/V/Flowfield-V-' + str(i_plt) + '.png')
		plt.close()

	if plot_W == 1:
		# Plot  vorticity
		plt.figure(figsize=(12,6))
		plt.pcolormesh(W.T , cmap='coolwarm' , vmin = -2 , vmax = 2 )
		plt.xlabel('x' , fontsize=16)
		plt.ylabel('y' , fontsize=16)
		ttl_str = 'W(x,y ; t = ' + str(i_plt) + ')'
		plt.title(ttl_str , fontsize=16)
		plt.xticks(fontsize=14)
		plt.yticks(fontsize=14)
		plt.colorbar()
		plt.savefig(str_runTitle + '/W/Flowfield-W-' + str(i_plt) + '.png')
		plt.close()

