import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('NewFiles/enroltf.csv').astype(float, errors='ignore')

# Create a line plot with two y-axes
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot the total enrollment on the first y-axis
ax1.plot(df['Academic Year'], df['Total'], label='Total Enrollment', color='blue')
ax1.set_xlabel('Academic Year')
ax1.set_ylabel('Total Enrollment')
ax1.tick_params(axis='y', labelcolor='blue')

# Create the second y-axis
ax2 = ax1.twinx()

# Plot the tuition fee on the second y-axis
ax2.plot(df['Academic Year'], df['Tuition Fee'], label='Tuition Fee', color='red')
ax2.set_ylabel('Tuition Fee')
ax2.tick_params(axis='y', labelcolor='red')

# Set the title and x-axis labels
plt.title('University Enrollment vs. Tuition Fee')
plt.xticks(rotation=45)

# Show the plot
plt.show()
