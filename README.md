Handling Missing Values Using Pandas

Project Overview

This project demonstrates how to identify and handle missing values in a dataset using Python and the Pandas library.

Missing values are common in real-world datasets. Handling them properly helps improve data quality and makes the dataset suitable for further analysis and machine learning.

Objective

To understand basic data preprocessing techniques and learn how to handle missing values using Pandas.

Tools and Technologies

- Python
- Pandas
- NumPy
- Jupyter Notebook

Dataset Description

A sample employee dataset is created with the following columns:

Column| Description
Name| Employee name
Age| Employee age
Salary| Employee salary
Department| Employee department

The dataset contains some missing values to demonstrate data-cleaning techniques.

Steps Performed

1. Create Dataset

Created a sample employee dataset using Pandas DataFrame.

2. Identify Missing Values

Used "isnull().sum()" to find the number of missing values in each column.

3. Calculate Missing Value Percentage

Calculated the percentage of missing values in every column.

4. Handle Numerical Missing Values

Used the median method to fill missing values in:

- Age
- Salary

5. Handle Categorical Missing Values

Used the mode method to replace missing values in the Department column.

6. Verify Cleaned Dataset

Checked the dataset again to confirm that all missing values were handled.

Pandas Functions Used

Function| Purpose
"pd.DataFrame()"| Creates a dataset
"isnull()"| Identifies missing values
"sum()"| Counts missing values
"median()"| Calculates the median
"mode()"| Finds the most frequent value
"fillna()"| Replaces missing values

Why These Methods Were Used

- Median: Used for numerical columns because it is less affected by extreme values.
- Mode: Used for categorical columns because it replaces missing values with the most frequently occurring category.
- Fillna(): Helps replace missing values without removing useful records.

Final Result

Successfully identified and handled missing values in the employee dataset.

- Original dataset analyzed.
- Missing values identified.
- Numerical values replaced using median.
- Categorical values replaced using mode.
- Cleaned dataset generated successfully.

Conclusion

This task helped me understand the importance of data cleaning and preprocessing. I learned how to use Pandas and NumPy to handle missing values and prepare datasets for machine learning.

Author

Kiran

Internship: Veda Technology
Task: Handling Missing Values Using Pandas 