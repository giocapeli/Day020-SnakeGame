from turtle import Turtle, Screen
import time

start_positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        
    def create_snake(self):
        for position in start_positions:
            snake_piece = Turtle("square")
            snake_piece.penup()
            snake_piece.color("red")
            snake_piece.goto(position)
            self.segments.append(snake_piece)
            
            
    def move_foward(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        if self.segments[0].xcor() > 300:
            self.segments[0].goto(-300, new_y)
        if self.segments[0].ycor() > 300:
            self.segments[0].goto(new_x, -300)
        if self.segments[0].xcor() < -300:
            self.segments[0].goto(300, new_y)
        if self.segments[0].ycor() < -300:
            self.segments[0].goto(new_x, 300)

        self.segments[0].forward(MOVE_DISTANCE)
            
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)      
            
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)     
              
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)       
            
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)