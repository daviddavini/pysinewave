import time

from pysinewave import SineWave

fur_elise = [                       12,11,12,11,12,7,10,8,
        5,5,5,-3,0,5,7,7,7,0,4,7,8,8,8,0,12,11,12,11,12,7,10,8,
        5,5,5,-3,0,5,7,7,7,0,8,7,5,5,5,5]

o_christmas_tree = [-5,-5, 0, 0, 0, 0, 2, 2, 4, 4, 4, 4, 4, 4, 2, 4, 5, 5, -1, -1, 2, 2, 0, 0,
                    -5,-5, 0, 0, 0, 0, 2, 2, 4, 4, 4, 4, 4, 4, 2, 4, 5, 5, -1, -1, 2, 2, 0, 0,
                    7, 7, 4, 9, 9, 9, 7, 7, 5, 5, 5, 5, 5, 5, 2, 7, 7, 7, 5, 5, 4, 4, 4, 4,
                    -5,-5, 0, 0, 0, 0, 2, 2, 4, 4, 4, 4, 4, 4, 2, 4, 5, 5, -1, -1, 2, 2, 0, 0]

white_christmas = [4,4,4,4,5,4,3,4,5,5,5,5,6,7,7,7,7,9,11,12,14,12,11,9,7,7,7,7,7,7,0,2,
                   4,3,4,3,4,9,9,7,0,-1,0,-1,0,7,7,5,4,4,4,4,5,4,2,0,2,2,2,2,2,2,2,2,
                   4,4,4,4,5,4,3,4,5,5,5,5,6,7,7,7,7,9,11,12,14,12,11,9,7,7,7,7,7,7,0,2,
                   4,3,4,3,4,9,9,7,12,12,12,12,12,12,0,2,4,4,4,4,7,2,2,-5,0]

# sw1 = SineWave(pitch=12, pitch_per_second=12)
# sw1.play()
# time.sleep(1)
# sw1.set_volume(10)
# time.sleep(1)
# sw1.set_volume(-10)
# time.sleep(3)
# sw1.set_volume(0)
# time.sleep(100)

def play_song(song, note_per_second=4):

    sinewave = SineWave(song[0],36)

    sinewave.play()

    for pitch in song:
        sinewave.set_pitch(pitch)
        time.sleep(1/note_per_second)

play_song(white_christmas, 2)
#play_song(o_christmas_tree, 2)
