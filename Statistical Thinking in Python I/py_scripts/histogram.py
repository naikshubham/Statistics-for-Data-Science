# generating a histogram

import matplotlib.pyplot as plt

_ = plt.hist(df_swing['dem_share'])
_ = plt.xlabel('percent of vote for obama')
_ = plt.ylabel('number of counties')
plt.show()

# setting the bins of a histogram

bin_edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
_ = plt.hist(df_swing['dem_share'], bins=bin_edges)
plt.show()

# auto binning
_ = plt.hist(df_swing['dem_share'], bins = 20)
plt.show()

# matplotlib will automatically generate 20 automatically spaced bins


# SEABORN (Setting seaborn styling)
import seaborn as sns
sns.set()
_ = plt.hist(df_swing['dem_share'])
_ = plt.xlabel('percent of vote for obama')
_ = plt.ylabel('number of counties')
plt.show()
