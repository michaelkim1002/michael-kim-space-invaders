from turtle import Turtle
from size import *
class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.block_healths = []
        self.hideturtle()
        self.create_blocks()
    def create_blocks(self):
        for x in range(-2,2):
            block = Turtle("square")
            block.color("lime")
            block.shapesize(1, 3)
            block.penup()
            block.goto((x*125)+62.5, -125)
            self.blocks.append(block)
            self.block_healths.append(3)





