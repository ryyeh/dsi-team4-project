import pandas as pd

#
# Load dataset from file and apply basic data cleaning:
#
#  1. align all end dates to 2018-11-29
#  2. sort by 'slug' and 'date'
#
def load_coin_data(data_file='../../data/crypto-markets.csv'):
    try:
        df = pd.read_csv(data_file)
    except FileNotFoundError:
        print("ERROR: data file not found")
        return None
    
    # convert date column from string to datetime
    df['date'] = pd.to_datetime(df['date'])

    # align all end dates to '2018-11-29'
    df = df[df['date'] != '2018-11-30']

    # sort the dataset by 'slug' and 'dates'
    df = df.sort_values(['slug', 'date'])

    # add next closing price and next day return columns
    df['next_close'] = df.groupby('slug')['close'].shift(-1)
    df['next_return'] = (df['next_close'] - df['close']) / df['close']

    # drop the last row of each coins as we don't have the next day's closing price
    df = df.dropna()

    # reset the dataframe index
    df = df.reset_index(drop=True)

    return df

#
# Filter dataset to only contain coins with specific number of years of data.
# available. By default filter out coins with less than 4 years of data.
#
def filter_by_years(df, years=4):
    return df.groupby('slug').filter(lambda x: len(x) > (365 * years)).reset_index(drop=True)

#
# Split dataset by specific date. By default it will split the data so there's
# one year worth of data for the test dataset.
#
def split_train_test(df, date='2017-11-28'):
    train = df.loc[df['date'] < date].reset_index(drop=True)
    test = df.loc[df['date'] >= date].reset_index(drop=True)
    return train, test