# Numerical Missing Imputation in Feature Engineering
# Using numerical missing imputation techniques is an important step in feature engineering, as missing data can lead to biased estimates and reduced model performance. There are several techniques to handle missing values, including:
# 1. Imputing with the mean
# 2. Imputing with the median
# 3. Imputing with the mode
# 4. Using advanced imputation techniques like KNN or MICE

# Using Pandas, we can easily impute missing values in a dataset. Below is an example of how to impute missing values in a numerical column using the mean, median, and mode.
import pandas as pd
import seaborn as sns # type: ignore
from sklearn.model_selection import train_test_split

df = pd.read_csv('titanic.csv')

X = df.drop('Survived', axis=1)

y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Using mean imputation
age_mean = df['Age'].mean()

X_train['age_mean_imputed'] = X_train['Age'].fillna(age_mean)

X_test['age_mean_imputed'] = X_test['Age'].fillna(age_mean)

# Using median imputation
age_median = df['Age'].median()

X_train['age_median_imputed'] = X_train['Age'].fillna(age_median)

X_test['age_median_imputed'] = X_test['Age'].fillna(age_median)

# KDE Plot
sns.kdeplot(X_train['age_mean_imputed'], label='Mean Imputation', color='blue')