from turtle import Turtle
import random

ball_width = 1
ball_length = 1
ball_outline = 1

move_distance = 10
ball_speed = 0.05
speed_increament = 0.99


class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.rvalue = 0
        self.gvalue = 0
        self.bvalue = 0

        self.shape("circle")
        self.shapesize(ball_width,ball_length,ball_outline)
        self.ball_color()
        self.speed(0)
        self.penup()
        self.move_speed = ball_speed
        self.x_move = move_distance
        self.y_move = move_distance


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= speed_increament

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = ball_speed
        self.bounce_x()
        self.bounce_y()


    def ball_color(self):
        r = random.randint(0, 200)
        g = random.randint(0, 200)
        b = random.randint(0, 200)

        self.rvalue = r
        self.gvalue = g
        self.bvalue = b

        self.color((r,g,b))


        
