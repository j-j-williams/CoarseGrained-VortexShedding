###  Place this file within the main directory of a given IBPM simulation,
# with parameters and data in `/Parameters/` and `/Data/U` etc
# eg `/Users/stevebrunton/Documents/ibpm-master/Lab iMac Sims/Production Runs/Re050-prd/`
# Then run with eg `python coarseGrain-new.py 8 -8`
# MUST be run with (upper bound) first, then (lower bound), otherwise doesn't work.


import argparse
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

def load_data(stem):
    x = np.load(stem + 'x.npy')
    y = np.load(stem + 'y.npy')
    t = np.load(stem + 't.npy')
    return x, y, t

def process_data(stem, y_CG_1, y_CG_2, nx, nt, dt):
    U_yPt = np.zeros((nx - 1, nt))
    V_yPt = np.zeros((nx - 1, nt))
    W_yPt = np.zeros((nx - 1, nt))

    for it in range(nt):
        print(f'i  =  {it}  /  {nt-1}')

        U = np.load(stem + 'U/' + f'U_{it}.npy')
        V = np.load(stem + 'V/' + f'V_{it}.npy')
        W = np.load(stem + 'W/' + f'W_{it}.npy')

        # U_yPt[:, it] = np.mean(U[:, y_CG_1:y_CG_2], axis=1)
        # V_yPt[:, it] = np.mean(V[:, y_CG_1:y_CG_2], axis=1)
        # W_yPt[:, it] = np.mean(W[:, y_CG_1:y_CG_2], axis=1)

        U_yPt[ : , it ] =    np.trapz( U[ : , y_CG_1 : y_CG_2 ] ,  dx = dt ,  axis=1 )
        V_yPt[ : , it ] =    np.trapz( V[ : , y_CG_1 : y_CG_2 ] ,  dx = dt ,  axis=1 )
        W_yPt[ : , it ] =    np.trapz( W[ : , y_CG_1 : y_CG_2 ] ,  dx = dt ,  axis=1 )

    
    return U_yPt, V_yPt, W_yPt, U, V, W


def save_cg_data(save_dir, U_yPt, V_yPt, W_yPt, save_str):
    np.save(save_dir + f'U{save_str}', U_yPt)
    np.save(save_dir + f'V{save_str}', V_yPt)
    np.save(save_dir + f'W{save_str}', W_yPt)


def plot_flow_data( save_dir, show_figs, U, V, W, x, y, t, x_plt):

    print('x_plt     =  ' + str(x_plt) +'\n' )
    print('x[x_plt]  =  ' + str(x[x_plt+1]) +'\n' )

    plt.figure(dpi=100)
    plt.plot(U[x_plt, :] , y[1:-1])
    plt.xlabel('U', fontsize=16)
    plt.ylabel('y', fontsize=16)
    plt.title(f'U(y; x = ' +str(np.round(x[x_plt+1],2)) + ', t = t[-1])', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.tight_layout()
    plt.savefig(save_dir + f'U-x_plt{x_plt}.png')
    if show_figs == 1: plt.show()

    plt.figure(dpi=100)
    plt.plot(V[x_plt, :] , y[1:-1])
    plt.xlabel('V', fontsize=16)
    plt.ylabel('y', fontsize=16)
    plt.title(f'V(y; x = ' +str(np.round(x[x_plt+1],2)) + ', t = t[-1])', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.tight_layout()
    plt.savefig(save_dir + f'V-x_plt{x_plt}.png')
    if show_figs == 1: plt.show()

    plt.figure(dpi=100)
    plt.plot(W[x_plt, :] , y[1:-1])
    plt.xlabel('W', fontsize=16)
    plt.ylabel('y', fontsize=16)
    plt.title(f'W(y; x = ' +str(np.round(x[x_plt+1],2)) + ', t = t[-1])', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.tight_layout()
    plt.savefig(save_dir + f'W-x_plt{x_plt}.png')
    if show_figs == 1: plt.show()


    plt.figure(figsize=(12, 6))
    plt.pcolormesh(U.T, cmap='coolwarm')
    plt.xlabel('x', fontsize=16)
    plt.ylabel('t', fontsize=16)
    plt.title('U(x,y; t = t[-1]', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.colorbar()
    plt.savefig(save_dir + f'U-xy-t_plt.png')
    if show_figs == 1: plt.show()

    plt.figure(figsize=(12, 6))
    plt.pcolormesh(V.T, cmap='coolwarm')
    plt.xlabel('x', fontsize=16)
    plt.ylabel('t', fontsize=16)
    plt.title('V(x,y; t = t[-1]', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.colorbar()
    plt.savefig(save_dir + f'V-xy-t_plt.png')
    if show_figs == 1: plt.show()

    plt.figure(figsize=(12, 6))
    plt.pcolormesh(W.T, cmap='coolwarm')
    plt.xlabel('x', fontsize=16)
    plt.ylabel('t', fontsize=16)
    plt.title('W(x,y; t = t[-1]', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.colorbar()
    plt.savefig(save_dir + f'W-xy-t_plt.png')
    if show_figs == 1: plt.show()


def plot_cg_data(save_dir, show_figs, U_yPt, V_yPt, W_yPt, y, y_CG_1, y_CG_2, t_plt=0):
    ttl_str = f'y = {round(y[y_CG_1+1])}_y{round(y[y_CG_2+1])}'

    plt.figure(dpi=100)
    plt.plot(U_yPt[:, t_plt])
    plt.xlabel('x', fontsize=16)
    plt.ylabel(r'$\overline{U}$', fontsize=16)
    plt.title(r'$\overline{U}(x; t = $' + str(t_plt) + '$)$' + '\n' + r'with $[y_a,y_b] = [$' + str(y_CG_1) + ',' + str(y_CG_2) + r'$]$', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.savefig(save_dir + f'U-cg-t_plt{t_plt}.png')
    if show_figs == 1: plt.show()

    plt.figure(dpi=100)
    plt.plot(V_yPt[:, t_plt])
    plt.xlabel('x', fontsize=16)
    plt.ylabel(r'$\overline{V}$', fontsize=16)
    plt.title(r'$\overline{V}(x; t = $' + str(t_plt) + '$)$' + '\n' + r'with $[y_a,y_b] = [$' + str(y_CG_1) + ',' + str(y_CG_2) + r'$]$', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.tight_layout()
    plt.savefig(save_dir + f'V-cg-t_plt{t_plt}.png')
    if show_figs == 1: plt.show()

    plt.figure(dpi=100)
    plt.plot(W_yPt[:, t_plt])
    plt.xlabel('x', fontsize=16)
    plt.ylabel(r'$\overline{W}$', fontsize=16)
    plt.title(r'$\overline{W}(x; t = $' + str(t_plt) + '$)$' + '\n' + r'with $[y_a,y_b] = [$' + str(y_CG_1) + ',' + str(y_CG_2) + r'$]$', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.tight_layout()
    plt.savefig(save_dir + f'W-cg-t_plt{t_plt}.png')
    if show_figs == 1: plt.show()

def plot_cg_colormaps(save_dir, show_figs, U_yPt, V_yPt, W_yPt, y, y_CG_1, y_CG_2):
    ttl_str = f'y = {round(y[y_CG_1+1])}_y{round(y[y_CG_2+1])}'

    plt.figure(figsize=(12, 6))
    plt.pcolormesh(U_yPt.T, cmap='coolwarm')
    plt.xlabel('x', fontsize=16)
    plt.ylabel('t', fontsize=16)
    plt.title(r'$\overline{U}(x, t)$' + '\n' + r'with $[y_a,y_b] = [$' + str(y_CG_1) + ',' + str(y_CG_2) + r'$]$', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.colorbar()
    plt.savefig(save_dir + f'U-cg-t_all.png')
    if show_figs == 1: plt.show()

    plt.figure(figsize=(12, 6))
    plt.pcolormesh(V_yPt.T, cmap='coolwarm')
    plt.xlabel('x', fontsize=16)
    plt.ylabel('t', fontsize=16)
    plt.title(r'$\overline{V}(x, t)$' + '\n' + r'with $[y_a,y_b] = [$' + str(y_CG_1) + ',' + str(y_CG_2) + r'$]$', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.colorbar()
    plt.savefig(save_dir + f'V-cg-t_all.png')
    if show_figs == 1: plt.show()

    plt.figure(figsize=(12, 6))
    plt.pcolormesh(W_yPt.T, cmap='coolwarm')
    plt.xlabel('x', fontsize=16)
    plt.ylabel('t', fontsize=16)
    plt.title(r'$\overline{W}(x, t)$' + '\n' + r'with $[y_a,y_b] = [$' + str(y_CG_1) + ',' + str(y_CG_2) + r'$]$', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.colorbar()
    plt.savefig(save_dir + f'W-cg-t_all.png')
    if show_figs == 1: plt.show()


def main(args):
    show_figs = 0
    print('\nshow_figs  =  ' + str(show_figs) + '\n\n')
    # stem = f'/Data/{args.str_regime}/{args.str_runTitle}/'
    
    x, y, t = load_data('Parameters/')
    nx = len(x) - 1
    ny = len(y) - 1
    nt = len(t)
    # nt = 10

    dt = t[1] - t[0]

    U_yPt, V_yPt, W_yPt, U_tN, V_tN, W_tN = process_data('Data/', args.y_CG_1, args.y_CG_2, nx, nt, dt)

    
    # save_dir = f'../Vortex Shedding Data/{args.str_regime}/{args.str_runTitle}/CoarseGrained-Data/'
    save_dir = f'CoarseGrained-Data/'

    save_str = f'_y{round(y[args.y_CG_1+1])}_y{round(y[args.y_CG_2+1])}.npy'
    
    # print(f'Taking average between y-lines (rounded to O(1e0)):\n')
    print(f'Integrating between y-lines (rounded to O(1e0)):\n')
    print(f'y_1  =   {round(y[args.y_CG_1+1])}')
    print(f'y_2  =   {round(y[args.y_CG_2+1])}\n\n')
    
    save_cg_data(          save_dir,            U_yPt, V_yPt, W_yPt, save_str)
    plot_cg_data(          save_dir, show_figs, U_yPt, V_yPt, W_yPt, y, args.y_CG_1, args.y_CG_2)
    plot_cg_colormaps(save_dir, show_figs, U_yPt, V_yPt, W_yPt, y, args.y_CG_1, args.y_CG_2)

    plot_flow_data( save_dir, show_figs, U_tN, V_tN, W_tN, x, y, t, x_plt = 600)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process and analyze simulation data.")
    # parser.add_argument('str_runTitle', type=str, help="Title of the run")
    # parser.add_argument('str_regime'  , type=str, help="'Steady State' or 'Transient'")
    parser.add_argument('y_CG_1', type=int, help="Lower bound y index for averaging")
    parser.add_argument('y_CG_2', type=int, help="Upper bound y index for averaging")
    args = parser.parse_args()

    main(args)