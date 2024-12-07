# Problem Statement

## The Data and The Problem

This [cryptocurrency dataset](https://www.kaggle.com/datasets/jessevent/all-crypto-currencies/data) consists of 1 million rows of historical data for 2071 different coins, containing their transaction volume, market and daily price information such as open, high, low and close values. 
Our aim is to utilize this data to provide actionable advice for traders by giving them selling or buying signals. Signals are produced based on the predicted value of closing price compared to that of today, with a 5% gauge, meaning increase or decrease of the price should be exceeding that limit to result in a buy/sell signal, below that it is a hold. 

[Note: due to time constraint, only model development and evaluation were done. Buy/Sell signal generation will be done at a later time]

As proof of concept, our models are only trained with the 'bitcoin':

![btc_price](https://github.com/user-attachments/assets/70d732a5-58b9-499b-bf9c-02fccf3257a9)

## Solution

Various machine learning models were built to solve this time series prediction problem. The most significant feature engineering done was using lagged features, for instance, by transforming the closing price to 3 more lagged variables named “Closing T-1”, “Closing T-2”, and “Closing T-3”, representing closing prices for the day before, two days before and 3 days before each date. For training and testing data split, we set aside the data from last year as the test set. Finally, for each model visualization of predicted values over validation values are done and along side other metrics, performance of all the models were shown and compared.

## Summary of our models

| Models | MAE | MSE | RMSE | Explained Variance | Max Error | R-Squared |
| ----------- | ----------- | ----------- | ----------- |----------- |----------- |----------- |
| Linear Regression | 95.49 | 62829.70 | 250.66 | Nan | Nan | Nan |
| Knn Regression | 1225.32 | Nan | 2160.37 | 0.5247 | 9679.05 | 0.4926 |

### Linear Regression

The linear regression was the first model we built as proof of concept. The input variable are the closing price of the 3 previous days. The model's predictions are on average $95.49 away from the actual values (MAE), which is 4.2% of the average close price ($2287.29). This indicates a relatively good model.

### KNN Regression

The KNN regression predicts the coin's next day's closing price using past 5 days' closing prices and the %change in the past 5-day moving average of closing price. The resulting predictions and errors show that that KNN regression is range-bound and meets challenge with data that falls outside the training range.

![knn_price_prediction](https://github.com/user-attachments/assets/b8e86ad6-67eb-424b-9d6a-7af9a2d95a64)

### Deep Learning 1

### Deep Learning 2


## Team Members and their presentation videos

* Mung O Zhou
* Ryan Yeh
* Hosein Aliyari
* Obinna Emmanuel Nwachukwu-udaku
* Dayaram Khadka
    * https://drive.google.com/file/d/14bMeP8Fzza8vLgAJw50hsG2S1d2uBbLc/view?usp=sharing


## Future Enhancements

1. An automated selling/buying program to maximize the profit gained from a limited entry amount, traded between a limited number of coins, in a limited timeframe (for instance, a week). Next step would be to removing the limitation on the set of coins available for trading.
