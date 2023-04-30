import re
import pandas as pd

# Define the paragraph as a string
paragraph = "In England, tuition fees have been capped at £9,250 since 2017 and are set to remain at this level until 2025. Tuition fees were initially introduced in 1998, under New Labour, at £1,000. They were subsequently raised to £3,000 in 2006 and £9,000 in 2012."

# Define the regex pattern to match tuition fees
pattern = r"£(\d{1,3}(,\d{3})*(\.\d{1,2})?)"

# Find all matches of the pattern in the paragraph
matches = re.findall(pattern, paragraph)

# Convert the matches to integers and store them in a list
tuition_fees = [int("".join(match[0].split(","))) for match in matches]

# Define the academic years
academic_years = ['2000/01', '2001/02', '2002/03', '2003/04', '2004/05', '2005/06', '2006/07', '2007/08', 
                  '2008/09', '2009/10', '2010/11', '2011/12', '2012/13', '2013/14', '2014/15', '2015/16', 
                  '2016/17', '2017/18', '2018/19', '2019/20', '2020/21', '2021/22']

# Define a function to calculate the tuition fee based on the academic year
def calculate_tuition(year):
    if year < 2006:
        return 1000
    elif year < 2012:
        return 3000
    elif year < 2017:
        return 9000
    else:
        return 9250

# Use a loop to calculate the tuition fee for each academic year
tuition_fees = [calculate_tuition(int(year.split('/')[0])) for year in academic_years]

# Create a dictionary with the academic years and corresponding tuition fees
tuition_dict = {'Academic Year': academic_years, 'Tuition Fee': tuition_fees}

# Create a Pandas DataFrame from the dictionary
tuition_df = pd.DataFrame(tuition_dict)

# Store the dataframe into an Excel file
tuition_df.to_excel('tf.xlsx', index=False)
# Print the DataFrame
print(tuition_df)
