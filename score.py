from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.player2_score = -1
        self.player1_score = -1
        self.color("black")
        self.hideturtle()
        self.speed(0)
        self.penup()

    def scoreboard(self):
        self.clear()
        self.goto(50,310)
        self.write(f"{self.player2_score}" , False , "center" , ("Arial" , 30 , "bold"))
        self.goto(-50,310)
        self.write(f"{self.player1_score}" , False , "center" , ("Arial" , 30 , "bold"))

    def player2_points(self):
        self.player2_score += 1
        self.scoreboard()

    def player1_points(self):
        self.player1_score += 1
        self.scoreboard()

    def won_game(self,winner):
        self.goto(-35,0)
        self.write(f"PLAYER {winner}    WON!" , False , "center" , ("Cambria" , 30 , "bold"))


    def game_logo(self):
        self.goto(-550,150)
        self.write("P" , False , "center" , ("Algerian" , 80 , "bold"))
        self.goto(-550,30)
        self.write("O" , False , "center" , ("Algerian" , 80 , "bold"))
        self.goto(-550, -90)
        self.write("N" , False , "center" , ("Algerian" , 80 , "bold"))
        self.goto(-550,-210)
        self.write("G" , False , "center" , ("Algerian" , 80 , "bold"))

        self.goto(550,150)
        self.write("G" , False , "center" , ("Algerian" , 80 , "bold"))
        self.goto(550,30)
        self.write("A" , False , "center" , ("Algerian" , 80 , "bold"))
        self.goto(550,-90)
        self.write("M" , False , "center" , ("Algerian" , 80 , "bold"))
        self.goto(550,-210)
        self.write("E" , False , "center" , ("Algerian" , 80 , "bold"))


    def game_player(self):
        self.goto(-300,310)
        self.write("PLAYER 1" , False , "center" , ("Calibri" , 30 , "bold"))
        self.goto(300,310)
        self.write("PLAYER 2" , False , "center" , ("Calibri" , 30 , "bold"))

    
