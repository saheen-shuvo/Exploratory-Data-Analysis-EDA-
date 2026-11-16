# Univariate Numerical Analysis
# Univariate numerical analysis is a type of data analysis that focuses on examining and understanding the characteristics of a single numerical variable in a dataset. It involves summarizing and visualizing the distribution, central tendency, and variability of the variable to gain insights into its behavior.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore

df = pd.read_csv('data.csv')  # Load your dataset

# histogram for numerical variable 'Age'
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Age', bins=30, kde=True)  # Histogram with KDE for 'Age'
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()