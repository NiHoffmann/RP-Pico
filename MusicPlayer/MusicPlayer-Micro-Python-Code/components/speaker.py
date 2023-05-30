from machine import Pin,PWM

import pin_config

class speaker:
    buzzer = None
    volume = 0
    frequenzy = 0
    
    
    def __init__(self,pin_number):
        self.buzzer = PWM(Pin(pin_number))
    
    def set_frequenzy(self, frequenzy):
        if not frequenzy < 0:
            self.frequenzy = frequenzy

    def set_volume(self, volume):
        if not (volume > 1000 or volume < 0):
            self.volume = volume

    def play_note(self):
        self.buzzer.freq(self.frequenzy)
        self.buzzer.duty_u16(self.volume)
        
    def stop(self):
        self.buzzer.duty_u16(0)