import turtle
from turtle import Turtle,Screen
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick
import time

screen=Screen()
screen.title("Build Pong")
screen.setup(width=800,height=600)
screen.bgcolor("pink")
turtle.tracer(0) #hides the animation of movement of brick from center to the given place


pong=Ball()
score=Scoreboard()

r_brick=Brick(350,0)
l_brick=Brick(-350,0)


screen.listen()
screen.onkey(r_brick.up,"Up")
screen.onkey(r_brick.down,"Down")

screen.onkey(l_brick.up,"W")
screen.onkey(l_brick.down,"S")

game_is_on=True

while game_is_on:
    turtle.update() #shows the animation after the bricks are at their places
    time.sleep(pong.move_speed)
    pong.move_the_pong()

    #detect collision with walls
    if pong.ycor()>280 or pong.ycor()<-280:
        pong.bounce_y()


    #detect collision with brick:
    if pong.distance(r_brick)<50 and pong.xcor()>320 or pong.distance(l_brick)<50 and pong.xcor()<-320 :
# the "pong.xcor()" is when ball is at the top or bottom edge of the brick where the distance between them is more than 50
        pong.bounce_x()


    #if right brick misses the ball:
    if pong.xcor()>390:
        pong.reset_the_pong()
        score.increase_l_score()


    #if left brick misses the ball:
    if pong.xcor()<-390:
        pong.reset_the_pong()
        score.increase_r_score()

screen.exitonclick()