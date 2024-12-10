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
| Linear Regression | 328.06 | 296458.68 | 544.48 | 0.9689 | 3281.01 | 0.9678 |
| KNN Regression | 1247.33 | 4714672.25 | 2171.33 | 0.5179 | 9679.05 | 0.4875 |
| Deep Learning 1 | 431.16 | 448236.18 | 669.50 | 0.9552 | 5219.09 | 0.9515 |
| Deep Learning 2 | 514.77 | 542471.52 | 736.53 | 0.9604 | 5280.18 | 0.9413 |


### Linear Regression

The linear regression was the first model we built as proof of concept. The input variables are the closing prices of the 3 previous days. The model's predictions are on average $328.06 away from the actual values (MAE), which is 3.82% of the average close price ($8580.20). This indicates a relatively good model.

![linear_regression](https://github.com/user-attachments/assets/d94ce6b8-167e-4b21-ac0b-1dc2d939bc99)

### KNN Regression

The KNN regression predicts the coin's next day's closing price using past 5 days' closing prices and the %change in the past 5-day moving average of closing price. The resulting predictions and errors show that that KNN regression is range-bound and meets challenge with data that falls outside the training range.

![knn_price_prediction](https://github.com/user-attachments/assets/b8e86ad6-67eb-424b-9d6a-7af9a2d95a64)

### Deep Learning 1

The deep learning model trained have the following parameters:
* input features consists of closing price from 3 previous days
* 4 layers of dense layer consisting of 690k parameters

One important caveat regarding the performance metrics is that for deep learning, the dependent variable was normalized thus all the numbers seems significantly bettern than that of the non-deep learning models. A better metrics for comparison is the R_Squared score which indicates the corrlation between the actual and predicted prices.

![dl_1](https://github.com/user-attachments/assets/4acbca70-78e8-4320-8d4e-4815ef2c271d)
  
### Deep Learning 2

The second deep learning model trained have the following parameters:
* input features consists of open, high, low and close prices
* 3 layers of dense layers and dropout layers in between

detailed explanation in model file

![dl_2](https://github.com/ryyeh/dsi-team4-project/blob/main/code/Hosein's/predection.png)


## Team Members and their presentation videos

* Mung O Zhou - [Video](https://drive.google.com/file/d/1pBl9xKKIH0rX4qNzNdeFPcdHm3KO0UDz/view?usp=sharing)
* Ryan Yeh - [Video](https://drive.google.com/file/d/1oWu48oy8xFslrAcduzJ2ha7mC7BzDvcw/view?usp=share_link)
* Hosein Aliyari - [Video](https://drive.google.com/file/d/1ZDgDCYVKxKktJ3nrAl2e59BY-UTdcYhV/view?usp=sharing)
* Obinna Emmanuel Nwachukwu-udaku
* Dayaram Khadka - [Video](https://drive.google.com/file/d/14bMeP8Fzza8vLgAJw50hsG2S1d2uBbLc/view?usp=sharing)

## Future Enhancements

1. An automated selling/buying program to maximize the profit gained from a limited entry amount, traded between a limited number of coins, in a limited timeframe (for instance, a week). Next step would be to removing the limitation on the set of coins available for trading.
