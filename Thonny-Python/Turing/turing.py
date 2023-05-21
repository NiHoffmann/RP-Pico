#default imports
import machine
import time
import utime

#project pin config
from pin_config import *
from components.led_array import led_array
from components.seven_segment import seven_segment

io_leds = led_array(io_led_pin_numbers)
segment = seven_segment(segment_pin_numbers)

#clear leds
io_leds.set(0)
segment.clear()


button_left = button(button_left_number)
button_right = button(button_right_number)

#def machine_input_loop():
    
    

#inpurt



