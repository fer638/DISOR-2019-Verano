from tkinter import *
from NumeroFibonacci import NumeroFibonacci
from numeroPadovan import NumeroPadovan


class Botones():
    def __init__(self):
    	self.vacia=" "
    	self.inicial =0

    	self.botonAvanzarFibonacci = Button(None, text='Siguiente Numero Fibonacci',command=self.clickFib)
    	self.botonAvanzarPadovan = Button(None, text='Siguiente Serie Padovan', command= self.clickPado)
    	self.retrocederTodo = Button(None, text='Regresar', command= self.clickRegresar)

    	self.txtFibonacci=Entry(None)
    	self.txtFibonacci.insert(0, self.inicial)
    	self.txtPadovan=Entry(None)
    	self.txtPadovan.insert(0, self.inicial)

    	self.txtFibonacciBinario=Entry(None)
    	self.txtFibonacciBinario.insert(0, self.inicial)
    	self.txtPadovanBinario=Entry(None)
    	self.txtPadovanBinario.insert(0, self.inicial)

    	self.txtFibonacciHexadecimal=Entry(None)
    	self.txtFibonacciHexadecimal.insert(0, self.inicial)
    	self.txtPadovanHexadecimal=Entry(None)
    	self.txtPadovanHexadecimal.insert(0, self.inicial)

    	self.txtFibonacciEspañol=Entry(None)
    	self.txtFibonacciEspañol.insert(0, self.inicial)
    	self.txtPadovanEspañol=Entry(None)
    	self.txtPadovanEspañol.insert(0, self.inicial)

    	self.fibonacciDecimal= Label(None,text="Fibonacci Decimal : ")
    	self.fibonacciBinario= Label(None,text="Fibonacci Binario : ")
    	self.fibonacciHexadecimal= Label(None,text="Fibonacci Hexadecimal : ")
    	self.fibonacciEspañol= Label(None,text="Fibonacci Español : ")
    	self.padovanDecimal= Label(None,text="Padovan Decimal : ")
    	self.padovanBinario= Label(None,text="Padovan Binario : ")
    	self.padovanHexadecimal= Label(None,text="Padovan Hexadecimal : ")
    	self.padovanEspañol= Label(None,text="Padovan Español : ")

    	self.botonAvanzarFibonacci.pack()
    	self.fibonacciDecimal.pack()
    	self.txtFibonacci.pack()
    	self.fibonacciBinario.pack()
    	self.txtFibonacciBinario.pack()
    	self.fibonacciHexadecimal.pack()
    	self.txtFibonacciHexadecimal.pack()
    	self.fibonacciEspañol.pack()
    	self.txtFibonacciEspañol.pack()

    	self.botonAvanzarPadovan.pack()
    	self.padovanDecimal.pack()
    	self.txtPadovan.pack()
    	self.padovanBinario.pack()
    	self.txtPadovanBinario.pack()
    	self.padovanHexadecimal.pack()
    	self.txtPadovanHexadecimal.pack()
    	self.padovanEspañol.pack()
    	self.txtPadovanEspañol.pack()

    	self.retrocederTodo.pack()


    numeroFibonacci = NumeroFibonacci()
    def clickFib(self):
    	self.numeroFibonacci.avanzar()
    	self.txtFibonacci.insert(0, self.vacia)
    	self.txtFibonacci.insert(0, self.numeroFibonacci.getValor())

    	self.numeroFibonacci.GenerarNumeroBinario()
    	self.txtFibonacciBinario.insert(0, self.vacia)
    	self.txtFibonacciBinario.insert(0, self.numeroFibonacci.getBinario())

    numeroPadovan = NumeroPadovan()
    def clickPado(self):
    	self.numeroPadovan.avanzar()
    	self.numeroPadovan.GenerarNumeroBinario()
    	self.txtPadovan.insert(0, self.vacia)
    	self.txtPadovan.insert(0, self.numeroPadovan.getValor())

    	self.numeroPadovan.GenerarNumeroBinario()
    	self.txtPadovanBinario.insert(0, self.vacia)
    	self.txtPadovanBinario.insert(0,self.numeroPadovan.getBinario())

    def clickRegresar(self):
    	self.numeroPadovan.retroceder()
    	self.numeroFibonacci.retroceder()

    	self.txtFibonacci.insert(0, self.vacia)
    	self.txtFibonacci.insert(0, self.numeroFibonacci.getValor())
    	self.numeroFibonacci.GenerarNumeroBinario()
    	self.txtFibonacciBinario.insert(0, self.vacia)
    	self.txtFibonacciBinario.insert(0, self.numeroFibonacci.getBinario())

    	self.txtPadovan.insert(0, self.vacia)
    	self.txtPadovan.insert(0, self.numeroPadovan.getValor())
    	self.numeroPadovan.GenerarNumeroBinario()
    	self.txtPadovanBinario.insert(0, self.vacia)
    	self.txtPadovanBinario.insert(0,self.numeroPadovan.getBinario())














