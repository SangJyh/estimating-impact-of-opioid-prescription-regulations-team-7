import os
import glob
import pandas as pd
import numpy as np

os.getcwd()
os.chdir("/Users/josephlee/estimating-impact-of-opioid-prescription-regulations-team-7/10_code/Concatenate")

# concatenate 51 files and export : "output.csv"
interesting_files = glob.glob("/Users/josephlee/estimating-impact-of-opioid-prescription-regulations-team-7/10_code/Concatenate/*.csv") 
df = pd.concat((pd.read_csv(f, header = 0) for f in interesting_files))
df.to_csv("output.csv")


#
df1 = pd.read_csv("output.csv")
df1.head()
df1['BUYER_STATE'].describe()
