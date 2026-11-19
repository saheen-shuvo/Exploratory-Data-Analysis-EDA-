# Y Data Profiling - This script is used to profile the data in the Y dataset. It provides insights into the structure, distribution, and quality of the data, helping to identify potential issues and areas for improvement.

# Install required libraries
# pip install ydata__profiling

from ydata_profiling import ProfileReport # type: ignore

# Load your dataset
import pandas as pd

df = pd.read_csv('titanic_data.csv')  

# Generate a profile report
profile = ProfileReport(df, title="Titanic Data Profile")
profile.to_file("titanic_data_profile.html")