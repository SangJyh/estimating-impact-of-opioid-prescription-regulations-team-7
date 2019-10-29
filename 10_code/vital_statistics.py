import pandas as pd
import os

# Folder where all vital statistics txt files are held
directory = '/Users/vanessatang/estimating-impact-of-opioid-prescription-regulations-team-7/00_source/US_VitalStatistics/'

# Loop through directory to get list of filenames 
all_vs_fn = []

for filename in os.listdir(directory):
    if filename.endswith(".txt"): 
         all_vs_fn.append(filename)

# Loop through list of filenames and add directory to get filepath for each txt file
all_vs_fp = []

for file in all_vs_fn:
    fp = directory + file
    all_vs_fp.append(fp)
        
# Loop through list of filepaths
# Append each dataframe with columns of interest (cols)

all_vital_statistics = pd.DataFrame()

cols = ['County', 'County Code', 'Year', 'Drug/Alcohol Induced Cause', 'Drug/Alcohol Induced Cause Code', 'Deaths']

for fp in all_vs_fp:
    df = pd.read_csv(fp, sep = '\t', usecols = cols)
    all_vital_statistics = all_vital_statistics.append(df, ignore_index = True)

all_vital_statistics.head()

# Rename County Code colunn to FIPS to be able to merge in the future
all_vital_statistics = all_vital_statistics.rename(columns={"County Code": "FIPS"})

all_vital_statistics.sample(10)
all_vital_statistics.shape

all_vital_statistics.to_csv('all_vital_statistics.csv')
