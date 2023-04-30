import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




# Using python calculate the summary statistics for the dataset clasenrol like mean, median,
# mode, standard deviation, and range for enrolment and classification data. Use the
# value_counts() function in pandas to find the frequency distribution of different
# classifications. Add any sort of simple visualization so I can put it into the essay and talk
# about it even if it’s just a table.


# Read the CSV file into a DataFrame
df = pd.read_csv('NewFiles/clasenrol.csv').astype(float, errors='ignore')


# Convert the DataFrame into a dictionary with the desired format
data = {
    "Academic_Year": df["Academic Year"].tolist(),
    "Undergraduate": df["Undergraduate"].str.replace(',', '').astype(int).tolist(),
    "First_class_honours": df["First class honours"].str.replace(',', '').astype(int).tolist(),
    "Upper_second_class_honours": df["Upper second class honours"].str.replace(',', '').astype(int).tolist(),
    "Lower_second_class_honours": df["Lower second class honours"].str.replace(',', '').astype(int).tolist(),
    "Third_class_honours_Pass": df["Third class honours/Pass"].str.replace(',', '').astype(int).tolist(),
}

df = pd.DataFrame(data)

# Compute summary statistics
enrolment_summary = df["Undergraduate"].describe()
first_class_summary = df["First_class_honours"].describe()
upper_second_class_summary = df["Upper_second_class_honours"].describe()
lower_second_class_summary = df["Lower_second_class_honours"].describe()
third_class_summary = df["Third_class_honours_Pass"].describe()

# Print summary statistics
print("Enrolment Summary:\n", enrolment_summary)
print("\nFirst Class Summary:\n", first_class_summary)
print("\nUpper Second Class Summary:\n", upper_second_class_summary)
print("\nLower Second Class Summary:\n", lower_second_class_summary)
print("\nThird Class Summary:\n", third_class_summary)


df = pd.DataFrame(data)

# Set the index to 'Academic_Year' to make it easier to plot
df.set_index('Academic_Year', inplace=True)

# Create a bar plot for the frequency distribution
ax = df.plot(kind='bar', figsize=(12, 6))
plt.xlabel("Academic Year")
plt.ylabel("Frequency")
plt.title("Frequency Distribution of Classifications by Academic Year")

# Show the plot
plt.show()


# Assuming 'data' is the dictionary containing the data you provided
df = pd.DataFrame(data)

# Set the index to 'Academic_Year' to make it easier to plot
df.set_index('Academic_Year', inplace=True)

# Calculate the total frequency for each classification across all academic years
total_freq = df.sum(axis=0)

# Create a pie chart for the frequency distribution
ax = total_freq.plot.pie(autopct='%1.1f%%', figsize=(12, 6))
plt.ylabel('')
plt.title("Frequency Distribution of Classifications by Academic Year")

# Show the plot
plt.show()



































# # Melt the DataFrame to bring data into long format
# melted_df = df.melt(id_vars="Academic_Year", var_name="Classification", value_name="Count")

# # Calculate the frequency distribution using value_counts()
# frequency_distribution = melted_df["Classification"].value_counts()

# # Create a bar plot for the frequency distribution
# fig, ax = plt.subplots()
# ax.bar(frequency_distribution.index, frequency_distribution.values)
# plt.xticks(rotation=45)
# plt.xlabel("Classification")
# plt.ylabel("Frequency")
# plt.title("Frequency Distribution of Classifications")

# # Show the plot
# plt.show()
