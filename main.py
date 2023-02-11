from turtle import Turtle, Screen
import time
from snake import Snake


s = Screen()
s.setup(600, 600)
s.bgcolor((0, 0, 0))
s.title("Snake Game")
s.tracer(0)

snake = Snake()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.right, "Right")
s.onkey(snake.left, "Left")

game_over = False
def turn(angle):
    snake[0].right(angle)


while not game_over:
    s.update()
    time.sleep(0.1)
    snake.move_forward()

    
    

s.exitonclick()