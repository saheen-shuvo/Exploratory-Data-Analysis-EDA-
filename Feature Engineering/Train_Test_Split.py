# Train Test Split is a technique used to evaluate the performance of machine learning models. It involves dividing the dataset into two subsets: one for training the model and another for testing its performance. This helps in assessing how well the model generalizes to unseen data.

# Train-Test Split is an essential step in the machine learning pipeline, as it allows us to evaluate the model's performance on unseen data and prevent overfitting.

# Steps
# 1. Import the necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split

# 2. Load the dataset
df = pd.read_csv('titanic.csv')

# 3. Separate the features and target variable
X = df.drop('Survived', axis=1)

y = df['Survived']

# 4. Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Display the shapes of the training and testing sets
print("Training set shape:", X_train.shape, y_train.shape)
print("Testing set shape:", X_test.shape, y_test.shape)

