# import numpy as np

# import numpy as np

# # Create a numpy array
# array = np.array([[1, 2, 3],
#                   [4, 5, 6],
#                   [7, 8, 9]])

# # Specify the filename
# filename = "array_data.txt"

# # Save the numpy array as a text file
# np.savetxt(filename, array)

# print(f"Array saved as '{filename}'.")

# reindexing in pandas dataframe
import pandas as pd
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data, index=['x', 'y', 'z'])
print("Original DataFrame:")
print(df)

new_index = ['x', 'y', 'z', 'w']  
new_columns = ['A', 'B', 'D']  

df_reindexed = df.reindex(index=new_index, columns=new_columns)
print("\nDataFrame after reindexing:")
print(df_reindexed)

# multiplication of two dataframe
data1 = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
data2 = {'A': [10, 11, 12], 'B': [13, 14, 15], 'C': [16, 17, 18]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

result = df1 * df2

print("Element-wise multiplication result:")
print(result)

# create a pandas series from dictionary
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
series = pd.Series(data)
print(series)

# do column wise addition and make a new row matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

column_sums = [sum(col) for col in zip(*matrix)]

new_row_matrix = [column_sums]

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nColumn-wise Sum Matrix (as a new row):")
print(new_row_matrix)
