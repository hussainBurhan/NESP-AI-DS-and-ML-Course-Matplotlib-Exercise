# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading the CSV file
phone_csv = pd.read_csv("Mobile phone price.csv")

# Displaying information about the DataFrame
print(phone_csv.info())

# Cleaning and converting data types
phone_csv['Storage '] = phone_csv['Storage '].str.replace('GB','').astype(int)
phone_csv['RAM '] = phone_csv['RAM '].str.replace('GB','').astype(int)
phone_csv['Price ($)'] = phone_csv['Price ($)'].str.replace('$','')
phone_csv['Price ($)'] = phone_csv['Price ($)'].str.replace(',','').astype(int)
phone_csv['Screen Size (inches)'] = phone_csv['Screen Size (inches)'].astype(float)

# Creating subplots
fig1, ((subplot_1,subplot_2),(subplot_3,subplot_4)) = plt.subplots(nrows=2, ncols=2, figsize= (30,20))

# Creating visualizations
subplot_1.scatter(phone_csv['Brand'],phone_csv['Storage '])
subplot_2.bar(phone_csv['Brand'],phone_csv['Price ($)'])
subplot_3.barh(phone_csv['Brand'],phone_csv['RAM '])
subplot_4.hist(phone_csv['Brand'], bins=16)

# Adding titles and labels to subplots
subplot_1.set(title='Brand vs Storage', xlabel= 'Brand', ylabel='Storage(GB)')
subplot_2.set(title='Brand vs Price', xlabel= 'Brand', ylabel='Price ($)')
subplot_3.set(title='Brand vs RAM', xlabel= 'Brand', ylabel='RAM (GB)')
subplot_4.set(title='Brand vs frequency', xlabel= 'Brand', ylabel= 'frequency')
