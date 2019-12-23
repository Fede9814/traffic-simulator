import pygame


arrayDritti = [(325, 0), (475, 600), (800, 225), (0, 375)]
arraySX = [(375, 0), (425, 600), (800, 275), (0, 325)]

class Waypoint():
	def __init__(self):
		self.arraySX = []
		self.arrayDXdri = []
		self.arrayDXdex = []
		
		for x in arrayDritti:
			print(x[0], x[1])
			if((x[0] % 2) == 0):
				if(x[0] == 0):
					arrayToken = []
					for i in range(800):
						arrayToken.append([i, x[1]])
						print(arrayToken)
					self.arrayDXdri.append(arrayToken)
				else:
					token = x[0]
					arrayToken = []
					while token != 0:
						arrayToken.append([token, x[1]])
						token = token - 1
					self.arrayDXdri.append(arrayToken)

			if((x[1] % 2) == 0):
				if(x[1] == 0):
					arrayToken = []
					for i in range(600):
						arrayToken.append([x[0], i])
					self.arrayDXdri.append(arrayToken)
				else:
					token = x[1]
					arrayToken = []
					while token != 0:
						arrayToken.append([x[0], token])
						token = token - 1
					self.arrayDXdri.append(arrayToken)

	def 

Waypoint()