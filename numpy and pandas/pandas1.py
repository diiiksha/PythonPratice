import pandas as pd

data={
    'Name': ['rahul','priya','amit','sneha','vikram'],
    'age': [22,21,23,20,24],
    'marks':[85,92,78,88,73],
    'city':['bhopal','indore','bhopal','jabalpur','indore']
}

df = pd.DataFrame(data)
# print(df)

# # print(df.shape)
# # print(df.head(3))
# print(df.dtypes)
# # print(df.describe())

# #select columns
# print("df['Name]:\n",df['Name'])
# print(df[['Name','marks']])

# #Filter rows

# print(df[df['marks']>=85])
# print(df[df['city'] == 'bhopal'])
# print(df[(df['marks']>=80) & (df['city']=='indore')])

# def get_grade(x):
#     if x >= 90:
#         return 'A'
#     elif x >=75:
#         return 'B'
#     else:
#         return 'C'
    
# df['Grade'] = df['marks'].apply(get_grade)
# print(df['Grade'])
# print("-------")
# print(df)


# #Groupby-like excel pivot
# city_avg = df.groupby('city') ['marks'].mean()
# print(city_avg)

#Read real Csv file
df2 = pd.read_csv('students.csv') 
print(df2)
df2['Name'] = df2['Name'].str.strip() 
print(df2)
#cleaning
df2.to_csv('clean_output.csv',index = False) #save
