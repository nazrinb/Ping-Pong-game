import turtle
import random

#variables
FONT = ("Courier", 24, "normal")
MAX_HEIGHT = 290
MAX_WEIGHT = 390
WINNER_SCORE = 10

PLAYER_SPEED = 50
Player1 = 'PLAYER1'
Player2 = 'PLAYER2'
FORWARD_DST = 15


def init_pen():
    pen = turtle.Turtle()
    pen.hideturtle()

    return pen

def init_scr():
    wn = turtle.Screen()
    wn.title("Pong by nazrin")
    wn.bgcolor('black')
    wn.setup(width=1.0, height=1.0)
    wn.tracer(0)

    return wn

def init_player1():
    player_1 = turtle.Turtle()
    player_1.speed(PLAYER_SPEED)
    player_1.shape("square")
    player_1.color("blue")
    player_1.shapesize(stretch_wid=5, stretch_len=1)
    player_1.penup()
    player_1.goto(-350,0)
    player_1.direction = "Stop"

    return player_1

def init_player2():
    player_2 = turtle.Turtle()
    player_2.speed(PLAYER_SPEED) 
    player_2.shape("square")
    player_2.color("orange")
    player_2.shapesize(stretch_wid=5, stretch_len=1)
    player_2.penup()
    player_2.goto(350, 0)
    player_2.direction = "Stop"

    return player_2

def init_ex1():
    ex_1 = turtle.Turtle()
    ex_1.speed(PLAYER_SPEED)
    ex_1.shape('square')
    ex_1.color('blue')
    ex_1.shapesize(stretch_wid=5, stretch_len=1)
    ex_1.penup()
    ex_1.goto(-350, -600)
    ex_1.direction = "Stop"

    return ex_1

def init_ex2():
    ex_2 = turtle.Turtle()
    ex_2.speed(PLAYER_SPEED)
    ex_2.shape('square')
    ex_2.color('orange')
    ex_2.shapesize(stretch_wid=5, stretch_len=1)
    ex_2.penup()
    ex_2.goto(350, -600)
    ex_2.direction = "Stop"

    return ex_2

def init_ball():
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color('white')
    ballheading = random.randint(1,360)
    ball.penup()
    ball.setheading(ballheading)
    ball.dx = 0.5
    ball.dy = -0.5

    return ball

def move(player):
    if player.direction == "up":
        y = player.ycor()
        player.sety(y+FORWARD_DST)
    
    if player.direction == "down":
        y = player.ycor()
        player.sety(y-FORWARD_DST)

    if player.direction == "left":
        x = player.xcor()
        player.setx(x-FORWARD_DST)

    if player.direction == "right":
        x = player.xcor()
        player.setx(x+FORWARD_DST)