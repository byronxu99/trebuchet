# Trebuchet
Physics modeling and simulation code for a new trebuchet design.

## Intro
A trebuchet is roughly a double pendulum consisting of the arm and sling. A falling weight rotates the arm, which then transfers energy into the sling. The sling releases at a certain angle, tuned to maximize velocity.

## Design
Traditional designs attach the driving mass to the short end of the arm. It has certain limitations:
- The driving mass moves along a curved path, while gravitational force only acts straight downward.
- When approaching peak sling velocity, the arm is near vertical and the mass moves roughly horizontally. Gravity exerts little torque to rotate the arm, at the moment where we would like the most torque.
- At the moment of projectile launch, the driving mass is moving quite fast. This remaining kinetic energy is wasted.

This design consists of a freely spinning arm attached to a horizontal axle:
- The arm is able to rotate more than 360 degrees.
- The driving mass is tied to a string, which is wound around the axle.
- As the mass is released and falls straight down, it rotates the axle and spins up the arm.
- The arm can gradually accelerate over multiple rotations.
- The small axle diameter relative to arm length gives a large "gear ratio", which lets the speed of the driving mass remain slow. A greater fraction of kinetic energy can be transferred to the arm.
- After the desired number of revolutions, the sling is released. This part may require electronic sensing and control.

There are two stages with different dynamics:
- Spin up - the falling mass accelerates the arm, and the sling is held fixed relative to the arm.
- Launch - the sling is released shortly before the mass hits the ground, and it launches the projectile. Only this stage behaves like a double pendulum.

## Code
- `equations.ipynb` - compute the equations of motion for this system
- `design.ipynb` - calculate design parameters and write to file
- `simulation.ipynb` - simulate the trebuchet dynamics
- `projectile_motion.ipynb` - simulate projectile motion after launch
