import math
class NumeroPadovan():
	def __init__(self):
		self.terminoActual=0
		self.terminoAnterior=0
		self.tercerTermino=0
		self.cuartoTermino=0
		self.numeroVecesActualizado=0
		self.valor=0
		self.binario=''
		self.__copiaValor=0
		
	def avanzar(self):
		self.numeroVecesActualizado+=1

		if(self.numeroVecesActualizado ==0):
			self.terminoActual=1

		if(self.numeroVecesActualizado==1):
			self.terminoActual=1

		if(self.numeroVecesActualizado==2):
			self.terminoAnterior=1

		if(self.numeroVecesActualizado>=3):
			self.cuartoTermino = self.tercerTermino
			self.tercerTermino = self.terminoAnterior
			self.terminoAnterior = self.terminoActual
			self.terminoActual = self.cuartoTermino + self.tercerTermino

		self.valor = self.terminoActual


	def retroceder(self):
		self.numeroVecesActualizado-=1

		if(self.numeroVecesActualizado ==0):
			self.terminoActual=0

		if(self.numeroVecesActualizado==1):
			self.terminoActual=1

		if(self.numeroVecesActualizado==2):
			self.terminoAnterior=1

		if(self.numeroVecesActualizado>=3):
			self.terminoActual = self.terminoAnterior
			self.terminoAnterior = self.tercerTermino
			self.tercerTermino = self.cuartoTermino
			self.cuartoTermino = self.terminoActual - self.tercerTermino

		self.valor = self.terminoActual

	def GenerarNumeroBinario(self):
		self.binario=''
		numero = self.valor
		while(numero > 0):
			if(numero %2 ==0):
				self.binario = "0" + self.binario
			else:
				self.binario = "1" + self.binario
			numero = int(math.floor(numero/2))
		self.__copiaValor = self.binario

	def getValor(self):		
		return self.valor

	def getBinario(self):
		return self.binario
		






		

