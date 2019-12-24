# PySineWave

PySineWave offers an easy way to generate and play sine waves that can make smooth, continuous transitions in pitch and volume in real time. These sine waves are created, threaded and played (fed into an sound channel) behind the scenes, so that all you have to do is call their easy-to-use functions!

## Installation
Open the terminal, and type:
```
pip install pysinewave
```

## Code Example
This code will play a sinewave that smoothly decreases its pitch.
```
import time

from pysinewave import SineWave

# Create a sine wave, with a starting pitch of 12, and a pitch change speed of 10/second.
sinewave = SineWave(pitch = 12, pitch_per_second = 10)

# Turn the sine wave on.
sinewave.play()

# Sleep for 2 seconds, as the sinewave keeps playing.
time.sleep(2)

# Set the goal pitch to -5.
sinewave.set_pitch(-5)

# Sleep for 3 seconds, as the sinewave smoothly slides its pitch down from 12 to -5, and stays there.
time.sleep(3)
```

## Useful Functions

Use `SineWave.set_pitch(pitch)` to change the pitch of a SineWave object. The SineWave object will smoothly transition to this new pitch at a rate of `SineWave.pitch_per_second`.

Use `SineWave.set_volume(decibels)` to change the volume of a SineWave object. The SineWave object will smoothly transition to this new volume at a rate of `SineWave.decibels_per_second`.

Use `SineWave.play()` and `SineWave.stop()` to start and stop the SineWave, respectively.

Use `SineWave.set_pitch_per_second(pitch_per_second)` and `SineWave.set_decibels_per_second(decibels_per_second)` to change the values of `SineWave.pitch_per_second` and `SineWave.decibels_per_second`, respectively.

## A Note on Pitch and Volume
You may want to directly modify the frequency and amplitude of a SineWave. We do provide two alternative functions, `SineWave.set_frequency(hertz)` and `SineWave.set_amplitude(percent)`, however we suggest that you use `SineWave.set_pitch(pitch)` and `SineWave.set_volume(decibels)` instead.

Why? The brain naturally perceives *ratios* between sound's frequency and amplitude much better than differences. This means that working directly with frequency will cause high frequencies to be much harder to distinguish than low frequencies. Similarly for amplitude.

The conversion between pitch and frequency (in Hz) is: **frequency = 440 * 2^((pitch-9)/2)**. For instance, note that a pitch of 0 is middle C, i.e. a frequency of 261.63 Hz.

The conversion between volume (in decibels) and amplitude is: **amplitude = 2^(volume/10)**. For instance, increasing the volume by 10 decibels doubles the amplitude of the sine wave.

Here's a helpful table showing the relationship between frequency, pitch, and musical notes for one octave:

| Pitch | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|:---------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| Frequency | 261.63 | 277.18 | 293.66 | 311.13 | 329.63 | 349.23 | 369.99 | 392.00 | 415.30 | 440.00 | 466.16 | 493.88 | 523.25 |
| Note | C | C#/Db | D | D#/Eb | E | F | F#/Gb | G | G#/Ab | A | A#/Bb | B | C |

If you don't know anything about music theory, no worries! Just be sure to stick to `SineWave.set_pitch(pitch)` and `SineWave.set_volume(decibels)`. Your Python projects will thank you.
