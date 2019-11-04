import pandas as pd
import os

os.chdir("C:\Duke")
df = pd.read_csv("FL.csv", sep=",")
#itr_csv = pd.read_csv("arcos-fl-statewide-itemized.tsv.gz", iterator=True, chunksize=500000, low_memory = False, encoding = 'utf-8',error_bad_lines=False) 
#df = pd.concat([chunk for chunk in itr_csv]) ##failed to load in chunk.... don't know why
#to_parquet(df, FL_drug, engine='auto', compression='snappy', index=None, partition_cols=None, **kwargs)### doesn't work....
df.shape
list(df.columns.values)
#take a look at elemants and column names
# since reporters are all distributer we can drop it
######drop columns that we think we don't need
df1 = df.drop(columns = ['ACTION_INDICATOR', 'ORDER_FORM_NO', 'CORRECTION_NO', 'STRENGTH', 'Combined_Labeler_Name','TRANSACTION_ID', 'Ingredient_Name', 'Measure', 'BUYER_BUS_ACT','BUYER_NAME', 'BUYER_CITY','NDC_NO', 'Revised_Company_Name', 'UNIT',"Unnamed: 0","DRUG_NAME","TRANSACTION_CODE","BUYER_ZIP"])
list(df1.columns.values)
"""
df1 = df.drop(columns = ['REPORTER_BUS_ACT','REPORTER_ADDRESS1', 'REPORTER_DEA_NO','REPORTER_NAME','REPORTER_ADDL_CO_INFO','REPORTER_ADDRESS1', 'REPORTER_ADDRESS2','REPORTER_CITY','REPORTER_ZIP','REPORTER_COUNTY','BUYER_DEA_NO','BUYER_ADDL_CO_INFO', 'BUYER_ADDRESS1', 'BUYER_ADDRESS2','Product_Name','Reporter_family','MME_Conversion_Factor','Combined_Labeler_Name', 'Revised_Company_Name','Measure','ACTION_INDICATOR', 'ORDER_FORM_NO',"CORRECTION_NO",'CORRECTION_NO'])
#df1.to_csv("FL")###after processed we can save it
"""
df1.shape## check data frame size
df1.head()
"""
from datetime import datetime
date = datetime.striptime(str(df1['ACTION_INDICATOR']),'%m%d%Y')####process with string data
date.strftime()####we can use datetime to process date data
"""
######or, we can just drop any columns that contains na value
#df1 = df.dropna(axis='columns')

df2 = df1[['TRANSACTION_DATE', "BUYER_STATE"]].copy() #create a data frame for computation need
df2.head()#take a look!
df1["year"] = df1["TRANSACTION_DATE"]%10000 ##extract year
df2["month and date"] = df1["TRANSACTION_DATE"]//10000 ##extract month and date to df2 for futher computation
df1["month"] = df2["month and date"]//100 ## extract date
df1["day"] = df2["month and date"]%100#extract day
df1["year/month"] = df1["year"]*100 + df1["month"]#combine year and month
df1 = df1.drop(columns = ['TRANSACTION_DATE'])#drop original column
df1.head()


######group data together#######
###### still in progress ######
df3 = df1.copy()#mak a copy
df3['quantity'] = df1.groupby(['BUYER_COUNTY', 'year/month', 'DRUG_CODE'])["QUANTITY"].transform(sum)#aggregation function and group data by county and month
df3 = df1.groupby([ 'BUYER_COUNTY', 'year/month', 'DRUG_CODE',"BUYER_STATE","MME_Conversion_Factor"], as_index = False).sum()
df3.head()
df3.to_csv("FL_cleaned_grouped.csv")






#===============================================================================
#######we don't need them... maybe, leave them in case we still need them####
############################################################################
######################### clean Product_Name column ########################
############################################################################
##change the column names to see if there's anything should be modified
#########use replace to merge data that represent same thing but in different string name#######
df1['Product_Name'] = df1['Product_Name'].replace(to_replace = ['HYDROCODONE BIT. 7.5MG/ACETAMINOPHEN', 'HYDROCODONE BIT.7.5MG/ACETAMINOPHEN','HYDROCODONE BITARTRATE & ACETA 7.5MG','HYDROCODONE BITARTRATE AND ACETA 7.5','HYDROCODONEBITARTRATE & ACETA  7.5MG'], value = 'HYDROCODONE BIT. 7.5MG/ACETAMINOPHEN').copy()
set(df1['Product_Name'])####after replace, we take a look of the column again to see if still need further modification
df1['Product_Name'] = df1['Product_Name'].replace(to_replace = [ 'HYDROCODONE BIT. 10MG/ACETAMINOPHEN','HYDROCODONE BITARTRATE 10MG/ACETAMIN','HYDROCODONE BITARTRATE AND ACETA 10M'], value = 'HYDROCODONE BIT. 10MG/ACETAMINOPHEN').copy()
set(df1['Product_Name'])
############################################################################

set(df1['BUYER_BUS_ACT'])
df1.loc[df1["BUYER_BUS_ACT"]=="CHAIN PHARMACY"]
df1.loc[df1["BUYER_BUS_ACT"]=="RETAIL PHARMACY"]
df1['BUYER_BUS_ACT'] = df1['BUYER_BUS_ACT'].replace(to_replace = ["PRACTITIONER-DW/275"], value = 'PRACTITIONER').copy()
set(df1['QUANTITY'])



datalist = list()
for row, date in enumerate(arcos_fl['TRANSACTION_DATE']):
    date_raw = str(date)
    date_object = datetime.strptime(date_raw, '%m%d%Y')
    #date_string = date_object.strftime('%m/%d/%Y')
    date_string = date_object.strftime('%Y')
    datalist.append(date_string)
arcos_fl['Year'] = pd.DataFrame(datalist)
arcos_fl = arcos_fl.drop(['TRANSACTION_DATE'], axis=1)

arcos_fl = arcos_fl.groupby(['BUYER_COUNTY','Year','DRUG_CODE'], as_index=False).sum()