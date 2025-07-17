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

# We will limit the analysis to just red wine here. We start by splitting our data into train and test sets.
# We could include a validation set as well, but this will add another level of complexity. We avoid this for 
# the time being. 
# 
# Our goal is to build a model that works well on unseen data. For this reason, we will not touch the test set
# at this point 

# Exploratory data analysis
# Test / validation /  training splits are done under the assumption that random subsets of the data have 
# similar structure. If not, the 
