from turtle import Turtle
from size import *
class Tracker(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.round = 1
        self.score = 0
        self.lives = 5
        self.goto(0,height/2.5)
        self.update_score()
        self.kill_count = 0
    def increase_kills(self):
        self.kill_count += 1
    def increase_round(self):
        self.round += 1
        self.update_score()
    def increase_score(self, points):
        self.score += points
        self.update_score()
    def lose_life(self):
        self.lives-=1
        self.update_score()
    def update_score(self):
        self.clear()
        self.color("aqua")
        self.write(f"Round: {self.round}\t\t\t\t ", align="center", font=("Tiny5", 20, "bold"))
        self.color("royal blue")
        self.write(f"Score: {self.score}", align="center",font=("Tiny5", 20, "bold"))
        self.color("yellow")
        self.write(f"\t\t\tLives: {self.lives}", align="center",font=("Tiny5", 20, "bold"))


