import pandas as pd

# Load the CSV file data into a Data Frame
files_path = './Files'
data_frame = pd.read_csv(files_path + "/Employees.csv")

# Remove any duplicates in the table
data_without_duplicates = data_frame.drop_duplicates()

# Remove any decimal places in the Age column
data_without_duplicates['Age'] = data_without_duplicates['Age'].astype(int)

# Convert the USD salary to EGP
USD_to_EGP = 30.89
data_without_duplicates = data_without_duplicates.copy()
data_without_duplicates['Salary(EGP)'] = data_without_duplicates['Salary(USD)'] * USD_to_EGP

# Print in the console some stats:

# Average Age
ages_average = data_without_duplicates['Age'].mean()
print(f"Average age = {ages_average}")

# Median Salaries
salaries_median_USD = data_without_duplicates['Salary(USD)'].median()
salaries_median_EGP = data_without_duplicates['Salary(EGP)'].median()
print(f"Median salaries in USD = {salaries_median_USD}")
print(f"Median salaries in EGP = {salaries_median_EGP}")

# Ratio between males and female employees
males_count = (data_without_duplicates['Gender'] == 'M').sum()
females_count = (data_without_duplicates['Gender'] == 'F').sum()
print(
    f"The ratio between males and female employees is {males_count} : {females_count}")

# Write the data in a new CSV file
data_without_duplicates.to_csv(files_path + "/EmployeesNew.csv", index=False)
