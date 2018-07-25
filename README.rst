some paraview post-processing scripts to highlight different orientations in colour
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
**what**
   Minimising surface energy by **surface diffusion** (surface divergence of the mean curvature) [Mullins1957]. This is not equivalent to evolving shape by surface tension (mean curvature)

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/sequence.gif

**how**
    - The surfaces of different families are identified and the surface energy associated with the surface are specified.

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/surfaces.jpg

- gamma-plot is obtained by fine tuning of the parameters alpha and w to ensure no overlapping between the energy minima

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/gamma.png

- similarly xi vector is obtained by differentiating $\hat{\gamma}=P\gamma(\vec{n})$ in P space where $P=r\gamma$

     $ \vec{\xi}=\nabla_{P}\hat{\gamma}$

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/xi.png

- missing orientations are found by means of the inverse-gamma-plot and the well-known crition [Sekerka2005]

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/inverse1.png

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/inverse2.png

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/cig.png

- coloring the surfaces by orientations. This is done in paraview.
.. image:: https://github.com/Ezone2016/surface-flow/blob/master/sequence2.gif

- A much easier example of a cubic crystal can be seen down below 

.. image:: https://github.com/Ezone2016/surface-flow/blob/master/cubicA2.png
