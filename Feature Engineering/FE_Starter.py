# Feature Engineering Starter
# Step1: Delete the columns which are not useful for the model building. For example, if we have a column which has only one unique value, then it is not useful for the model building. So, we can delete that column.
import pandas as pd

df = pd.read_csv('titanic.csv')

df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

# Step2: Separating features and target variable. For example, if we have a column which is the target variable, then we can separate that column from the features.

X = df.drop('Survived', axis=1)

y = df['Survived']