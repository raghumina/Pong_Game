# Pong game
# Pong game in Python using Pycharm module
#
# Lets Start

import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Pong by Raghu Mina")
wn.setup(width=800, height=600)
wn.tracer(0)

# Player B/ Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(-350, 0)

# Player A/ Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(350, 0)

# bALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)


# Functions for movement of ball and Paddle A and Paddle B

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")

# Main gaming loop
while True:
    wn.update()
