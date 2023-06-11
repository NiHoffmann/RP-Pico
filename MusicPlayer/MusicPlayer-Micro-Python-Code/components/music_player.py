from musik.notes import *
from musik.songs import * 
from components.speaker import speaker
from components.volume_display import volume_display
from components.joy_stick import joy_stick
#LCD imports
from components.LCD.pico_i2c_lcd import I2cLcd as LCD
from machine import I2C, Pin
#misc
from utime import sleep
import _thread

#Thread Variables
song = songs[0]
interrupt = False
play = False

class music_player:
    speaker = None
    volume_display = None
    volume_knob = None
    joy_stick = None
    interrupt_button = None
    lcd = None
    song_select_idx = 0
    song_idx = 0
    lcd_updated = True
    lcd_string_1 = "PA: " +(songs[0])[0]
    lcd_string_2 = "SE: " +(songs[0])[0]
    lcd_updated = True
    thread = None
    
    def __init__(self, speaker, volume_display, volume_knob, lcd, interrupt_button, joy_stick):
        self.lcd = lcd 
        self.speaker = speaker
        self.volume_display = volume_display
        self.volume_knob = volume_knob
        self.lcd.hide_cursor()
        self.interrupt_button = interrupt_button
        self.joy_stick = joy_stick
        #start music thread to run in background
        _thread.start_new_thread(self.music_thread_function, ())

    def play_song(self, song, time_between_notes = 0.3):
        global interrupt, play
        
        self.lcd_string_1 = "PL: " +(songs[self.song_idx])[0]
        ix = self.song_idx
        self.lcd_updated = True
        
        song = song[1:len(song)]
        for idx in range(len(song)):
            #interrupt button
            if interrupt :
                interrupt = False
                return
            
            #paused doesnt work somehow
            if not play:
                self.speaker.stop()    
                self.lcd_string_1 = "PA: " +(songs[self.song_idx])[0]        
                self.lcd_updated = True
                ix = self.song_idx                
                
                while not play :
                    #check if selected song has changed
                    if ix != self.song_idx :
                        self.lcd_string_1 = "PA: " +(songs[self.song_idx])[0]        
                        self.lcd_updated = True
                        ix = self.song_idx
                        
                self.lcd_string_1 = "PL: " +(songs[self.song_select_idx])[0]
                self.lcd_updated = True
                
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
            self.lcd.putstr(self.lcd_string_1)
            self.lcd.move_to(0,1)
            self.lcd.putstr(self.lcd_string_2)
            self.lcd_updated = False
    
    def volume_routine(self):
        self.set_volume(self.volume_knob.read_value())
        
    def menu_routine(self):
        global song, play, interrupt
        if self.joy_stick.is_down():
            self.song_select_idx = (self.song_select_idx + 1) % len(songs)
            self.lcd_updated = True
        if self.joy_stick.is_up():
            self.song_select_idx = (self.song_select_idx - 1) % len(songs)
            self.lcd_updated = True
        if self.joy_stick.get_button():
            song = songs[self.song_select_idx]
            self.song_idx = self.song_select_idx
            interrupt = True
            self.lcd_updated = True
            while self.joy_stick.get_button():
                pass
            sleep(0.25)
        self.lcd_string_2 = "SE: "+(songs[self.song_select_idx])[0]
    
    def interrupt_button_routine(self):
        global play, interrupt
        if 1&~self.interrupt_button.value():
            play = not play  
            self.lcd_updated = True

            while 1&~self.interrupt_button.value():
                pass
            sleep(0.25)
        
    def music_thread_function(self):
        global song, play
        while True :
                self.play_song(song)
            
    def input_loop(self):
        while True:
            self.volume_routine()
            self.interrupt_button_routine()
            self.menu_routine()
            self.lcd_update_routine()
            