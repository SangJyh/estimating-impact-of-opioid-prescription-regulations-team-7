import os
import pandas as pd
import numpy as np

os.getcwd()

d1=pd.read_csv("/Users/josephlee/estimating-impact-of-opioid-prescription-regulations-team-7/10_code/Concatenate/output.csv")
d2=pd.read_csv("/Users/josephlee/estimating-impact-of-opioid-prescription-regulations-team-7/00_source/population/pop_counties_20062012.csv")

merge=pd.merge(d1, d2, on=['BUYER_STATE','BUYER_COUNTY','year'], how='inner')
merge.head()
dr= ['countyfips','STATE','COUNTY','county_name','NAME','variable']
merge=merge.drop(columns=dr)
merge.head()

merge.to_csv("merged.csv",index = False)
