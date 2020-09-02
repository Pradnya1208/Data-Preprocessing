import pandas as pd 
import numpy as np 

# Create a dictionary for the dataframe 
dict = {'Name': ['A', 'B', 'C', 
				'D', 'E'], 
		'Age': [23, 21, np.inf, -np.inf, 32], 
		'Marks': [40, 54, 63, 77, 88]} 

# Converting Dictionary to Pandas Dataframe 
df = pd.DataFrame(dict) 
df_filter = df.isin([np.nan, np.inf, -np.inf])
# Masking df with the filter 
df_ = df[~df_filter] 

# Dropping rows with nan values 
df_.dropna(inplace=True)


