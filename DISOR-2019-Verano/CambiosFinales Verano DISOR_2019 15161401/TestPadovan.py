import unittest
from numeroPadovan import NumeroPadovan

class TestPadovan(unittest.TestCase):
	def test_CrearObjto(self):
		self.numPado = NumeroPadovan()
		self.assertEquals(0,self.numeroPado.getValor())

	def avanzar_uno(self):
		self.numPado = NumeroPadovan()
		self.numPado.avanzar()
		self.assertEquals(1,self.numeroPado.getValor())

	def avanzar_dos(self):
		self.numPado = NumeroPadovan()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.assertEquals(1,self.numeroPado.getValor())

	def avanzar_tres(self):
		self.numPado = NumeroPadovan()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.assertEquals(1,self.numeroPado.getValor())

	def avanzar_cuatro(self):
		self.numPado = NumeroPadovan()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.assertEquals(2,self.numeroPado.getValor())

	def avanzar_cinco(self):
		self.numPado = NumeroPadovan()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.assertEquals(2,self.numeroPado.getValor())

	def avanzar_seis(self):
		self.numPado = NumeroPadovan()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.assertEquals(3,self.numeroPado.getValor())

	def avanzar_siete(self):
		self.numPado = NumeroPadovan()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.numPado.avanzar()
		self.assertEquals(4,self.numeroPado.getValor())


