from turtle import Turtle,Screen

ALIGN="center"
FONT=("Courier",25,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score=0
        self.l_score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.goto(-200, 250)
        self.write(f"{self.l_score}", align=ALIGN, font=FONT)
        self.goto(200, 250)
        self.write(f"{self.r_score}", align=ALIGN, font=FONT)
    def increase_r_score(self):
        self.r_score+=1
        self.clear()
        self.update_scoreboard()

    def increase_l_score(self):
        self.l_score+=1
        self.clear()
        self.update_scoreboard()