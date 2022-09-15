##"""
##Boxplots and paired differences
##=================================================    FAILED

##Plot boxplots for FSIQ, PIQ, and the paired difference between the two:
##while the spread (error bars) for FSIQ and PIQ are very large, there is a
##systematic (common) effect due to the subjects. This effect is cancelled
##out in the difference and the spread of the difference ("paired" by
##subject) is much smaller than the spread of the individual measures.

##import matplotlib.pyplot as plt
##import numpy as np

##x = np.linspace(0, 10, 100)

##plt.plot(x, np.sin(x))
##plt.plot(x, np.cos(x))

##plt.show()

######################

from numpy import np
import pandas 

import matplotlib.pyplot as plt

data = pandas.read_csv(r'C:\Users\premd\OneDrive\Desktop\HHA_507_\descriptives-scipy\data\brain_size.csv', sep=';', na_values='.')
data.columns


data['FSIQ'] = pd.to_numeric(data['FSIQ'])
# Box plot of FSIQ and PIQ (different measures of IQ)
plt.figure(np.figsize==(4, 3))
data.boxplot(['FSIQ', 'PIQ'])

######   ValueError: boxplot method requires numerical columns, nothing to plot.

# Boxplot of the difference
plt.figure(figsize=(4, 3))
plt.boxplot(data['FSIQ'] - data['PIQ'])
plt.xticks((1, ), ('FSIQ' - 'PIQ',))


######  TypeError: unsupported operand type(s) for -: 'str' and 'str'

plt.show()
