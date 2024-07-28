# Setting up the scoreboard

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Score(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0

		with open("panty.smell") as pussy:
			self.high_score = int(pussy.read())

		self.color("#FFC700")
		self.penup()
		self.goto(0, 265)
		self.hideturtle()
		self.update_score()

	def update_score(self):
		"""Updating score function"""
		self.clear()
		self.write(f'Score : {self.score} HiScore: {self.high_score}', align=ALIGNMENT, font=FONT)

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
			with open("panty.smell", mode="w") as pussy:
				pussy.write(f"{self.high_score}")
		self.score = 0
		self.update_score()

	def increase_score(self):
		"""Increment Score"""
		self.score += 1
		self.update_score()

	def game_over(self):
		"""GameOver"""
		self.goto(0, 0)
		self.write(f'GAMEOVER!', align=ALIGNMENT, font=FONT)
