import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")
wn.tracer(0)

balls = []
colors = ["yellow", "red", "purple", "green", "blue", "orange", "pink", "white"]
shapes = ["circle", "triangle", "square"]

for _ in range(20):
    balls.append(turtle.Turtle())

for ball in balls:
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-300, 300)
    y = random.randint(100, 400)
    ball.goto(x, y)
    ball.dy = 0
    ball.dx = random.randint(-2, 2)
    ball.da = random.randint(-5, 5)
    gravity = 0.1

while True:
    wn.update()

    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor() + ball.dx)

        if ball.ycor() < -315:
            ball.dy *= -1
            ball.da *= -1
            ball.sety(-315)

        if ball.xcor() > 320:
            ball.dx *= -1
            ball.da *= -1
        if ball.xcor() < -320:
            ball.dx *= -1
            ball.da *= -1
