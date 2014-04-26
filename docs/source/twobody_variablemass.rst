
Variable mass two-body problem 
==============================

Introduction/History
--------------------
Mention important/relevant works here:
- Gylden, Mestschersky
- Hadjidimetriou
- Veras


Equations of motion
-------------------

Hadjidemetriou (1963) showed that in the case of isotropic mass-loss, 
the angular momentum h is conserved and equal to:

.. math::
   :label: conservation_angular_momentum

   h = \sqrt{ G\mu a (1-e^2) } = \text{constant}

where :math:`\mu` is the total mass of the system, :math:`a` the 
semi-major axis and :math:`e` the eccentricity.

.. note::

   Todo, include derivation of :eq:`conservation_angular_momentum`? 

Furthermore, he showed that for a variable mass two-body system, the 
evolution of the orbital elements :math:`a e \mu f` is governed by the 
following equations of motion:

.. math::
   :label: sma_evolution

   \frac{da}{dt} = -\frac{a(1+e^2+2e\cos f)}{1-e^2}\frac{1}{\mu}\frac{d\mu}{dt}

.. math::
   :label: eccentricity_evolution

   \frac{de}{dt} = -(e+\cos f) \frac{1}{\mu}\frac{d\mu}{dt}

.. math::
   :label: argument_of_periapsis_evolution

   \frac{d \omega}{dt} = -\frac{\sin f}{e} \frac{1}{\mu}\frac{d\mu}{dt}

.. math::
   :label: true_anomaly_evolution

   \frac{df}{dt} = \frac{\sin f}{e} \frac{1}{\mu}\frac{d\mu}{dt} + \frac{n(1+e \cos f)^2}{(1-e^2)^{3/2}}



Mass-loss prescriptions
-----------------------


Definition of adiabaticity
--------------------------

Veras(2011) quantify the degree of adiabaticity with a dimensionless 
mass-loss index :math:`\Psi`:

.. math::
   :label: definition_mass_loss_index

   \Psi \equiv \frac{\alpha}{n \mu} 

where :math:`n` is the mean motion of the orbit and :math:`\alpha=-\frac{d\mu}{dt}` the 
constant mass-loss rate.

Since the mean motion is equal to:

.. math::
   :label: definition_mean_motion

   n \equiv \frac{2\pi}{P} = G^{1/2} \mu^{1/2} a^{-3/2}

one can derive the equation that governs the evolution of the mean motion by
taking the time derivative of :eq:`definition_mean_motion` and subsituting
back in :eq:`sma_evolution` which then yields:

.. math::
   :label: mean_motion_evolution

   \frac{dn}{dt} = \frac{n(2+e^2+3e\cos f)}{1-e^2} \frac{1}{\mu}\frac{d\mu}{dt}


Then by taking the time derivative of :eq:`definition_mass_loss_index` and plugging in 
equation :eq:`mean_motion_evolution` the equation that governs 
the evolution of :math:`\Psi` is obtained:

.. math::
   :label: mass_loss_index_evolution

   \frac{d\Psi}{dt} = -3\Psi \frac{1+e\cos f}{1-e^2} \frac{1}{\mu}\frac{d\mu}{dt} 


Solutions in the adiabatic regime
---------------------------------

By imposing that the evolution of a two-body system is well in the adiabatic regime,
certain solution can be found.






