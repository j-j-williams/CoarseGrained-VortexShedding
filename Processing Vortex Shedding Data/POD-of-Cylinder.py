import numpy as np
import matplotlib.pyplot as plt



def compute_pod(U_data):
    # Reshape the data to form a matrix X of size (M, T), where M = Nx * Ny
    Nx, Ny, T = U_data.shape
    M = Nx * Ny
    X = U_data.reshape(M, T)
    
    # covariance matrix C = X^T X (size T x T)
    C = np.dot(X.T, X)
    
    # eigenvalue decomposition of the covariance matrix
    eigvals, eigvecs = np.linalg.eigh(C)  # eigvecs is a T x T matrix
    
    # sort eigenvalues and eigenvectors in descending order
    sorted_indices = np.argsort(eigvals)[::-1]
    eigvals = eigvals[sorted_indices]
    eigvecs = eigvecs[:, sorted_indices]
    
    # compute POD modes (size M x T) and normalize
    POD_modes = np.dot(X, eigvecs) ;  POD_modes = POD_modes / np.linalg.norm(POD_modes, axis=0)
    
    return POD_modes, eigvals



def plot_pod_modes(POD_modes, Nx, Ny, mode_idx , stem , results_dir ):

    plt_fontsize  = 24
    tick_fontsize = 18

    if mode_idx == 0:
        prm_vminmax = 0.0025 

    x_L = -2
    y_B = -4
    L = 54
    H = 8
    x = np.linspace( x_L ,  x_L + L ,  num=Nx+2 )
    y = np.linspace( y_B ,  y_B + H ,  num=Ny+2 )


    mode = POD_modes[:, mode_idx].reshape(Nx, Ny)
    prm_vminmax = np.max( np.abs( [np.max(mode) , np.min(mode)]  )  )


    xy_mshgrd , yx_mshgrd = np.meshgrid(x[1:-1],y[1:-1])
    prm_cmap = 'RdBu_r'


    plt.figure(dpi=150)
    plt.pcolormesh(xy_mshgrd, yx_mshgrd, mode.T, cmap=prm_cmap , vmin = -prm_vminmax , vmax = prm_vminmax )
    

    # plt.colorbar()

    cbar = plt.colorbar()
    cbar.ax.tick_params( labelsize = tick_fontsize )  # Adjust tick mark font size


    plt.title(f'POD Mode {mode_idx}' , fontsize = plt_fontsize )
    plt.xlabel('x' , fontsize = plt_fontsize )
    plt.ylabel('y' , fontsize = plt_fontsize )
    plt.xticks( fontsize= tick_fontsize)
    plt.yticks( fontsize= tick_fontsize)
    plt.tight_layout()
    # plt.show()
    plt.savefig( stem + results_dir + '2_' + str(mode_idx)  + '-POD-Mode-'  + str(mode_idx)  + '.png' )



###     Parameters

prm_N_modes_save = 3
prm_N_modes_plot = 9


Nx = 2699
Ny = 799
Nt = 501

data_choice = 'W'

stem = '/Users/stevebrunton/Documents/ibpm-master/Lab iMac Sims/Production Runs/Re050-prd/'

data_dir = 'Data/' + data_choice + '/'

results_dir = 'POD/'



print('\nData location stem:')
print(stem)
print('\nData directory:')
print(data_dir)
print('\nResults directory stem:')
print(results_dir)
print('')


# Load the data

U_data = np.zeros((Nx, Ny, Nt))

print('\nLoading the data...')
for i_load in range(Nt):
    if np.mod(i_load , np.round(Nt/10)) == 0: print('i_load = ' + str(i_load) + ' / ' + str(Nt-1))
    U_data[:,:,i_load] = np.load(stem + data_dir + data_choice + '_' + str(i_load) + '.npy' )

print('\nFinished loading the data!\n')



# Compute POD

print('\nComputing POD...')
POD_modes, POD_eigvals = compute_pod(U_data)
print(np.shape(POD_modes))


print('First ' +str(prm_N_modes_plot)+ ' POD eigenvalues are:')
print(POD_eigvals[:prm_N_modes_plot])
### Saving the entire POD is huge, so save just the first modes
np.save( stem + results_dir + 'POD_modes_'+str(prm_N_modes_save)+'.npy'   ,  POD_modes[:,:prm_N_modes_save] )
np.save( stem + results_dir + 'POD_eigvals.npy' ,  POD_eigvals )

print('\nFinished computing POD!\n')



# Plot the POD modes and eigenvalue spectrum 

print('\nPlotting POD...')
for i in range(prm_N_modes_plot):
    plot_pod_modes(POD_modes, Nx, Ny, i , stem , results_dir)

plt.figure()
plt.plot(POD_eigvals , 'b.--', markersize = 8)
plt.yscale('log')
plt.xlabel('Mode number')
plt.ylabel('Eigenvalue (Energy)')
plt.title('POD Eigenvalue Spectrum')
# plt.show()
plt.savefig( stem + results_dir + '1-Eigenvalue-Spectrum.png' )

print('\nFinished plotting POD!\n')




