from components.led_array import led_array

class seven_segment():
    leds = None
    symbols = [0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xF8,0x80,0x90]
    
    def __init__(self, pin_numbers, common_cathode_configuration = True):
        self.leds = led_array(pin_numbers)
        if common_cathode_configuration :
            for x in range(len(self.symbols)):
                self.symbols[x] = ~self.symbols[x]
        
    def set(self,num):
        num %= len(self.symbols)
        self.leds.set(self.symbols[num])