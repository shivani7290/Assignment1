#Assignment 7:-
#--------------------------------------------------------------------------------------------------------------
#Question 1:- regex patterns:- The regex pattern used to validate email addresses, mobile no, string, and more
#--------------------------------------------------------------------------------------------------------------
# a) Email Validation
import re
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
emails = ["a@b.com", "abc@", "abc@site", "good.email@ok.org"]
for e in emails:
    if re.match(pattern, e):
        print("Valid email =>",e)
    else:
        print("Invalid email =>",e)

# b) Mobile Number Validation
import re
pattern = r'^[6-9]\d{9}$'
numbers = ["9876543210", "1234567890", "9123456789", "90000abcde"]
for num in numbers:
    if re.match(pattern, num):
        print("Valid number =>",num)
    else:
        print("Invalid number =>",num)

# c)Strings
import re
pattern = r'^[a-zA-Z0-9]+$'
words = ["Test123", "Test_123", "HelloWorld", "123456"]
for word in words:
    if re.match(pattern, word):
        print("Valid :",word)
    else:
        print("Invalid :",word)
#-------------------------------------------------------
# 2) Explore more datetime function and uses in pandas
#-------------------------------------------------------
import pandas as pd
dates = pd.date_range(start='2023-01-01', end='2023-01-10')
df = pd.DataFrame({'Date': dates})
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Weekday'] = df['Date'].dt.day_name()
df['Is Weekend'] = df['Weekday'].isin(['Saturday', 'Sunday'])
print(df)
#------------------------------------------------------------------------------------------
# 3) Import a Meaningful CSV File for Data Analysis and Perform Data Cleaning and Analysis
#------------------------------------------------------------------------------------------
import pandas as pd
df = pd.read_csv('customers-100.csv')
print(df.head())
print(df.isnull().sum())
df['First Name'].fillna(df['Last Name'])
df.dropna(subset=['Company'], inplace=True)
df.drop(columns=['Last Name'], inplace=True)
df['Email'].value_counts()
print(df)
if 'City' in df.columns and 'Customer' in df.columns:
    print(df.groupby('City')['Country'].count())
if 'Country' in df.columns:
    print(df['Country'].nunique())
    print(df.head())



