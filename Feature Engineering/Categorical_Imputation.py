# Categorical Value Imputation with Mode value

from sklearn.impute import SimpleImputer
import pandas as pd
# Load the dataset
df = pd.read_csv('titanic.csv')

X = df.drop('Survived', axis=1)
y = df['Survived']

# Create a SimpleImputer object with the desired strategy (most_frequent)
embarked_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')

# Fit the imputer on the training data
embarked_imputer.fit(X[['Embarked']])

# Transform the training and test data
X['Embarked'] = embarked_imputer.transform(X[['Embarked']])

y['Embarked'] = embarked_imputer.transform(y[['Embarked']])