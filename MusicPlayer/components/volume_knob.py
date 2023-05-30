from machine import Pin,ADC
import utime

class volume_knob:
    poti = None
    def __init__(self, poti_pin_number):
        self.poti = ADC(poti_pin_number)
    
    #return 0-100% value
    def read_value(self):
        return int((self.poti.read_u16())/(65535/100))