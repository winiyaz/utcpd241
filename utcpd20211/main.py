# This is the second version of the code , being made here for further work

import time
from turtle import Screen

from snake import Snake

from food import Food
from score import Score

scn = Screen()
scn.setup(width=600, height=600)
scn.bgcolor("#020617")
scn.title("PussyJuices")
scn.tracer(0)

# Initialize classes from files
snake = Snake()
food = Food()
score = Score()

scn.listen()
scn.onkey(snake.up, "Up")
scn.onkey(snake.down, "Down")
scn.onkey(snake.left, "Left")
scn.onkey(snake.right, "Right")

# Print text on screen


game_is_on = True
while game_is_on:
	scn.update()
	time.sleep(0.1)
	snake.move()

	# Detect Collision of the snake with food
	if snake.head.distance(food) < 15:
		print('nom nom nom')
		food.refresh()
		snake.extend()
		score.increase_score()

	# Detect Collision with wall
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		score.reset()


	# Detect collision with tail
	for segment in snake.segments:
		if snake.head.distance(segment) < 10:
			pass
		elif snake.head.distance(segment) < 10:
			score.reset()
			snake.reset()



# --- #
scn.exitonclick()  # Exit on clic
# ---
