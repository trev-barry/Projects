#------------------------------------------------------------------
# imports
import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns

# global variables/constants
total_energy_error = [] # total energy list for later plotting
total_energy_time = [] # used for plotting energy error
solar_mass = 1.9e30 #kg
terra_mass = 10e24 #kg
G = 6.67408e-11 #m^3/(kg s^2)
planets_val = [] # stores the classes of each planet generated
#------------------------------------------------------------------
# functions used
def KE(mass,vel): # kinetic energy
    return 0.5*mass*vel**2

def PE(m1,m2,r): # potential energy
    return (G*m1*m2)/r

def vel_circular(m1,r): # calculates the tangential velocity of an object
    return math.sqrt((G*m1)/r)

def f_grav(m1,m2,r,G): # force gravitational
    return (m1*m2*G)/r**2

def distance(x1,y1,x2,y2): # distance between two points on a graph
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
#------------------------------------------------------------------
#classes used in the rk4 integration

class Position_Velocity: # class that holds position and velocity for the planets to call from
    def __init__(self,x,y,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

class Derivative: # stores the position and velocity change so the rk4 method can call it up to use
    def __init__(self,dx,dy,dvx,dvy):
        self.dx = dx
        self.dy = dy
        self.dvx = dvx
        self.dvy = dvy
#------------------------------------------------------------------
# creating our solar system (will be similar to our solar system)
class Planet:
    def __init__(self):
        self.mass = np.random.uniform(terra_mass*0.01,terra_mass*2000) # typical range of planet masses
        self.crashed = False
        #------------------------------------------------------------------
        # generating the random position and calculating its intial velocity based on keps' law
        x = np.random.randint(-1e12,1e12) # typical range for a planet postion around a star
        y = np.random.randint(-1e12,1e12)

        # calculating the tang velocity
        r = (x**2 + y**2)**(0.5)
        velocity_tan = vel_circular(sun.mass,r)

        # finding theta
        theta = math.atan2(y,x)

        # adding in the x, y component of velocity
        velocity_x = -velocity_tan*np.sin(theta)
        velocity_y = velocity_tan*np.cos(theta)
        #------------------------------------------------------------------
        self.position_velocity = Position_Velocity(x,y,velocity_x,velocity_y) # storing x,y,dx,dy in the class

    def acceleration(self, pv):
        ax = 0.0
        ay = 0.0
        r = math.sqrt(self.position_velocity.x**2 + self.position_velocity.y**2)
        force_sun = -f_grav(self.mass,sun.mass,r,G)
        #calculating force of sun on self first
        ax += (force_sun*self.position_velocity.x/r)/self.mass
        ay += (force_sun*self.position_velocity.y/r)/self.mass
        for p in planets_val:
            if p is self or p.crashed == True:
                continue  # ignore ourselves
            dx = p.position_velocity.x - pv.x
            dy = p.position_velocity.y - pv.y
            dsq = dx*dx + dy*dy  # distance squared
            r = math.sqrt(dsq)  # distance
            if r < 1e-10:
                force = 0 # preventing a divide by a r=0 (computer rounding)
                print('Attempting to divide by zero :(')
            else:
                force = -f_grav(p.mass,self.mass,r,G)
            # Accumulate acceleration
            ax += (force*dx/r)/self.mass
            ay += (force*dy/r)/self.mass
        return (ax, ay)

    #------------------------------------------------------------------
    #using the rk4 method of integration
    def initialDerivative(self, pv, t):
        ax, ay = self.acceleration(pv)
        return Derivative(pv.dx, pv.dy, ax, ay)

    def nextDerivative(self, initialState, derivative, t, dt):
        pv = Position_Velocity(0,0,0,0)
        pv.x = initialState.x + derivative.dx*dt
        pv.y = initialState.y + derivative.dy*dt
        pv.dx = initialState.dx + derivative.dvx*dt
        pv.dy = initialState.dy + derivative.dvy*dt
        ax, ay = self.acceleration(pv)
        return Derivative(pv.dx, pv.dy, ax, ay)

    def updatePlanet(self, t, dt): # combines above declarations to preform an rk4 integration
        a = self.initialDerivative(self.position_velocity, t)
        b = self.nextDerivative(self.position_velocity, a, t, dt*0.5)
        c = self.nextDerivative(self.position_velocity, b, t, dt*0.5)
        d = self.nextDerivative(self.position_velocity, c, t, dt)
        dxdt = 1.0/6.0 * (a.dx + 2.0*(b.dx + c.dx) + d.dx)
        dydt = 1.0/6.0 * (a.dy + 2.0*(b.dy + c.dy) + d.dy)
        dvxdt = 1.0/6.0 * (a.dvx + 2.0*(b.dvx + c.dvx) + d.dvx)
        dvydt = 1.0/6.0 * (a.dvy + 2.0*(b.dvy + c.dvy) + d.dvy)
        self.position_velocity.x += dxdt*dt
        self.position_velocity.y += dydt*dt
        self.position_velocity.dx += dvxdt*dt
        self.position_velocity.dy += dvydt*dt
    #------------------------------------------------------------------

class Sun:
    def __init__(self):
        self.mass = np.random.uniform(solar_mass*0.5,solar_mass*8) # typical range of solar masses
        self.x_pos = 0
        self.y_pos = 0
#------------------------------------------------------------------
# EXECUTING THE MAIN PROGRAM

# initializing planets and a sun
sun = Sun()
num_planets = np.random.randint(1,5)
for i in range(num_planets):
    planets_val.append(Planet())

# finding our maximum radius to scale our graph
r_max = 0
vel_r_max = 0
for p in planets_val:
    r = math.sqrt(p.position_velocity.x**2 + p.position_velocity.y**2)
    if r > r_max:
        r_max = r
    if r == r_max:
        vel_r_max = math.sqrt(p.position_velocity.dx**2 + p.position_velocity.dy**2)

r_max = r_max * 1.3

# finding the initial total energy
total_energy_initial = 0
for p in planets_val:
    K_E = KE(p.mass,math.sqrt(p.position_velocity.dx**2 + p.position_velocity.dy**2))
    P_E = PE(p.mass,sun.mass,math.sqrt(p.position_velocity.x**2 + p.position_velocity.y**2))
    tot = K_E+P_E
    total_energy_initial += tot
#------------------------------------------------------------------
# graphing the planetary motions using matplotlib

# setting up our graph
plt.ion() # changing the matplotlib to interactive mode, will be used to create the animation
fig, ax1 = plt.subplots()
px, py = [],[]
for p in planets_val: # filling the list with initial positions
    px.append(p.position_velocity.x)
    py.append(p.position_velocity.y)
px.append(0) # filling in the sun's coordinates
py.append(0)
sc = ax1.scatter(px,py)
plt.xlim(-r_max,r_max)
plt.ylim(-r_max,r_max)

# returns a time proportional to the outermost planets initial speed
time = int((2*np.pi*r_max)/vel_r_max)
dt = 1000 # timestep in seconds
print_i = 0

plt.draw()
for t in range(0,time,dt):
    p_index = 0
    total_energy = 0
    for p in planets_val:
        p.updatePlanet(t,dt)

        if p.crashed == True: # stops tracking p if it crashes into something else
            continue

        if math.sqrt(p.position_velocity.x**2 + p.position_velocity.y**2) > r_max:
            p.crashed = True # calling it "crashed" so it's no longer plotted
        px[p_index] = p.position_velocity.x
        py[p_index] = p.position_velocity.y
        p_index += 1

        if (print_i%1000) == 0:
            K_E = KE(p.mass,math.sqrt(p.position_velocity.dx**2 + p.position_velocity.dy**2))
            P_E = PE(p.mass,sun.mass,math.sqrt(p.position_velocity.x**2 + p.position_velocity.y**2))
            tot = K_E+P_E
            total_energy += tot

    if (print_i%2000) == 0:
        sc.set_offsets(np.c_[px,py])
        fig.canvas.draw_idle()
        plt.pause(0.0001)
        total_energy_error.append((total_energy_initial-total_energy)/total_energy_initial)
        total_energy_time.append(t)

    print_i += 1


    #------------------------------------------------------------------
    # checking for planetary collisions
    for p in planets_val:
        for p2 in planets_val:
            if p2.crashed == True:
                continue
            if p2 != p:
                diff_x = p.position_velocity.x-p2.position_velocity.x
                diff_y = p.position_velocity.y-p2.position_velocity.y

                r = math.sqrt(diff_x**2+diff_y**2)
                if r <= 3.84e8:# distance from Earth to moon. Using this as a constraint for collisions
                    p.crashed = True
                    p2.crashed = True
    #------------------------------------------------------------------

#------------------------------------------------------------------
# printouts of all the information of the animation plus graphs
print('Number of randomly generated planets:',num_planets)

# checking for crashed planets
crashed_planets = 0
for i in planets_val:
    if i.crashed == True: # looping through all the planets to preform a status check
        crashed_planets += 1

print('Number of crashed/lost planets:',crashed_planets)
print('Initial total energy is:',total_energy_initial)
print('Fractional energy lost is:', total_energy_error[-1]*100,'%')

plt.ioff() # closes matplotlib's animation mode
plt.figure() # sets up for a new graph to be plotted

sns.set(style="darkgrid")
plt.title('Fractional Energy Loss over Time')
plt.xlabel('Time')
plt.ylabel('Fractional Energy Loss')
energy_graph = sns.lineplot(total_energy_time,total_energy_error).get_figure()
energy_graph.savefig('Fractional Energy Lost')
