from turtle import Turtle
from random import randint

INITIAL_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
SNAKE_SPEED = 15

class Snake:
    def __init__(self):
       self.parts = []
       self.create_snake()
       self.head = self.parts[0]
    
    def create_snake(self):
        for part_position in INITIAL_POSITIONS:
            self.create_part(part_position)
    
    def create_part(self, position):
        new_part = Turtle(shape="square")
        new_part.penup()
        new_part.color("white")
        new_part.goto(position)
        self.parts.append(new_part)
    
    def increase_part(self):
        self.create_part(self.parts[-1].position())
    
    def move(self):
        for part in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[part - 1].xcor()
            new_y = self.parts[part - 1].ycor()
            self.parts[part].goto(new_x, new_y)
        self.head.forward(SNAKE_SPEED)
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.3, stretch_wid=0.3)
        self.speed("fastest")
        self.color("yellow")
        self.new_location()
        
    def new_location(self):
        new_x = randint(-280, 280)
        new_y = randint(-280, 280)
        self.goto(new_x, new_y)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__() 
        self.score = 0 
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setposition(0, 280)
        self.new_score()
    
    def new_score(self):
        text = f"Score : {self.score}"
        self.write(text, align="center", font=('Arial', 12, 'bold'))
    
    def increase_score(self):
        self.score += 1 
        self.clear()
        self.new_score()
    
    def gameover(self):
        text = f"Game Over!"
        self.setposition(0, -120)
        self.write(text, align="center", font=('Arial', 24, 'bold'))