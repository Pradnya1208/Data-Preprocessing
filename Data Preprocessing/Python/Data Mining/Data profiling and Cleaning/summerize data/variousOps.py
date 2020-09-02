import pandas as pd
import re

s_data = pd.read_csv("OUT_2_TreatMissingBy_modify.csv", sep=';')

s1_data = pd.read_csv("OUT_2_TreatMissingBy_modify.csv", sep=';', index_col = 'EmployeeID')

data_top = s_data.head()
print(data_top) 

# creating series 
series = s_data["Gender"] 
  
# returning top n rows 
top = series.head(20) 

print(top)

# Convert the dictionary into DataFrame  
df = pd.DataFrame(s_data) 
print((df[['EmployeeID', 'Gender', 'Age', 'Education']]).head(8))

# adding a row
new_row = pd.DataFrame({'EmployeeID':'AA0001', 'Gender':'Male', 'Age':24.0, 
                        'Education':'Graduation', 'EducationType':'Economics', 'MaritalStatus':'Married', 
                        'TotalCompanies':8.0, 'TotalExperience':7.0, 'DistanceToOffice':9.0, 'Department':'ClientSolutions',
                        'Traveltype_last_year': 'Conference', 'BillingRate':73.0, 'MonthlyIncome':2718.0,'Years_at_Company':1.0,'Years_InCurrentRole':0.0,
                        'LastSalaryHike':19.0,'PotentialReview':'Very High','PerformanceReview':'Met Expectations','SatisfactionScore':'Passive', 'JobRole_SatisfactionScore':'Passive',
                        'Overall_SatisfactionScore':'Detractor'},
                                                            index =[0]) 

# simply concatenate both dataframes 
df = pd.concat([new_row, df]).reset_index(drop = True) 
df.head(5)

# retrieving row by loc method 
first = s1_data.loc[["AB0001", "AB0003"]] 
second = s1_data.loc["AB0005"] 
 
print(first, "\n\n\n", second) 


# retrieving data by iloc method
row = s_data.iloc[3:7]
row2 = s_data.iloc [[3, 4], [0, 1, 2]]
row3 = s_data.iloc [: , [0, 1, 2]]
print(row)
print (row2)
print(row3)

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
  
grp = df.groupby(['MaritalStatus', 'Gender']) 
s_grp = grp.get_group(('Married', 'Female'))
print(s_grp)