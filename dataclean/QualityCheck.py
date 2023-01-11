import pandas as pd
import numpy as np
import datetime as dt
import altair as alt
import missingno as msno

# QC data
class QualityCheck():

    def __init__(self, data):
        self.data = data
    
    def check_duplicates(self, cols=None):
        """Checks for duplicates in a dataframe and returns all instances

        Args:
            df (DataFrame): Company's sales data containing an 'ID' column
            cols(str or list): pass a string for a single column or list of the column names

        Returns:
            DataFrame: All duplicates in a DataFrame
        """
        if cols is None:
            cols = ['ID']
        try:
            dups = pd.concat(g for _, g in self.data.groupby(cols) if len(g) > 1)
        except ValueError:
            print("No duplicates")
        else:
            return dups
    
    def check_missing_daily_dates(self, col='DATE'):
        """Converts your date column in datetime data type and then checks for any missing daily dates between the minimum and maximum

        Args:
            df (DataFrame): Company's sales data containing the 'DATE' column

        Returns:
            str: States the minimum and maximum date and returns a list of missing daily dates
        """
        # Convert to datetime
        self.data[col] = pd.to_datetime(self.data[col])
        print('The minimum date is:', self.data[col].min())
        print('The maximum date is:', self.data[col].max())
        # Store the min and max date
        min_date = self.data[col].min()
        max_date = self.data[col].max()
        # Set the datetime as the DataFrame's index and find any missing dates 
        df1 = self.data.set_index(col)
        df1.index = pd.to_datetime(df1.index)
        # Create a range with all the dates, then use 'difference' to find what's missing
        return pd.date_range(start=min_date, end=max_date).difference(df1.index)

    def check_missing_weekly_dates(self, col='DATE'):
        """Converts your date column in datetime data type and then checks for any missing weekly dates between the minimum and maximum

        Args:
            df (DataFrame): Company's sales data containing the 'DATE' column
            col (str): date column name

        Returns:
            str: States the minimum and maximum date and returns a list of missing weekly dates
        """
        # Convert to datetime
        self.data[col] = pd.to_datetime(self.data[col])
        print('The minimum date is:', self.data[col].min())
        print('The maximum date is:', self.data[col].max())
        # Store the min and max date
        min_date = self.data[col].min()
        max_date = self.data[col].max()
        # Set the datetime as the DataFrame's index and find any missing dates 
        df1 = self.data.set_index(col)
        df1.index = pd.to_datetime(df1.index)
        # Create a range with all the dates, then use 'difference' to find what's missing
        return pd.date_range(start=min_date, end=max_date, freq='7D').difference(df1.index)
    
    def min_and_max_dates(self, col='DATE'):
        """Returns the minimum and maximum dates in the date range and the 3 year history and 5 years back for the CTMU date
        
        Args:
            df (DataFrame): Company's sales data containing the 'DATE' column

        Returns:
            str: Description of the dataset's date range, history, and CTMU date
        """
        min_date = pd.to_datetime(self.data[col]).dt.date.min()
        max_date = pd.to_datetime(self.data[col]).dt.date.max()
        history = pd.to_datetime(self.data[col]).dt.date.max()-dt.timedelta(weeks=156)
        CTMU = pd.to_datetime(self.data[col]).dt.date.max()-dt.timedelta(weeks=260)
        print(f'Date range: {min_date} to {max_date}')
        return print(f'The 3-year history is {history}. The CTMU is {CTMU}')

    def monthly_revenue_plot(self, title='Chart', date='date', metric='revenue', width=800):
        """Plots a visual of the company's monthly revenue/metric/transactions

        Args:
            df (pandas DataFrame): Company's sales data with 'DATE' and 'REVENUE' column

        Returns:
            plot: Plot of monthly revenue
        """
        # Convert 'DATE' column to datetime
        self.data[date] = pd.to_datetime(self.data[date])
        # Group by the dates being transformed in month and year
        sum_of_revenue = self.data.groupby(by=self.data[date].dt.strftime('%Y %B')).sum().reset_index(drop=False)
        # Convert the date into datetime again to sort in order
        sum_of_revenue[date] = pd.to_datetime(sum_of_revenue[date]).sort_values().reset_index(drop=True)
        sum_of_revenue = sum_of_revenue.rename(columns={date: 'MONTH'})
        return alt.Chart(sum_of_revenue).mark_line(
            color='lightblue',
            point=alt.OverlayMarkDef(color='darkblue'),
            width=30).encode(
                x=alt.X('MONTH:O', timeUnit='yearmonth', axis=alt.Axis(labelAngle=-90)),
                y=metric,
                ).properties(width=width, title=title).interactive()

    def multiple_line_plot(self, title='Chart', date='date', width=800):
        # Convert 'DATE' column to datetime
        self.data[date] = pd.to_datetime(self.data[date])
        # Group by the dates being transformed in month and year
        sum_of_revenue = self.data.groupby(by=self.data[date].dt.strftime('%Y %B')).sum().reset_index(drop=False)
        # Convert the date into datetime again to sort in order
        sum_of_revenue[date] = pd.to_datetime(sum_of_revenue[date]).sort_values().reset_index(drop=True)
        sum_of_revenue = sum_of_revenue.rename(columns={date: 'MONTH'})
        # Transform data so multiple metrics can be plotted
        df_melt = sum_of_revenue.melt(id_vars='MONTH', var_name='VARIABLE', value_name='VALUE')

        alt.Chart(df_melt).mark_line(
            color='lightblue',
            point=alt.OverlayMarkDef(color='darkblue'),
            width=30).encode(
                x=alt.X('MONTH:O', timeUnit='yearmonth', axis=alt.Axis(labelAngle=-90)),
                y='VALUE',
                color='VARIABLE'
                ).properties(title=title, width=width).interactive()
    
    def missing_values_matrix(self):
        return msno.matrix(self.data)