from variables import *

import time 


def main():

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
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write(("Player1 : 0 Player2 : 0"), align="center", font=FONT)

    # Functions to move paddle vertically
    def paddleaup():
        y = player_1.ycor()
        y += 20
        player_1.sety(y)
    
    
    def paddleadown():
        y = player_1.ycor()
        y -= 20
        player_1.sety(y)
    
    
    def paddlebup():
        y = player_2.ycor()
        y += 20
        player_2.sety(y)
    
    
    def paddlebdown():
        y = player_2.ycor()
        y -= 20
        player_2.sety(y)
    
    
    # Keyboard bindings
    wn.listen()
    wn.onkeypress(paddleaup, "w")
    wn.onkeypress(paddleadown, "s")
    wn.onkeypress(paddlebup, "Up")
    wn.onkeypress(paddlebdown, "Down")

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
                pen.write("Winner is Player1".format(PLAYER_1_SCORE), align="center", font=FONT)
                time.sleep(3)

        if PLAYER_2_SCORE >= WINNER_SCORE:
            pen.penup
            pen.home()
            pen.sety(-13)
            for i in range(1):
                pen.color('white')
                pen.write("Winner is Player2".format(PLAYER_2_SCORE), align="center", font=FONT)
                time.sleep(3)
                

if __name__ == '__main__':
    main()
