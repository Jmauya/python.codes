import pandas as pd


df = pd.DataFrame({'temperature (F)': [32, 212, 98.6, 68]})
df

df['temperature (C)'] = df['temperature (F)'].apply(lambda x: (x - 32) * 5/9)
df
