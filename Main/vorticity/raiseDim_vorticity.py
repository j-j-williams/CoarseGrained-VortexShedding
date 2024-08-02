
def fnc_raiseDim_vorticity( TDE_or_ddt , t , TD_Embed, data ):


	if  TDE_or_ddt == "TDE":
	    from raiseDim_TDE_vorticity import fnc_raiseDim_TDE_vorticity
	    t_PS , data_1 , data_2 = fnc_raiseDim_TDE_vorticity( t , TD_Embed, data )

	elif TDE_or_ddt == "ddt":
	    from raiseDim_ddt_vorticity import fnc_raiseDim_ddt_vorticity
	    t_PS , data_1 , data_2 = fnc_raiseDim_ddt_vorticity( t , TD_Embed, data )


	else: print('\n******\nError!\n******\n\nSelected invalid method of raising dimension! \
	In the .JSON config file, the parameter "TDE_or_ddt" must be either "TDE" or "ddt", \
	and the parameter "TD_Embed" must be a positive, real number, even when doing d/dt.\n\n\n')





	return t_PS , data_1 , data_2