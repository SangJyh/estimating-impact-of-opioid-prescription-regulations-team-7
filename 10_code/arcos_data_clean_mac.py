#from arcos_data_clean import clean
import pandas as pd
import os
dir_path = os.path.dirname(os.path.realpath('arcos_data_clean.py'))#set .py file path for future use
lst = ['ar','de','fl','tx','wa']
#lst = ['al','az','ca','co', 'ct','ga','hi', 'ia', 'id', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md','me','mi','mn','mo','ms','mt','ne','nv', 'nh', 'nj','nm','ny','nc', 'nd', 'oh', 'ok', 'or', 'pa', 'pr', 'ri' , 'sc','sd','tn','ut','vt', 'va', 'wv', 'wi', 'wy'] 
#except Alaska and Washington D.c.
#create read list  ##backup 'fl','wa','tx','ak','al','az','ca','co', 'ct','ga','hi', 'ia', 'id', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md','me','mi','mn',
for i in lst:
    read_file = "/Users/josephlee/Downloads/arcos-{}-statewide-itemized.tsv.gz".format(i)#read file name
    print("now process {} data".format(i))
    df = pd.read_csv(read_file, sep="\t")#read files
#df.shape
#list(df.columns.values)
#take a look at elemants and column names
# since reporters are all distributer we can drop it
######drop columns that we think we don't need
    df1 = df.drop(columns = ['REPORTER_BUS_ACT','REPORTER_ADDRESS1', 'REPORTER_DEA_NO','REPORTER_NAME' ,'REPORTER_ADDL_CO_INFO' , 'REPORTER_ADDRESS1' , 'REPORTER_ADDRESS2' , 'REPORTER_CITY' ,'REPORTER_ZIP' , 'REPORTER_COUNTY' , 'BUYER_DEA_NO' , 'BUYER_ADDL_CO_INFO' , 'BUYER_ADDRESS1' , 'BUYER_ADDRESS2' , 'Product_Name' , 'Reporter_family'  , 'Combined_Labeler_Name' , 'Revised_Company_Name' , 'Measure' , 'ORDER_FORM_NO' , "CORRECTION_NO" , 'CORRECTION_NO' , 'ACTION_INDICATOR','ORDER_FORM_NO', 'CORRECTION_NO', 'STRENGTH', 'REPORTER_STATE', 'Combined_Labeler_Name','TRANSACTION_ID','Ingredient_Name', 'Measure', 'BUYER_NAME', 'BUYER_CITY','NDC_NO', 'Revised_Company_Name' , 'UNIT' , "DRUG_NAME" , "TRANSACTION_CODE","BUYER_ZIP"])##  this sounds important 'MME_Conversion_Factor'
#list(df1.columns.values)#check columns again
#df1.shape## check data frame size
#df1.head()
######or, we can just drop any columns that contains na value
#df1 = df.dropna(axis='columns')# might not be a good idea
#########

    df1["year"] = df1["TRANSACTION_DATE"]%10000 ##extract year
    #df1["month"] = (df1["TRANSACTION_DATE"]//10000)//100 ## extract month
    #df1["year/month"] = df1["year"] *100 + df1["month"]#combine year and month
    df1 = df1.drop(columns = ['TRANSACTION_DATE'])#drop original column       'month'
#df1.head()
######group data together#######
###### still in progress ######
    df2 = df1.copy() #mak a copy
    df2['quantity'] = df1.groupby(['BUYER_COUNTY', 'year', 'DRUG_CODE', "MME_Conversion_Factor"])["QUANTITY"].transform(sum)
#aggregation function and group data by county and month    ###I keep df1 unchanged for possible future need
#df2.head()
#df2 = df1.groupby([ 'BUYER_COUNTY', 'year/month', 'DRUG_CODE',"BUYER_STATE"], as_index = False).sum()
    df2 = df2.drop('QUANTITY',axis=1) 
    df2['MME'] = df2['CALC_BASE_WT_IN_GM'] * df2['MME_Conversion_Factor']
    df2 = df2.drop_duplicates(subset = ['BUYER_STATE','year', 'DRUG_CODE','quantity', 'MME'], keep='first').copy()
    write = "/Users/josephlee/Downloads/{}_cleaned_grouped.csv".format(i.upper())
    df2.to_csv(write, index =False)
######end of first clean stage##########