import numpy as np


def fnc_raiseDim_TimeDelayEmbed_lift( t , TD_Embed , data , should_normalize ):

	t_1 = t
	t_2 = t+TD_Embed
	TD_Embed_Index = np.argmin( np.abs(t - TD_Embed) )
	TD_Embed_backendIndex = np.argmin( np.abs( t_2 - np.max(t_1) ) ) 

	data_1 = data[TD_Embed_Index:-1 ]      
	data_2 = data[0:TD_Embed_backendIndex ]
	t_Ovlp = t[TD_Embed_Index:-1]


    if should_normalize == True: 
    	data_1 = data_1 / np.max(np.abs(data_1));
    	data_2 = data_2  / np.max(np.abs(data_2)); 
    

	return t_Ovlp , data_1 , data_2

