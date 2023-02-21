"""
Data Analytics Fundamentals

Eric Meyer

2/18/2023

Creating custom functions for use in data exploration. This should speed up time to quickly analyze a dataset in the future.

"""

# custom functions for quick data analysis of a dataset

def load():
    import pandas as pd
    global df
    df = pd.read_csv('human_resources.csv', index_col=1)

def top_rows():
    print('Top 5 rows of data:')
    print()
    a = df.head()
    print(a,'\n')
    print('--------------------------------------------------------------------------------------------------------------')

def bottom_rows():
    print('Bottom 5 rows of data:')
    print()
    b = df.tail()
    print(b, '\n')
    print('--------------------------------------------------------------------------------------------------------------')

def rows_columns():
    print('Number of rows and columns in data:')
    print()
    print(df.shape, '\n')
    print('--------------------------------------------------------------------------------------------------------------')

def col_names():
    print('Column names in data:')
    print()
    d = df.columns
    print(d, '\n')
    print('--------------------------------------------------------------------------------------------------------------')

def stats_summary():
    print('Descriptive statistics summary of data:')
    print()
    e = df.describe()
    print(e, '\n')

def eda():
    load()
    top_rows()
    bottom_rows()
    rows_columns()
    col_names()
    stats_summary()


