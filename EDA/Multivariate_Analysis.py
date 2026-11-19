# Multivariate Analysis
# Multivariate analysis is a type of data analysis that focuses on examining and understanding the relationships between multiple variables in a dataset. It involves summarizing and visualizing the interactions, correlations, and dependencies among the variables to gain insights into their behavior.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore

df = pd.read_csv('data.csv')  # Load your dataset

sns.countplot(data=df, x='Survived', hue='Sex')  # Count plot for 'Survived' with 'Sex' as hue

# find the percentage of each category in 'Survived' for each 'Sex'
survived_sex_percentages = df.groupby('Sex')['Survived'].value_counts(normalize=True).unstack() * 100
print("Percentage of each category in 'Survived' for each 'Sex':")
print(survived_sex_percentages)

