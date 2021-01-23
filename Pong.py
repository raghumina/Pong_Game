# Pong game
# Pong game in Python using Pycharm module
#
# Lets Start

import turtle

wn = turtle.Screen()
wn.bgcolor("red")
wn.title("Pong by Raghu Mina")
wn.setup(width=800, height=600)
wn.tracer(0)

# Player A/ Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Player B/ Paddle B
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(350, 0)

# bALL


# Main gaming loop
while True:
    wn.update()
