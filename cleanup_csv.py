# reformats the csv to remove the brackets and add headers
import matplotlib.pyplot as plt

import sys
if len(sys.argv) != 2:
    print("Provide the csv data file name!")
    exit(1)
filename = sys.argv[1]
lines = []

with open(filename) as f:
    lines = f.readlines()

filestr = 'Time,Volts\n'

for line in lines:
     if line != '\n': 
        spl = line.split(",")
        time = spl[0]
        value = spl[1]
        filestr += time + "," + value + "\n"

f = open(filename, "w")
f.write(filestr)
f.close()