from turtle import Turtle

moving_distance = 20

paddle_width = 1
paddle_length = 5
paddle_outline = 1

class Paddle(Turtle) :

    def __init__(self,x,y):
        super().__init__()
        self.r = 0
        self.g = 0
        self.b = 0
        
        self.shape("square")
        self.shapesize(paddle_width , paddle_length , paddle_outline)
        self.color(self.r,self.g,self.b)
        self.speed(0)
        self.penup()
        self.seth(90)
        self.setpos(x,y)
            
        
    def move_up(self):
        if self.ycor() <= 230:
            new_y = self.ycor() + moving_distance
            self.goto(self.xcor(), new_y)
        
    def move_down(self):
        if self.ycor() >= -230:
            new_y = self.ycor() - moving_distance
            self.goto(self.xcor(), new_y)

        
    def paddle_color(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

        self.color(r,g,b)


