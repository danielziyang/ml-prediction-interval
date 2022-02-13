import pandas as pd
import pytest

from src.data_prep.categorical import lowercase_string, lowercase_column, extract_title


def test_extract_title():
    string_col = ['futrelle, mme. jacques heath (lily may peel)',
                  'johnston, ms. catherine helen "carrie"',
                  'sloper, mr. william thompson',
                  'ostby, lady. engelhart cornelius',
                  'backstrom, major. karl alfred (maria mathilda gustafsson)']
    df_dict = {'string': string_col}
    lowercased_df = pd.DataFrame(df_dict)

    result = extract_title(lowercased_df, col='string')
    assert result['title'].tolist() == ['mme', 'ms', 'mr', 'lady', 'major']