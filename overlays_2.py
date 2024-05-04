import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
import pandas as pd

color1= 'forestgreen'
color2= 'mediumvioletred'

#file 1 
filename1 = "AB4113B-LW100-R_H4.csv"
# Importing data from the piezoelectric sensor
raw_data1 = pd.read_csv(filename1)
data1 = raw_data1["Volts"].values
presignal1 = np.delete(data1, 1, 0)
signal1 = presignal1.flatten()

# creating the appropriate time vector
signal_len1 = 0
signal_len1 = raw_data1["Time"].iloc[-1] 
fs = 1000.0  # Sampling frequency (Hz)
duration1 = signal_len1 / fs  # Duration of the signal (seconds)
time1 = np.linspace(0, duration1, int(fs*duration1))  # Time vector

peaks1, _ = find_peaks(signal1, height= 0.05, distance= 100)
troughs1, _ = find_peaks(-signal1, height=0, distance= 100)


#file 2

filename2 = "AB4113B-LW100-R_P3.csv"
# Importing data from the piezoelectric sensor
raw_data2 = pd.read_csv(filename2)
data2 = raw_data2["Volts"].values
presignal2 = np.delete(data2, 1, 0)
signal2 = presignal2.flatten()

# creating the appropriate time vector
signal_len2 = 0
signal_len2 = raw_data2["Time"].iloc[-1] 
fs = 1000.0  # Sampling frequency (Hz)
duration2 = signal_len2 / fs  # Duration of the signal (seconds)
time2 = np.linspace(0, duration2, int(fs*duration2))  # Time vector

peaks2, _ = find_peaks(signal2, height= 0.04, distance= 100)
troughs2, _ = find_peaks(-signal2, height=0, distance= 100)


# Plot the signal with significant points
plt.figure(figsize=(18, 6))

#plotting file 1
plt.plot(time1, signal1, color=color1, label="Group 2")
plt.plot(time1[peaks1], signal1[peaks1], 'ro')
plt.plot(time1[troughs1], signal1[troughs1], 'go')

#plotting file 2
plt.plot(time2, signal2, color=color2, label='Group 1')
plt.plot(time2[peaks2], signal2[peaks2], 'ro', label='Peaks')
plt.plot(time2[troughs2], signal2[troughs2], 'go', label='Troughs')

plt.xlabel('Time (s)', fontsize=16)
plt.ylabel('Amplitude (V)', fontsize=16)
plt.legend()
plt.show()
