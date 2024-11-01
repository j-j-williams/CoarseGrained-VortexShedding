import numpy as np
import matplotlib.pyplot as plt



def plot_pod_modes(POD_modes, Nx, Ny, mode_idx  ):

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

    # cbar = plt.colorbar()
    # cbar.ax.tick_params( labelsize = tick_fontsize )  # Adjust tick mark font size


    # plt.title(f'POD Mode {mode_idx}' , fontsize = plt_fontsize )
    # plt.xlabel('x' , fontsize = plt_fontsize )
    # plt.ylabel('y' , fontsize = plt_fontsize )
    plt.xticks( [], fontsize= tick_fontsize)
    plt.yticks( [], fontsize= tick_fontsize)

    plt.axis([-2,15,-2,2])

    plt.tight_layout()
    # plt.show()
    plt.savefig( '2_' + str(mode_idx)  + '-POD-Mode-'  + str(mode_idx)  + '.png' )




###     Parameters

prm_N_modes = 3


Nx = 2699
Ny = 799
Nt = 501

# data_choice = 'W'


# stem = '/Users/josephwilliams/Documents/GitHub/CoarseGrained-VortexShedding/Vortex Shedding Data/Steady State/Re50/POD/'
stem = '/Users/josephwilliams/Downloads/'


# stem = '/Users/stevebrunton/Documents/ibpm-master/Lab iMac Sims/Production Runs/Re050-prd/'

# data_dir = 'Data/' + data_choice + '/'

# results_dir = 'POD/'




# POD_eigvals = np.load(stem+'POD_eigvals.npy')

POD_modes   = np.load(stem+'POD_modes_'+str(prm_N_modes)+'.npy')

# Plot the POD modes and eigenvalue spectrum 

print('\nPlotting POD...')
for i in range(prm_N_modes):
    plot_pod_modes(POD_modes, Nx, Ny, i )

# plt.figure()
# plt.plot(POD_eigvals , 'b.--', markersize = 8)
# plt.yscale('log')
# plt.xlabel('Mode number')
# plt.ylabel('Eigenvalue (Energy)')
# plt.title('POD Eigenvalue Spectrum')
# # plt.show()
# plt.savefig( stem + results_dir + '1-Eigenvalue-Spectrum.png' )

# print('\nFinished plotting POD!\n')

