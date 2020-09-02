import pandas as pd
import re
import numpy as np

s_data = pd.read_csv("OUT_2_TreatMissingBy_modify.csv", sep=';')
df_m = pd.DataFrame(s_data)
df_m_ = pd.DataFrame(s_data)
# Get missing values in the form of dataframe
df_mi = df_m.isnull()

# Gives column name with True if NaN present
print(df_m.isnull().any())

# Get the count of missing values columnwise
# Method1
print(df_m.isnull().sum())
# Method2
print(df_m.isna().sum())
# Method3
count_nan = len(df_m) - df_m.count()
print(count_nan)

# Total missing values
print(df_m.isnull().sum().sum())

# Get the count of missing values of rows in panda frame
# Method1
df_r = df_m.isnull().sum(axis = 1)
# Method2
for i in range(len(df_m.index)):
    if df_m.iloc[i].isnull().sum().any():
        print("Null value in row " + str(i) + " is : " + str(df_m.iloc[i].isnull().sum()))
        
        
# Count null values in particular column of dataframe
print(df_m.Gender.isnull().sum())
print(df_m.Years_at_Company.isnull().sum())

# Count of missing values in a column by group
print(df_m.groupby(['Education'])['Age'].apply(lambda x: x.isnull().sum()))
print(df_m.groupby(['Gender'])['EducationType'].apply(lambda x: x.isnull().sum()))
print(df_m.groupby(['Gender'])['Age'].apply(lambda x: x.isnull().sum()))



###############################################################################
# Removing missing values
# isnull()
# notnull()
# dropna()
# fillna()
# replace()
# interpolate()
###############################################################################

# fillna #TODO
df_m_.dropna(how  = 'all')

