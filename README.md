# PySineWave
PySineWave offers an easy way to generate and play sine waves in real time that can make smooth, continuous transitions in pitch and volume.",

## Installation
Open the terminal, and type:
```
pip install pysinewave
```

## Quick Start
```
import time

from pysinewave import SineWave

# Create a sine wave, with a starting pitch of 7, and a pitch increase/decrease speed of 12/second
sinewave = SineWave(pitch = 7, pitch_per_second = 12)

# Turn the sine wave on
sinewave.play()

# Sleep for 5 seconds, during which the sinewave keeps playing
time.sleep(5)

# Set the goal pitch to 12
sinewave.set_pitch(12)
