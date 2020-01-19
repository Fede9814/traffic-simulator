import random
import numpy
import pygame
from pygame.math import *


nord = 1
sud = 2
est = 3
ovest = 4
cardinali = [nord, sud, est, ovest]
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
			self.vision = self.image.get_rect(center=self.rect.midbottom)
			self.vision.height = 20
			self.vision.center = self.rect.midbottom

		if(self.index == 1):
			self.image = pygame.transform.rotate(self.image, 0)
			self.vision = self.image.get_rect(center=self.rect.midtop)
			self.vision.height = 20
			self.vision.center = self.rect.midtop

		if(self.index == 2):
			self.image = pygame.transform.rotate(self.image, 90)
			self.vision = self.image.get_rect(center=self.rect.midleft)
			self.vision.width = 20

		if(self.index == 3):
			self.image = pygame.transform.rotate(self.image, 270)
			self.vision = self.image.get_rect(center=self.rect.midright)
			self.vision.width = 20


	def update(self, passa_NS_DX, passa_EO_DX, passa_EO_SX, passa_NS_SX, cars):
		for brum in cars:
			if(brum.rect != self.rect):
				if(self.rect.colliderect(brum.rect) == True):
					self.kill()
					brum.kill()
					print("Incidente")
							
		if(self.direzione == "DX"):			
			if(self.index == 0):
				check = 0
				safe = 0
				for brum in cars:
					if(brum.rect != self.rect and brum.vision != self.vision):
						if(self.vision.colliderect(brum.rect) == True):
							check = 1
							safe = brum
							if(self.vision.colliderect(safe.rect) == False):
								check = 0
				if(check == 1):
					self.rect.center = (self.rect.center[0], self.rect.center[1])
				else:
					if(passa_NS_DX == False and self.rect.center[1] == 145):	
						self.rect.center = (self.rect.center[0], self.rect.center[1])
					else:
						self.rect.center = (self.rect.center[0], self.rect.center[1] + 1)
					self.rect = self.image.get_rect(center=self.rect.center)
					self.vision = self.image.get_rect(center=self.rect.midbottom)
					self.vision.height = 20
					self.vision.center = self.rect.midbottom
					if(self.rect.center[1] == 600):
						self.kill()

			if(self.index == 1):
				check = 0
				safe = 0
				for brum in cars:
					if(brum.rect != self.rect and brum.vision != self.vision):
						if(self.vision.colliderect(brum.rect) == True):
							check = 1
							safe = brum
							if(self.vision.colliderect(safe.rect) == False):
								check = 0
				if(check == 1):
					self.rect.center = (self.rect.center[0], self.rect.center[1])
				else:
					if(passa_NS_DX == False and self.rect.center[1] == 455):
						#self.pos.y -= 0
						self.rect.center = (self.rect.center[0], self.rect.center[1])
					else:
						#self.pos.y -= 1
						self.rect.center = (self.rect.center[0], self.rect.center[1] - 1)
					self.rect = self.image.get_rect(center=self.rect.center)
					self.vision = self.image.get_rect(center=self.rect.midtop)
					self.vision.height = 20
					self.vision.center = self.rect.midtop
					if(self.rect.center[1] == 0):
						self.kill()

			if(self.index == 2):
				check = 0
				safe = 0
				for brum in cars:
					if(brum.rect != self.rect and brum.vision != self.vision):
						if(self.vision.colliderect(brum.rect) == True):
							check = 1
							safe = brum
							if(self.vision.colliderect(safe.rect) == False):
								check = 0
				if(check == 1):
					self.rect.center = (self.rect.center[0], self.rect.center[1])
				else:
					if(passa_EO_DX == False and self.rect.center[0] == 555):
						self.rect.center = (self.rect.center[0], self.rect.center[1])
					else:
						self.rect.center = (self.rect.center[0] - 1, self.rect.center[1])
					self.rect = self.image.get_rect(center=self.rect.center)
					self.vision = self.image.get_rect(center=self.rect.midleft)
					self.vision.width = 20
					self.vision.center = self.rect.midleft
					if(self.rect.center[0] == 0):
						self.kill()

			if(self.index == 3):
				check = 0
				safe = 0
				for brum in cars:
					if(brum.rect != self.rect and brum.vision != self.vision):
						if(self.vision.colliderect(brum.rect) == True):
							check = 1
							safe = brum
							if(self.vision.colliderect(safe.rect) == False):
								check = 0
				if(check == 1):
					self.rect.center = (self.rect.center[0], self.rect.center[1])
				else:
					if(passa_EO_DX == False and self.rect.center[0] == 243):
						self.rect.center = (self.rect.center[0], self.rect.center[1])
					else:
						self.rect.center = (self.rect.center[0] + 1, self.rect.center[1])
					self.rect = self.image.get_rect(center=self.rect.center)
					self.vision = self.image.get_rect(center=self.rect.midright)
					self.vision.width = 20
					self.vision.center = self.rect.midright
					if(self.rect.center[0] == 800):
						self.kill()

		if(self.direzione == "SX"): 

			if(self.index == 0):
				check = 0
				safe = 0
				for brum in cars:
					if(brum.rect != self.rect and brum.vision != self.vision):
						if(self.vision.colliderect(brum.rect) == True):
							check = 1
							safe = brum
							if(self.vision.colliderect(safe.rect) == False):
								check = 0
				if(check == 1):
					self.rect.center = (self.rect.center[0], self.rect.center[1])
				else:
					if(passa_NS_SX == False and self.rect.center[1] == 145):
						self.rect.center = (self.rect.center[0], self.rect.center[1])
					else:
						if(self.rect.center[1] < 325):
							self.rect.center = (self.rect.center[0], self.rect.center[1] + 1)
							if(self.rect.center[1] == 325):
								self.image = pygame.transform.rotate(self.image, 90)
								self.rect.center = (self.rect.center[0]  + 1, self.rect.center[1])
						else:
							self.rect.center = (self.rect.center[0] + 1, self.rect.center[1])
				self.rect = self.image.get_rect(center=self.rect.center)
				if(self.rect.center[1] < 325):
					self.vision = self.image.get_rect(center=self.rect.midbottom)
					self.vision.height = 20
					self.vision.center = self.rect.midbottom
				else:
					self.vision = self.image.get_rect(center=self.rect.midright)
					self.vision.width = 20
					self.vision.center = self.rect.midright
				if(self.rect.center[0] == 800):
					self.kill()

			if(self.index == 1):
				check = 0
				safe = 0
				for brum in cars:
					if(brum.rect != self.rect and brum.vision != self.vision):
						if(self.vision.colliderect(brum.rect) == True):
							check = 1
							safe = brum
							if(self.vision.colliderect(safe.rect) == False):
								check = 0
				if(check == 1):
					self.rect.center = (self.rect.center[0], self.rect.center[1])
				else:
					if(passa_NS_SX == False and self.rect.center[1] == 455):
						self.rect.center = (self.rect.center[0], self.rect.center[1])
					else:
						if(self.rect.center[1] > 275):
							self.rect.center = (self.rect.center[0], self.rect.center[1] - 1)
							if(self.rect.center[1] == 275):
								self.image = pygame.transform.rotate(self.image, 90)
								self.rect.center = (self.rect.center[0] - 1, self.rect.center[1])
						else:
							self.rect.center = (self.rect.center[0] - 1, self.rect.center[1])
				self.rect = self.image.get_rect(center=self.rect.center)
				if(self.rect.center[1] > 275):
					self.vision = self.image.get_rect(center=self.rect.midtop)
					self.vision.height = 20
					self.vision.center = self.rect.midtop
				else:
					self.vision = self.image.get_rect(center=self.rect.midleft)
					self.vision.width = 20
					self.vision.center = self.rect.midleft
				if(self.rect.center[0] == 0):
					self.kill()

			if(self.index == 2):
				check = 0
				safe = 0
				for brum in cars:
					if(brum.rect != self.rect and brum.vision != self.vision):
						if(self.vision.colliderect(brum.rect) == True):
							check = 1
							safe = brum
							if(self.vision.colliderect(safe.rect) == False):
								check = 0
				if(check == 1):
					self.rect.center = (self.rect.center[0], self.rect.center[1])
				else:
					if(passa_EO_SX == False and self.rect.center[0] == 555):
						self.rect.center = (self.rect.center[0], self.rect.center[1])
					else:
						if(self.rect.center[0] > 375):
							self.rect.center = (self.rect.center[0] - 1, self.rect.center[1])
							if(self.rect.center[0] == 375):
								self.image = pygame.transform.rotate(self.image, 90)
								self.rect.center = (self.rect.center[0], self.rect.center[1] + 1)
						else:
							self.rect.center = (self.rect.center[0], self.rect.center[1] + 1)
				self.rect = self.image.get_rect(center=self.rect.center)
				if(self.rect.center[0] > 375):
					self.vision = self.image.get_rect(center=self.rect.midleft)
					self.vision.width = 20
					self.vision.center = self.rect.midleft
				else:
					self.vision = self.image.get_rect(center=self.rect.midbottom)
					self.vision.height = 20
					self.vision.center = self.rect.midbottom
				if(self.rect.center[1] == 600):
					self.kill()

			if(self.index == 3):
				check = 0
				safe = 0
				for brum in cars:
					if(brum.rect != self.rect and brum.vision != self.vision):
						if(self.vision.colliderect(brum.rect) == True):
							check = 1
							safe = brum
							if(self.vision.colliderect(safe.rect) == False):
								check = 0
				if(check == 1):
					self.rect.center = (self.rect.center[0], self.rect.center[1])
				else:
					if(passa_EO_SX == False and self.rect.center[0] == 243):
						self.rect.center = (self.rect.center[0], self.rect.center[1])
					else:
						if(self.rect.center[0] < 425):
							self.rect.center = (self.rect.center[0] + 1, self.rect.center[1])
							if(self.rect.center[0] == 425):
								self.image = pygame.transform.rotate(self.image, 90)
								self.rect.center = (self.rect.center[0], self.rect.center[1] - 1)
						else:
							self.rect.center = (self.rect.center[0], self.rect.center[1] - 1)
				self.rect = self.image.get_rect(center=self.rect.center)
				if(self.rect.center[0] < 425):
					self.vision = self.image.get_rect(center=self.rect.midright)
					self.vision.width = 20
					self.vision.center = self.rect.midright
				else:
					self.vision = self.image.get_rect(center=self.rect.midtop)
					self.vision.height = 20
					self.vision.center = self.rect.midtop
				if(self.rect.center[1] == 0):
					self.kill()


