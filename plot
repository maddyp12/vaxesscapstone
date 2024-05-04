# Plot
# 28FEB2024
# Author: Shanni Zhou

import matplotlib.pyplot as plt
import os
import csv
import pandas as pd

testNum = 2 # CHANGE THIS
filename = ".venv\\Demo\\demo.csv"


try: 
    df = pd.read_csv(filename, header=None)
    average = (filename[1])
    df.plot(x=0, y=1, kind='line', color='blue')
    plt.title('Plot of DataFrame Columns')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

except KeyboardInterrupt:
    print('Quit')
