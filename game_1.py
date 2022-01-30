from variables import *

import time 


def game():

    pen = init_pen()
    wn = init_scr()
    player_1 = init_player1()
    player_2 = init_player2()
    ex_1 = init_ex1()
    ex_2 = init_ex1()
    ball = init_ball()

    pen.penup()
    pen.home()
    pen.sety(-13)
    pen.color('white')
    pen.clear()

    # Pen
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write(("Player1 : 0 Player2 : 0"), align="center", font=FONT)

    # player movement functions
    def go_up(player, ex):
        if player.direction != "down":
            player.direction = "up"
            ex_1.direction = "up"

    def go_down(player, ex):
        if player.direction != "up":
            player.direction = "down"
            ex_1.direction = "up"

    def turn_w(player, ex):
        if player.direction != "s":
            player.direction = "w"
            ex_2.direction = "up"

    def turn_s(player, ex):
        if player.direction != "w":
            player.direction = "s"
            ex_2.direction = "up"

    # respond to user input
    wn.listen()
    wn.onkeypress(go_up(player_1, ex_1), "Up")
    wn.onkeypress(go_down(player_1, ex_1), "Down")
    wn.onkeypress(turn_w(player_2, ex_2), "w")
    wn.onkeypress(turn_s(player_2, ex_2), "s")

    # #BOTH
    # def both_1():
    #     player_1_up()
    #     ex_1_up()
        
    # def both_2():
    #     player_2_up()
    #     ex_2_up()

    # def both_3():
    #     player_1_down()
    #     ex_1_down()

    # def both_4():
    #     player_2_down()
    #     ex_2_down()
    
    # # Keyboards
    # wn.listen()
    # wn.onkeypress(both_1, "w")
    # wn.onkeypress(both_3, "s")
    # wn.onkeypress(both_2, "Up")
    # wn.onkeypress(both_4, "Down")
    PLAYER_1_SCORE = 0
    PLAYER_2_SCORE = 0
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
            pen.write("Player1 : {} Player2 : {}".format(PLAYER_1_SCORE, PLAYER_2_SCORE), align="center", font=FONT)
            
        if ball.xcor() < -MAX_WEIGHT:
            ball.goto(0, 0)
            ball.dx *= -1
            PLAYER_2_SCORE += 1
            pen.clear()
            pen.write("Player1 : {} Player2 : {}".format(PLAYER_1_SCORE, PLAYER_2_SCORE), align="center", font=FONT)


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
                pen.write("Winner is Player1 with {} scores!!!".format(PLAYER_1_SCORE), align="center", font=FONT)
                time.sleep(3)

        if PLAYER_2_SCORE >= WINNER_SCORE:
            pen.penup
            pen.home()
            pen.sety(-13)
            for i in range(1):
                pen.color('white')
                pen.write("Winner is {} with {} scores!!!".format(Player2.get(), PLAYER_2_SCORE), align="center", font=FONT)
                time.sleep(3)
                

if __name__ == '__main__':
    game()
