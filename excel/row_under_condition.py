# This script grabs the row directly below a condition in excel
# In this case, we are interested in the row below the X indicating the user was promoted for each user in the file

import pandas as pd
import numpy as np

# Reading data
df = pd.read_csv("filepath")

# Creating empty dictionary for dataframe grouping
data_dict = {}
# Creating a dataframes for all rows with the same persno
# Groping those dataframes into a dictionary
for i, g in df.groupby('persno'):
    data_dict.update({'data_' + str(i): g.reset_index(drop=True)})

# Creating an empty list
df_list = []
# Iterating through the dictionary
for i in data_dict.values():
    # Checking if the dataframe has more than 1 row
    if len(i) > 1:
        # Isolating the column of interest
        x_ = i.iloc[:, 7]
        # Replacing nulls with the string None
        x_ = x_.replace(np.nan, 'None', regex=True)
        # Returning the index of the row matching the condition
        index = [x for x in range(len(x_)) if x_[x] == "X"]
        # Boolean variable ensuring that the index is correct
        boolean = i.iloc[index[-1]][7] == "X"
        if boolean:
            # Creating a new index for the row below the row matching the condition
            new_index = index[-1] + 2
            # Extracting the rows of interest using the created indeces
            i = i.iloc[index[-1]:new_index]
            # Appending the dataframe to the list
            df_list.append(i)
        else:
            pass
    else:
        pass

# Combining the dataframes in the list into one
df_ = pd.concat(df_list)

# Saving to a csv
df_.to_csv("filepath")
