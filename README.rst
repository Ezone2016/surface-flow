=====
2d-iso-s-ani
=====

Requirements
------------
 1. pre-processing

- `python 3.x` (Tested on `3.5.3`)
- `numpy`, `deepdish`

 2. compiling and running

- `mpi` (Tested on `Open MPI 2.0.2`)
- a working version of HDF5 library

 3. post-processing

- `h5utils`
- `imagemagick`
- `paraview`

General workflow
------------

<<<<<<< HEAD
- edit the `model.cpp` `utencil.h` in `./include` if necessary 
=======
- edit the `model.cpp` `stencil.h` in `./include` if necessary 
>>>>>>> 7422c16e012584f0c2c3fc8287f8fd8efd81e66e

- edit model parameters in `input.txt`, the notation in `input.txt` here comes from the paper cited below.

- use python package `deepdish` to create an input file that contains the initial conditions, e.g. see `init.py` 

- the initial condition used here is a circle with phi=1 inside (white), phi=0 outside (green) and a hyperbolic tangent profile in the interface:

.. image:: https://github.com/Ezone2016/2d-iso-s-ani/blob/master/output/init.png

- compile the code using makefile provided.

.. code-block:: shell

    	>>> make all

- This will generate an executable called `ani`, run it using `mpirun` e.g.

.. code-block:: shell

		>>> mpirun -np 8 ani

- The output is named `strand.h5`, use `Paraview` to view it or `h5utils` to convert it into readable format. An basic example script amounts to:

.. code-block:: shell

		>>> for i in `seq 1 1 100`;
		>>> do
		>>> h5topng strand.h5:phi/$(printf %06d $i) -o $(printf %06d $i).png;
		>>> done

- use `imagemagick` to convert the time series into an animation, e.g.:

.. code-block:: shell
	>>>convert -layers OptimizePlus -quality 99 *.png -loop 12 sequence.gif
		

.. image:: https://github.com/Ezone2016/2d-iso-s-ani/blob/master/output/sequence.gif

#ToDo

- contact angle enhenced 2d single crystal with substrate
- include surface tension for faceted dendritic growth 
- include pulsing within the parameter d, i.e. d = d(t)

Reference
------------
<<<<<<< HEAD
L.K. Aagesen, L.K. Lee, P.-C. Ku, K. Thornton, `Phase-field simulations of GaN/InGaN quantum dot growth by selective area epitaxy <https://www.sciencedirect.com/science/article/pii/S0022024812006057>`_ , Journal of Crystal Growth, Volume 361, 2012 
=======
L.K. Aagesen, L.K. Lee, P.-C. Ku, K. Thornton, `Phase-field simulations of GaN/InGaN quantum dot growth by selective area epitaxy <https://www.sciencedirect.com/science/article/pii/S0022024812006057>`_ , Journal of Crystal Growth, Volume 361, 2012 
>>>>>>> 7422c16e012584f0c2c3fc8287f8fd8efd81e66e
