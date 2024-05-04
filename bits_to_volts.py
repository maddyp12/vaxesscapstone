import pandas as pd

import sys
if len(sys.argv) != 2:
    print("Provide the csv data file name!")
    exit(1)
filename = sys.argv[1]

def conversion(x):
    return x * (5.0 / 4096)


#remove 'header=None' if the csv has the header Time,Bits or whatever at the top of the file
df = pd.read_csv(filename, header=None)

df.iloc[:, 1] = df.iloc[:, 1].apply(conversion)



df.to_csv(filename, index=False, header=False)
