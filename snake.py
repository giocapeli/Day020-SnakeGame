from turtle import Turtle, Screen
import time

start_positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in start_positions:
            self.add_segment(position)

    def move_forward(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        if self.head.xcor() > 290:
            self.head.goto(-290, new_y)
        if self.head.ycor() > 290:
            self.head.goto(new_x, -290)
        if self.head.xcor() < -290:
            self.head.goto(290, new_y)
        if self.head.ycor() < -290:
            self.head.goto(new_x, 290)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

        
    def add_segment(self, position):
        snake_piece = Turtle("square")
        snake_piece.penup()
        snake_piece.color("red")
        snake_piece.goto(position)
        self.segments.append(snake_piece)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def reset(self):
        for seg in self.segments:
            seg.goto(600, 600)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]