# team4-project

Riseup Pad
https://pad.riseup.net/p/H9d3HHx6M4Qwnss_R_vq-keep


Problem Statement
________________________________________
This cryptocurrency dataset consists of 1 million rows of historical data for 2071 different coins, containing their transaction volume, market and daily price information such as open, high, low and close values.
Our aim is to utilize this data to provide actionable advice for traders by giving them selling or buying signals. 
These are planned to be achieved by using linear regression as the first approach. As the first step and to experiment the data, we limited our calculation to prediction of closing price for bitcoin, by transforming its closing price to 3 more lagged variables named “Closing T-1”, “Closing T-2”, and “Closing T-3”, representing closing prices for the day before, two days before and 3 days before each date (not necessarily continuous days in calendar as prices not represented for each day of the week). Then we would do the same for all of the coins, achieving the next day predicted price. By comparing that day price and the predicted price, now we are able to signal whether the price increases or decreases.
This would simply benefit day-traders, but we aim to include prediction for extended time periods in future as well, namely for 10,20 and 30 days.

To add:
? Different Models
? Use Deep Learning Models
? Turning it into a Classification problem
? Confidence Metric
? Error Metric, Precision Metric

To Implement:
•	Use past tense for last edition

Extra steps:
Also, another helpful scenario would be an automated selling/buying program to maximize the profit gained from a limited entry amount, traded between a limited number of coins, in a limited timeframe (for instance, a week). Next step would be to removing the limitation on the set of coins available for trading. (Hosein)


## Team Members
* Mung O Zhou
* Ryan Yeh
* Hosein Aliyari
* Obinna Emmanuel Nwachukwu-udaku
* Dayaram Khadka
