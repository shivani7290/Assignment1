#Assignment 5:-
#---------------------------------------------------
# question 1:-Practice Pandas Series
# <> Create a  Pandas Series from Dictionary
import pandas as pd
dict = {'a': 5, 'b': 6, 'c': 7}
series = pd.Series(dict)
print(series)
print('\n')

# <> Pandas Series from Dictionary
list = [10, 20, 30, 40]
series = pd.Series(list)
print(series)
print('\n')

# <>  Access the elements of a Series
print("\nFirst element (by index 0):", series[0])
print('\n')

#---------------------------------------------------
# question 2:- data frames
# <> make a Pandas DataFrame with a two-dimensional Python list
data_2dim = [['shivu', 19], ['tarun', 23], ['kirti', 17]]
df = pd.DataFrame(data_2dim, columns=['Name', 'Age'])
print(df)
print('\n')

# <>  Create DataFrame from Python dictionary
dict = {
    'Name': ['golu', 'gola', 'goli'],
    'Age': [20, 24, 25]
}
df = pd.DataFrame(dict)
print(df)
print('\n')

# <> Create Pandas DataFrame using list of lists
lists = [['India', 'New Delhi'],
              ['USA', 'Washington'],
              ['UK', 'London']]
df = pd.DataFrame(lists, columns=['Country', 'Capital'])
print("\nDataFrame from List of Lists:\n", df)
print('\n')

# <>  Create a Pandas DataFrame using list of tuples
tuples = [('avatar', 2022), ('barbie', 2023), ('spiderman', 2021)]
df= pd.DataFrame(tuples, columns=['movie', 'Year'])
print(df)
print('\n')

# <>  Create a Pandas DataFrame from List of Dictionaries
list_of_dicts = [
    {'Name': 'Shivani', 'Marks': 90},
    {'Name': 'tanu', 'Marks': 91},
    {'Name': 'Pooja', 'Marks': 92}
]
df= pd.DataFrame(list_of_dicts)
print(df)
print('\n')

#------------------------------------------------
# Question 3:- data iteration
#------------------------------------------------
# <>Import pandas and create a sample DataFrame
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Shivu', 'Tarun', 'Kirti', 'Anu'],
    'Age': [19, 23, 17, 21],
    'City': ['Delhi', 'Alwar', 'Jaipur', 'Bhopal']
}
df = pd.DataFrame(data)
print(df)
print('\n')

# 1. Different ways to iterate over rows in Pandas DataFrame
print("\nIterating using iterrows():")
for index, row in df.iterrows():
    print(row['Name'], row['Age'])

print("\nIterating using itertuples():")
for row in df.itertuples(index=False):
    print(row.Name, row.Age)
    print('\n')

# 2. Selecting rows in pandas DataFrame based on conditions
print("\nselect name which older than 18:\n", df[df['Age'] > 20])
print('\n')

# 3. Select any row from a DataFrame using iloc[]
print(df.iloc[1])
print('\n')

# 4. Limited rows selection with given column
print(df.loc[:1, ['Name']])
print('\n')

# 5. Drop rows from the DataFrame based on condition applied on a column
df_drop = df[df['Age'] >= 20]  # drops rows where age < 20
print(df_drop)
print('\n')

# 6. Insert row at a given position in Pandas DataFrame
new_row= pd.DataFrame([{'name': 'shivu', 'Age': 20, 'City': 'delhi'}])
df = pd.concat([df.iloc[:2], new_row, df.iloc[2:]]).reset_index(drop=True)
print(df)
print('\n')

# 7. Create a list from rows in Pandas DataFrame
l = df.values.tolist()
print(l)
print('\n')


