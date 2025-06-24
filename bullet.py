from turtle import Turtle
import time
class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1.25,0.3)
        self.reset_position()
        self.fired = False
    def reset_position(self):
        self.goto(0,-1000)




