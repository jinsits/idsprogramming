from vpython import*
# Equations used:
# acceleration = x(t) * (-k/mass)
# x(t) = eq - mass position
# velocity = initial_velocity + acceleration * dt
# position = initial_position + (velocity* * dt)
# display(width = 600, height = 600, center = vector(6, 0, 0), background = color.white)

# Objects
mass = box(pos=vector(12, 0, 0), velocity=vector(0, 0, 0), size=vector(1, 1, 1), mass=1.0, color=color.blue)
pivot = vector(0, 0, 0)  # Center of coordinate system
spring = helix(pos=pivot, axis=mass.pos-pivot, radius=0.4, constant=1, thickness=0.1, coils=20, color=color.red)
wall = box(pos=vector(0, 1, 0), size=vector(0.2, 3, 2), color=color.yellow)
floor = box(pos=vector(6, -0.6, 0), size=vector(14, 0.2, 2), color=color.yellow)
# Position of spring is at pivot
# Axis = other end of spring is at position of mass, helix rings radius are 0.4 units, wires are 0.1 units, 20 coils
# Constant = k (spring constant)

eq = vector(9, 0, 0)  # Equilibrium position
t = 0  # Time
dt = 0.01  # Time interval

# Loop to update the position of the mass/spring
while t < 50:
    rate(100)
    acc = (eq - mass.pos) * (spring.constant/mass.mass)
    mass.velocity = mass.velocity + (acc*dt)
    mass.pos = mass.pos + (mass.velocity*dt)
    spring.axis = mass.pos - spring.pos  # New position of end of helix
    t = t + dt  # Time increases with each loop