import pandas as pd

# Manipulating the data
class DataPrep:

    def __init__(self):
        self.df = self
    
    def format_date_col(self, date_col='date'):
            
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
        
        return self[date_col].agg(date_to_str)


    def split_dataframes(self, col):
        """Splits the dataframe into separate dataframes based on different values in a column

        Args:
            df (DataFrame): pandas DataFrame
            col (str): column name
        
        Returns:
            dict: Dictionary of dataframes separated based on a column's category
        """
        dataframe_dict = {elem: pd.DataFrame() for elem in self[col].unique()}

        for key in dataframe_dict:
            dataframe_dict[key] = self[:][self.col == key]
        return dataframe_dict

    def intersection_between_df(self, groupby_id, col):
        """Returns the values that intersect between each df Group specified. For example, for each Date (groupby_id), you want to see which Shops (col) intersect

        Args:
            groupby_id (str): Column name(s) to how you want to split your dataframe up into groups
            col (str): Column name for what you want to see intersect

        Returns:
            set: All values that intersect between each group
        """

        return set.intersection(*[set(group[col]) for name, group in self.groupby(groupby_id)])