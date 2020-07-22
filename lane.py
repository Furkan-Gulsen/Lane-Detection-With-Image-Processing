# IMPORT THE NECESSARY LIBRARIES
import numpy as np
import cv2

class Lane:
	def __init__(self,x1,y1,x2,y2):
		"""
		Here, setted up the coordinates of the two different points of the lane.
		(x1,y1) (x2,y2)
		"""
		self.x1 = np.float32(x1)
		self.y1 = np.float32(y1)
		self.x2 = np.float32(x2)
		self.y2 = np.float32(y2)

		# Find the slope of the lane using the coordinates of the two points
		self.slope = self.calculate_slope()

		# Finding the coefficient of the lane using coordinates and slope
		self.bias = self.calculate_bias()

	def calculate_slope(self):
		return (self.y2 - self.y1) / (self.x2 - self.x1)

	def calculate_bias(self):
		return self.y1 - self.slope * self.x1

	def get_coordinates(self):
		return np.array([self.x1, self.y1, self.x2, self.y2])

	def set_coordinates(self):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = x2

	def draw(self, img, color=[255, 0, 0], thickness=8):
		cv2.line(img, (self.x1, self.y1), (self.x2, self.y2), color, thickness)

	