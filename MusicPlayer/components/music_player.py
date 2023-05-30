from musik.notes import *
from components.speaker import speaker
from components.volume_display import volume_display
from utime import sleep
import _thread

class music_player:
    speaker = None
    volume_display = None
    volume_knob = None
    
    def __init__(self, speaker, volume_display, volume_knob):
        self.speaker = speaker
        self.volume_display = volume_display
        self.volume_knob = volume_knob
        _thread.start_new_thread(self.second_thread, ())

    def play_song(self, song, time_between_notes = 0.3):
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

    def second_thread(self):
        while True:
            sleep(0.25)
            self.set_volume(self.volume_knob.read_value())
        
