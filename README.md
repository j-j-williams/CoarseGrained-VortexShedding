# CoarseGrained-VortexShedding

This repository features code and datasets for analyzing a coarse-grained cylinder vortex shedding dataset. This work is discussed in Williams et al. (_in progress_) and features the code used to perform coarse-grained analyses. The work makes extensive use of the Sparse Identification of Nonlinear Dynamical systems (SINDy) method (Brunton et al. (2016a)) and PDE-FIND (Rudy et al. (2017)); see the PySINDy repospitory here [at this repository](https://github.com/dynamicslab/pysindy).



### GitHub Repository

This GitHub repo features the following:
1. `Vortex Shedding Data`: Simulation files for cylinder flow at a range of Reynolds numbers Re, both transient and steady-state
2. `Processing Vortex Shedding Data`: Python scripts and notebooks for post-processing and visualizing this data
3. `Main`: Python scripts and notebooks for finding reduced-order models for cylinder vortex shedding



### Vortex Shedding

Vortex shedding is an important and striking physical phenomenon observed in fluids charaterized by alternating, periodic vortices behind a body in a freestream with sufficient Reynolds number Re. Below is the cylinder flow's vorticity flowfield at Re=100, from a zero initial condition through its transient phase until steady state.

<p align="center">
	<img src="assets/W.gif" alt="Vortex shedding at Re=100, transient to saturation" width="600"/>
</p>



### Coarse-Graining

Flowfield data consists of pressure, velocity, and vorticity flowfields in time and two spatial dimensions. We spatially coarse-grain the data, removing the vertical $y$-coordinate from the dataset by integrating across it:

$$ \overline{\omega}(x,t) = \int_{-H}^{+H} \omega(y; x,t) dy $$

By so doing, we reduce the dimension of our data to one-dimensional spatiotemporal.



### Model Selection

We seek for a reduced-order model (ROM) for cylinder vortex shedding. We generate ROMs by using the SINDy method (Brunton et al. (2016a), Rudy et al. (2017)) to find systems of ordinary and partial differential equations to explain the reduced-order dynamics, including the dynamics of the coefficients of lift and drag and the coarse-grained velocity and vorticity flowfields.


