
class State:
    def __init__(self) -> None:
        self.isMIcrophoneActive: bool = False
        self.language: str = "id"
    
    def toggleMicroPhone (self, isActive: bool, button, images: dict) -> None:
        self.isMIcrophoneActive = isActive
        button.config(image=images["on" if not isActive else "off"])
        
    