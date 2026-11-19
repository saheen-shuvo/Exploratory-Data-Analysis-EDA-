from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('titanic.csv')

X = df.drop('Survived', axis=1)

y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a SimpleImputer object with the desired strategy (mean, median, or most_frequent)
age_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

#  FIt vs Transform
# Fit helps the imputer learn the statistics (mean, median, or most frequent value) from the training data. Transform applies the learned statistics to fill in the missing values in the dataset.
# Transform is applied to the training data, and the same statistics are used to fill in missing values in the test data.

# Fit the imputer on the training data
age_imputer.fit(X_train[['Age']])

# Transform the training and test data
X_train['Age'] = age_imputer.transform(X_train[['Age']])

X_train