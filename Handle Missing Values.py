import pandas as pd
import numpy as np

# Creating a sample employee dataset
data = {
    "Name": ["Kiran", "Ravi", "Priya", "Suresh", "Anu", "Rahul"],
    "Age": [23, np.nan, 22, 25, np.nan, 24],
    "Salary": [30000, 40000, np.nan, 35000, 45000, np.nan],
    "Department": ["IT", "HR", "IT", np.nan, "Finance", "HR"]
}

df = pd.DataFrame(data)

# Displaying the original data
print("Original Employee Data:")
print(df)

# Finding missing values
print("\nChecking Missing Values:")
print(df.isnull().sum())

# Finding missing value percentage
print("\nMissing Value Percentage:")
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage)

# Replacing missing Age and Salary with median values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

# Replacing missing Department with the most common value
most_common_department = df["Department"].mode()[0]
df["Department"] = df["Department"].fillna(most_common_department)

# Displaying the updated dataset
print("\nEmployee Data After Cleaning:")
print(df)

# Checking whether any missing values remain
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nMissing Values Handled Successfully!")
