from components.speaker import speaker
from components.music_player import music_player
from components.volume_display import volume_display
from components.volume_knob import volume_knob
import musik.songs as songs
from pin_config import *
from utime import sleep


speaker = speaker(speaker_pin_number)
knob = volume_knob(volume_knob_pin_number)
display = volume_display(htc_data_pin_number,htc_latch_pin_number,gtc_clock_pin_number,led9_pin_number,led10_pin_number)
player = music_player(speaker, display, knob)

for i in range(0,5):
    player.play_song(songs.song)
