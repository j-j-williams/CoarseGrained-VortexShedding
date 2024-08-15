import argparse
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

def load_data(stem):
    x = np.load(stem + 'x.npy')
    y = np.load(stem + 'y.npy')
    t = np.load(stem + 't.npy')
    return x, y, t

def process_data(stem, y_CG_1, y_CG_2, nx, nt):
    U_yPt = np.zeros((nx - 1, nt))
    V_yPt = np.zeros((nx - 1, nt))
    W_yPt = np.zeros((nx - 1, nt))

    for it in range(nt):
        print(f'i  =  {it}  /  {nt-1}')

        U = np.load(stem + 'U/' + f'U_{it}.npy')
        V = np.load(stem + 'V/' + f'V_{it}.npy')
        W = np.load(stem + 'W/' + f'W_{it}.npy')

        U_yPt[:, it] = np.mean(U[:, y_CG_1:y_CG_2], axis=1)
        V_yPt[:, it] = np.mean(V[:, y_CG_1:y_CG_2], axis=1)
        W_yPt[:, it] = np.mean(W[:, y_CG_1:y_CG_2], axis=1)
    
    return U_yPt, V_yPt, W_yPt

def save_data(save_dir, U_yPt, V_yPt, W_yPt, save_str):
    np.save(save_dir + f'U{save_str}', U_yPt)
    np.save(save_dir + f'V{save_str}', V_yPt)
    np.save(save_dir + f'W{save_str}', W_yPt)

def plot_data(save_dir, show_figs, U_yPt, V_yPt, W_yPt, y, y_CG_1, y_CG_2, t_plt=0):
    ttl_str = f'y = {round(y[y_CG_1+1])}_y{round(y[y_CG_2+1])}'

    plt.figure(dpi=100)
    plt.plot(U_yPt[:, t_plt])
    plt.xlabel('x', fontsize=16)
    plt.ylabel('U', fontsize=16)
    plt.title(f'U(x; t = t_plt ; {ttl_str})', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.savefig(save_dir + f'U-cg-t_plt{t_plt}.png')
    if show_figs == 1: plt.show()

    plt.figure(dpi=100)
    plt.plot(V_yPt[:, t_plt])
    plt.xlabel('x', fontsize=16)
    plt.ylabel('V', fontsize=16)
    plt.title(f'V(x; t = t_plt ; {ttl_str})', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.savefig(save_dir + f'V-cg-t_plt{t_plt}.png')
    if show_figs == 1: plt.show()

    plt.figure(dpi=100)
    plt.plot(W_yPt[:, t_plt])
    plt.xlabel('x', fontsize=16)
    plt.ylabel('W', fontsize=16)
    plt.title(f'W(x; t = t_plt ; {ttl_str})', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.savefig(save_dir + f'W-cg-t_plt{t_plt}.png')
    if show_figs == 1: plt.show()

def plot_full_colormaps(save_dir, show_figs, U_yPt, V_yPt, W_yPt, y, y_CG_1, y_CG_2):
    ttl_str = f'y = {round(y[y_CG_1+1])}_y{round(y[y_CG_2+1])}'

    plt.figure(figsize=(12, 6))
    plt.pcolormesh(U_yPt.T, cmap='coolwarm')
    plt.xlabel('x', fontsize=16)
    plt.ylabel('t', fontsize=16)
    plt.title(f'U(x, t ; {ttl_str})', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.colorbar()
    plt.savefig(save_dir + f'U-cg-t_all.png')
    if show_figs == 1: plt.show()

    plt.figure(figsize=(12, 6))
    plt.pcolormesh(V_yPt.T, cmap='coolwarm')
    plt.xlabel('x', fontsize=16)
    plt.ylabel('t', fontsize=16)
    plt.title(f'V(x, t ; {ttl_str})', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.colorbar()
    plt.savefig(save_dir + f'V-cg-t_all.png')
    if show_figs == 1: plt.show()

    plt.figure(figsize=(12, 6))
    plt.pcolormesh(W_yPt.T, cmap='coolwarm')
    plt.xlabel('x', fontsize=16)
    plt.ylabel('t', fontsize=16)
    plt.title(f'W(x, t ; {ttl_str})', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.colorbar()
    plt.savefig(save_dir + f'W-cg-t_all.png')
    if show_figs == 1: plt.show()

def main(args):
    show_figs = 0
    print('\nshow_figs  =  0\n\n')
    stem = f'../Vortex Shedding Data/{args.str_regime}/{args.str_runTitle}/'
    
    x, y, t = load_data(stem+'Parameters/')
    nx = len(x) - 1
    ny = len(y) - 1
    nt = len(t)

    U_yPt, V_yPt, W_yPt = process_data(stem+'Data/', args.y_CG_1, args.y_CG_2, nx, nt)

    save_dir = f'../Vortex Shedding Data/{args.str_regime}/{args.str_runTitle}/CoarseGrained-Data/'
    save_str = f'_y{round(y[args.y_CG_1+1])}_y{round(y[args.y_CG_2+1])}.npy'
    
    print(f'Taking average between y-lines (rounded to O(1e0)):\n')
    print(f'y_1  =   {round(y[args.y_CG_1+1])}')
    print(f'y_2  =   {round(y[args.y_CG_2+1])}\n\n')
    
    save_data(          save_dir,            U_yPt, V_yPt, W_yPt, save_str)
    plot_data(          save_dir, show_figs, U_yPt, V_yPt, W_yPt, y, args.y_CG_1, args.y_CG_2)
    plot_full_colormaps(save_dir, show_figs, U_yPt, V_yPt, W_yPt, y, args.y_CG_1, args.y_CG_2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process and analyze simulation data.")
    parser.add_argument('str_runTitle', type=str, help="Title of the run")
    parser.add_argument('str_regime'  , type=str, help="'Steady State' or 'Transient'")
    parser.add_argument('y_CG_1', type=int, help="Lower bound y index for averaging")
    parser.add_argument('y_CG_2', type=int, help="Upper bound y index for averaging")
    args = parser.parse_args()

    main(args)