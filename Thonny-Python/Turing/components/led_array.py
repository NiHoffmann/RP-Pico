#default imports
import machine

class led_array:
    pins = None
    
    def __init__(self, pin_numbers):
        pins = [None]*len(pin_numbers)
        for idx,pin in enumerate(pin_numbers):
            pins[idx] = machine.Pin(pin,machine.Pin.OUT)
            self.pins = pins
        
    def set(self, set_byte):
        byte = set_byte & 0xFF
        for i in range(0,len(self.pins)):
            if((byte & 1)):
                self.pins[i].high()
            else:
                self.pins[i].low()
            byte >>=  1