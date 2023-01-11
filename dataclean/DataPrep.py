import pandas as pd

def format_date_col(df, date_col='date'):
        
    def date_to_str(date):
        """
        Takes in datetime and outputs a string formatted as mm/dd/yyyy

        Apply to a dataframe by using `df['date'].agg(date_to_str)`

        Args:
            date (datetime): datetime value
        
        Returns:
            date (str): date as "mm/dd/yyyy"
        """
        year, month, day = str(date.date()).split("-")
        return f"{month}/{day}/{year}"
    
    df[date_col] = pd.to_datetime(df[date_col])
    return df[date_col].agg(date_to_str)


def split_dataframes(df, col):
    """Splits the dataframe into separate dataframes based on different values in a column

    Args:
        df (DataFrame): pandas DataFrame
        col (str): column name
    
    Returns:
        dict: Dictionary of dataframes separated based on a column's category
    """
    dataframe_dict = {elem: pd.DataFrame() for elem in df[col].unique()}

    for key in dataframe_dict:
        dataframe_dict[key] = df[:][df.col == key]
    return dataframe_dict

def intersection_between_df(df, groupby_id, col):
    """Returns the values that intersect between each df Group specified. For example, for each Date (groupby_id), you want to see which Shops (col) intersect

    Args:
        groupby_id (str): Column name(s) to how you want to split your dataframe up into groups
        col (str): Column name for what you want to see intersect

    Returns:
        set: All values that intersect between each group
    """

    return set.intersection(*[set(group[col]) for name, group in df.groupby(groupby_id)])