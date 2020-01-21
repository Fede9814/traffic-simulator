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
	#Inizializzazione del mezzo
	def __init__(self):
		pygame.sprite.Sprite.__init__(self) 
		self.entra = numpy.random.choice(cardinali, p=[0.25, 0.25, 0.25, 0.25])
		self.direzione = numpy.random.choice(["SX", "DX"], p = [0.50, 0.50])
		self.colore = numpy.random.choice([1, 2, 3, 4], p=[0.25, 0.25, 0.25, 0.25])
		
		
		if(self.colore == 1):
			self.image = pygame.image.load('A:/DAM/Traffico/ZioBilly/Try 2.0/venv/img/macchinina_brum_brum.png')
		elif(self.colore == 2):
			self.image = pygame.image.load('A:/DAM/Traffico/ZioBilly/Try 2.0/venv/img/macchinina_brum_brum1.png')
		elif(self.colore == 3):
			self.image = pygame.image.load('A:/DAM/Traffico/ZioBilly/Try 2.0/venv/img/macchinina_brum_brum2.png')
		elif(self.colore == 4):
			self.image = pygame.image.load('A:/DAM/Traffico/ZioBilly/Try 2.0/venv/img/macchinina_brum_brum3.png')

			#Dichiarazione punto di spawn a seconda del valore uscito casualmente
		if(self.direzione == "SX"): 
				#Cerca l'indice nell'array corrispondente al punto cardinale uscito, da li cerca allo stesso indice dell'array contenente i punti di spawn 
				#tutti gli array hanno un ordinamento rispetto ai numeri cardinali cioe "0 = Nord" "1 = Sud" "2 = Est" "3 = Ovest"
			token = 1
			for x in cardinali:
				if (x == cardinali[self.entra-1]):
					self.index = cardinali.index(token)
					pos = arraySX[self.index]
				token = token + 1

		if(self.direzione == "DX"): 
			self.dir = numpy.random.choice(["DR", "DX"], p = [0.50, 0.50])

		if(self.direzione == "DX"): 
			token = 1
			for x in cardinali:
				if (x == cardinali[self.entra-1]):
					self.index = cardinali.index(token)
					pos = arrayDritti[self.index]
				token = token + 1

			#Crea un rettangolo grande quanto la grandezza dell'immagine
		self.rect = self.image.get_rect(center=pos)
		
		self.pos = Vector2(pos)

			#A seconda del punto di spawn ruota l'immagine e crea l'area di trigger di fronte alla vettura
		if(self.index == 0):
			self.image = pygame.transform.rotate(self.image, 180)
				#l'area visiva viene piazzata dove l'immagine è rivolta per andare avanti
			self.vision = self.image.get_rect(center=self.rect.midbottom)
				#viene ridotta la sua grandezza
			self.vision.height = 20
				#se non viene aggiornato il centro di congiunzione tra la macchina e l'area di trigger questa rischia di essere scollegata dalla macchina
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


	def update(self, passa_N, passa_S, passa_E, passa_O, cars):

			#Controllo se avviene una collisione nell'incrocio tra 1 o piu macchine
		for brum in cars:
			if(brum.rect != self.rect):
				if(self.rect.colliderect(brum.rect) == True):
					self.kill()
					brum.kill()
					print("Incidente")
			#Controllo per il movimento di tutte le macchine che si trovano in ogni corsia di Destra				
		if(self.direzione == "DX"):			
			if(self.index == 0):
				check = 0
				safe = 0
					#Passo in rassegna la lista contenente tutti gli sprite, cioè tutte le macchine precedentemente create
				for brum in cars:
						#viene controllato che ogni macchina non controlli le collisione con se stessa altrimenti sarebbe sempre in True
					if(brum.rect != self.rect and brum.vision != self.vision):
							#se all'interno del ciclo viene segnalata l'esistenza di una collisione tra l'area di trigger (vision) e il rettangolo costruito sull'immagine
							#di un'altra macchina questa  blocca il passaggio al resto del codice che permette il movimento del mezzo bloccandola sul punto in cui si trova
						if(self.vision.colliderect(brum.rect) == True):
							check = 1
							safe = brum
								#viene salvata però la macchina con cui ha avuto l'ultima collisione e nel caso non vi siano altre collisioni con essa la macchina puo cominciare a muoversi
							if(self.vision.colliderect(safe.rect) == False):
								check = 0
				if(check == 1):
					self.rect.center = (self.rect.center[0], self.rect.center[1])
				else:
						#Controllo del semaforo, se la macchina supera il punto stabilito prima che il semaforo diventi giallo allora puo passare
					if(passa_N == False and self.rect.center[1] == 160):	
						self.rect.center = (self.rect.center[0], self.rect.center[1])
					else:
						if(self.dir == "DX"):
							if(self.rect.center[1] < 225):
								self.rect.center = (self.rect.center[0], self.rect.center[1] + 1)
								if(self.rect.center[1] == 225):
									self.image = pygame.transform.rotate(self.image, 270)
									self.rect.center = (self.rect.center[0] - 1, self.rect.center[1])
							else:
								self.rect.center = (self.rect.center[0] - 1, self.rect.center[1])
						else:
							#Permette il movimento del veicolo, sposta il punto di centro del rettangolo incrementandolo o decrementandolo
							self.rect.center = (self.rect.center[0], self.rect.center[1] + 1)
						#Sostituisce il vecchio rettangolo grazie al nuovo punto centrale
					self.rect = self.image.get_rect(center=self.rect.center)
						#Aggiorna il campo visivo con uno nuovo
					if(self.dir == "DX" and self.rect.center[1] == 225):
						self.vision = self.image.get_rect(center=self.rect.midleft)
						self.vision.height = 20
						self.vision.center = self.rect.midleft
					else:
						self.vision = self.image.get_rect(center=self.rect.midbottom)
						self.vision.height = 20
						self.vision.center = self.rect.midbottom
					if(self.dir == "DX" and self.rect.center[0] == 0):
						self.kill()
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
					if(passa_S == False and self.rect.center[1] == 440):
						self.rect.center = (self.rect.center[0], self.rect.center[1])
					else:
						if(self.dir == "DX"):
							if(self.rect.center[1] > 375):
								self.rect.center = (self.rect.center[0], self.rect.center[1] - 1)
								if(self.rect.center[1] == 375):
									self.image = pygame.transform.rotate(self.image, 270)
									self.rect.center = (self.rect.center[0] + 1, self.rect.center[1])
							else:
								self.rect.center = (self.rect.center[0] + 1, self.rect.center[1])
						else:
							self.rect.center = (self.rect.center[0], self.rect.center[1] - 1)
					self.rect = self.image.get_rect(center=self.rect.center)
					
					if(self.dir == "DX" and self.rect.center[1] == 375):
						self.vision = self.image.get_rect(center=self.rect.midright)
						self.vision.height = 20
						self.vision.center = self.rect.midright
					else:
						self.vision = self.image.get_rect(center=self.rect.midtop)
						self.vision.height = 20
						self.vision.center = self.rect.midtop
					if(self.dir == "DX" and self.rect.center[1] == 0):
						self.kill()
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
					if(passa_E == False and self.rect.center[0] == 540):
						self.rect.center = (self.rect.center[0], self.rect.center[1])
					else:
						if(self.dir == "DX"):
							if(self.rect.center[0] > 475):
								self.rect.center = (self.rect.center[0] - 1, self.rect.center[1])
								if(self.rect.center[0] == 475):
									self.image = pygame.transform.rotate(self.image, 270)
									self.rect.center = (self.rect.center[0], self.rect.center[1] - 1)
							else:
								self.rect.center = (self.rect.center[0], self.rect.center[1] - 1)
						else:
							self.rect.center = (self.rect.center[0] - 1, self.rect.center[1])
					self.rect = self.image.get_rect(center=self.rect.center)
					
					if(self.dir == "DX" and self.rect.center[0] == 475):
						self.vision = self.image.get_rect(center=self.rect.midtop)
						self.vision.height = 20
						self.vision.center = self.rect.midtop
					else:
						self.vision = self.image.get_rect(center=self.rect.midleft)
						self.vision.width = 20
						self.vision.center = self.rect.midleft
					if(self.dir == "DX" and self.rect.center[1] == 0):
						self.kill()
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
					if(passa_O == False and self.rect.center[0] == 258):
						self.rect.center = (self.rect.center[0], self.rect.center[1])
					else:
						if(self.dir == "DX"):
							if(self.rect.center[0] < 325):
								self.rect.center = (self.rect.center[0] + 1, self.rect.center[1])
								if(self.rect.center[0] == 325):
									self.image = pygame.transform.rotate(self.image, 270)
									self.rect.center = (self.rect.center[0], self.rect.center[1] + 1)
							else:
								self.rect.center = (self.rect.center[0], self.rect.center[1] + 1)
						else:
							self.rect.center = (self.rect.center[0] + 1, self.rect.center[1])
					self.rect = self.image.get_rect(center=self.rect.center)
					if(self.dir == "DX" and self.rect.center[0] == 325):
						self.vision = self.image.get_rect(center=self.rect.midbottom)
						self.vision.height = 20
						self.vision.center = self.rect.midbottom
					else:
						self.vision = self.image.get_rect(center=self.rect.midright)
						self.vision.width = 20
						self.vision.center = self.rect.midright
					if(self.dir == "DX" and self.rect.center[0] == 600):
						self.kill()
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
					if(passa_N == False and self.rect.center[1] == 160):
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
					if(passa_S == False and self.rect.center[1] == 440):
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
					if(passa_E == False and self.rect.center[0] == 540):
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
					if(passa_O == False and self.rect.center[0] == 258):
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


