import numpy as np

from continuous_sinewave import utilities

class SineWaveGenerator:
    '''Generates continuous pressure arrays'''
    def __init__(self, pitch, pitch_per_second=12, decibels=1, decibels_per_second=1, 
                samplerate=utilities.DEFAULT_SAMPLE_RATE):
        self.frequency = utilities.pitch_to_frequency(pitch)
        self.phase = 0
        self.amplitude = utilities.decibels_to_amplitude_ratio(decibels)

        self.pitch_per_second = pitch_per_second
        self.decibels_per_second = decibels_per_second
        self.goal_frequency = self.frequency
        self.goal_amplitude = self.amplitude
        self.samplerate = samplerate
    
    def new_frequency(self, time):
        dir = utilities.direction(self.frequency, self.goal_frequency)
        new_frequency = self.frequency * utilities.interval_to_frequency_ratio(
                            dir * self.pitch_per_second * time)
        return utilities.bounded_by_end(new_frequency, self.frequency, self.goal_frequency)

    def new_phase_array(self, new_frequency_array, delta_time):
        return self.phase + np.cumsum(new_frequency_array * delta_time)

    def new_amplitude_array(self, time):
        dir = utilities.direction(self.amplitude, self.goal_amplitude)
        new_amplitude = self.amplitude + dir * self.decibels_per_second * time
        return utilities.bounded_by_end(new_amplitude, self.amplitude, self.goal_amplitude)

    def set_frequency(self, frequency):
        '''Set the goal frequency that the sinewave will gradually shift towards.'''
        self.goal_frequency = frequency
    
    def set_pitch(self, pitch):
        '''Set the goal pitch that the sinewave will gradually shift towards.'''
        self.goal_frequency = utilities.pitch_to_frequency(pitch)

    def set_amplitude(self, amplitude):
        '''Set the amplitude that the sinewave will gradually shift towards.'''
        self.goal_amplitude = amplitude
    
    def set_decibels(self, decibels):
        '''Set the amplitude (in decibels) that the sinewave will gradually shift towards.'''
        self.goal_amplitude = utilities.decibels_to_amplitude_ratio(decibels)

    def next_array(self, frames):
        '''Get the pressure array for the given number of frames'''

        # Convert frame information to time information
        time_array = utilities.frames_to_time_array(0, frames, self.samplerate)
        delta_time = time_array[1] - time_array[0]

        # Calculate the frequencies of this batch of data
        new_frequency_array = self.new_frequency(time_array)

        # Calculate the phases
        new_phase_array = self.new_phase_array(new_frequency_array, delta_time)

        # Calculate the amplitudes
        new_amplitude_array = self.new_amplitude_array(time_array)

        # Create the sinewave array
        sinewave_array = new_amplitude_array * np.sin(2*np.pi*new_phase_array)
        
        # Update internal state
        self.frequency = new_frequency_array[-1]
        self.phase = new_phase_array[-1]
        self.amplitude = new_amplitude_array[-1]

        #print('Frequency: {0} Phase: {1} Amplitude: {2}'.format(self.frequency, self.phase, self.amplitude))

        return sinewave_array