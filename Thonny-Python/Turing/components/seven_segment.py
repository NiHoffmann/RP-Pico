from components.led_array import led_array

class seven_segment():
    leds = None
    numbers = [0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xF8,0x80,0x90]
    rect = 0xA3
    
    def __init__(self, pin_numbers, common_cathode_configuration = True):
        self.leds = led_array(pin_numbers)
        if common_cathode_configuration :
            self.rect = ~self.rect
            for x in range(len(self.numbers)):
                self.numbers[x] = ~self.numbers[x]
        
    def set_number(self,num):
        num %= len(self.numbers)
        self.leds.set(self.numbers[num])
        
    def set_rect(self):
        self.leds.set(self.rect)
    