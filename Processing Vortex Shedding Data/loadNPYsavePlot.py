#!/usr/bin/env python
# coding: utf-8

# In[1]:


###  Import modules


import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# get_ipython().run_cell_magic('javascript', '', 'require("notebook/js/notebook").Notebook.prototype.scroll_to_bottom = function () {}')


# In[4]:


###  Set  loading string  and  i_plt


# stem = '/Volumes/Backup Hard Drive/Holding Folder/Research/IBPM Simulations/Main Simulations/2022_06_21_Re050_Big_Prd/Data/'
# stem = '/Volumes/Backup Hard Drive/Holding Folder/Research/IBPM Simulations/Main Simulations/2022_06_21_Re062_Big_Prd/Data/'
# stem = '/Volumes/Backup Hard Drive/Holding Folder/Research/IBPM Simulations/Main Simulations/2022_06_21_Re075_Big_Prd/Data/'
# stem = '/Volumes/Backup Hard Drive/Holding Folder/Research/IBPM Simulations/Main Simulations/2022_06_21_Re087_Big_Prd/Data/'
# stem = '/Volumes/Backup Hard Drive/Holding Folder/Research/IBPM Simulations/Main Simulations/2022_06_21_Re100_Big_Prd/Data/'



# stem = '/Volumes/Backup Hard Drive/Holding Folder/Research/IBPM Simulations/Main Simulations/2022_06_21_Re062_Big_Prd/Data/'

str_runTitle = 'Re100-1'

stem = '/Users/stevebrunton/Documents/ibpm-master/Lab iMac Sims/' +str_runTitle+ '/Data/'


# In[ ]:





# In[6]:



import os

directory = stem + 'U/'
N_plt = len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])


# In[ ]:





# In[2]:


###  Plot full colormaps of the data


for i_plt in range( N_plt  ):
    
    if np.mod( i_plt , N_plt//10 ) == 0: print('i  =  ' +str(i_plt) + '  /  ' +str(N_plt+1) )






    # x = np.load(stem+'x.npy')
    # y = np.load(stem+'y.npy')
    # t = np.load(stem+'t.npy')


    U = np.load( stem + 'U/' + 'U_' + str(i_plt) + '.npy' )
    V = np.load( stem + 'V/' + 'V_' + str(i_plt) + '.npy' )
    W = np.load( stem + 'W/' + 'W_' + str(i_plt) + '.npy' )





    # Plot  x-velocity
    plt.figure(figsize=(12,6))
    plt.pcolormesh(U.T , cmap='coolwarm' , vmin = -0.25 , vmax = 1.35 )

    plt.xlabel('x' , fontsize=16)
    plt.ylabel('y' , fontsize=16)
    ttl_str = 'U(x,y ; t = ' + str(i_plt) + ')'
    plt.title(ttl_str , fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.colorbar()
    plt.savefig('Flowfield-U-' + str(i_plt) + '.png')
    # plt.show()
    plt.close()

    # Plot  y-velocity
    plt.figure(figsize=(12,6))
    plt.pcolormesh(V.T , cmap='coolwarm' , vmin = -0.75 , vmax = 0.75 )

    plt.xlabel('x' , fontsize=16)
    plt.ylabel('y' , fontsize=16)
    ttl_str = 'V(x,y ; t = ' + str(i_plt) + ')'
    plt.title(ttl_str , fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.colorbar()
    plt.savefig('Flowfield-V-' + str(i_plt) + '.png')
    # plt.show()
    plt.close()

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
    plt.savefig('Flowfield-W-' + str(i_plt) + '.png')
    # plt.show()
    plt.close()

# In[ ]:




