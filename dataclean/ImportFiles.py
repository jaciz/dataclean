import pandas as pd
import glob
import os

# File reading
def bringing_in_multiple_csv(path: str, dtype=None, parse_dates=None, skiprows=None, sep=None, header='infer', file_extension='csv'):
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

def bringing_in_multiple_csv_with_filename(path, dtype=None, parse_dates=None, skiprows=None, sep=None, header='infer', file_extension='csv'):
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
