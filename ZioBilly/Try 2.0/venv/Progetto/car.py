import random
import numpy
import pygame
from Waypoint import Waypoint

nord = 1
sud = 2
est = 3
ovest = 4
cardinali = [nord, sud, est, ovest]
velMax = 50
frena = 0

class Car():
	#super().__init__()

	def __init__(self):

		self.entra = numpy.random.choice(cardinali, p=[0.25, 0.25, 0.25, 0.25])
		cardinali.remove(self.entra)
		self.direzione = numpy.random.choice(["DX", "SX"], p = [0.50, 0.50])
		if(self.direzione == "DX"):
			waypoint = Waypoint()
			self.waypoint = Waypoint.goDritto(waypoint, self.entra)
			print(self.waypoint)


Car()
