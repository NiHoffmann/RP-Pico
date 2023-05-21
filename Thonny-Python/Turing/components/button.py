import machine

class button:
    pin = None
    
    def __init__(self, pin_number):
        self.pin = machine.Pin(pin_number, machine.Pin.IN, machine.Pin.PULL_DOWN)
        
    def wait_for_pressed(self):
        while(not self.pin.value()):
            pass

    def pressed(self):
        return self.pin.value()
    

