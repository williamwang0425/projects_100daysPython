# Day 20 Snake Game
# Step 1: Create a snake body
# Step 2: Move the snake, control the snake
# Step 3: Create snake food
# Step 4: Detect collision with food
# Step 5: Create a scoreboard
# Step 6: Detect collision with wall
# Step 7: Detect collision with tail

# Learning Goals:
# 1. OOP
# 2. Inheritance
# 3. Slicing lists and tuples (e.g. print(piano_keys[2:5]) => print 3,4,5.

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 0:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
