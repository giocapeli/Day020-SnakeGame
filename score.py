from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update()
        self.hideturtle()
        
    def increasse(self):
        self.score += 1
        self.update()
    
    def update(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', move=False, align='center', font=('Arial', 16, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f'GAME OVER', move=False, align='center', font=('Arial', 20, 'normal'))

