
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
- Spreadsheets have 3 formulas for calculating the y-intercept and slope given two variables.
**SLOPE()** - will return the slope of a trend line or linear regression representing the linear change in one unit to another.
**INTERCEPT()** - returns the value where the trendline will intersect the y-axis.
**LINEST()** - calculates both the slope & the intercept of two variables using the least-squares method.

### Bar Charts
- Visualize non-numeric data.
- **`COUNTIF()`** function can been to used to count the number of "1"s and "0"s. 

## Statistical Hypothesis Testing

### Central to stats - Sampling
- **Population** : In stats, a population is defined as an **entire** distribution of similar observations or events.
- Often its costly and time consuming to work with entire population, so its better to **sample** the population. A sample is a subset of the population's observations.
- **Central Limit Theorem** : It finds that if we repeatedly randomly sample independently from any distribution, skewed or not, **the resulting sample will be normal**. Using an appropriate sample size along with the central limit theorem helps overcome the problem of using data from non-normal populations.
- The more data that's gathered in a sample, the more certainty exists in the resulting statistics. The normalcy of the sample, proven in the central limit theorem let's us make statistical inferences from the sample to the population which leads us to hypothesis testing.
- **Central limit theorem** is defined as `If a sample size from an independent random variable is *large enough* then the sampling distribution will be normal or nearly normal`. This lets us make inferences to the population.
- However, "large enough" is vague. The size is dictated by two factors. First, exactly how precise do we need to be ? Second factor is how the population distribution behaves. The more normal the underlying population the less sample data points are needed to make accurate inferences based on the sample. If the underlying population is normal they would say a sample of 30-40 would be sufficent to make inferences about the population. 

#### Sampling in Spreadsheets 
- There are many ways to sample data. Sampling choices affect the statistics and as a result, what we learn about the data population. A popular method for sampling is to do it randomly.

### Central Limit Theorem in action
- increasing the sample size changes both the statistics as well as the histogram
- **CLT** : If a sample size from an independent, random variable is large enough, then the sampling distribution will be normal or nearly normal.

#### "Large enough" is vague. The sample size is impacted by:
- How accurate we need to be. Since a sample is a representation, the resulting stats will be approximate. If we need a high degree of certainty, we will need more samples to more closely resemble the population.
- The more closely the population follows a normal distribution, the fewer sample points will be required.

### Hypothesis Testing
- **Hypothesis** : Is any testable claim
- Stating that the price of a Ferrari is high, isnt testable.This is because high isnt defined. To make it testable we can define the hypothesis such as `average Ferrari price is higher than the average sports car price.`
- There are two types of hypothesis the **NULL** and **alternate**.
- **Null hypothesis** : represents the status quo or the accepted fact. The NULL is short for NULLIFY. This is because our statistical test seeks to NULLify or reject, the statement. 
- **Alternate/Research Hypothesis** : is the challenger statement meaning everything else not represented in the NULL hypothesis.
- Generally an **H0** denote the NULL while **H1** represent the alternate.
- In our example the **NULL** is that the **`average Ferrari price is equal to the average sports car price`** . The **Alternate/Challenger** hypothesis is that the **`average ferrari price is greater or less than the average sports car price.`**
- The status quo is that there is no difference but we want to test if there is a difference.

#### Common sense testing
- **NULL Hypothesis (H0):**  `Average Ferrari Price equals Average Sports car Price`

- **Alternate Hypothesis (H1):** `Average Ferrari price does not equal Average sports car price`

- Average Ferrari Price(Sample size = 50) = $252,000
- Average non-Ferrari Sports Car Price(Sample Size = 50) = $85,000


- There is a large difference in the average prices, so we dont agree with the status quo. In stats quo, we REJECT the NULL hypothesis.

#### Another common sense test
- **NULL Hypothesis (H0) :** `Average toyota price equals average honda price`
- **Alternate Hypothesis (H1):** `Average toyota price does not equal average honda price`

- Average Toyota Price (sample size = 50) = $23,845
- Average Honda Price (sample size=50) = $23,720

- The values are so close, so the difference may only be from sampling. So we accept the NULL Hypothesis. In stats we say `Fail to reject the NULL Hypothesis`.

#### Removing subjectivity in a test
- To further avoid subjectivity, hypothesis testing uses a **test statistics** to measure the H0 validity.
- The car price experiment tests the independence of two samples. So we use a **t-test** as the statistic. Example : t-test (In spreadsheets : T.TEST(range1, range2, tails, type))
- The t-Test produces a p-value. **p-value** is the probability that the results are due to chance/error.
- We have to predetermine a p-value cutoff for our test. Choose a p-value cutoff (Example: 1%/0.01, or 5%/0.05). This means we want to have a probabilty of say 1% or 5% that the results are an error.
- We use a p-value of 5% in most cases.
- If the p-value(probability) is less than the cutoff, 5% then we will **REJECT the NULL Hypothesis** and conclude that there is a difference between the samples.
- **If the p-value from our test statistic is less than 0.05 then we reject the NULL hypothesis**

- **Spreadsheet Formula** : **`=T.TEST(range1, range2, tails, type)`** - It accepts range1, range2, the number of tails being tested & type of test.
- If we are testing whether the `difference is only greater than or only less than the t-test has 1 tail.`
- In our case, the H0 operator is equals. So values can be above or below the mean. Thus the test has `two tails` in either direction from mean. 
- Next if we measure the `same observations at different times, the type equals 1.` If we measure `different observations with the same variance the type is 2` and i`f we measure different observations with different varainces, then use type 3`

### Comparing samples with a t-test
- How can we be sure if a sample is the same or different compared to a population or other sample? **Sample independence can be tested with a T.TEST()!**
- examining data from a farm. Prior to introducing a new fertilizer, 10 plant heights were measured. After the new fertilizer was used another 10 plants were measured. We will perform a t-test to understand if the plant heights in the samples are in fact different. `This is a two-tailed test because the heights are either above or below the original sample, "tails" to either side of the original distribution.The type is 2 because the samples are not from the same subjects but they have the same variance.` Had they been the same plants before and after fertilizer treatment, it would be a "paired" t-test which is type 1. 
- `NULL Hypothesis` : `Prior plants height equals next plants height`.
- `Alternate Hypothesis` : `Prior plants height does not equal next plant height`.
- Refer excel [t-test](excels/t-test.xlsx)

### Paired t-test
- Now we are looking at driver data. Most research suggests drivers perform better in the morning versus in the afternoon. The researcher here measured 10 drivers in the morning and again the same drivers in the evening. The milliseconds response time is the time needed to apply the brakes after seeing a prompt in the simulator. We need to perform a t-test to see if this data supports the research that drivers do indeed perform better in the morning.
- `NULL Hypothesis (H0)` : Morning driver response times  <  Afternoon driver response times
- `Alternate Hypothesis (H1)` : Morning driver response times  >=  Afternoon driver response times
- `Tails` : This should have `one tails` as we are testing whether difference is greater than or equal only.
- `Type` : `Type equals 1` as same drivers are measured at different times.
- Refer excel [t-test_2](excels/t-test_2.xlsx)

### Hypothesis testing with the Z-test
- The t-test infers whether there is a difference between two mean averages. Similarly a Z-test will give us a probability that two dataset averages are different. 

#### Comparing the T-tests and Z-tests
##### Similarities
- Determine  whether two population means are statistically different
- Select a p-value cutoff prior to the test (Usually 0.05)
- If the resulting p-value is less than 0.05, then REJECT H0 else FAIL TO REJECT H0.

#### Contrasting T-tests and Z-tests
##### Even though both t-tests and Z-tests work with sample averages there are some differences
- Z-Test Formula **`Z.TEST(rnge1, testStatisctic, Stdev)`**
- T-Test Formula **`T.TEST(range1, range2, tails, type)`**
- A T-test needs 2 ranges in the formula incontrast Z-test needs only one.
- Instead of worrying about tails and types like in a t-test, a z-test accepts a known summary statistic from the population.
- Z-test needs a test statistic(i.e population mean). T-test works when variance is unknown.
- Z-test is used with bigger datasets (n > 30) whereas T-test is used with smaller datasets (n < 30).
- Just like how the z score measured how many standard deviations a value was from the mean. A Z-test is similar and measures a distance. 

#### Z-tests calculates the probability
- Instead of z-score we will be calculating a z-test statistic. The result of a z-test is a probability not a distance like z-score.

#### Z-Tests in Spreadsheets
- **`Z.TEST(data, value, [standard_deviation])`**
- Data array, next add the value called "test statistics", std deviation. Reject the NULL hypothesis if the p-value is less than 0.05.

### Performing a Z-test
- When we have over 30 observations, we should use a Z.TEST() over a T.TEST() to compare means. Excel [z-test_2](excels/Z-test.xlsx) has some salary data of U.S Government workers. Our job is to conduct a hypothesis test using the Z-test. 
- Here we want to know if the sample average salary is less than or equal to the government's published average. Are we going to compare one or two tails of the distribution? The <= operator is exploring a single direction away from the value. Thus, this is a one-tailed test.
- A Z-test accepts the data range followed by the population's mean - in this case, the government's published average salary. We can also add the population's standard deviation as a third parameter. If we don't, Z.TEST() will use the sample's standard deviation.

### What changes in a two-tailed test?
-  Now we want to determine if the sample worker salary is equal to the population's. The NULL hypothesis operator changes to = .
This means we are testing whether the sample average is statistically above or below the average. As a result, the experiement is testing in 2 directions from the mean, so it's a two-tailed test.
- If we have a two-tailed test we must multiple the Z.TEST() results by 2. 
- Refer excel [z-test-2-tailed](excels/Z-test-2-tailed.xlsx)

### Hypothesis testing with Chi-squared test

#### Applications of the chi-squared test
- When we are doing research we often have a set of prior observations and after some treatment like applying a new drug we need to know if the treatment actually made a difference. This is determined with the chi-squared test.
- Comparing samples for meaningful differences.

#### Testing before and after 
When we have prior observations and new sample we are left with two choices. Two possibilities :
- The difference in the new group stems from random sampling (H0)
- There is in fact a meaningful difference (H1)
- These two choices are used for the NULL and alternate hypothesis. Further the chi-square test will provide a probability that the two groups are independent or truly different.

#### Chi-sqaured test conditions
- For a chi-squared test to be useful data has to be in groups such as (e.g "old treatement", "new treatment") or values based on gender or other dividing data characteristic.
- Avoids really small expected values (<5). The general consensus is that the expected numbers we are measuring should be greater than 5. Otherwise we may need to perform different tests.

#### Testing the independence of two groups
- Often we see in advs "Clinically proven" or "Lab tested". Inorder to make claims about how the drug improves outcomes ethically and legally the owners need to create an experiment controlling for lifestyle factors and ultimately comparing weight within two groups one treated with the supplement and the other not.
- **Its in the lab or clinic that a chi-squared test is often performed to test the independence of the two groups.**

#### Chi-squared test in Spreadsheets
`CHITEST(observed_range, expected_range)`
- FAIL TO REJECT H0 if the p-value is greater than 0.05
- REJECT H0 if the p-value is less than 0.5

#### Performing a chi-squared test
- In science and other disciplines, it's important to know if the variation we observe in our data is due to chance or is actually stemming from another source.One way to understand this is with a chi-squared test.
- CHITEST() function accepts two ranges. The first represents the observations, and the second represents the expected values.In this case, both ranges must have the same COUNT() or the formula will fail. The formula returns the p-value we will use to determine whether or not to reject the null hypothesis.
- In this example we are reviewing a call center agent's call times. The agent has a higher average call time than the expected call time for all other agents. Let's see if this agent's specific call times are due to chance, i.e. random call variation, or because the agent needs more training to speed up. 
- To perform chi squared test in sheets, use the CHITEST function. Refer excel [chitest](excels/chitest.xlsx)

#### Are bank loans getting worse?
- The previous CHITEST() experiment had equal expected probabilities. However, it is often the case that there are multiple states of an experiment, referred to as degrees of freedom.Furthermore, not all experiment outcomes are equal - some may be more or less likely.A senior vice president at a bank believes the loans of the bank are getting worse. A loan can have these states:
    Current: in good standing
    Grace Period: the loan hasn't made a payment but is late by less than 30 days
    Late 30-60: the loan is past due 30-60 days
    Late 60-90: the loan is past due 60+ days
    Collections: the loan was sent to collections to recieve any payment
    Charged Off: the loan has no value
- test this hypothesis against the bank's expected distribution for these states. For example, the bank expects 80% of loans to be current each month. A chi-squared test comparing the observed loan frequencies with expected will help us determine if the VP's estimation is correct.
- Refer [loan_chitest](excels/loan_chitest.xlsx)  Even though each class has different probabilities, chi-squared adjusts so we can trust the p-value!

### Dating Data!

#### Maximum and Minimum Age 
- MAX(...)  MIN(.....)

#### Social behavior
- We may also suspect that how often someone drinks alcohol or observes religious ceremonies may indicate social behavior.As a result, describing these varaibles with additional summary statistics could prove to be relevant when learning about the site's profiles.
- Using spreadsheet formulas we will identify the percent of non-alcohol drinkers from a sample of profiles. Then we'll calculate the quartiles for annual church visits.Lastly, we will explore the relationship between AGE and annual church visits using correlation
- `COUNTIF(A1:A10, <3)` , `QUARTILE(A1:B10, 4)` , `CORREL(A1:A10, B1:B10)`
- To get the percent of non-drinkers, we first need to use COUNTIF. COUNTIF Accepts the data to review and only tallies cells when a condition is true.

### Understanding the distribution of ages
- As an analyst at a social networking site trying to match like minded singles, we decide to first explore profile ages. This is a basic profile attribute but this alone is often an important factor in relationships.While we might expect that most people searching for love will tend to be younger, we should verify this by using statistics to better understand the distribution of ages. Refer [distribution](excels/Distribution_of_age.xlsx)

#### What's the drinking age?
- Now we want to add more data to your descriptive stats. In profiles, users report how often they drink alcohol in a week so we add it to our sample. Drinking behaviour can be important in relationships so obtaning additional summary statistics could help us learn more about profiles.Here, we'll count the number of non-drinkers. use COUNTIF() to calculate the number of non-drinkers - that is, rows where "Drinks per week" is 0. 
- Conclusion : 8.4% non drinkers, but mostly moderate drinks per week. Refer [drinking age](excels/drinking_age.xlsx)

#### Profile login behavior
- We suspect that people login about once a day. However, after they are in a relationship the hours since last login will likely grow dramatically. After all, people in a relationship have no incentive to continue to look for love! Let’s check.This data measures how many hours have passed since the user last logged in. The mode, 2nd quartile, and mean have already been calculated. Notice that the mean is vastly different. So, we need to calculate the variance, standard deviation, and maximum to understand the spread of the data. We also want to analyze the z-score of the maximum value. Remember, a z-score is the number of standard deviations from the mean and is calculated by subtracting the mean from the data point (in this case, the maximum), and dividing by the standard deviation.
- Connclusion : We confirmed our prior beliefs: some outliers skew the mean! Refer [profile_login_behaviour](excels/profile_login_behaviour.xlsx)

#### Visuals & Distributions
##### Distribution stats
- Variance : how far the data is spread
- Standard Deviation : unit of dispersion relative to mean, square root of variance
- z-score : the number of std deviations a point is from mean

##### Visualizing Distributions
- It can be hard to imagine the shape of a distribution from the statistics alone. The histogram is a helpful way to see the variable distribution. Histogram buckets data points into groups. Low values are grouped together, then middle values and so on.As a result, histograms can be misleading because the visual changes based on the number of bins or buckets used. As a practitioner we need to ensure that our histogram represents the distribution fairly.
- Other consideration for histogram is to ensure that we have enough data points to make the visuals informative & whether or not we are working with a sample or entire population.

##### Comparing Distributions
- We will also be visually exploring the important matching feature AGE. Constructing an AGE histogram will illustrate a different type of data distribution compared to hours since last login.As a major matching factor, the company may want to ensure the distribution is "normal".
- A non normal distribution for an important customer characteristics may indicate the site over-indexes with young, middle-aged or old people. For some type of businesses, an over emphasis illustrated in a non-normal distribution could become a risk factor.For example, a mutual fund heavily indexed to large market cap stocks may expose the fund to additional risk where diversification could help.
- In our case, if age was non-normal, we would identify new age groups for marketing. Even though in many cases we can visually inspect a normal versus non-normal distributions, we can still need to calculate the skew & kurtosis for AGE.
- To review, the **skew is a measure of a non-symmetrical "tail" to the right or left of the mean**. **The Kurtosis measures how the distribution trails off on either side of a peak in the histogram.**
- `A general practise to test for normalcy is to measure the skew & kurtosis values`. **When both values are between -2 & 2 we can state the distribution is normally distributed.**

##### Visualizing logins
- Earlier we calculated descriptive statistics for the profile logins. Now we will plot them to confirm the sample's distribution.
The mode and 2nd quartile are similar yet the other descriptive statistics are much larger. Considering 50% of the data is less than 45 hours since the last login, we think this data must be "non-normal" or skewed in some way. Skewed distributions mean the values are not evenly spread out on either side of the mean.
This data must have some outliers skewing the mean away from the modal average and second quartile. Let's verify this using a histogram. Remember, a histogram is a series of rectangles whose size is proportional to the frequency of records in the bin or interval. It’s not the same as a bar chart!   
- Conclusion : the visual confirmed the positive skew described in your stats! Refer [viz_logins](excels/viz_logins.xlsx)

##### How old do users look?
- Let's check the age variable to compare the age distribution with the previous histogram.
For hours since last login, recall that the mode and 2nd quartile were similar, yet the other descriptive statistics were much larger. In contrast, the age variable's descriptive stats are closer together. How this will change the way a histogram of age will look? .We know the age data should look more "normal". A normal distribution will have a symmetric and "bell-shaped" silouette. There shouldn't be outliers or a skew.
- COnclusion : Age is less skewed and more "normal". Marketing isn't targeting one age demographic disproportionately.Refer [viz_age](excels/viz_age.xlsx)

### Tipping the scale to positive correlation
- Here we will learn how a scatter plot represents a correlation value

#### Correlation tips from one to negative one
- Correlation is a measure between two variables. Its value ranges from -1 to 1. 
- `Correlation = -1` : When the value is **negative** that means the variables have an **opposite relationship**. As one variable increases the other will decrease.
- `Correlation = 1` : Positive correlation means as one variable increases so does the other.
- `Correlation = 0` : Means a weak or no relationship
- Note that just because one value increases doesnt mean that it **causes** the other values to increase or decrease.
- Correlation can be visualized on scatter plot.

##### Investigating age and volunteering
- Earlier we observed a strong correlation between age & annual religious observation. Another interesting field which could indicate a profile's moral values is the number of volunteer hours annually. In each profile a user can add information regarding their annual estimated hours spent volunteering.In addition to correlation we decide to plot a scatter plot. If there is a correlation between age & volunteer_hrs, we should be able to observe a trend sloping upward or downward. If the correlation is low, we could sumarize that people volunteer at similar rates regardless of their age.
- COnclusion : We didn't see any correlation relationship. Let's try another variable! Refer [correl_age_volunteering](excels/correl_age_volunteering.xlsx)

### More complex statistical relationships
- Multiple Regression in sheets : `LINEST(y-variables, x-variables)`

##### Are gender and number of roommates independent?
- As it turns out, the dating website also has information on gender and the number of roommates each profile has, so let's "pivot" for a moment and explore whether the two are independent using a chi-squared independence test.Although we believe age and roommates could be related, we suspect that gender has no impact on the number of roommates.On the right is a frequency pivot table from 200 profiles. 
- H0: The `roommates` & `gender` variables are independent
- H1: The `roommates` & `gender`  variables are not independent
- Accept H0. Refer [chi_test](excels/chi_test.xlsx)

##### Getting old and rich
- Going a level deeper, we now want to calculate the exact relationship between age and income. Explicitly calculating the incremental relation between these important matching variables will help the marketers in our company complete user person and gain a specific picture of many of the profile attributes. In review, the CORREL() function accepts an X column and a Y column for comparison. In our analysis, x = age and y = income. Refer [correl](excels/correl.xlsx)

##### Multiple relationships!
- Using the LINEST() function, we explored how one variable related to another. This is a univariate linear regression with a y-intercept and one coefficient. The single coefficient along with the y-intercept demonstrates how the dependent-y variable changes with one unit measure change in the single independent-x variable. Since we are concerned with many dimensions of a profile and the users' overall site activity, we need **multiple linear regression**, in which there are many X variable coefficients impacting Y. This equation calculates the estimated outcome of our **multiple linear regression**, where we're interested in how the hours since last login is affected by age, income, and hours volunteered.
- `Hours since last login = (age_coeff * age) + (income_coeff * income) + (volunteer_coeff * volunteerHrs) + y-intercept`
- Refer [multiple_regression](excels/multiple_regression.xlsx)


## Reference
- Datacamp : Introduction to Statistics in Spreadsheets
































