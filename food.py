from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.refresh()
        
    def refresh(self):
        self.goto(random.randint(-260, 260), random.randint(-280, 280))