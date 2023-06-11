from components.speaker import speaker
from components.music_player import music_player
from components.volume_display import volume_display
from components.volume_knob import volume_knob
from components.joy_stick import joy_stick

from components.LCD.pico_i2c_lcd import I2cLcd as LCD
from machine import I2C, Pin

from musik.songs import *
from pin_config import *
from utime import sleep


speaker = speaker(speaker_pin_number)
knob = volume_knob(volume_knob_pin_number)
display = volume_display(htc_data_pin_number,htc_latch_pin_number,gtc_clock_pin_number,led9_pin_number,led10_pin_number)
i2c = I2C(0, sda=Pin(lcd_sda_pin_number), scl=Pin(lcd_scl_pin_number), freq=400000)
lcd = LCD(i2c, lcd_i2c_address, 2, 16)
joystick = joy_stick(joy_stick_vdx_pin, joy_stick_vdy_pin, joy_stick_sw_pin)
interrupt_button = Pin(interrupt_button_pin, Pin.IN, Pin.PULL_UP)
player = music_player(speaker, display, knob, lcd, interrupt_button, joystick)

player.input_loop()
#sleep(10)
    
