# Univariate Analysis
# Univariate analysis is a type of data analysis that focuses on examining and understanding the characteristics of a single variable in a dataset. It involves summarizing and visualizing the distribution, central tendency, and variability of the variable to gain insights into its behavior.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore

df = pd.read_csv('data.csv')  # Load your dataset
plt.show()

# Categorical Variable Analysis
sns.countplot(data =df, x=df['Survived'])  # Count plot for categorical variable 'Survived'

# find the percentage of each category
category_percentages = (df['Survived'].value_counts() / len(df)) * 100
print("Percentage of each category in 'Survived':")
print(category_percentages)
# example of a categorical variable: 'Survived' (0 = No, 1 = Yes)

# using pie chart to visualize the distribution of the categorical variable 'Survived'
survived_counts = df['Survived'].value_counts()
survived_labels = ['Not Survived', 'Survived']
plt.figure(figsize=(6, 6))
plt.pie(survived_counts, labels=survived_labels, autopct='%1.1f%%')
plt.title('Distribution of Survived')
plt.show()