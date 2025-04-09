import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dic=pd.read_csv("C:\\Users\\junai\\OneDrive\\Desktop\\Border_Crossing_Entry_Data.csv")
df=pd.DataFrame(dic)
#print(df)

infromation=df.info()
#print(information)

describe=df.describe()
#print(describe)

h_ead=df.head()
#print(h_ead)

t_ail=df.tail()
#print(t_ail)

drop_na=df.dropna()
#print(drop_na)

is_null_sum=df.isnull().sum()
#print(is_null_sum)

is_null_sum_sum=df.isnull().sum().sum()
#print(is_null_sum_sum)

is_null=df.isnull()
#print(is_null)

unique_value=df['Border'].unique()
#print(unique_value)

us_border_df = df[df['Border'] == 'US-Mexico Border']
#print(us_border_df.head())

df_filled = df.fillna("Unknown")
#print(df_filled)

df.rename(columns={'Port Name': 'Port_Name', 'Measure': 'Entry_Type'}, inplace=True)
#print(df.columns)

summary = df.groupby('Border')['Value'].sum()
#print(summary)

sorted_df = df.sort_values(by='Date', ascending=False)
#print(sorted_df[['Date', 'Border', 'Value']].head())

filtered_df = df[(df['Border'] == 'US-Canada Border') & (df['Value'] > 1000)]
#print(filtered_df)

q1=df['Value'].quantile(0.25)
q3=df['Value'].quantile(0.75)
IQR=q3-q1
lower_bond=q1-1.5*IQR
upper_bond=q3+1.5*IQR
Outlier=df[(df['Value']<lower_bond) | (df['Value']>upper_bond)]
#print(Outlier)

correlation=df.corr(numeric_only=True)
#print(correlation)

covariance=df.cov(numeric_only=True)
#print(covariance)