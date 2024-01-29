from application.libraries.Gui import Gui
from application.includes.environment import environment

class Program:
    def __init__ (self):
        pass
    
    def start (self):
        gui = Gui()
        
        gui.load()
        #command = gui.listen()
        