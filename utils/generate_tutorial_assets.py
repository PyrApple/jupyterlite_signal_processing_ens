# import
import scipy
import numpy as np
import math

#region: generate resampling aliasing assets

# load audio 
fs, audio = scipy.io.wavfile.read('../content/assets/drums.wav')
audio = audio / np.max(np.abs(audio))

# add sine
resample_factor = 2
fs_out = fs / resample_factor
f1 = 5000
duration_in_sec = len(audio)/fs
t = np.arange(duration_in_sec * fs) / fs
audio += 0.01*np.sin(2*math.pi* (fs_out/2 + (fs_out/2 - f1)) *t)

# save to disk
scipy.io.wavfile.write("../content/assets/drums_corrupted.wav", fs, audio)

#endregion

#region: generate delay estimation via correlation assets

# load audio 
fs, audio = scipy.io.wavfile.read('../content/assets/drums.wav')
audio = audio / np.max(np.abs(audio))

# create delayed version
delay_in_ms = 4.3
delay_in_samp = int(fs * (delay_in_ms / 1000))
audio = np.pad(audio, [delay_in_samp, 0])

# save to disk
scipy.io.wavfile.write("../content/assets/drums_delayed.wav", fs, audio)

#endregion