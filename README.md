# CoarseGrained-VortexShedding

This repository features code and datasets for analyzing a coarse-grained cylinder vortex shedding dataset. This work is discussed in Williams et al. (_in progress_) and features the code used to perform coarse-grained analyses. The work makes extensive use of the Sparse Identification of Nonlinear Dynamical systems (SINDy) method (Brunton et al. (2016a)) and PDE-FIND (Rudy et al. (2017)); see the PySINDy repospitory here: [link]([url](https://github.com/dynamicslab/pysindy))



# Vortex Shedding

Vortex shedding is an important and striking physical phenomenon observed in fluids charaterized by alternating, periodic vortices behind a body in a freestream with sufficient Reynolds number Re.  



# Coarse-Graining

Flowfield data consists of pressure, velocity, and vorticity flowfields in time and two spatial dimensions. We spatially coarse-grain the data, removing the vertical $y$-coordinate from the dataset by integrating across it:

\begin{equation} \label{eq:coarseGrainEqn}
\overline{\omega}(x,t) = \int_{-H}^{+H} \omega(y; x,t) dy.
\end{equation}

By so doing, we reduce the dimension of our data to one-dimensional spatiotemporal.



# Model Selection

We search for a reduced-order model (ROM) for our cylinder vortex shedding by finding a model to explain the coarse-grained dynamics. We use the SINDy method (Brunton et al. (2016a)) and its extension, PDE-FIND (Rudy et al. (2017)) to find systems or ordinary and partial differential equations to explain the coarse-grained dynamics.







