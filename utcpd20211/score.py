# Setting up the scoreboard

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Score(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		self.color("#FFC700")
		self.penup()
		self.goto(0, 265)
		self.hideturtle()
		self.update_score()

	def update_score(self):
		"""Updating score function"""
		self.write(f'Score : {self.score}', align=ALIGNMENT, font=FONT)

	def increase_score(self):
		"""Increment Score"""
		self.score += 1
		self.clear()
		self.update_score()

	def game_over(self):
		"""GameOver"""
		self.goto(0, 0)
		self.write(f'GAMEOVER!', align=ALIGNMENT, font=FONT)
