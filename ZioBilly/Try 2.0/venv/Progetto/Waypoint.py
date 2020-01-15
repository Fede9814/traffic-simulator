import pygame

arrayDritti = [(325, 0), (475, 600), (800, 225), (0, 375)]
arraySX = [(375, 0), (425, 600), (800, 275), (0, 325)]
nord = 1
sud = 2
est = 3
ovest = 4
cardinali = [nord, sud, est, ovest]

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

	def goDritto (self, spawnPT):
		token = 1
		for x in cardinali:
			if(x == spawnPT):
				index = cardinali.index(token)
				waypoint = self.arrayDXdri[index]
				return waypoint
			token = token + 1
			
