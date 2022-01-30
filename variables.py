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
posx = random.randint(-360, 360)
posy = random.randint(-360, 360)

# Initialize the score
left_player = 0
right_player = 0


def init_pen():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.color("white")

    return pen

def init_scr():
    wn = turtle.Screen()
    wn.title("Pong by nazrin")
    wn.bgcolor('black')
    wn.setup(width=1000, height=600)
    wn.tracer(0)

    
    return wn

def init_player1():
    lpaddle = turtle.Turtle()
    lpaddle.speed(PLAYER_SPEED)
    lpaddle.shape("square")
    lpaddle.color("blue")
    lpaddle.shapesize(stretch_wid=5, stretch_len=1)
    lpaddle.penup()
    lpaddle.goto(-350,0)
    lpaddle.direction = "Stop"

    return lpaddle

def init_player2():
    rpaddle = turtle.Turtle()
    rpaddle.speed(PLAYER_SPEED) 
    rpaddle.shape("square")
    rpaddle.color("orange")
    rpaddle.shapesize(stretch_wid=5, stretch_len=1)
    rpaddle.penup()
    rpaddle.goto(350, 0)
    rpaddle.direction = "Stop"

    return rpaddle

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