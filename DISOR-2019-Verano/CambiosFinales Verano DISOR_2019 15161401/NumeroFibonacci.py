import math

class NumeroFibonacci():

	def __init__(self):

		self.__terminoAnterior=0
		self.__terminoActual=0
		self.__numeroVecesActualizado=0
		self.__valor=0
		self.__copiaValor=0
		self.hexadecimal=''
		self.binario=''
		self.copHexadecimal=0


	def avanzar(self):

		self.__numeroVecesActualizado+=1
		if(self.__numeroVecesActualizado==0):
			self.__terminoActual=1

		if(self.__numeroVecesActualizado==1):
			self.__terminoActual=1

		if(self.__numeroVecesActualizado>=2):
			respaldoTerminoAnterior = self.__terminoAnterior
			self.__terminoAnterior = self.__terminoActual
			self.__terminoActual = self.__terminoAnterior + respaldoTerminoAnterior
		
		self.__valor = self.__terminoActual
		self.__copiaValor = self.__valor

	def retroceder(self):
		self.__numeroVecesActualizado-=1
		if(self.__numeroVecesActualizado==0):
			self.__terminoActual=0

		if(self.__numeroVecesActualizado==1):
			self.__terminoActual=0

		if(self.__numeroVecesActualizado>=2):
			respaldoTerminoActual = self.__terminoActual
			self.__terminoActual = self.__terminoAnterior
			self.__terminoAnterior = respaldoTerminoActual - self.__terminoActual

		self.__valor = self.__terminoActual
		



	def GenerarNumeroBinario(self):
		self.binario=''
		numero = self.__valor
		while(numero > 0):
			if(numero %2 ==0):
				self.binario = "0" + self.binario
			else:
				self.binario = "1" + self.binario
			numero = int(math.floor(numero/2))
		self.__copiaValor = self.binario

	def hexadecimal(self):
		self.hexadecimal=''
		decimal = 17
		while decimal != 0:
			residuo = self.__CambiarDigitos(decimal % 16)
			self.hexadecimal = str(residuo) + self.hexadecimal
			decimal = int(decimal / 16)
		self.copHexadecimal = self.hexadecimal

	def __CambiarDigitos(self,digitos):
		decimales =     [10 , 11 , 12 , 13 , 14 , 15 ]
		hexadecimal = ["A", "B", "C", "D", "E", "F"]
		for caracter in range(7):
		  if digitos == decimales[caracter - 1]:
		  	digitos = hexadecimal[caracter - 1]
		  	return digitos

	def getValor(self):
		return self.__valor

	def getBinario(self):
		return self.binario

	def getHexadecimal(self):
		return self.copHexadecimal








