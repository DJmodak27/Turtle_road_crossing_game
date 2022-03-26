from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.goto(x=-280, y=250)
        self.update_score()
    def update_score(self):
        self.write(f"Level : {self.score}", move=False, align= "left", font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGN, font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
