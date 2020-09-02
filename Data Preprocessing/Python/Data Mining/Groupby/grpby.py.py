import pandas as pd
import re
import numpy as np

s_data = pd.read_csv("OUT_2_TreatMissingBy_modify.csv", sep=';')

# Convert the dictionary into DataFrame  
df = pd.DataFrame(s_data) 
print((df[['EmployeeID', 'Gender', 'Age', 'Education']]).head(8))


# Groupby
gb = df.groupby('Education')
print(gb.first())

row_ = s_data.iloc [[3, 4],[0,1,2,3,4]]
gb_r = row_.groupby('Education')
print(gb_r.first())

# Using multiple keys in 
# groupby() function 
 
print(df.groupby(['EmployeeID', 'Education']).groups)

row4 = s_data.iloc [:, [ 1, 12]]

#combined monthly income
s = row4.groupby(['Gender']).sum()
print(s)

# selecting a single group 

grp = df.groupby(['Education', 'Gender']) 
s_grp = grp.get_group(('Masters / PHD', 'Female'))
print(s_grp)

###############################################################################
# Applying Functions to Groups
###############################################################################

# Aggregation
grp_agr = df.groupby('Education')
gr_a = grp_agr['TotalExperience'].agg([np.sum, np.mean, np.std])

# using different aggregation function by passing dictionary to aggregate 
grp_agr1 = df.groupby('EducationType') 
gr_a1 = grp_agr1.agg({'Age' : 'mean', 'TotalExperience' : 'mean', 'MonthlyIncome':'std'})


# Transformation (TODO)
# using transform function 
grp_t = df.groupby('EmployeeID') 
grp_t_ = grp_t['Age']
sc = lambda x: (x - x.mean()) / x.std()*10
gr_t = grp_t_.transform(sc)

# Filtration
grp_fi = df.groupby('EmployeeID') 
gr_fi = grp_fi.filter(lambda x: len(x) >= 1)