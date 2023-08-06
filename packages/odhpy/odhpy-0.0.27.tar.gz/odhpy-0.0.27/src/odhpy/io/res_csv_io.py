import os
import numpy as np
import pandas as pd
from odhpy import utils
#na_values = ['', ' ', 'null', 'NULL', 'NAN', 'NaN', 'nan', 'NA', 'na', 'N/A' 'n/a', '#N/A', '#NA', '-NaN', '-nan']



def read_res_csv(filename, df=None, colprefix="", **kwargs):
    """Reads a res csv data file into a DataFrame, and sets the index to the Date.

    Args:
        filename (_type_): _description_

    Returns:
        _type_: _description_
    """
    # If no df was supplied, instantiate a new one
    if df is None:
        df = pd.DataFrame()  
    # Scrape through the header
    metadata_lines = []
    with open(filename) as f:
        line = ""
        for line in f:
            metadata_lines.append(line)   
            if line.strip() == "EOH":
                break
    header_line = len(metadata_lines) - 2
    lines_to_skip = [i for i in range(header_line)] + [header_line + 1]
    # Read the data
    temp = pd.read_csv(filename, skiprows=lines_to_skip) #lines_to_skip, **kwargs)
    temp = utils.set_index_dt(temp, dayfirst=True, format=r"%Y-%m-%d")    
    temp.index.name = 'Date'
    temp = temp.replace(r'^\s*$', np.nan, regex=True)
    if colprefix is not None:
        for c in temp.columns:
            temp.rename(columns = {c:f"{colprefix}{c}"}, inplace = True)        
    df = df.join(temp, how="outer").sort_index()
    utils.assert_df_format_standards(df)
    return df
