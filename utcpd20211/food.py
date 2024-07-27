# Food rendering logic here

import random as rp
from turtle import Turtle


class Food(Turtle):
	def __init__(self):
		"""Place food at random coordintes within window"""
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_len=0.5, stretch_wid=0.5)
		self.color("#FFFF80")
		self.speed("fastest")
		self.refresh()

	def refresh(self):
		"""Refresh screen to score gets updates"""
		random_x = rp.randint(-240, 240)
		random_y = rp.randint(-240, 240)
		self.goto(random_x, random_y)
