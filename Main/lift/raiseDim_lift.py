

def fnc_raiseDim_lift( TDE_or_ddt , t , TD_Embed, C_l , should_normalize ):

	if  TDE_or_ddt == "TDE":
	    from raiseDim_TimeDelayEmbed_lift import fnc_raiseDim_TimeDelayEmbed_lift
	    t_PS , zeta , eta = fnc_raiseDim_TimeDelayEmbed_lift( )
	    
	elif TDE_or_ddt == "ddt":
	    from raiseDim_ddt_lift import fnc_raiseDim_ddt_lift
	    t_PS , zeta , eta = fnc_raiseDim_ddt_lift( t , TD_Embed, C_l , should_normalize)  
	    #  be sure to still pass a good TD_Embed, even when doing d/dt
	    
	else: print('\n******\nError!\n******\n\nSelected invalid method of raising dimension! \
	In the .JSON config file, the parameter "TDE_or_ddt" must be either "TDE" or "ddt", \
	and the parameter "TD_Embed" must be a positive, real number, even when doing d/dt.\n\n\n')




	return t_PS , zeta , eta 