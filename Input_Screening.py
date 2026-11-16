# Input Screening


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore

df = pd.read_csv('titanic.csv')

# find missing values in the dataset
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# check for duplicate rows in the dataset
duplicate_rows = df.duplicated().sum()
print("Number of duplicate rows:", duplicate_rows)

# Drop duplicate
df.drop_duplicates(inplace=True)