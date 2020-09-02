import pandas as pd 
import re


# Dataset1
data = pd.read_csv("dup.csv") 

# sorting by first name 
data.sort_values("First Name", inplace = True) 

# making a bool series 
bool_series = data["First Name"].duplicated() 

# displaying data 
data.head() 

# display data 
data[bool_series] 



# Dataset2
# Convert the dictionary into DataFrame  

s_data = pd.read_csv("OUT_2_TreatMissingBy_modify.csv", sep=';')

df = pd.DataFrame(s_data) 

# Manually add duplicate values
# adding a row
new_row = pd.DataFrame({'EmployeeID':'AB0005', 'Gender':'Male', 'Age':24.0, 
                        'Education':'Graduation', 'EducationType':'Economics', 'MaritalStatus':'Married', 
                        'TotalCompanies':8.0, 'TotalExperience':7.0, 'DistanceToOffice':9.0, 'Department':'ClientSolutions',
                        'Traveltype_last_year': 'Conference', 'BillingRate':73.0, 'MonthlyIncome':2718.0,'Years_at_Company':1.0,'Years_InCurrentRole':0.0,
                        'LastSalaryHike':19.0,'PotentialReview':'Very High','PerformanceReview':'Met Expectations','SatisfactionScore':'Passive', 'JobRole_SatisfactionScore':'Passive',
                        'Overall_SatisfactionScore':'Detractor'},
                                                            index =[0]) 
new_row1 = pd.DataFrame({'EmployeeID':'AB0006', 'Gender':'Male', 'Age':25.0, 
                        'Education':'Graduation', 'EducationType':'Economics', 'MaritalStatus':'Married', 
                        'TotalCompanies':7.0, 'TotalExperience':7.0, 'DistanceToOffice':9.0, 'Department':'ClientSolutions',
                        'Traveltype_last_year': 'Conference', 'BillingRate':74.0, 'MonthlyIncome':2718.0,'Years_at_Company':1.0,'Years_InCurrentRole':0.0,
                        'LastSalaryHike':19.0,'PotentialReview':'Very High','PerformanceReview':'Met Expectations','SatisfactionScore':'Passive', 'JobRole_SatisfactionScore':'Passive',
                        'Overall_SatisfactionScore':'Detractor'},
                                                            index =[0])
# simply concatenate both dataframes 
df = pd.concat([new_row, df]).reset_index(drop = True) 
df = pd.concat([new_row1, df]).reset_index(drop = True)

# describe dataframe
s_d = df.describe(include = 'object') 

df.sort_values("EmployeeID", inplace = True)

#Mulultiple values
dup_series = df["EmployeeID"].duplicated()
df_d = df[dup_series]