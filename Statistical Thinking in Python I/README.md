

```python

# Statistics in Python

### Histogram
- The default bin size in matplotlib is **10**. 
- The **square root rule** is a commonly-used rule of thumb for choosing number of bins : `choose the number of bins to be the **square root** of the number of samples.`

#### Disadvantages of histogram
- Major drawback of histogram is the same data look different depending on how the bins are chosen, and the choice of bins is in many ways arbitrary.
- This leads to **binning bias.**
- The same data may be interpreted differently depending on choice of bins.
- Additional problem with histograms is we are not plotting all of our data, we are sweeping the data into bins and loosing their actual values.
- TO remedy these problems we can make a `**Bee swarm plot**`

### Plot all of your data : Bee swarm plots
- We dont have a binning bais and whole data is displayed

#### Generating a bee swarm plot

```python
_ = sns.swarmplot(x='state', y='dem_share', data=df_swing)
_ = plt.xlabel('state')
_ = plt.ylabel('percent of vote for obama')
plt.show()
```

### Plot all of the data : ECDFs (Empirical cumulative distribution function)
- Using a bee swarm plot to plot all of the data is not the best option. As an alternative we can compute an **Empirical cumulative distribution function (ECDF)** 
- The x-value of ECDF is the quantity that we are measuring. The yvalue is the fraction of data points that have a value smaller than the corresponfing x-value.

#### Making an ECDF
- The x-axis is the sorted data. We need to generate it using the numpy function sort. The y-axis is evenly spaced data points with a maximum of one, which we can generate using numpy arange function, and dividing by the total no of data points.
- By default, plt.plot plots lines connecting the data  . To plot our ECDF we just want points.

```python
import numpy as np

x = np.sort(df_swing['dem_share'])
y = np.arange(1, len(x)+1) / len(x)
_ = plt.plot(x, y, marker=".", linestyle='none')
_ = plt.xlabel('percent of vote for obama')
_ = plt.ylabel('ECDF')
plt.margins(0.02) # keeps data off plot edges
plt.show()
```

### Percentiles, outliers and box plots

#### Percentiles on ECDF

<p align="center">
  <img src="./images/ECDF.JPG" width="350" title="Medain ECDF">
</p>

- Median is the special name for 50th percentile, that is 50% of the data are less than the median.Similarly, the 25th percentile is the value of the data point that is greater than 25% of the sorted data, and so on for any other percentile we want
- Percentile are used for summary statistics and can be computed using `np.percentile(df_swing['share'], [25,50,75])` . We just pass a list of percentiles we want, and it returns the data that match those percentiles.

##### Box plot

<p align="center">
  <img src="./images/Boxplot.JPG" width="350" title="Box plot">
</p>

- The center of the box is the median, which we know is the 50th percentile of the data. The edges of the boxes are the 25th and 75th percentile. The total height of the box contains the middle 50% of the data, and is called the **interquartile range or IQR.**
- The whiskers extends a distance of **1.5 * IQR**, or to the extent of the data, whichever is more extreme. 
- Finally, any points outside of the whiskers are plotted as individual point, which we often demarcrate as **outliers**.
- While there is no single definition for an outlier, being **more than 2 IQRs away from the median is a common criterion**. It is important to understand that an outlier is not necessarily an erroneous data point. Sometimes they are just alternative.
- When the number of data is very large and bee swarm plots are too cluttered, box plots are a great alternative.

##### Generating a box plot using seaborn

```python
import matplotlib.pyplot as plt
import seaborn as sns

_ = sns.boxplot(x='east_west', y='dem_share', data=df_all_states)
_ = plt.xlabel('region')
_ = plt.ylabel('percent of vote for obama')
plt.show()
```
















```
