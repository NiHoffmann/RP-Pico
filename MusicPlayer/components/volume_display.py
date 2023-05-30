from machine import Pin
import utime
#volume display using hc595 for leds 1-8 and 2 additional gpio pins
class volume_display:
    latch = None
    clock = None
    data = None
    led9 = None
    led10 = None
    
    def __init__(self,data_pin_number,latch_pin_number,clock_pin_number,led9_pin_number,led10_pin_number):
        self.latch = Pin(latch_pin_number, Pin.OUT)
        self.clock = Pin(clock_pin_number, Pin.OUT)
        self.data = Pin(data_pin_number, Pin.OUT)
        self.led9 = Pin(led9_pin_number, Pin.OUT)
        self.led10 = Pin(led10_pin_number, Pin.OUT)
        
    def set_volume_display(self, percent): 
        #incorrect value turns display off
        if percent > 100 or percent < 0:
            percent = 0
            
        #10 bit value each bit is one led 10% jumps
        value = 0
        for i in range(10,101,10):
            value = value << 1
            if i <= int(percent):
                value |= 1 
            
        self.htc595_set(value >> 2)
        self.led9.value((value & (1<<1) ) >> 1)
        self.led10.value(value & 1)
        
    def htc595_set(self, value):
        self.latch.low()
        for i in range(7,-1,-1):
            self.clock.low()
            utime.sleep_us(50)
            self.data.value((value >> i) & 1)
            self.clock.high()
            utime.sleep_us(50)
            
        self.latch.high()
        utime.sleep_us(200)
        self.clock.low()
        self.latch.low()