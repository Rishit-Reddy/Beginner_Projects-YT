from turtle import Screen
from time import sleep
from snake import Snake, Food, ScoreBoard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="Snake Game")

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    
    
    
    if snake.head.distance(food) < 10:
        food.new_location()
        snake.increase_part()
        score.increase_score()
    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        score.gameover() 
        game_on = False
    
    for part in snake.parts[1:]:
        if snake.head.distance(part)< 10:
            score.gameover()
            game_on = False
            
screen.exitonclick()
