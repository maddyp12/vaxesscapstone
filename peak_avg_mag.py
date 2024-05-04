from scipy.signal import find_peaks
import numpy as np
import pandas as pd

#import sys
#if len(sys.argv) != 2:
    #print("Provide the csv data file name!")
    #exit(1)
#filename = sys.argv[1]

filename = "AB4113B-LW100-R_P1.csv"

# Importing data from the piezoelectric sensor
raw_data = pd.read_csv(filename)
data = raw_data["Volts"].values
presignal = np.delete(data, 1, 0)
signal = presignal.flatten()

# Creating the appropriate time vector
signal_len = 0
signal_len = raw_data["Time"].iloc[-1] 
fs = 1000.0  # Sampling frequency (Hz)
duration = signal_len / fs  # Duration of the signal (seconds)
time = np.linspace(0, duration, int(fs*duration))  # Time vector

# Find peaks and troughs in the filtered signal
peaks, _ = find_peaks(signal, height= 0.01, distance= 150)
troughs, _ = find_peaks(-signal, height=0, distance= 60)

avg_peak_mag= np.mean(signal[peaks])
num_breaths= len(peaks)

print(avg_peak_mag, num_breaths)
