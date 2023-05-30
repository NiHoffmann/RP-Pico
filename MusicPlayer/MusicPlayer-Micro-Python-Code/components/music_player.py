from musik.notes import *
from components.speaker import speaker
from components.volume_display import volume_display
#LCD imports
from components.LCD.pico_i2c_lcd import I2cLcd as LCD
from machine import I2C, Pin
#misc
from utime import sleep
import _thread

class music_player:
    speaker = None
    volume_display = None
    volume_knob = None
    lcd = None
    lcd_string = "Current Song"
    lcd_updated = True
    
    def __init__(self, speaker, volume_display, volume_knob, lcd):
        self.lcd = lcd 
        self.speaker = speaker
        self.volume_display = volume_display
        self.volume_knob = volume_knob
        self.lcd.hide_cursor()
        _thread.start_new_thread(self.second_thread, ())

    def play_song(self, song, time_between_notes = 0.3):
        self.lcd_string = "Now Playing \n"+song[0]
        self.lcd_updated = True
        
        song = song[1:len(song)]
        for idx in range(len(song)):
            if (song[idx] == "P"):
                self.speaker.stop()
            else:
                self.speaker.set_frequenzy(notes[song[idx]])
                self.speaker.play_note()
            sleep(time_between_notes)
        self.speaker.stop()
        
    def set_volume(self, percent):
        self.speaker.set_volume(percent * 10)
        self.volume_display.set_volume_display(percent)
        
    def lcd_update_routine(self):
        #add barrier later
        if self.lcd_updated:
            self.lcd.clear()
            self.lcd.move_to(0,0)
            self.lcd.putstr(self.lcd_string)
            self.lcd_updated = False
    
    def volume_routine(self):
        self.set_volume(self.volume_knob.read_value())
    
    def second_thread(self):
        while True:
            sleep(0.5)
            self.volume_routine()
            self.lcd_update_routine()