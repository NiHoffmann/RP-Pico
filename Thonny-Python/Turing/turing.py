#default imports
import machine
import time
import utime

#project pin config
from pin_config import *
from components.led_array import led_array
from components.seven_segment import seven_segment
from components.button import button
from turing_machine.turing_machine import turing_machine
from turing_machine.turing_machine import interpreter

io_leds = led_array(io_led_pin_numbers)
segment = seven_segment(segment_pin_numbers)

#clear leds
io_leds.set(0)
segment.clear()

button_left = button(button_left_number)
button_right = button(button_right_number)

t_machine = None
t_tupel = load_data_from_file()

def intToBinaryTape(value, length):
    tape = ['0']*length
    i = length - 1
    
    while i >= 0 :
        if (value & 1) == 1 :
            tape[i] = '1'
        else :
            tape[i] = '0'
        value >>= 1
        i -= 1
    return tape

def binaryTapeToInt(tape):
    value = 0
    for idx,cell in enumerate(tape):
        if cell == '1':
           value += 2**(len(tape)-(idx+1))
    return value
            
            
#button_right is next value
#button_left is confirm input
def machine_input_loop():
    global t_machine, t_tupel
    
    input_length = len(io_led_pin_numbers)
    turing_machine_input = 0
    
    while True :
        #input not confirmed
        if not button_right.pressed():
            if button_left.pressed():
                turing_machine_input += 1
                #max input value with given leds
                turing_machine_input %= (2**input_length)
                io_leds.set(turing_machine_input)
                
                #300000us feel nice
                utime.sleep_us(250000)
        #input was confirmed
        else:
            #initialize turing machine with given input
            t_machine = turing_machine(intToBinaryTape(turing_machine_input, input_length), t_tupel)
            return 

def machine_running_loop():
    global t_machine,button_right,segment
    while not t_machine.is_accepting() :
        button_right.wait_for_pressed()
        t_machine.apply_transition_function()
        
        if t_machine.get_current_cell() == '0':
            segment.set_number(0)
        elif t_machine.get_current_cell() == '1':
            segment.set_number(1)
        elif t_machine.get_current_cell() == t_machine.tupel.blank_symbol:
            segment.set_rect()
        utime.sleep_us(250000)

machine_input_loop()
machine_running_loop()
io_leds.set(binaryTapeToInt(t_machine.get_return_value()))