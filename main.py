from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time
from pygame import mixer


# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("pong game")
screen.bgcolor("black")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()

scoreboard = Scoreboard()


POSITIONS = [(0, 280), (0, 240), (0, 200), (0, 160), (0, 120), (0, 80), (0, 40),
             (0, 0), (0, -40), (0, -80), (0, -120), (0, -160), (0, -200), (0, -240), (0, -280)]

for position in POSITIONS:
    square = Turtle("circle")
    square.goto(position)
    square.color("white")


# # If keys are pressed
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

mixer.init()
song = "C:/Users/tomer/Downloads/onlymp3.to - Popcorn Remix [HD]-I3sKIV6KugA-192k-1654122869483.mp3"
mixer.Channel(1).play(mixer.Sound(song))
mixer.music.set_volume(0.2)


while scoreboard.left_score < 10 and scoreboard.right_score < 10:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with the upper or downer wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        mixer.music.load("C:/Users/tomer/Downloads/click-button-140881.mp3")
        mixer.music.play()

        mixer.music.play()

    # Detect if ball missed right paddle.
    if ball.xcor() > 380:
        scoreboard.increase_left_score()
        ball.reset_position()
    # Detect if ball missed left paddle.
    if ball.xcor() < -380:
        scoreboard.increase_right_score()
        ball.reset_position()

scoreboard.game_over()
screen.exitonclick()
