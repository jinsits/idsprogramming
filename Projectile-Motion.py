from vpython import*

floor = box(pos=vec(0, -0.2, 0), size=vec(2, 0.1, 0.1), color=color.green)
ball = sphere(pos=vec(-1, -0.1, 0), radius=0.05, color=color.red, make_trail=True)

g = vec(0, -9.8, 0)
ball.m = 0.1
v0 = 4.0   # initial velocity
theta = 60   # angle of projectile

ball.p = ball.m*v0*vec(cos(theta*pi / 180), sin(theta*pi / 180), 0)   # momentum = m*v; vector shows vx & vy together

t = 0
dt = 0.01

while ball.pos.y >= -0.1:
    rate(100)   # determines how fast to run the equation, no more than 100 calculations per second
    force = ball.m * g  # force of gravity is only force in system
    ball.p = ball.p + (force * dt)  # new ball momentum
    ball.pos = ball.pos + ((ball.p/ball.m) * dt)  # new ball position
    t = t + dt   # new time value
