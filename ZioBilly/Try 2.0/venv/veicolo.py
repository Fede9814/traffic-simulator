import random
import numpy
import pygame

nord = 1
sud = 2
est = 3
ovest = 4
direzione = [nord, sud, est, ovest]
velMax = 50
frena = 0


class Veicolo():
    
    def __init__(self):
        super().__init__()
        
        # 25% di probabilità di entrare da una strada qualsiasi
        self.entra = numpy.random.choice(direzione, p=[0.25, 0.25, 0.25, 0.25])
        
        # presa la strada iniziale toglila dalla lista (non esco da dove entro)
        direzione.remove(self.entra)
        
        # 33% di probabilità di uscire verso una strada qualsiasi
        self.esci = numpy.random.choice(direzione, p=[0.33, 0.33, 0.34])
        
        # per sport togli (serve solo per verificare la rimozione effettiva della strada presa)
        direzione.remove(self.esci)
        
        # fammi vedere che scelta hai fatto
        print("Entra da qua: ", self.entra, " + ", direzione)
        
        # fammi vedere che scelta hai fatto
        print("Esci da qua: ", self.esci, " + ", direzione)
        
        ###
        
while True:
    
    Veicolo()