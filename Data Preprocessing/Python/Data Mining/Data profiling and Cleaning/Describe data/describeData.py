import pandas as pd
import re

da = pd.read_csv("OUT_2_TreatMissingBy_modify.csv", sep=';')


# Null values removal
da.dropna(inplace = True)

#percentile list
perc =[.05, .10, .25, .50, 0.75, 0.90, 0.95] 

# list of dtypes to include 
include =['float', 'int'] 
ch = ['character', "object"]

# calling describe method 
#desc = da.describe(percentiles = perc, include = 'all') 
#desc = da.describe(percentiles = perc, include = include).transpose()

desc = da.describe(percentiles = perc, include = include)
desc_ = da.describe(include = ch)
d_Null = da.isnull()

print(d_Null)
print(desc)
print(desc_)