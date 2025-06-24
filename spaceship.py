from turtle import Turtle
from bullet import Bullet
import time
from size import *
class Spaceship(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("triangle")
        self.color("white")
        self.shapesize(1.2,1.2)
        self.setheading(90)
        self.penup()
        self.goto(position)
    def go_left(self):
        if self.xcor() >-(0.5 * width) + 50:
            new_x = self.xcor() - 25
            self.goto(new_x,self.ycor())
    def go_right(self):
        if self.xcor() < (width / 2) - 50:
            new_x = self.xcor() + 25
            self.goto(new_x, self.ycor() )



