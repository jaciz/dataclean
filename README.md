# Data Cleaning Library

`dataclean` provides a small toolset of quality check, data prep, and location prep utilities to bring your messy dataset to the desired format. These tools are mainly used for time series sales datasets.

## Get Started

Use `pip install git+https://github.com/jaciz/dataclean.git` to install the library

## Example

### `DataPrep`

```Python
from dataclean import DataPrep

# Will return date formatted  as mm/dd/yyyy
DataPrep.format_date_col(df, date_col='InvoiceDate')

# Will return a dictionary of dataframes split by Country
DataPrep.split_dataframes(df, 'Country')

# Will return the stock codes that are in all invoice dates
DataPrep.intersection_between_df(df, 'InvoiceDate', 'StockCode')
```

### `ImportFiles`

```Python
from dataclean import ImportFiles

# Brings in all files with a `.txt` extension into one dataframe
ImportFiles.bringing_in_multiple_csv(r'data/live/TestStores', sep='\t', dtype={
    'ShopCode': str, 
    'Article Category': str, 
    'Article Sub Category': str,
    'ArticleCode': str,
    'Article Name':str,
    'Date': str,
    'Variable': str
}, file_extension='txt')

# Brings in all files with a `.txt` extension into one dataframe with a filename column
ImportFiles.bringing_in_multiple_csv_with_filename(r'data/live/TestStores', sep='\t', dtype={
    'ShopCode': str, 
    'Article Category': str, 
    'Article Sub Category': str,
    'ArticleCode': str,
    'Article Name':str,
    'Date': str,
    'Variable': str
}, file_extension='txt')
```

### `LocationPrep`

```Python
from dataclean import LocationPrep

# Checks if all zip codes are in a 5 digit format or a 9 digit format with the hyphen
LocationPrep.valid_zip_codes(df, col='Zip')
```

### `QualityCheck`

```Python
from dataclean import QualityCheck

# Checks duplicates by product_name, date, and store
QualityCheck.check_duplicates(df, cols=['product_name', 'date', 'store'])

# Checks missing daily dates if data is in a daily frequency
QualityCheck.check_missing_daily_dates(df, col='DATE')

# Checks missing weekly dates if data is in a weekly frequency
QualityCheck.check_missing_weekly_dates(df, col='DATE')

# Returns the min and max dates, as well as the 3-year history and CTMU
QualityCheck.min_and_max_dates(df, col='DATE')

# Will output an Altair line chart
QualityCheck.monthly_revenue_plot(df, title='Chart', date='date', metric='revenue', width=800)

# Will output an Altair line chart of multiple metrics
QualityCheck.multiple_line_plot(df, title='Chart', date='date', width=800)

# Will output a matrix of missing values for each column
QualityCheck.missing_values_matrix(df)
```
