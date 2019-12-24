import sys

import numpy as np
import sounddevice as sd

from pysinewave import utilities
from pysinewave import sinewave_generator

class SineWave:
    '''Generates and plays a continuous sinewave, with smooth transitions in frequency (pitch)
        and amplitude (volume).'''

    def __init__(self, pitch=0, pitch_per_second=12, decibels=0, decibels_per_second=1,
                samplerate=utilities.DEFAULT_SAMPLE_RATE):
        self.sinewave_generator = sinewave_generator.SineWaveGenerator(
                                    pitch=pitch, pitch_per_second=pitch_per_second,
                                    decibels = decibels, decibels_per_second=decibels_per_second,
                                    samplerate=samplerate)

        # Create the output stream
        self.output_stream = sd.OutputStream(channels=1, callback= lambda *args: self._callback(*args), 
                                samplerate=samplerate)

    def _callback(self, outdata, frames, time, status):
        '''Callback function for the output stream.'''
        # Print any error messages we receive
        if status:
            print(status, file=sys.stderr)

        # Get and use the sinewave's next batch of data
        data = self.sinewave_generator.next_data(frames)
        outdata[:] = data.reshape(-1, 1)

    def play(self):
        '''Plays the sinewave (in a separate thread). Changes in frequency or amplitude will transition smoothly.'''
        self.output_stream.start()
    
    def stop(self):
        '''If the sinewave is playing, stops the sinewave.'''
        self.output_stream.stop()

    def set_frequency(self, frequency):
        '''Sets the goal frequency of the sinewave, which will be smoothly transitioned to.'''
        self.sinewave_generator.set_frequency(frequency)
    
    def set_pitch(self, pitch):
        '''Sets the goal pitch of the sinewave (relative to middle C), 
        which will be smoothly transitioned to.'''
        self.sinewave_generator.set_pitch(pitch)
    
    def set_volume(self, volume):
        '''Sets the goal volume (in decibels, relative to medium volume) of the sinewave'''
        self.sinewave_generator.set_decibels(volume)