import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('NewFiles/sex.csv', index_col=0)

# Remove the 'Total first degree' column, as it's not needed for the analysis
df = df.drop(columns='Total first degree')

# Select only the rows related to gender
gender_df = df.loc[['Female', 'Male', 'Other']]

# Plot observed frequencies (contingency table)
gender_df.plot(kind='bar', stacked=True)
plt.title('Observed Frequencies')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.legend(title='Graduation Classification', loc='upper left')
plt.show()

# Calculate expected frequencies
chi2, p_value, dof, expected = chi2_contingency(gender_df)

# Convert expected frequencies to DataFrame with similar structure as gender_df
expected_df = pd.DataFrame(expected, index=gender_df.index, columns=gender_df.columns)

# Plot expected frequencies
expected_df.plot(kind='bar', stacked=True)
plt.title('Expected Frequencies')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.legend(title='Graduation Classification', loc='upper left')
plt.show()
