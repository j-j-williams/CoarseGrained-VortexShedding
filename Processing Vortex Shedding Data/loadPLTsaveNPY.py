
###########################################################################
# This code is adapted from Sam Rudy's code for loading IBPM  data, 
# published as part of his original work on PDE-FIND
# See: https://github.com/snagcliffs/PDE-FIND
# and: https://github.com/snagcliffs/PDE-FIND/blob/master/Datasets/von_karman/Loading%20ibpm%20output.ipynb
# and:  <<  link to my own copy of "Sam Rudy's Code for Loading IBPM Data.ipynb"  >>
###########################################################################


###  Import modules
import numpy as np
import os
import time
import matplotlib.pyplot as plt


###  Set the load file
data_path = '/Users/stevebrunton/Documents/ibpm-master/Lab iMac Sims/Production Runs/' + str_runTitle + '/'


nx = 2700
ny = 800


###  Set  loading string
save_path = data_path + 'Data/'
filenames = sorted([os.path.join(data_path,f) for f in os.listdir(data_path) if f[-3:] == 'plt'])
nt = len(filenames)


###  Load the .PLT data and save it as .NPY


U = np.zeros(( nx-1 , ny-1 ))
V = np.zeros(( nx-1 , ny-1 ))
W = np.zeros(( nx-1 , ny-1 ))
start = time.time()


# partial_fudge_factor = 660
partial_fudge_factor = 0

print('Beginning data conversion!')
print('Automatic removal of .PLT files set to  OFF -- right ??')

for it in range( nt ):
    print('i  =  ' + str(it+partial_fudge_factor) + '  /  ' + str(nt-1+partial_fudge_factor))
    
    
    timestep_data = np.genfromtxt(filenames[it], delimiter=' ',skip_header=6)
    
    for ix in range( nx-1 ):
        
        for iy in range( ny-1 ):

            U[ ix , iy ] = timestep_data[ ix + (nx-1) * iy , 2]
            V[ ix , iy ] = timestep_data[ ix + (nx-1) * iy , 3]
            W[ ix , iy ] = timestep_data[ ix + (nx-1) * iy , 4]
        
    np.save( save_path + 'U/U_' + str(it+partial_fudge_factor) + '.npy' , U )
    np.save( save_path + 'V/V_' + str(it+partial_fudge_factor) + '.npy' , V )
    np.save( save_path + 'W/W_' + str(it+partial_fudge_factor) + '.npy' , W )
    
#   os.remove(filenames[it])


print('\n\nFinished!!\n\n')




###  Plot full colormaps of the data


# Plot  x-velocity
plt.figure(figsize=(12,6))
plt.pcolormesh(U.T , cmap='coolwarm' )

plt.xlabel('x' , fontsize=16)
plt.ylabel('y' , fontsize=16)
ttl_str = 'U(x,y ; t = ' + str(it) + ')'
plt.title(ttl_str , fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.colorbar()

plt.show()


# Plot  y-velocity
plt.figure(figsize=(12,6))
plt.pcolormesh(V.T , cmap='coolwarm' )

plt.xlabel('x' , fontsize=16)
plt.ylabel('y' , fontsize=16)
ttl_str = 'V(x,y ; t = ' + str(it) + ')'
plt.title(ttl_str , fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.colorbar()

plt.show()


# Plot  vorticity
plt.figure(figsize=(12,6))
plt.pcolormesh(W.T , cmap='coolwarm' )

plt.xlabel('x' , fontsize=16)
plt.ylabel('y' , fontsize=16)
ttl_str = 'W(x,y ; t = ' + str(it) + ')'
plt.title(ttl_str , fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.colorbar()

plt.show()






