from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from brick import BrickWall
from scoreboard import ScoreBoard
import time

# Screen Setup

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("BRICKOUT")
screen.tracer(0)

paddle = Paddle((0, -250))
ball = Ball()

brick_wall = BrickWall()
brick_wall.make_wall()

scoreboard = ScoreBoard()
scoreboard.update_scoreboard()

# Key Commands

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")


#The Game

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Increase Speed?
    if ball.bounce_counter % 10 == 0 and ball.bounce_counter != 0:
        ball.move_speed *= 0.99

    # Bounce off Paddle
    if ball.distance(paddle) < 30:
        ball.bounce_y()

    # Bounce off Border
    if ball.xcor() < -380 or ball.xcor() > 380:
        ball.bounce_x()
    if ball.ycor() > 280:
        ball.bounce_y()


    # Gutter Ball
    if ball.ycor() < -280:
        scoreboard.decrease_score()
        ball.reset_position()

    # Hit a Brick
    for brick in brick_wall.bricks:
        if ball.distance(brick) < 30 and brick.is_bouncy == True:
            if (ball.ycor() < brick.ycor()-3) or (ball.ycor() > brick.ycor()+3):
                ball.bounce_y()
                brick_wall.delete_brick(brick_wall.bricks.index(brick))
                scoreboard.increase_score()
            else:
                ball.bounce_x()
                brick_wall.delete_brick(brick_wall.bricks.index(brick))
                scoreboard.increase_score()


    #See if game is over
    true_bricks = 0
    for brick in brick_wall.bricks:
        if brick.is_bouncy == True:
            true_bricks += 1
    if true_bricks == 0:
        game_is_on == False




screen.exitonclick()
