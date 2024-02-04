# PROJECT ON PONG GAME

from turtle import Screen , Turtle
import time
from paddle import Paddle
from boundary import Boundary
from ball import Ball
from score import Score

myscreen = Screen()
myscreen.setup(1350,1000,0,0)
myscreen.title("PONG GAME")
myscreen.colormode(255)
myscreen.bgcolor("grey")

myscreen.tracer(0)

boundary = Boundary()
player2_paddle = Paddle(350,0)
player1_paddle = Paddle(-350,0)
ball = Ball()
score = Score()
logo = Score()

logo.game_logo()
logo.game_player()
score.player1_points()
score.player2_points()

myscreen.update()

time.sleep(0.5)

myscreen.listen()

myscreen.onkeypress(player1_paddle.move_up, "w")
myscreen.onkeypress(player1_paddle.move_down, "s")
myscreen.onkeypress(player2_paddle.move_up, "Up")
myscreen.onkeypress(player2_paddle.move_down, "Down")

end = False

while not end:
    myscreen.update()
    time.sleep(ball.move_speed)
    ball.move()

    r = ball.rvalue
    g = ball.gvalue
    b = ball.bvalue

    if ball.distance(player1_paddle) < 50 and ball.xcor() < -325 and ball.xcor() > -335:
        ball.bounce_x()
        player1_paddle.paddle_color(r, g, b)
        ball.ball_color()

    if ball.distance(player2_paddle) < 50 and ball.xcor() > 325 and ball.xcor() < 335:
        ball.bounce_x()
        player2_paddle.paddle_color(r, g, b)
        ball.ball_color()


    if ball.ycor() >= 280 or ball.ycor() <= -280 :
        ball.bounce_y()
        ball.ball_color()

    if ball.xcor() >= 400 :
        ball.reset_position()
        score.player1_points()
        ball.ball_color()

    if ball.xcor() <= -400 :
        ball.reset_position()
        score.player2_points()
        ball.ball_color()

    if score.player1_score == 10 :
        score.won_game(1)
        end = True

    elif score.player2_score == 10:
        score.won_game(2)
        end = True

myscreen.exitonclick()


