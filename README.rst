some paraview post-processing scripts to highlight different orientations in colour
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
**what**
   Minimising surface energy by **surface diffusion** (surface divergence of the mean curvature) [Mullins1957]_. This is not equivalent to evolving shape by surface tension (mean curvature). The regularisation method used is well-documented in [Torabi2009]_ and the gamma construction method is due to [Siem2005]_.

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/sequence.gif

**how**
    - The surfaces of different families are identified and the surface energy associated with the surface are specified.

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/surfaces.png

- the alpha values are normalised according to:

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/eq1.png

- gamma-plot is obtained by fine tuning of the parameters alpha and w to ensure no overlapping between the energy minima. The units of xyz are dimensionless as gamma is normalised by gamma_0

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/gamma.png

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/eq2.png

- similarly xi vector is obtained by differentiating $\hat{\gamma}=r\gamma(\vec{n})$ in $r$ space where $\vec{r}$ is the position vector

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/eq3.png

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/xi.png

- missing orientations are found by means of the inverse-gamma-plot [Herring1951]_ and the well-known criteria [Sekerka2005]_

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/inverse1.png

- of course the equilirium shape is only bounded by 8 {101} surfaces - a result that can be easily deduced from Wulff construction. Here we demonstrate that the convexified xi-plot gives the equivalent result:

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/eq.png

- however the time it requires to reach this state follows a power law according to Mullins and it's heavily dependent on particle size. Since the transient shape is of interest here we only allow it to evolve for certain time. The result is shown below. Finally colour the surfaces by orientations. This is done in paraview (see 001.py, 112.py etc.)

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/sequence2.gif

ToDo
------------

- kinetics of deposition by ballistic transport

Reference
------------

.. [Mullins1957] W.W. Mullins, `Theory of Thermal Grooving <https://aip.scitation.org/doi/10.1063/1.1722742>`_, Journal of Applied Physics 28, 333 (1957)

.. [Sekerka2005] R.F. Sekerka, `Analytical criteria for missing orientations on three-dimensional equilibrium shapes <https://www.sciencedirect.com/science/article/pii/S0022024804013843?via%3Dihub>`_, Journal of Crystal Growth, Volume 275, Issues 1–2 (2005)

.. [Herring1951] C.Herring, `Surface Tension as a Motivation for Sintering, The Physics of Powder Metallurgy, p. 143, McGraw-Hill, New York (1951)

.. [Torabi2009] S.Torabi, J. Lowengrub, A. Voigt, S. Wise, `A new phase-field model for strongly anisotropic systems <http://rspa.royalsocietypublishing.org/content/465/2105/1337>`_, Proc. R. Soc., 465 1337-1359 (2009)

.. [Siem2005] E.J. Siem, W. C. Carter, `Orientation-dependent surface tension functions for surface energy minimizing calculations <https://link.springer.com/article/10.1007/s10853-005-2671-7>`_, Journal of Materials Science, Volume 40, Issue 12, pp 3107–3113  (2005)
