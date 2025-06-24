from turtle import Turtle, Screen
import time
from size import *
from spaceship import Spaceship
from bullet import Bullet
from wall import Wall
from enemies import Enemies
from tracker import Tracker
import random

screen = Screen()
screen.setup(width = width, height = height)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

title = Turtle()
title.penup()
title.goto(280,-290)
title.color("white")
title.write("Space Invaders", align="Right", font=("Tiny5", 30, "bold"))
title.hideturtle()

spaceship = Spaceship((0,-200))

bullet = Bullet()
enemy_bullet = Bullet()
enemy_bullet.color("red")

wall = Wall()
enemies = Enemies()
tracker = Tracker()

screen.listen()
screen.onkeypress(spaceship.go_left,"Left")
screen.onkeypress(spaceship.go_right,"Right")

def shoot():
    if not bullet.fired:
        bullet.fired = True
        bullet.goto(spaceship.xcor(), spaceship.ycor()+15)
def game_is_over():
    game_over = Turtle()
    game_over.color("red")
    game_over.write("GAME OVER", align="center", font=("Tiny5", 30, "bold"))

def reset_bullet():
    bullet.goto(0, 1000)
    bullet.fired = False

def reset_enemy_bullet():
    enemy_bullet.goto(-1000, -1000)
    enemy_bullet.fired = False

screen.onkeypress(shoot,"space")

game_on = True
while game_on:
    time.sleep(0.075)
    screen.update()
    enemies.move()
    for enemy in enemies.enemies:
        if enemy.xcor() >= (width/2)-50 or (((-1 * width) / 2) + 50 >= enemy.xcor() > -800):
            enemies.go_down()
            enemies.speed *= -1
            break
        if random.randint(1, 10) < 5 and not enemy_bullet.fired:
            enemy_bullet.goto(random.choice(enemies.enemies).xcor(), random.choice(enemies.enemies).ycor())
            enemy_bullet.fired = True
        if (spaceship.ycor()+40 >= enemy.ycor() > -1000) and enemy.distance(spaceship)<40:
            game_is_over()
            game_on = False
            break

    if enemy_bullet.fired:
        enemy_bullet.sety(enemy_bullet.ycor() - 25)
        if enemy_bullet.ycor() <= (-1*height)/2:
            reset_enemy_bullet()
        if enemy_bullet.distance(spaceship)<25 and enemy_bullet.ycor() <= spaceship.ycor():
            reset_enemy_bullet()
            tracker.lose_life()
            if tracker.lives == 0:
                game_is_over()
                game_on = False
        for block in range(len(wall.blocks)):
            if enemy_bullet.distance(wall.blocks[block]) < 35 and enemy_bullet.ycor() <= wall.blocks[block].ycor():
                reset_enemy_bullet()
                if wall.block_healths[block] == 3:
                    wall.blocks[block].color("yellow")
                    wall.block_healths[block] -= 1
                elif wall.block_healths[block] == 2:
                    wall.blocks[block].color("red")
                    wall.block_healths[block] -= 1
                else:
                    wall.blocks[block].goto(0,-1000)

    if bullet.fired:
        bullet.sety(bullet.ycor() + 25)
        if bullet.ycor() >= height/2:
            reset_bullet()
        for enemy in range(len(enemies.enemies)):
            if bullet.distance(enemies.enemies[enemy])<27 and bullet.ycor() >= enemies.enemies[enemy].ycor():
                reset_bullet()
                tracker.increase_kills()
                enemies.enemies[enemy].goto(0,-1000)
                if enemies.enemy_tags[enemy] == 1:
                    tracker.increase_score(20)
                elif enemies.enemy_tags[enemy] == 2:
                    tracker.increase_score(40)
                else:
                    tracker.increase_score(60)
                if tracker.kill_count % 60 == 0:
                    temp = enemies.speed
                    tracker.increase_round()
                    if tracker.round > 3:
                        winner = Turtle()
                        winner.color("lime")
                        winner.write("WINNER", align="center", font=("Tiny5", 30, "bold"))
                        game_on = False
                    wall = Wall()
                    enemies = Enemies()
                    reset_bullet()
                    reset_enemy_bullet()
                    enemies.speed = temp + 0.5

        for block in range(len(wall.blocks)):
            if bullet.distance(wall.blocks[block]) < 30 and bullet.ycor() >= wall.blocks[block].ycor():
                reset_bullet()
                if wall.block_healths[block] == 3:
                    wall.blocks[block].color("yellow")
                    wall.block_healths[block] -= 1
                elif wall.block_healths[block] == 2:
                    wall.blocks[block].color("red")
                    wall.block_healths[block] -= 1
                else:
                    wall.blocks[block].goto(0,-1000)

screen.exitonclick()