##Plotting simple quantities of a pandas dataframe
##=================================================     FAILED

##This example loads from a CSV file data with mixed numerical and
##categorical entries, and plots a few quantities, separately for females
##and males, thanks to the pandas integrated plotting tool (that uses
##matplotlib behind the scene).

###See http://pandas.pydata.org/pandas-docs/stable/visualization.html


import pandas

data = pandas.read_csv(r'C:\Users\premd\OneDrive\Desktop\HHA_507_\descriptives-scipy\data\brain_size.csv', sep=';', na_values='.')

# Box plots of different columns for each gender
groupby_gender = data.groupby('Gender')
groupby_gender.boxplot(column=['FSIQ', 'VIQ', 'PIQ'])


###I got an error :name 'groupby_gender' is not defined

from pandas.tools import plotting


####NameError: name 'plotting' is not defined

# Scatter matrices for different columns
plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])
plotting.scatter_matrix(data[['PIQ', 'VIQ', 'FSIQ']])

####NameError: name 'plotting' is not defined

import matplotlib.pyplot as plt
plt.show()
