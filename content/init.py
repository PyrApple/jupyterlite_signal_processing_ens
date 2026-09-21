# import
import matplotlib.pyplot as plt
import numpy as np
import scipy
from IPython.display import Audio
import math

# local function
def get_sine(f, sampling_rate = 48000, duration_in_sec = 1, phase = 0):
    t = np.arange(0, duration_in_sec, 1/sampling_rate)
    return np.sin(2*math.pi*f*t + phase), t

def playsound(audio, fs):
    display(Audio(audio, rate=fs))

def wavread(filepath):
    fs, audio = scipy.io.wavfile.read(filepath)
    audio = audio / np.max(np.abs(audio))
    return audio, fs

# not used atm
"""
def filter_formula(b, a):
    terms = []

    for k, gain in enumerate(b):
        var = "x[n]" if k == 0 else f"x[n-{k}]"
        terms.append((gain/a[0], var))

    for k, gain in enumerate(a[1:], start=1):
        terms.append((-gain/a[0], f"y[n-{k}]"))

    formula = "y[n] = "
    for i, (gain, var) in enumerate(terms):
        if i == 0:
            formula += f"{gain:g}.{var}"
        else:
            formula += f" {'+' if gain >= 0 else '-'} {abs(gain):g}.{var}"

    return formula
"""  

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
    'lines.markersize': 3,

    # Figure
    'figure.figsize': (6, 3.5),
    'figure.dpi': 120,

    # Output
    'savefig.bbox': 'tight',
    'savefig.dpi': 300,
})