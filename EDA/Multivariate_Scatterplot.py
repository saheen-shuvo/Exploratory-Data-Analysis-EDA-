# Multivariate Scatterplot
# A multivariate scatterplot is a type of data visualization that allows us to explore the relationships between three or more variables in a dataset. It extends the concept of a traditional scatterplot by incorporating additional dimensions, such as color, size, or shape, to represent different variables.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore

df = pd.read_csv('data.csv')  # Load your dataset
plt.show()

# Create a multivariate scatterplot using Seaborn's scatterplot function
sns.scatterplot(data=df, x='Variable1', y='Variable2', hue='Category', size='Variable3', style='Variable4')

# Customize the plot with titles and labels
plt.title('Multivariate Scatterplot')
plt.xlabel('Variable 1')
plt.ylabel('Variable 2')