import pandas as pd
import numpy as np
import datetime as dt
import re
import altair as alt
import glob


# Location functions
class LocationPrep():

    def __init__(self, df):
        self.df = df      
    
    def valid_zip_codes(self, df, col='ZIP', pattern='^[0-9]{5}(-[0-9]{4})?$'):
        zip_list = list(df[col].unique())

        yes_list = []
        no_list = []

        p = pattern
        for eachnumber in zip_list:
            if result := re.match(p, eachnumber):
                yes_list.append(eachnumber)
            else:
                no_list.append(eachnumber)
        return print(f"There are {len(no_list)} entries that don't match zip code format")
