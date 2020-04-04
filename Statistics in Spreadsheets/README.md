
# Statistics in Spreadsheets

#### Statistics is just a piece of information from large quantity of data. It describes data.

- Mode : A number that appears most often in the dataset.
- We can the mean using the **`=AVERAGE(B2:B11)`** function.
- **`=MEDIAN(B2:B11)`** to calculate the median.
- **`=MODE(B2:B11)`** to calculate mode.

### Data point distance from average
- *Variance* : Variance measures how dispersed a dataset is from its mean. The smaller the variance the less spread the data is. Conversely, large differences between data points increase the variance.
- A : 37,37,37 | B : 10, 14, 10, 10 | C : 10, 14, 100, 10
- Column A variance : 0, Column B : 3 , Column C : 1476.75
- Column C has an outlier as a result its variance is maximum.
- **`=VARP(A1:A14)`** to calculate variance.
- Variance is the average of squared values. Thus variance is different from the original sample values making it less intutive.
- **Most often we need to make sense of the variation by putting it in the scale of the original data.** `This is done by taking the square root of the variance, called standard deviation`
- After taking the variance with **`VARP`** we can use **`SQRT`**, squareroot to calculate the **standard deviation**
- More easy we can use **`STDEVP`** to get standard deviation

#### Standard deviation as a unit of measure
- Std dev scores shows how a data point relates to the distribution.
- =average(10, 14, 10, 10) = 11 | =stdevp(10, 14, 10, 10) = 1.73 | new data point : 12.73
- Subtracting new data point from standard dev gives back the mean | 12.73 - 1.73 = 11
- **Thus this new data point is exactly one standard deviation away from the mean**

<p align="center">
  <img src="./images/1_std.JPG" width="350" title="1 std-dev">
</p>

#### Another statistic for understanding a distribution is percentile 
- Ordering a distribution & calculating the percentage of values below a specific point will tell us its **percentile**
- **Quartiles** are percentiles that segment the data into 4 chunks.
- To get the popular percentiles in sheets we use the **=QUARTILE(b1:b5, 1)**

- Calculating standard deviations
There is a lot of seasonal variability in the train data. To better understand this, we will calculate the standard deviation to understand how "spread out" the data is from the mean average.

To calculate the standard deviation:
Calculate the variance of the data.
Take the SQRT(), or square root, of the variance.

- The QUARTILE() function accepts an array of values followed by an integer 1 to 4 to declare the specific quartile.
Quartile 4: The maximum value in the data.
Quartile 3: 75% of the data is less than the third quartile.
Quartile 2: The median of the data.
Quartile 1: The smallest values 25% of the data.

- A useful statistic computed from the quartiles is the "interquartile range" (IQR), which lies between the Q1 and Q3 and represents the middle 50% of the data.

### Standardizing Data
- Many real world datasets have variables that are measured on different scales. For e.g, height might me measured in feet and weight might be measured in pounds. This poses a problem because variables on different scales are harder to compare, and it may lead to misinterpretation of the importance of a particular column - that column may appear more important simply because it has larger values than another, while in reality it may actually have a very similar distribution to the column with smaller values.
- **The solution to this problem is to standardize the data so that all the variables are on the same scale**
- In statistics, standardization centers a dataset's distribution around the mean of the data and calculates the number of std devs away from the mean each point is.
- We can standardize our data by calculating **z-scores**, also known as standard scores.
- **The z-score measures how far a value is from the mean using standard deviations.**
- TO calculate the z-score of a data pt, subtract the mean and divide by the std-dev
- **=STANDARDIZE(DATA POINT, MEAN, STD-DEV)** to calculate z-score

<p align="center">
  <img src="./images/z_scores.JPG" width="350" title="z scores">
</p>

- As we can see, the new data points despite being 10 times larger, the distance of each data point to their respective sample's mean & std-dev are the same as in the first column, and this allows us to easily compare the two columns.

### Visualizing Distributions

<p align="center">
  <img src="./images/common_dist.JPG" width="350" title="common distribution">
</p>

- A lot of the things we measure in the world looks something like above.

<p align="center">
  <img src="./images/common_dist2.JPG" width="350" title="common distribution">
</p>

- Above distribution is of pizza delivery times.
- In both cases, the highest point is in the middle of the distribution, or the most frequent value is the highest point.
- The resulting shape is similar to a bell so this distribution is often called a **bell curve**. It is technically called the **normal distribution**.

<p align="center">
  <img src="./images/hist.JPG" width="350" title="normal histogram">
</p>

- Conceptually, a normal distribution is symmetrical and shaped like a bell.
- In normal distributions ,the mean, median and modes have similar values. As a result, not only is the distribution centered at the mean, median and mode but the frequencies of these values decrease symmetrically so other summary stats are affected like quartiles and std -devs.

<p align="center">
  <img src="./images/dists.JPG" width="350" title="distributions">
</p>

- There are many distribution shapes, some of the common ones are shown above. For each, the summary statistics will change. For e.g the mean is affected by outliers, or extreme values in the data, however the median is not.
- So in a `skewed distribution` these values will differ **unlike the normal or symmetrical distribution where mean and median are very close.**
- Often in stats we want to test how "normal" the data is. Even though we can see a bell curve shape, there are two mathematical aspects to a normal distribution. 

<p align="center">
  <img src="./images/skew.JPG" width="350" title="normal distributions">
</p>

- First, how much does the data lean or skew from the most frequent value. In the visual its shown with the red arrows. A normal distribution will have little to now skew, represented by the vertical red line.
- Second, to measure symmetry and how the tails trail off, we review the blue lines.
- These aspects, leaning and trailing off are measured in **skew** and **kurtosis**.
- In sheets we use **=skew(a1:a10)** and **kurt(a1:a10)** , to get leaning and trailing off statistics. 
- There are many opinions on acceptable values for skew and kurtosis to describe a normal distribution. Typically, values between **-2 & 2 for both skew and kurtosis** can indicate a **normal distribution**
- To add histogram in sheets : Go to insert -> then chart -> select histogram from chart type drop down and finally declare the data range.

#### Is the data "normally" distributed?
- Earlier, we noted that the mean and median savings values were almost equal. The savings histogram was also roughly symmetrical and resembled a bell curve.
- Now we want to use statistics to verify if the distribution is approximately symmetrical or "normally distributed". To do so, we will calculate the skew and kurtosis.
- **Kurtosis**: Calculated using `KURT()`. Measures how the tails behave. It identifies how values are concentrated around the mean and how they trail away from it in the tails.
- **Skew**: Calculated using `SKEW()`. Measures how symmetrical the distribution is. 0 means the distribution is exactly symmetrical. Values above or below 0 indicate that there are more values above or below the mean.

### Visualizing Correlations
- We will transition from histogram which visualizes a single variables to a scatter plot which explores relationship among two variables.
- In  sheets we can add a imaginary line passing through our scattered data points. Its called a trend line to help see the overall trend relationship.
- To add a trendline in sheet : click "insert" then "chart" then select "scatter chart" from the drop down , then click customize in the dialog and under "series" check the "trendline" box.
- The trend line is added or fit so that the distance between the line and each point is minimized.

#### Stats about the trendline
- In sheets we can get the slope and intercept of the trend line using the **=LINEST(rangeX, rangeY)** or line estimate function. It accepts two ranges and will return the slope then the intercept.
- The slope can be interesting because it declares the trend relationship between the variables. For e.g a slope of 1.5 means that as the X varaible increases 1 then the Y varaible will increase by 1.5. IF the slope is -1, then if the slope variable decreases by 1 then so does the Y variable.
- correlation can be calculated using **CORREL()**, ranges between -1 and 1. 
- 0 correlation means there is no relationship between variables.
- Positive correlation indicate that as one variable increases, the other also increases.
- Negative correlation values signify that as one variable increases, the other decreases.

