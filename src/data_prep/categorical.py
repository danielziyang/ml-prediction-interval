import numpy as np
import pandas as pd

def lowercase_string(string: str) -> str:
    """Rerturns a lowercase string

    Args:
        string (str)

    Returns:
        str: lowercase
    """    
    return string.lower()

def lowercase_column(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Lowercases a column in a dataframe

    Args:
        df (pd.DataFrame): A dataframe
        col (str): Column in dataframe

    Returns:
        pd.DataFrame: Dataframe with column lowercased
    """    

    df[col] = df[col].apply(lowercase_string)
    return df 

def extract_title(df: pd.DataFrame, col:str, replace_dict: dict = None, title_col: str = 'title') -> pd.DataFrame:
    """Extracts title into a new title column

    Args:
        df (pd.DataFrame): A df
        col (str): A col in df
        replace_dict (dict, optional): Optional dict to map titles. Defaults to None.
        title_col (str, optional): Name of new column containing extracted titles. Defaults to 'title'.

    Returns:
        pd.DataFrame: A df wiith an additional column of extracted titles
    """    

    df[title_col] = df[col].str.extract(r'([A-Za-z]+)\.', expand=False)

    if replace_dict:
        df[title_col] = np.where(df[title_col].isin(replace_dict.keys()),
        df[title_col].map(replace_dict),
        df[title_col])
    
    return df