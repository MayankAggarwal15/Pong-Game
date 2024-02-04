from turtle import Turtle

class Boundary: 

    def __init__(self):

        self.create_boundary()
        self.mid_line()

    def create_boundary(self):
        tim = Turtle()
        tim.hideturtle()
        tim.color("black")
        tim.pensize(7.5)
        tim.speed(0)
        tim.penup()
        tim.setpos(-400 , -295)
        tim.pendown()
        tim.fillcolor("white")
        tim.begin_fill()

        for i in range(2):
            tim.forward(800)
            tim.left(90)
            tim.forward(590)
            tim.left(90)

        tim.end_fill()

    def mid_line(self):
        line = Turtle()
        line.hideturtle()
        line.color("black")
        line.pensize(5)
        line.speed(0)
        line.seth(90)
        line.penup()
        line.setpos(0,-290)

        for i in range(33):
            line.pendown()
            line.forward(10)
            line.penup()
            line.forward(10)



