import pandas as pd
import io

data = '''\
Student,Date
Joe,December 2017
Bob,April 2018
Joe,December 2018'''

df = pd.read_csv(io.StringIO(data), sep=',')
print(df)

# store a boolean series
boolean = df.duplicated(subset=['Student']).any()
print(boolean, end='\n\n') # True

# First store boolean array, check then remove
duplicate_in_student = df.duplicated(subset=['Student'])
if duplicate_in_student.any():
    print(df.loc[duplicate_in_student], end='\n\n')

# Use drop_duplicates method
df.drop_duplicates(subset=['Student'], inplace=True)
print(df)