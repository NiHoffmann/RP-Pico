from components.speaker import speaker
from components.music_player import music_player
from components.volume_display import volume_display
from components.volume_knob import volume_knob

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
player = music_player(speaker, display, knob, lcd)

for song in songs:
    player.play_song(song)
    
