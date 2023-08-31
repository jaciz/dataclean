import pandas as pd
import glob
import os
import polars as pl
# Increase column width to see more of the data
pl.Config.set_fmt_str_lengths(200)

# File reading
def read_multiple_txt(path: str, dtype=None, parse_dates=None, skiprows=None, sep=None, header='infer', file_extension='csv'):
    """Brings in all files in a directory and combines it into one dataframe

    Args:
        path (str): Folder path
        dtype (dict/str, optional): Datatypes of your columns. Defaults to None.
        parse_dates (list, optional): list of columns you want transformed to date type. Defaults to None.
        skiprows (int, optional): number of rows to skip when reading file. Defaults to None.
        sep (str, optional): field separator. Defaults to None.
        header (str, optional): _description_. Defaults to 'infer'.
        file_extension (str, optional): File extension, can be gz, txt, tab, csv, etc. Defaults to 'csv'.

    Returns:
        pandas DataFrame: Combined pandas dataframe of all files in the folder along with a column of the filename
    """
    # Create a list of dataframes
    df_list = (pd.read_csv(file, dtype=dtype, parse_dates=parse_dates, skiprows=skiprows, sep=sep, header=header) for file in glob.glob(f'{path}/*.{file_extension}'))

    # Concatenate all DataFrames
    return pd.concat(df_list, ignore_index=True)

def read_multiple_txt_with_filename(path, dtype=None, parse_dates=None, skiprows=None, sep=None, header='infer', file_extension='csv'):
    """Brings in all files in a directory and combines it into one dataframe with a column listing the file name

    Args:
        path (str): Folder path
        dtype (dict/str, optional): Datatypes of your columns. Defaults to None.
        parse_dates (list, optional): list of columns you want transformed to date type. Defaults to None.
        skiprows (int, optional): number of rows to skip when reading file. Defaults to None.
        sep (str, optional): field separator. Defaults to None.
        header (str, optional): _description_. Defaults to 'infer'.
        file_extension (str, optional): File extension, can be gz, txt, tab, csv, etc. Defaults to 'csv'.

    Returns:
        pandas DataFrame: Combined pandas dataframe of all files in the folder along with a column of the filename
    """
    df = pd.DataFrame()
    for p in list(glob.glob(f'{path}/*.{file_extension}')):
        subset = pd.read_csv(p, dtype=dtype, parse_dates=parse_dates, skiprows=skiprows, header=header, sep=sep)
        subset['file'] = os.path.basename(p)
        df = pd.concat([df, subset])
    
    return df

# Functions written in polars
def read_multiple_txt_with_filename_polars(path, dtypes=None, parse_dates=False, skip_rows=0, sep=',', has_header=True, null_values=None, new_columns=None, file_extension='csv'):
    df = pl.DataFrame().lazy()
    for p in list(glob.glob(f'{path}/*.{file_extension}')):
        subset = (
            pl.read_csv(p, dtypes=dtypes, parse_dates=parse_dates, skip_rows=skip_rows, has_header=has_header, sep=sep, new_columns=new_columns, infer_schema_length=0, null_values=null_values)
            .lazy()
        ).with_column(pl.lit(os.path.basename(p)).alias('file'))
        

        df = pl.concat([df, subset], how='diagonal')
    
    return df.collect()

def read_multiple_txt_polars(path: str, dtypes=None, sep=None, has_header=True, file_extension='csv', new_columns=None):
    # Create a list of dataframes
    df_list = [
        pl.read_csv(file, dtypes=dtypes, sep=sep, has_header=has_header, new_columns=new_columns)
        for file in glob.glob(f'{path}/*.{file_extension}')
    ]

    # Concatenate all DataFrames
    return pl.concat(df_list, how='diagonal')


def read_multiple_parquet_polars(path):
    # Create a list of dataframes
    df_list = [
        pl.read_parquet(file)
        for file in glob.glob(f'{path}/*.parquet')
    ]

    # Concatenate all DataFrames
    return pl.concat(df_list, how='diagonal')