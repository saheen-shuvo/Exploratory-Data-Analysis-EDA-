# Analytical view of dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore

df = pd.read_csv('titanic.csv')

df.shape # (891, 12)

print("Total number of rows:", df.shape[0])
print("Total number of columns:", df.shape[1])

# find first 10 rows of the dataset
print(df.head(10))

# find sample of 10 rows of the dataset
print(df.sample(10)) 