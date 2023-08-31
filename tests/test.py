import pytest
import pandas as pd
from dataclean import QualityCheck as qc


@pytest.fixture
def get_test_weekly_df():
    """Create test pandas DataFrame
    """
    return pd.DataFrame(
                    [
                        ['Ice Cream', 'Albany', '12/09/2017', 199, 491.81], 
                        ['Ice Cream', 'Los Angeles', '12/16/2017', 170, 417.46], 
                        ['Cheese', 'Chicago', '12/23/2017', 192, 465.11], 
                        ['Milk', 'Albany', '12/30/2017', 135, 331.32]
                    ],
                    columns=['product', 'store', 'date', 'units', 'sales'])

@pytest.fixture
def get_test_daily_df():
    """Create test pandas DataFrame
    """
    return pd.DataFrame(
                    [
                        ['Ice Cream', 'Albany', '12/09/2017', 199, 491.81], 
                        ['Ice Cream', 'Los Angeles', '12/10/2017', 170, 417.46], 
                        ['Cheese', 'Chicago', '12/11/2017', 192, 465.11], 
                        ['Milk', 'Albany', '12/12/2017', 135, 331.32]
                    ],
                    columns=['product', 'store', 'date', 'units', 'sales'])

def test_check_dups(get_test_weekly_df: callable):
    assert qc.check_duplicates(get_test_weekly_df, cols=['product', 'store', 'date']) is None

def test_check_missing_daily_dates(get_test_daily_df: callable):
    assert qc.check_missing_daily_dates(get_test_daily_df, col='date').empty

def test_check_missing_weekly_dates(get_test_weekly_df: callable):
    assert qc.check_missing_weekly_dates(get_test_weekly_df, col='date').empty

