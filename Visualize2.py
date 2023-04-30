import pandas as pd
from scipy.stats import chi2_contingency

# Read the data from the CSV file
df = pd.read_csv("NewFiles/sex.csv", index_col=0).astype(float, errors='ignore')

# Select only the relevant rows for the Chi-squared test
df = df.loc[["Female", "Male", "Other"], :]

# Remove the 'Total first degree' column as it's not needed for the Chi-squared test
df = df.drop(columns=["Total first degree"])

# Convert the DataFrame to numeric values
df = df.apply(pd.to_numeric, errors='coerce')

# Perform the Chi-squared test
chi2, p_value, dof, expected_frequencies = chi2_contingency(df)

# Print the results
print("Contingency Table:")
print(df)
print(f"Chi2 Statistic: {chi2:.2f}")
print(f"P-Value: {p_value:.2e}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies:")
print(pd.DataFrame(expected_frequencies, columns=df.columns, index=df.index))
