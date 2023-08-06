import pandas as pd
import numpy as np
import datetime
from .date import (get_date_columns,
                  is_date)


def pivot_by_key(df, index_column_names, key_column_names, values_column_names, agg_funcs='sum'):
    """
    Description
        Pivots a DataFrame based on the given keys and performs aggregation on the specified value columns.

    Parameters:
        df (pd.DataFrame): The DataFrame to pivot and perform aggregation on.
        index_column_names (list): List of column names to be used as index during pivoting.
        key_column_names (list): List of column names to be used as keys for pivoting.
        values_column_names (list): List of column names to be used as values for pivoting.
        agg_funcs (dict, optional): Dictionary mapping columns to aggregation functions. The default is {'column_name': 'sum'}.

    Returns:
        pd.DataFrame: The resulting pivoted DataFrame with aggregation.
    
    Example:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'Date': ['1/1/2020', '1/2/2020', '1/3/2020'],
        ...                    'col1': ['A', 'B', 'C'],
        ...                    'col2': ['X', 'Y', 'Z'],
        ...                    'price': [10, 11, 15],
        ...                    'nb': [2, 1, 3]})
        >>> result = pivot_by_key(df, index_column_names='Date', key_column_names=['col1', 'col2'],
        ...                       values_column_names=['price', 'nb'], agg_funcs={'price': 'mean', 'nb': 'sum'})
        >>> print(result)
        
             Date          A_X_nb   B_Y_nb   C_Z_nb   A_X_price   B_Y_price   C_Z_price    
        0    1/1/2020        2        0        0        10          0           0
        1    1/2/2020        0        1        0        0           11          0
        2    1/3/2020        0        0        3        0           0           15
    """
    
    df['key'] = df.apply(lambda x: '_'.join([str(x[st]) for st in key_column_names]), axis=1)
    pivot_table = pd.pivot_table(df, values=values_column_names, index=index_column_names, columns='key', aggfunc=agg_funcs, fill_value=0)

    new_df = pd.DataFrame()
    for cols in pivot_table.columns:
       new_df['_'.join(cols[::-1]).strip(" .;,:*-()[]/!?").replace(" ","_")] = pivot_table[cols]
       
    new_df.reset_index(inplace=True)
    
    return new_df

def get_mapping_table(df, date_column_name, column_values, freq='D'):
    """
    Description
        Create a mapping table based on the provided DataFrame, date column, and column values.

        The function generates a new DataFrame that contains all unique combinations of the date
        values (within the specified frequency) and the unique values of each column in the 
        'column_values' list.

    Parameters:
        df (pandas.DataFrame): The original DataFrame containing the data.
        date_column_name (str): The name of the column that holds the date values.
        column_values (list): A list of column names for which unique values will be used
                              to create combinations in the mapping table.
        freq (str, optional): The frequency string for date_range(). 
                              Defaults to daily 'D'.

    Returns:
        pandas.DataFrame: A new DataFrame representing the mapping table with date_column_name 
                          and unique values from each column in column_values.

    Note:
        - If the 'freq' parameter is not provided, the function will attempt to infer it from the 
          date_column_name using the get_periodicity() function.
        - Make sure to provide a valid 'freq' frequency string, such as 'D' for daily, 'M' for monthly, 
          'Y' for yearly, etc.
        - The returned DataFrame will have a row for each unique combination of date and column 
          values from the original DataFrame.

    Example:
        >>> import pandas as pd
        >>> data = {
        ...     'Date': ['2023-07-01', '2023-07-02'],
        ...     'Product': ['A', 'B'],
        ...     'Category': ['X', 'Y'],
        ...     'Price': [100, 150],
        ... }
        >>> df = pd.DataFrame(data)
        >>> result = get_mapping_table(df, date_column_name='Date', column_values=['Product', 'Category'], freq='D')
        >>> print(result.to_string(index=False))
                 Date Product Category
        0  2023-07-01       A       X
        1  2023-07-02       A       X
        2  2023-07-01       B       X
        3  2023-07-02       B       X
        4  2023-07-01       A       Y
        5  2023-07-02       A       Y
        6  2023-07-01       B       Y
        7  2023-07-02       B       Y
    
    """
    
    new_df = pd.DataFrame()
    
    new_df[date_column_name] = pd.date_range(start=min(df[date_column_name]), end=max(df[date_column_name]), freq=freq, inclusive='both')

    for col in column_values:
        new_df = pd.DataFrame(df[col].unique()).join(new_df, how='cross')
        new_df.rename(columns={0: col}, inplace=True)
    
    return new_df[new_df.columns[::-1]]

def map_table(df, mapping_table):
    """
    Description
        The map_table function is designed to map data from the original DataFrame to the provided mapping table. 
        It performs a left merge between the mapping_table and the original DataFrame (df) based on their common date column(s). 
        The function then fills in missing values in the merged DataFrame with 0.

    Parameters:
        df (pandas.DataFrame): The original DataFrame containing the data to be mapped.
        mapping_table (pandas.DataFrame): The mapping table containing unique combinations of 
                                          data and columns to which the original data will be 
                                          mapped.

    Returns:
        pandas.DataFrame: A new DataFrame resulting from the left merge of the mapping_table and 
                          the original DataFrame (df), with missing values filled in with 0.
    
    Note:
        - The merge is performed based on the common columns between the mapping_table and the 
          original DataFrame. Make sure that the mapping_table and the df have at least one 
          common column.
        - Any missing values in the merged DataFrame are filled with 0.
        - The returned DataFrame will have the same number of rows as the mapping_table and will 
          include the additional columns from the original DataFrame (df) that matched the 
          common columns in the mapping_table.
    
    Example:
        >>> import pandas as pd
        >>> df = pd.DataFrame({
        ...     'Date': ['2023-08-01', '2023-08-02', '2023-08-03', '2023-08-04', '2023-08-05'],
        ...     'Value': [10, 20, 30, 40, 50]
        ... })
        >>> mapping_table = pd.DataFrame({
        ...     'Date': ['2023-08-01', '2023-08-03'],
        ...     'Label': ['Label A', 'Label B']
        ... })
        >>> result_df = map_table(df, mapping_table)
        >>> print(result_df)

            Date        Value    Label
        0 2023-08-01     10     Label A
        1 2023-08-03     30     Label B
    """

    # Cast Object type to datetime (df)
    date_cols = get_date_columns(df)
    
    if type(date_cols) is str:
        date_cols = [date_cols]
    
    
    for col in date_cols:
        df = df.drop(df[df.apply(lambda x: not(is_date(x[col]) or isinstance(x[col], datetime.datetime)), axis=1)].index)
        if np.issubdtype(df[col].dtype, np.object_):
            try:
                df[col] = pd.to_datetime(df[col])
            except:
                print("Can\'t cast object to datetime type")
    
    # Cast Object type to datetime (mapping_table)
    date_cols = get_date_columns(mapping_table)
    if type(date_cols) is str:
        date_cols = [date_cols]
    
    for col in date_cols:
        mapping_table = mapping_table.drop(mapping_table[mapping_table.apply(lambda x: not(is_date(x[col]) or isinstance(x[col], datetime.datetime)), axis=1)].index)
        if np.issubdtype(mapping_table[col].dtype, np.object_):
            try:
                mapping_table[col] = pd.to_datetime(mapping_table[col])
            except:
                print("Can\'t cast object to datetime type")
    
    map_table = mapping_table.merge(df, how='left').fillna(0)
    
    return map_table

