import pandas as pd
import re
import numpy as np
import seaborn as sns

s_data = pd.read_csv("OUT_2_TreatMissingBy_modify.csv", sep=';')
df_iqr = pd.DataFrame(s_data)



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

df_out1 = remove_outlier(df_iqr,'Years_at_Company')
df_out2 = remove_outlier(df_iqr,'Years_InCurrentRole')


bplot1 = sns.boxplot(x='Years_InCurrentRole', #Years_at_Company
                 data=df_iqr, 
                 width=0.5,
                 palette="colorblind")
# bplot1 = sns.swarmplot(x='Years_InCurrentRole', #Years_at_Company
#                  data=df_iqr, 
#                  width=0.5,
#                  palette="colorblind", color=".25")


bplot1.axes.set_title("Outlier detection",
                    fontsize=16)
 
bplot1.set_xlabel("Years_InCurrentRole", 
                fontsize=14)
 
bplot1.tick_params(labelsize=10)


