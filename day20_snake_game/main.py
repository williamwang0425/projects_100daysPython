# Day 20 Snake Game
# Step 1: Create a snake body
# Step 2: Move the snake, control the snake
# Step 3: Create snake food
# Step 4: Detect collision with food
# Step 5: Create a scoreboard
# Step 6: Detect collision with wall
# Step 7: Detect collision with tail

from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

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
        print("food is refreshed!")





screen.exitonclick()
