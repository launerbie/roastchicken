
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
One straightforward way to evolve a two-body system with variable mass, is to simply





- Variable mass update intervals
- Accuracy and conservation of energy/angular momentum

Large mass update --> large error in eccentricity ?
How do large mass updates influence the change in eccentricity?


Goal:
- Investigate large mass update intervals

Show behaviour at different starting mass-loss-indices

Motivation for numerical integration:

eccentricity cannot be solved exactly.


One planet system
-----------------

Simulate a one-planet system and plot the evolution of:

a vs t
e vs t
w vs t
f vs t
P vs t
phi vs t


Two planet system
-----------------








