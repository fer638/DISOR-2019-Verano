from tkinter import *
from Botones import Botones
from LabelBinario import LabelBinario


class FramePrincipal():
    def __init__(self):
    	self.frame = Frame()
    	
    	botones = Botones()
    
    	self.frame.pack()  
