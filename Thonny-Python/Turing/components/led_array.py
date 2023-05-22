import machine

class led_array:
    pins = None
    
    #takes array with pin numbers as an argument, displays binary number -> pin numbers should be sorted for ease of use (see set(...))
    def __init__(self, pin_numbers):
        pins = [None]*len(pin_numbers)
        for idx,pin in enumerate(pin_numbers):
            pins[idx] = machine.Pin(pin,machine.Pin.OUT)
            self.pins = pins
            
    #display binary number
    def set(self, set_byte):
        byte = set_byte & 0xFF
        #led 0 is displayed as bit 2^0, led 1 is displayed as 2^1,...
        for i in range(0,len(self.pins)):
            if((byte & 1)):
                self.pins[i].high()
            else:
                self.pins[i].low()
            byte >>=  1