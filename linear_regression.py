#import require libraries

import sklearn
import os
import pandas as pd
import numpy as np
import matplotlib as plot

#check working directory and set paths for data location as needed
print(os.getcwd()) # Data in current working directory as data set is small.
redw_path = "/home/danulg/Git/Data604/lr-redw.csv"
whitew_path = "/home/danulg/Git/Data604/lr-whitew.csv"

# Load data 
red_wine = pd.read_csv(redw_path, sep = ";")
white_wine = pd.read_csv(whitew_path, sep = ";")

