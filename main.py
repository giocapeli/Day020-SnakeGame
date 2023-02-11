from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score

SPEED = 0.3

s = Screen()
s.setup(600, 600)
s.bgcolor((0, 0, 0))
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
score = Score()

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
    time.sleep(SPEED)
    snake.move_forward()

    if snake.head.distance(food) < 15:
        score.increasse()
        food.refresh()
        snake.extend()
        SPEED -= 0.03 * score.score // 3
    
    for segment in snake.segments[1:]: #start the list in index 1 and go until last member
        if snake.head.distance(segment) < 5:
            score.game_over()
            game_over = True
    

s.exitonclick()