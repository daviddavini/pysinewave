import numpy as np

# Default frames per second
DEFAULT_SAMPLE_RATE = 44100

# Frequency of a middle C
MIDDLE_C_FREQUENCY = 261.625565

def direction(start, end):
    '''Returns 1 if end > start, and -1 if end < start.'''
    return 1 if end > start else -1

def bounded_by_end(value, start, end):
    '''Returns value if value is closer to start than end is, otherwise returns end.'''
    if start < end:
        return np.minimum(value, end)
    else:
        return np.maximum(value, end)

def frames_to_time(frames, framerate):
    '''Convert frame count to time (using framerate).'''
    return frames / framerate

def frames_to_time_array(start_frame, frames, framerate):
    '''Convert frame information into a time array.'''
    # Convert frame info to time info
    start_time = frames_to_time(start_frame, framerate)
    end_time = frames_to_time(start_frame + frames, framerate)

    # Create time array with one entry for each frame
    time_array = np.linspace(start_time, end_time, frames, endpoint=False)
    return time_array

def sinewave(frequency, time):
    '''Create a sinewave array for a sinewave of given constant frequency.'''
    return np.sin(2 * np.pi * time * frequency)

def interval_to_frequency_ratio(interval):
    '''The frequency of the given pitch (in Hz), relative to middle C'''
    return 2**(interval/12)

def pitch_to_frequency(pitch):
    '''The frequency of the given pitch (in Hz), relative to middle C'''
    return MIDDLE_C_FREQUENCY * 2**(pitch/12)

def decibels_to_amplitude_ratio(decibels):
    '''The ratio between two amplitudes given a decibel change'''
    return 2**(decibels / 10)