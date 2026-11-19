# Statistical profiling is a technique used to analyze the performance of a program by collecting and analyzing statistical data about its execution. It helps identify performance bottlenecks, optimize code, and improve overall efficiency.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore

df = pd.read_csv('titanic.csv')

df.describe() # statistical summary of the dataset

# All cols should be numeric for statistical profiling. If not, we can convert them to numeric using encoding techniques.