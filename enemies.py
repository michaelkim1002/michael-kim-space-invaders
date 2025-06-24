from turtle import Turtle
from size import *
class Enemies(Turtle):
    def __init__(self):
        super().__init__()
        self.enemies = []
        self.enemy_tags = []
        self.hideturtle()
        self.create_enemies()
        self.goto(0,150)
        self.speed = 2
    def create_enemies(self):
        for x in range(-6,6):
            for y in range(0,5):
                enemy = Turtle("turtle")
                enemy.setheading(-90)
                enemy.penup()
                enemy.shapesize(1.25,1.25)
                enemy.goto(x * 35, (y*35)+70)
                self.enemies.append(enemy)
                if y < 2:
                    enemy.color("orange")
                    self.enemy_tags.append(1)
                elif 2 <= y < 4:
                    enemy.color("magenta")
                    self.enemy_tags.append(2)
                else:
                    enemy.color("purple")
                    self.enemy_tags.append(3)
    def move(self):
        for enemy in self.enemies:
            new_x = enemy.xcor() + self.speed
            enemy.goto(new_x, enemy.ycor())
    def go_down(self):
        for enemy in self.enemies:
            new_y = enemy.ycor() - 5
            enemy.goto(enemy.xcor(), new_y)











