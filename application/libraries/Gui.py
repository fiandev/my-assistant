from tkinter import Tk, Button, Label, Frame, PhotoImage
from application.libraries.State import State
from application.libraries.Bot import Bot
from application.constants.paths import ROOT_PATH

class Gui (State):
    def __init__(self) -> None:
        super().__init__()
        
        self.root = Tk()
        self.root.geometry('500x500')
        self.frame = Frame(self.root)
        self.play_image = PhotoImage(file=f"{ ROOT_PATH }/assets/images/play.png", width=300, height=300)
        self.pause_image = PhotoImage(file=f"{ ROOT_PATH }/assets/images/pasue.png", width=300, height=300)

    def load (self):
        microPhoneToggleButton = Button(self.frame, image=self.play_image, width="28pt", height="28pt")
        statusText = Label(self.frame, text=f"active : { self.isMIcrophoneActive }")
        bot = Bot()
        
        def microPhoneHandler ():
            self.toggleMicroPhone(isActive=not self.isMIcrophoneActive, button=microPhoneToggleButton, images={  
                "on": self.play_image,
                "off": self.pause_image,
            })
            if self.isMIcrophoneActive:
                bot.listen()
        
        microPhoneToggleButton.config(command=microPhoneHandler)
        microPhoneToggleButton.pack(pady=10)
        
        statusText.pack(fill="x")
        self.frame.pack(expand=True, fill="both")
        
        self.root.mainloop()