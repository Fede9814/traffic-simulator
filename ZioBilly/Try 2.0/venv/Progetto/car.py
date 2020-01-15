import random
import numpy
import pygame
from pygame.math import *


nord = 1
sud = 2
est = 3
ovest = 4
cardinali = [nord, sud, est, ovest]
velMax = 50
frena = 0
arrayDritti = [(325, 0), (475, 600), (800, 225), (0, 375)]
arraySX = [(375, 0), (425, 600), (800, 275), (0, 325)]

class Car(pygame.sprite.Sprite):
	#super().__init__()

	def __init__(self):
		pygame.sprite.Sprite.__init__(self) 
		self.entra = numpy.random.choice(cardinali, p=[0.25, 0.25, 0.25, 0.25])
		self.direzione = numpy.random.choice(["SX", "DX"], p = [0.50, 0.50])

		self.image = pygame.image.load('C:/Users/PC/Desktop/traffic-simulator/ZioBilly/Try 2.0/venv/img/macchinina_brum_brum.png')
			# centro di massa della macchina

		if(self.direzione == "SX"): 
			token = 1
			for x in cardinali:
				if (x == cardinali[self.entra-1]):
					self.index = cardinali.index(token)
					pos = arraySX[self.index]
				token = token + 1

		if(self.direzione == "DX"): 
			token = 1
			for x in cardinali:
				if (x == cardinali[self.entra-1]):
					self.index = cardinali.index(token)
					pos = arrayDritti[self.index]
				token = token + 1

		
		self.rect = self.image.get_rect(center=pos)
		self.pos = Vector2(pos)

		if(self.index == 0):
			self.image = pygame.transform.rotate(self.image, 180)

		if(self.index == 1):
			self.image = pygame.transform.rotate(self.image, 0)

		if(self.index == 2):
			self.image = pygame.transform.rotate(self.image, 90)

		if(self.index == 3):
			self.image = pygame.transform.rotate(self.image, 270)


	def update(self):
		if(self.direzione == "DX"): 

			if(self.index == 0):
				self.pos.y += 1
				self.rect = self.image.get_rect(center=self.pos)
				if(self.pos.y == 600):
					self.kill()

			if(self.index == 1):
				self.pos.y -= 1
				self.rect = self.image.get_rect(center=self.pos)
				if(self.pos.y == 0):
					self.kill()

			if(self.index == 2):
				self.pos.x -= 1
				self.rect = self.image.get_rect(center=self.pos)
				if(self.pos.x == 0):
					self.kill()

			if(self.index == 3):
				self.pos.x += 1
				self.rect = self.image.get_rect(center=self.pos)
				if(self.pos.x == 800):
					self.kill()

		if(self.direzione == "SX"): 

			if(self.index == 0):
				if(self.pos.y < 325):
					self.pos.y += 1
					if(self.pos.y == 325):
						self.image = pygame.transform.rotate(self.image, 90)
						self.pos.x += 1
				else:
					self.pos.x += 1
				self.rect = self.image.get_rect(center=self.pos)
				if(self.pos.x == 800):
					self.kill()

			if(self.index == 1):
				if(self.pos.y > 275):
					self.pos.y -= 1
					if(self.pos.y == 275):
						self.image = pygame.transform.rotate(self.image, 90)
						self.pos.x -= 1
				else:
					self.pos.x -= 1
				self.rect = self.image.get_rect(center=self.pos)
				if(self.pos.x == 0):
					self.kill()

			if(self.index == 2):
				if(self.pos.x > 375):
					self.pos.x -= 1
					if(self.pos.x == 375):
						self.image = pygame.transform.rotate(self.image, 90)
						self.pos.y += 1
				else:
					self.pos.y += 1
				self.rect = self.image.get_rect(center=self.pos)
				if(self.pos.y == 600):
					self.kill()

			if(self.index == 3):
				if(self.pos.x < 425):
					self.pos.x += 1
					if(self.pos.x == 425):
						self.image = pygame.transform.rotate(self.image, 90)
						self.pos.y -= 1
				else:
					self.pos.y -= 1
				self.rect = self.image.get_rect(center=self.pos)
				if(self.pos.y == 0):
					self.kill()


