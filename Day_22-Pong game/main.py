# from turtle import Screen
# from paddle import Paddle
# from ball import Ball
# import time
# from scoreboard import Scoreboard

# screen=Screen()

# screen.bgcolor("black")
# screen.setup(width=800,height=600)
# screen.title("Pong")
# screen.tracer(0)

# paddle_r=Paddle((350,0))
# paddle_l=Paddle((-350,0))
# ball=Ball()
# score=Scoreboard()

# screen.listen()
# screen.onkey(paddle_r.move_up,"Up")
# screen.onkey(paddle_r.move_down,"Down")
# screen.onkey(paddle_l.move_up,"w")
# screen.onkey(paddle_l.move_down,"s")

# game_on=True
# while game_on:
#     time.sleep(ball.move_speed)
#     screen.update()
#     ball.move()

#     if ball.ycor()>280 or ball.ycor()<-280:
#         ball.bounce_y()

#     if ball.distance(paddle_r)<50 and ball.xcor()>320 or ball.distance(paddle_l)<50 and ball.xcor()<-320:
#         ball.bounce_x()

#     if ball.xcor()>380:
#         ball.reset_position()
#         score.l_point()
    
#     if ball.xcor()<-380:
#        ball.reset_position()
#        score.r_point()



# screen.exitonclick()


from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()