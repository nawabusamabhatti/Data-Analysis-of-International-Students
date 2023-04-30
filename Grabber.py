import re
import pandas as pd
# Retrieve the HTML content of the website
import requests
from bs4 import BeautifulSoup

def Graber_For_Fee():
    url = 'https://epigram.org.uk/2022/11/01/universities-under-pressure-to-hike-tuition-fees-amid-soaring-inflation/'
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the paragraph that contains the tuition fee information
    keyword = 'In England, tuition fees have been capped'
    paragraph = soup.find('p', text=lambda t: t and keyword in t).text
    
    # print(paragraph)

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
    tuition_df.to_csv('ProjectFiles/tf.csv', index=False)
    
    # Print the DataFrame
    return tuition_df
