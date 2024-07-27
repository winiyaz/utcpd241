# 188 - from snk1 organize code by pussystink
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Coordinate positions
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
	"""Creates a snake with 3 squares and new starting positons"""

	def __init__(self):
		"""Create the snake which is squares from turtle"""
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]

	def create_snake(self):
		"""Setting the shape and color"""
		for pos in STARTING_POSITIONS:
			self.add_segment(pos)

	def add_segment(self, position):
		new_seg = Turtle("square")
		new_seg.speed("fast")
		new_seg.color("#db2777")
		new_seg.penup()
		new_seg.goto(position)
		self.segments.append(new_seg)

	def extend(self):
		"""Add new segment to snake"""
		self.add_segment(self.segments[-1].position())

	def move(self):
		"""Moving the squares"""
		for seg_num in range(len(self.segments) - 1, 0, -1):
			new_x = self.segments[seg_num - 1].xcor()
			new_y = self.segments[seg_num - 1].ycor()
			self.segments[seg_num].goto(new_x, new_y)
		self.head.forward(MOVE_DISTANCE)

	def up(self):
		"""Press UP key"""
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		"""Press DOWN Key """
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		"""Press RIGHT key"""
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def right(self):
		"""Press LEFT key"""
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)