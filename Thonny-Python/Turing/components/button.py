import machine

class button:
    pin = None
    
    def __init__(self, pin_number):
        self.pin = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_DOWN)
        
    def wait_for_press():
        while(not self.pin.value()):
            pass

    def pressed():
        return self.pin.value()
    

