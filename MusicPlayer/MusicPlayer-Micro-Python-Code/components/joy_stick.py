from machine import Pin,ADC
import utime

class joy_stick:
    x_axis_poti = None
    y_axis_poti = None
    button = None
    #for 3.3 volt
    middle = (65535/2)
    
    def __init__(self,vrx_pin_number, vry_pin_number, sw_pin_number):
        self.x_axis_poti = ADC(Pin(vrx_pin_number))
        self.y_axis_poti = ADC(Pin(vry_pin_number))
        self.button = Pin(sw_pin_number,Pin.IN,Pin.PULL_UP)

    def is_up(self):
        return self.get_x() <= self.middle - (self.middle/2)
    
    def is_down(self):
        return self.get_x() >= self.middle + (self.middle/2)
    
    def is_left(self):
        return self.get_y() >= self.middle + (self.middle/2)
    
    def is_right(self):
        return self.get_y() <= self.middle - (self.middle/2)

    def get_x(self):
        return self.x_axis_poti.read_u16()
    
    def get_y(self):
        return self.y_axis_poti.read_u16()
    
    def get_button(self):
        return 1&~(self.button.value())