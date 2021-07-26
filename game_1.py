from functools import partial
from turtle import Turtle, Screen
from tkinter import *


import winsound
import turtle
import random 
import time 
# import soundfile as sf
# import sounddevice as sd


def game():
    def validate_login(username_1, username_2):
        print('username_1 entered: ', username_1.get())
        print('username_2 entered: ', username_2.get())
        return None

    tkWindow = Tk()
    tkWindow.geometry('400x400')
    tkWindow.title('Tkinter Login Form - pythonexamples.org')

    #First username:
    username_label_1 = Label(tkWindow, text='First User Name').grid(row=0, column=0)
    username_1 = StringVar()
    username_entry_1 = Entry(tkWindow, textvariable=username_1).grid(row=0, column=1)

    #Second username:
    username_label_2 = Label(tkWindow, text='Second User Name').grid(row=1, column=0)
    username_2 = StringVar()
    username_entry_2 = Entry(tkWindow, textvariable=username_2).grid(row=1, column=1)

    validate_login = partial(validate_login, username_1, username_2)

    login_button = Button(tkWindow, text='Start Game:-)', command=validate_login).grid(row=4, column=0)
    
    tkWindow.mainloop()



    #Enclosure
    FONT = ("Courier", 24, "normal")
    MAX_HEIGHT = 290
    MAX_WEIGHT = 390
    WINNER_SCORE = 10
    PLAYER_1_SCORE = 0
    PLAYER_2_SCORE = 0
    PLAYER_SPEED = 50
    
    #Pen
    pen = turtle.Turtle()
    pen.hideturtle()

    # wn 
    wn = turtle.Screen()
    wn.title("Pong by nazrin")
    wn.bgcolor('black')
    pen.penup()
    pen.home()
    pen.sety(-13)
    pen.color('white')
    pen.write('Ping Pong Game', align='center', font=('Arial', 26, 'bold'))
    time.sleep(2)
    pen.clear()
    wn.setup(width=800, height=600)
    wn.tracer(0)

    # Player_1 
    player_1 = turtle.Turtle()
    player_1.speed(PLAYER_SPEED)
    player_1.shape("square")
    player_1.color("blue")
    player_1.shapesize(stretch_wid=5, stretch_len=1)
    player_1.penup()
    player_1.goto(-350,0)

    # Player_2 
    player_2 = turtle.Turtle()
    player_2.speed(PLAYER_SPEED) 
    player_2.shape("square")
    player_2.color("orange")
    player_2.shapesize(stretch_wid=5, stretch_len=1)
    player_2.penup()
    player_2.goto(350, 0)
    
    # Extra_player_1
    ex_1 = turtle.Turtle()
    ex_1.speed(PLAYER_SPEED)
    ex_1.shape('square')
    ex_1.color('blue')
    ex_1.shapesize(stretch_wid=5, stretch_len=1)
    ex_1.penup()
    ex_1.goto(-350, -600)

    #Extra_player_2:
    ex_2 = turtle.Turtle()
    ex_2.speed(PLAYER_SPEED)
    ex_2.shape('square')
    ex_2.color('orange')
    ex_2.shapesize(stretch_wid=5, stretch_len=1)
    ex_2.penup()
    ex_2.goto(350, -600)

    # Ball 
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color('white')
    ballheading = random.randint(1,360)
    ball.penup()
    ball.setheading(ballheading)
    ball.dx = 0.5
    ball.dy = -0.5

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("{} : 0 {} : 0".format(username_1.get(), username_2.get()), align="center", font=FONT)

    # movement  
    #PLAYER_1
    def player_1_up():
        y = player_1.ycor()
        y += PLAYER_SPEED
        player_1.sety(y)

    def player_1_down():
        y = player_1.ycor()
        y -= PLAYER_SPEED
        player_1.sety(y)

    #PLAYER_2
    def player_2_up():
        y = player_2.ycor()
        y += PLAYER_SPEED
        player_2.sety(y)

    def player_2_down():
        y = player_2.ycor()
        y -= PLAYER_SPEED
        player_2.sety(y)
    
    #PLAYER_EXTRA_1
    def ex_1_up():
        y = ex_1.ycor()
        y += PLAYER_SPEED
        ex_1.sety(y)

    def ex_1_down():
        y = ex_1.ycor()
        y -= PLAYER_SPEED
        ex_1.sety(y)

    #PLAYER_EXTRA_2    
    def ex_2_up():
        y = ex_2.ycor()
        y += PLAYER_SPEED
        ex_2.sety(y)

    def ex_2_down():
        y = ex_2.ycor()
        y -= PLAYER_SPEED
        ex_2.sety(y)

    #BOTH
    def both_1():
        player_1_up()
        ex_1_up()
        
    def both_2():
        player_2_up()
        ex_2_up()

    def both_3():
        player_1_down()
        ex_1_down()

    def both_4():
        player_2_down()
        ex_2_down()
    
    # Keyboards
    wn.listen()
    wn.onkeypress(both_1, "w")
    wn.onkeypress(both_3, "s")
    wn.onkeypress(both_2, "Up")
    wn.onkeypress(both_4, "Down")

    # Main game loop 
    while max(PLAYER_2_SCORE, PLAYER_1_SCORE) <= 9:
        wn.update()
        
        # Move the ball 
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        
        # Border checking 
        if ball.ycor() > MAX_HEIGHT:
            ball.sety(MAX_HEIGHT)
            ball.dy *= -1 
            
        if ball.ycor() < -MAX_HEIGHT:
            ball.sety(-MAX_HEIGHT)
            ball.dy *= -1 
        
        if ball.xcor() > MAX_WEIGHT:
            ball.goto(0, 0)

            ball.dx *= -1
            PLAYER_1_SCORE += 1
            pen.clear()
            pen.write("{} : {} {} : {}".format(username_1.get(), PLAYER_1_SCORE, username_2.get(), PLAYER_2_SCORE), align="center", font=FONT)
            
        if ball.xcor() < -MAX_WEIGHT:
            ball.goto(0, 0)
            ball.dx *= -1
            PLAYER_2_SCORE += 1
            pen.clear()
            pen.write("{} : {} {} : {}".format(username_1.get(), PLAYER_1_SCORE, username_2.get(), PLAYER_2_SCORE), align="center", font=FONT)


        # Paddle and ball colluctions
        #PLAYER_1_2_BALL
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_2.ycor() +40 and ball.ycor() > player_2.ycor() -40):
            ball.setx(340)
            ball.dx *= -1 
        
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player_1.ycor() + 40 and ball.ycor() > player_1.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1 
        
        #PLAYER_EXTRA_1_2_BALL
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < ex_2.ycor() + 40 and ball.ycor() > ex_2.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
        
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < ex_1.ycor() + 40 and ball.ycor() > ex_1.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1


        # Winners
        if PLAYER_1_SCORE >= WINNER_SCORE:
            pen.penup()
            pen.home()
            pen.sety(-13)
            i = 0 
            i += 1
            for i in range(1):
                pen.color('white')
                pen.write("Winner is {} with {} scores!!!".format(username_1.get(), PLAYER_1_SCORE), align="center", font=FONT)
                time.sleep(3)

        if PLAYER_2_SCORE >= WINNER_SCORE:
            pen.penup
            pen.home()
            pen.sety(-13)
            for i in range(1):
                pen.color('white')
                pen.write("Winner is {} with {} scores!!!".format(username_2.get(), PLAYER_2_SCORE), align="center", font=FONT)
                time.sleep(3)
                

if __name__ == '__main__':
    game()
