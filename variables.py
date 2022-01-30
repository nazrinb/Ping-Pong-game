import pygame


#variables
FONT = ("Courier", 24, "normal")
MAX_HEIGHT = 290
MAX_WEIGHT = 390
WINNER_SCORE = 10
PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0
PLAYER_SPEED = 50

def init_pen():
    pen = turtle.Turtle()
    pen.hideturtle()