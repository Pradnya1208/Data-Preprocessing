import pandas as pd
import re
import numpy as np

s_data = pd.read_csv("OUT_2_TreatMissingBy_modify.csv", sep=';')
df = pd.DataFrame(s_data)
df_iqr = pd.DataFrame(s_data)



# method 1
q_low = df["Years_at_Company"].quantile(0.01)
q_hi  = df["Years_at_Company"].quantile(1)

q_low1 = df["Years_InCurrentRole"].quantile(0.01)
q_hi1  = df["Years_InCurrentRole"].quantile(1)


df_filtered = df[(df["Years_at_Company"] < q_hi) & (df["Years_at_Company"] > q_low)]


# Using Z Score
dataset= [10,12,12,13,12,11,14,13,15,10,10,10,100,12,14,13, 12,10, 10,11,12,15,12,13,12,11,14,13,15,10,15,12,10,14,13,15,10]
outliers=[]
def detect_outlier(data_1):
    
    threshold=3
    mean_1 = np.mean(data_1)
    std_1 =np.std(data_1)
    
    
    for y in data_1:
        z_score= (y - mean_1)/std_1 
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers

outlier_datapoints = detect_outlier(dataset)
print(outlier_datapoints)


#######################################
# Applying Z score method on s_data
#######################################
th = 1.6
m = df["Years_InCurrentRole"]
mean_ = np.mean(m)
std_ = np.std(m)

for i in m:
    z_ = (i - mean_)/std_
    if np.abs(z_) > th:
        outliers.append(i)
 
print(outliers)

#######################################
# Using IQR: Inter quartile range
#######################################

def remove_outlier(df_in, col_name):
    q1 = df_in[col_name].quantile(0.25)
    q3 = df_in[col_name].quantile(0.75)
    iqr = q3-q1 #Interquartile range
    fence_low  = q1-1.5*iqr
    print(fence_low)
    fence_high = q3+1.5*iqr
    print(fence_high)
    df_out = df_in.loc[(df_in[col_name] > fence_low) & (df_in[col_name] < fence_high)]
    print(df_out)
    return df_out

df_out = remove_outlier(df_iqr,'Years_InCurrentRole')




