import pandas as pd
import numpy as np
df=pd.read_csv("C:/Users/august/Downloads/covid.csv")
print(df.describe())
print(df.info)
print(list(df.iloc[:,0])
numbers=[500,1000,5000]
def death_rate(data, numbers):
    for n in numbers:
        filtered_data = data[data['Active'] > n]
        if not filtered_data.empty:
            death_rate_value = filtered_data['Deaths'].mean() / filtered_data['Confirmed'].mean()
            print(f"For Active cases > {n}, the death rate is: {death_rate_value}")
        else:
            print(f"No data for Active cases > {n}")
death_rate(df,numbers)
