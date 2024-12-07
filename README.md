# team4-project

# Problem Statement
________________________________________
The Data and The Problem:
This cryptocurrency dataset consists of 1 million rows of historical data for 2071 different coins, containing their transaction volume, market and daily price information such as open, high, low and close values. 
Our aim is to utilize this data to provide actionable advice for traders by giving them selling or buying signals. Signals are produced based on the predicted value of closing price compared to that of today, with a 5% gauge, meaning increase or decrease of the price should be exceeding that limit to result in a buy/sell signal, below that it is a hold. 

Solution:
This was achieved by using different models run by each team members on this time series problem. For the sake of simplicity, the calculations were limited to prediction of closing price for bitcoin. The most significant feature engineering done was using lagged features, for instance, by transforming the closing price to 3 more lagged variables named “Closing T-1”, “Closing T-2”, and “Closing T-3”, representing closing prices for the day before, two days before and 3 days before each date (not necessarily continuous days in calendar as prices not represented for each day of the week). As we are dealing with a time series problem, the main idea in spiliting the data was to use the last year as the validation set. Finally, for each model visualization of predicted values over validation values are done and along side other metrics, performance of all the models were shown and compared.

Some Additional Tips about Team Members' Model(s):
* Mung O Zhou


* Ryan Yeh


* Hosein Aliyari


* Obinna Emmanuel Nwachukwu-udaku


* Dayaram Khadka





Extra steps:
1- Do the same for all of the coins.
2- An automated selling/buying program to maximize the profit gained from a limited entry amount, traded between a limited number of coins, in a limited timeframe (for instance, a week). Next step would be to removing the limitation on the set of coins available for trading.


## Team Members
* Mung O Zhou
* Ryan Yeh
* Hosein Aliyari
* Obinna Emmanuel Nwachukwu-udaku
* Dayaram Khadka
