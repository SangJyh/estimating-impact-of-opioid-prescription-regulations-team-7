import os
import pandas as pd
import numpy as np

os.getcwd()

#d1=pd.read_csv("/Users/josephlee/estimating-impact-of-opioid-prescription-regulations-team-7/10_code/Concatenate/output.csv")
d1=pd.read_csv("C:/Duke/2019_fall/690_python/estimating-impact-of-opioid-prescription-regulations-team-7/10_code/Concatenate/output.csv")
d1.head()
#d2=pd.read_csv("/Users/josephlee/estimating-impact-of-opioid-prescription-regulations-team-7/00_source/population/pop_counties_20062012.csv")
d2=pd.read_csv("C:/Duke/2019_fall/690_python/estimating-impact-of-opioid-prescription-regulations-team-7/00_source/population/population_03-15.csv")
d2.head()
d2['BUYER_COUNTY']= d2['BUYER_COUNTY'].str.upper()
merge=pd.merge(d1, d2, on=['BUYER_STATE','BUYER_COUNTY','year'], how='outer')
merge.sample(5)
#dr= ['countyfips','STATE','COUNTY','county_name','NAME','variable']
merge1=merge[['BUYER_COUNTY','BUYER_STATE','mme','year','population']].copy()
merge1.sort_values(['year'])

merge1.to_csv("merged.csv",index = False)
