# import
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from IPython.display import Audio
import sys
import math
import time

# local function
def get_sine(f, sampling_rate = 48000, duration_in_sec = 1, phase = 0):
    t = np.arange(0, duration_in_sec, 1/sampling_rate)
    return np.sin(2*math.pi*f*t + phase), t

def playsound(audio, fs):
    display(Audio(audio, rate=fs))

def wavread(filepath):
    fs, audio = wavfile.read(filepath)
    audio = audio / np.max(np.abs(audio))
    return audio, fs
    
# init locals
fs = 48000

# init matplotlib 
plt.rcParams.update({
    # Typography
    'font.family': 'serif',
    'mathtext.fontset': 'cm',
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 10,

    # Axes
    'axes.grid': True,
    'axes.grid.which': 'major', # none, major, both
    'axes.axisbelow': True, # grid behind curves
    'axes.spines.top': False, # remove borders
    'axes.spines.right': False, # remove borders
    'axes.linewidth': 0.6,

    # Grid
    'grid.alpha': 0.3,
    'grid.linestyle': '-',
    'grid.linewidth': 0.8,

    # Curves
    'lines.linewidth': 1,

    # Figure
    'figure.figsize': (6, 3.5),
    'figure.dpi': 120,

    # Output
    'savefig.bbox': 'tight',
    'savefig.dpi': 300,
})