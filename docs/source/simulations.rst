
Simulations 
===========

Numerical Integrations
----------------------
For any N-body problem which is evolved by some numerical integrator,
choosing smaller integration timesteps, generally yields a smaller
error in the orbit. However, if the timescale on which the system
needs to be evolved is considerably large, one might wish to
choose large timesteps in order to limit the computational time
needed to complete the integration. 

Some integrators however, do not use a fixed, but use a variable timestepping
scheme to perform the integration. The motivation for using variable timesteps,
is that large timesteps need not imply a large error in the orbit.  
If say for example, a body is traveling along a highly eccentric orbit, then
the error made by a fixed timestep integrator is greater in parts of the orbit
where the curvature is large, than in parts of the orbit where the curvature 
is small. An integrator that uses a variable timestepping scheme can thus exploit
this by adapting its timesteps accordingly.


Fixed mass update timestep
--------------------------
The most straightforward way to evolve a two-body system with variable mass, 
is to choose a fixed timestep :math:`\Delta t` and update the masses at
times :math:`t_i`:

.. math::
   t_{i+1} = t_i + \Delta t

with masses :math:`m_i`:

.. math::
   m_{i+1} &= m_i + \Delta m \\
           &= m_i + \frac{dm}{dt} \Delta t 

The changes in mass which are applied at times :math:`t_i`,   


- Osculating orbits (due to change in mass)

- Large mass update --> large error in eccentricity ?

- How do large mass updates influence the change in eccentricity?


.. image:: http://home.strw.leidenuniv.nl/~lau/positions_e0.png
   :width: 1016 px
   :height: 841 px
   :scale: 50 %
   :align: center
   :alt: alternate text

.. image:: http://home.strw.leidenuniv.nl/~lau/positions_e05.png
   :width: 1003 px
   :height: 807 px
   :scale: 50 %
   :align: center
   :alt: alternate text

.. math::
   :label: conservation_angular_momentum

   h = \sqrt{ G\mu a (1-e^2) } = \text{constant}


Goal:
- Investigate large mass update intervals

- Variable mass update intervals
- Accuracy and conservation of energy/angular momentum

Motivation for numerical integration:
eccentricity cannot be solved exactly.









