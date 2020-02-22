A WALK AROUND A SOLAR SYSTEM

Semester Project PHY 480
Trevor Franklin

PACKAGES USED
1. numpy
2. matplotlib.pyplot
3. math
4. seaborn
----------------------------------------------------------------------------
HOW TO USE
1. Check to see if you have all the necessary libraries imported
2. Download the git repository to your local folder
2. Navigate to the folder containing this file in your command line and run:
   python semester_project.py
3. If it works correctly the program should output an animation, a graph of the
   fractional energy loss over time plus several print statements giving you
   additional information about the system.
4. To interrupt the animation simply press control C
5. PLEASE NOTE!!! Depending on the masses and distances of the planets randomly
   chosen the animation can take anywhere from 5 seconds to a minute to fully
   run. When the animation is completed running, it will exit and you should be
   able to find a graph of the fractional energy loss over time inside the folder
   the program is running in.
--------------------------------------------------------------------------
Overview
For this project I attempted to model a randomly generated solar system and see
if it would remain stable over a set period of time. I was interested in seeing
if integration errors would cause a quick devolution of the system or even if a
randomly generated system would stay stable at all.

The first part of the code describes the classes that I use to generate the
system. This will output a random position and mass for each planet. This
information is then used in a force calculation to give the planet an initial
velocity such that it will start out in a circular orbit. The sun however, remains
as the fixed center point of the system. I disregarded the effects of the planets
gravity because I bound the limits of the planets mass such that at its largest
it would be several magnitudes smaller than the sun and therefore have a negligible
effect on the sun's position.

The next portion of code describes the runge-kutta integration function
used to calculate the future trajectory of each of the generated planets. This
includes an initial derivative and several next derivative steps used to approximate
the future trajectory.

At the main part of the program I first generate a random number of planets
between 1 and 5 for my system. Next I loop through the number of planets and I
call on the planet class and store each planet I create in a planets_val list.
This list is then used by the matplotlib package for the animation process.

Next the program loops through the time range, additionally
looping through the updatePlanet function found in the planet class to calculate
the planets next position. At each updatePlanet calculation the program will
also will show a live animation of the system as the updatePlanet function
evolves the system.

(Sidebar)
I chose the iteration time based off the maximum time it would take for a planet at
the outermost bounds of the x and y positions to make one full rotation around
the sun. This iteration time was scaled by looping through the radii
of each planets orbit, taking the furthest planet, finding its velocity and
taking the circumference divided by it's speed to get its rotation time. This
ensures that the animation will show every planet moving around the sun at
least once.
----------------------------------------------------------------------------
CHECKS
To approximate the error of this code I chose to track the total energy of
the system to see how much energy is lost due to rounding error over the
totality of the process. I was able keep the energy loss under 5% which
I attribute to using a small step size together with an rk4 level integration.
By looking at my energy loss I could provide a system check to see if the rk4
integration was working properly. By seeing a small consistent drop in total
energy would signify that the only loss to the system would be due to rounding
errors and the limitations of the the rk4 integration technique.

I calculated energy loss by first calculating the energy of the system before the
integration process begun. Using a for loop to iterate though each planet, I
found both the combined KE and PE of the system. I approximated the system
to be very simple only looking at each planets KE and PE relative to the sun.
This was because the PE between planets would be so small compared to the PE
of the planet-sun relationship the "missing energy" of the system would be
negligible. After each integration I find the difference between the initial
total energy and the new total energy, which I in turn use to plot the energy
loss over time.
----------------------------------------------------------------------------
ANALYSIS
The bulk of the information garnered from this program comes from the Fractional
Energy Loss Graph. We can see from this graph that for each run you do, the graph
will tend to output a similar cyclical pattern, however small. The root cause of
this fluctuation most likely comes from the limits of the rk4 integration
process. As with any type of integration, there is a step size involved with
limiting the accuracy of the model. Since my planetary system uses a random
selection of orbiting radii, a singular step size is hard to choose. Within the
bounds of my program, I had to find a step size that worked fast enough at the
largest bounds of my radii, without being too big for the smallest radii
integrations. Due to this limitation, you will see that the fractional energy
loss tends to be slightly higher at smaller orbiting radii.

With later incarnations of this code a proactive subroutine to add would be
a function that can look at the scale of the randomly generated planetary radii
and average a decent time step that would work well between the extremes of the
system.

For the energy calculation I approximated the total energy of the system
to be the KE of each planet summed with the gravitational PE of each planet with
respect to the sun. I chose to ignore the PE of each planet with each other under
the assumption that the missing energy would be minuscule compared to the PE of
the sun planet system. However, we see from the energy graph this is not the
case. In several iterations of the system I found that the fractional energy loss
went negative, indicating that work was being done on the system (the planets).
My guess is that since my program is not tracking the GravPE of each planet, any
force the planets would act upon each other would appear as work done on the
planetary system by an outside entity. This would give a simple explanation to
why the fractional energy loss is sometimes negative.

A brute force method I used as a sanity check against my code was to randomly
generate a system and look at the initial masses and distances away from the sun.
From there I would use Kepler's 3rd law to generate its initial velocity, energy
equations to find its KE and PE, and check all of this against the corresponding
values the code would spit out. I used this as a confirmation check that the
force and energy equations I put into the program were being properly implemented.
