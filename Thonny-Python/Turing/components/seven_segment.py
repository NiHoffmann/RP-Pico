from components.led_array import led_array

class seven_segment():
    leds = None
    #these are values for ccc = false
    numbers = [0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xF8,0x80,0x90]
    rect = 0xA3
    common_cathode_configuration = False
    
    def __init__(self, pin_numbers, common_cathode_configuration = True):
        self.leds = led_array(pin_numbers)
        self.common_cathode_configuration = common_cathode_configuration
        
        if common_cathode_configuration :
            self.rect = ~self.rect
            for x in range(len(self.numbers)):
                self.numbers[x] = ~self.numbers[x]
        
    def clear(self):
        if self.common_cathode_configuration :
            self.leds.set(0)
        else:
            self.leds.set(0xFF)
            
    def set_byte(self, byte):
        self.leds.set(byte)
        
    def set_number(self,num):
        num %= len(self.numbers)
        self.leds.set(self.numbers[num])
        
    def set_rect(self):
        self.leds.set(self.rect)
    