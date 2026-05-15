import numpy as np
import pandas as pd

df = pd.read_csv('anime.csv')

def extract_episodes(txt):
    check = False
    data = ''
    for i in txt:
        if i == '(':
            check = True
        elif i == ')':
            check = False
            return data
        elif check:
            data += i
    return data

df["Episodes"] = df["Title"].apply(extract_episodes)
df['Episodes'] = df['Episodes'].str.replace(' eps', '')
df['Episodes'] = df['Episodes'].astype(int)
print(df)
