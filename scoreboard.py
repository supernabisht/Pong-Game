from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,250)
        self.r_score=0
        self.l_score=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(200, 250)  # Right player's score position
        self.write(f"{self.r_score}", align="center", font=("Arial", 20, "normal"))
        self.goto(-200, 250)  # Left player's score position
        self.write(f"{self.l_score}", align="center", font=("Arial", 20, "normal"))

    def increase_r_score(self):

        self.r_score+=1
        self.update_score()
    def increase_l_score(self):

        self.l_score += 1
        self.update_score()