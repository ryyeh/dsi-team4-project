import pandas as pd

#
# Load dataset from file and apply basic data cleaning:
#
#  1. align all end dates to 2018-11-29
#  2. sort by 'slug' and 'date'
#
def load_coin_data(data_file):
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

    return df

#
# Filter dataset to only contain coins with specific number of years of data.
# available. By default filter out coins with less than 4 years of data.
#
def filter_by_years(df, years=4):
    return df.groupby('slug').filter(lambda x: len(x) > (365 * years))

#
# Split dataset by specific date. By default it will split the data so there's
# one year worth of data for the test dataset.
#
def split_train_test(df, date='2017-11-29'):
    train = df.loc[df['date'] < date]
    test = df.loc[df['date'] >= date]
    return train, test