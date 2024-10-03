import pandas as pd
df = pd.read_csv('unclean_data 1.csv',encoding = 'ANSI') # opens csv file same way youd read it normally
 
columns = df.columns # prints name of colums (keys of the table dictionary)
columns = str(df.columns).upper() #makes it upper, df.columns.str.upper() works too
print(columns)
 
#to rename
#df = df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'}) 
df = df.rename(columns = {'duration' : 'length'}) # use same case as original name not the upper, upper doesnt rewrite just prints
columns = df.columns
print(columns)

#missing data
pd.set_option('display.max_columns',None)
print(df.isnull(),'\n')# shows if data is missing from a data point, true = empty, false = theres data
print(df.isnull().any(),'\n') # shows each column instead of each spot
print(df.isnull().sum(),'\n') # shows how many empty spots in each column
print(df.isnull().sum().sum(),'\n') # shows how many empty spots in whole file
