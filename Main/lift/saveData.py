
import numpy as np
import os

def fnc_saveData( save_dir , arrays , filenames ):
    # Check that the number of filenames matches the number of arrays
    if len(arrays) != len(filenames):  raise ValueError("The number of filenames must match the number of arrays.")
    
    # Save each array with the corresponding filename
    for array, filename in zip(arrays, filenames):  np.save(save_dir + 'Data/' + filename, array)

