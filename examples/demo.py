import numpy as np
from pyfilterlab import design_fir, apply_filter, plot_response, plot_signal

fs = 500  # Hz
t = np.linspace(0, 1, fs, endpoint=False)
signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 100 * t)

# Design low-pass FIR filter
fir = design_fir(num_taps=51, cutoff=30, fs=fs)

# Apply filter
filtered = apply_filter(fir, 1, signal)

# Plot
plot_signal(signal, fs=fs, title='Original Signal')
plot_signal(filtered, fs=fs, title='Filtered Signal')
plot_response(fir, a=1, fs=fs, title='FIR Filter Response')
