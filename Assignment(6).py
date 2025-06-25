#Assignmnet 6:-
#----------------------------------------------------------------------
# Question1:- How to convert a series of date-strings to a timeseries?
#----------------------------------------------------------------------
import pandas as pd
series = pd.Series(['2025-06-25', '2025-06-26', '2025-06-27'])

timeseries = pd.to_datetime(series)
print(timeseries)
print('\n')
#----------------------------------------------------------------
#Question 2:- Create two DataFrames with a common column ‘ID
#----------------------------------------------------------------
#perform following joins
import pandas as pd
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['shivu', 'kirti', 'varun', 'ram']
})

df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Score': [85, 90, 75, 88]
})
print('\n')

# - inner merge
inner_merged = pd.merge(df1, df2, on='ID', how='inner')
print(inner_merged)
# - left join
left_merged = pd.merge(df1, df2, on='ID', how='left')
print("Left Merge:\n", left_merged)

# - right join
right_merged = pd.merge(df1, df2, on='ID', how='right')
print("Right Merge:\n", right_merged)

# -  using  Index-Based Join
df1_indexed = df1.set_index('ID')
df2_indexed = df2.set_index('ID')

join_result = df1_indexed.join(df2_indexed, how='inner')
print(join_result)
print('\n')

#  - New DataFrames with multiple keys
df3 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Subject': ['Math', 'Sst', 'English'],
    'Marks': [90, 85, 88]
})

df4 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Subject': ['Math', 'Sst', 'English'],
    'Teacher': ['Mr. A', 'Ms. B', 'Mr. C']
})
merged_multiple = pd.merge(df3, df4, on=['ID', 'Subject'])
print(merged_multiple)
print('\n')
#------------------------------------------------------------------
# question 3: Concatenate 2 DataFrames and merge with a third one
#-----------------------------------------------------------------
df_s = pd.DataFrame({
    'ID': [1, 2],
    'City': ['Delhi', 'Mumbai']
})
df_t = pd.DataFrame({
    'ID': [3, 4],
    'City': ['Kolkata', 'Chennai']
})
df_u = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'State': ['Delhi', 'Maharashtra', 'West Bengal', 'Tamil Nadu']
})
con = pd.concat([df_s, df_t])
print(con)
final_merge = pd.merge(con, df_u, on='ID')
print( final_merge)
print('\n')

