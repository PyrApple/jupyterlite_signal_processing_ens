# import
import scipy
import numpy as np
import math

#region: generate filter homework assets

# load audio 
fs, audio = scipy.io.wavfile.read('../content/assets/drums.wav')
audio = audio / np.max(np.abs(audio))

# add sine
t = np.arange(len(audio))/fs
f1 = 1000
audio += 0.1*np.sin(2*math.pi*f1*t)

# save to disk
scipy.io.wavfile.write("../content/homework/filtering/assets/drums_corrupted.wav", fs, audio)

#endregion
