# CoarseGrained-VortexShedding

This repository features code and datasets for analyzing a coarse-grained cylinder vortex shedding dataset. This work is discussed in Williams et al. (_in progress_) and features the code used to perform coarse-grained analyses. The work makes extensive use of the Sparse Identification of Nonlinear Dynamical systems (SINDy) method (Brunton et al. (2016a)) and PDE-FIND (Rudy et al. (2017)); see the PySINDy repospitory here [at this repository](https://github.com/dynamicslab/pysindy).



### Vortex Shedding

Vortex shedding is an important and striking physical phenomenon observed in fluids charaterized by alternating, periodic vortices behind a body in a freestream with sufficient Reynolds number Re.  



Below is the cylinder flow's vorticity flowfield at $ Re=100 $, from a zero initial condition through its transient phase until steady state.

![Vortex shedding at Re=100, transient to saturation](assets/W.gif)



### Coarse-Graining

Flowfield data consists of pressure, velocity, and vorticity flowfields in time and two spatial dimensions. We spatially coarse-grain the data, removing the vertical $y$-coordinate from the dataset by integrating across it:

$$ \overline{\omega}(x,t) = \int_{-H}^{+H} \omega(y; x,t) dy $$

By so doing, we reduce the dimension of our data to one-dimensional spatiotemporal.



### Model Selection

We seek for a reduced-order model (ROM) for cylinder vortex shedding. We generate ROMs by using the SINDy method (Brunton et al. (2016a), Rudy et al. (2017)) to find systems of ordinary and partial differential equations to explain the reduced-order dynamics, including the dynamics of the coefficients of lift and drag and the coarse-grained velocity and vorticity flowfields.

