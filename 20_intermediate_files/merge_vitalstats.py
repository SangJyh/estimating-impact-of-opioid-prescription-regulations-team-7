import pandas as pd
import numpy as np

# loading the merged population/shipments data
original = pd.read_csv('merged.csv')

# loading the cleaned vital statistics data by state and year
# sorted to make checking easier
vitalstats = pd.read_csv('../10_code/vs_state_year.csv', index_col='Unnamed: 0')
vitalstats.sort_values(['State', 'Year'], inplace = True)

# grouping original merged data by state and year
original = original.groupby([original['BUYER_STATE'], original['year']], as_index = False).sum()

# renaming columns to match vital stats 
original.rename(columns={'BUYER_STATE':'State', 'year':'Year'}, inplace = True)

# merge new grouped population/shipments data with vital stats data
# sorted to make checking easier
full_merge = pd.merge(original, vitalstats, how = 'outer', on = ['State', 'Year'])
full_merge.sort_values(['State', 'Year'], inplace = True)

full_merge.to_csv('full_merge.csv', index = False)
