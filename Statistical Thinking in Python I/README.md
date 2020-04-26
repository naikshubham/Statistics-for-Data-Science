
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
