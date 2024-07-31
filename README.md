# CoarseGrained-VortexShedding

This repository features code and datasets for analyzing a coarse-grained cylinder vortex shedding dataset. This work is discussed in Williams et al. (_in progress_) and features the code used to perform coarse-grained analyses. The work makes extensive use of the Sparse Identification of Nonlinear Dynamical systems (SINDy) method (Brunton et al. (2016a)) and PDE-FIND (Rudy et al. (2017)); see the PySINDy repospitory here [at this repository](https://github.com/dynamicslab/pysindy).



# Vortex Shedding

Vortex shedding is an important and striking physical phenomenon observed in fluids charaterized by alternating, periodic vortices behind a body in a freestream with sufficient Reynolds number Re.  



# Coarse-Graining

Flowfield data consists of pressure, velocity, and vorticity flowfields in time and two spatial dimensions. We spatially coarse-grain the data, removing the vertical $y$-coordinate from the dataset by integrating across it:

$$ \overline{\omega}(x,t) = \int_{-H}^{+H} \omega(y; x,t) dy $$

By so doing, we reduce the dimension of our data to one-dimensional spatiotemporal.



# Model Selection

We search for a reduced-order model (ROM) for our cylinder vortex shedding by finding a model to explain the coarse-grained dynamics. We use the SINDy method (Brunton et al. (2016a)) and its extension, PDE-FIND (Rudy et al. (2017)) to find systems or ordinary and partial differential equations to explain the coarse-grained dynamics.


Test Gif:

![giphy](https://github.com/user-attachments/assets/07798fcd-a797-4f46-94db-307ce020a856) ![shutterstock_1260580581](https://github.com/user-attachments/assets/e78124fe-9dad-4fc1-9a70-af5f5f20ff77)

![images](https://github.com/user-attachments/assets/8a860b31-e4e0-4cda-9709-21989f4671cc) ![images](https://github.com/user-attachments/assets/8a860b31-e4e0-4cda-9709-21989f4671cc) ![images](https://github.com/user-attachments/assets/8a860b31-e4e0-4cda-9709-21989f4671cc)



Did it show?


