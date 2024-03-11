import pandas as pd
import numpy as np

dict1 = {
    "name": ['Ashish', 'Harry', 'Rohan', 'Subh'],
    "salary": [92, 34, 24, 17],
    "city": ['Rampur', 'Kolkata', 'Jaipur', 'Patna']
}
df = pd.DataFrame(dict1)
# print(df)

df.to_csv('../../data_folder/s2/friends.csv')
df.to_csv('../../data_folder/s2/friends_without_index.csv', index=False)
# print(df.head())
# print(df.head(2))
# print(df.tail())
# print(df.tail(2))
# print(df.describe())

df = pd.read_csv('../../data_folder/ashish.csv')
# print(df)
# print(df['Speed'])
# print(df['Speed'][0])
df['Speed'][0] = 50
# print(df)
df.to_csv('../../data_folder/s2/updated_ashish.csv', index=False)

# code to change the index of a dataframe
df.index = ['First', 'Second', 'Third', 'Fourth']
# print(df)

# code to generate one dimensional series

df = pd.Series(np.random.rand(34))
# print(df)
# print(type(df))

# code to generate a dataframe
df = pd.DataFrame(np.random.rand(334, 5), index=np.random.rand(334))
print(df)

