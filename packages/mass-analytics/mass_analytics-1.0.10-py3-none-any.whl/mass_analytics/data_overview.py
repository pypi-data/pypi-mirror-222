import pandas as pd
import os
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
from .reader import read_data

def data_summary(path):
    """
    Generate a summary of each CSV, XLS, or XLSX file in the specified path.

    Parameters:
        path (str): The directory path containing CSV, XLS, or XLSX files.

    Returns:
        pandas.DataFrame: A data frame with the following columns:
            - 'file_name': The name of the file (including the extension).
            - 'nb_rows': The number of rows in the file.
            - 'nb_columns': The number of columns in the file.
            - 'prop_null': The proportion of null values in the file.

    Note:
        - Supported file formats: CSV, XLS, and XLSX.
        - The function will skip files with unsupported formats.
        - The 'prop_null' column represents the proportion of missing (null) values
          in the data, calculated as the number of missing values divided by the total
          number of elements in the file.
    """
    
    if os.path.isdir(path):
        for (dirpath, dirnames, filenames) in os.walk(path):
            break
    else:
        filenames = [os.path.basename(path).split('/')[-1]]

    new_df = {'file_name': [],
              'nb_rows': [],
              'nb_columns': [],
              'prop_null': []
             }

    for file in filenames:
        try:
            df = read_data(path+'/'+file)
        except Exception as e:
            print(e, file)
            continue
        
        new_df['file_name'].append(file)
        new_df['nb_rows'].append(df.shape[0])
        new_df['nb_columns'].append(df.shape[1])
        new_df['prop_null'].append(("{:.2f}".format(((1 - (df.count().agg("sum") / (new_df['nb_rows'][-1] * new_df['nb_columns'][-1])))) * 100)))

    return pd.DataFrame(new_df)

def categorical_summary(path):
    """
    Generate a summary of categorical columns in CSV, XLS, or XLSX files located in the given path.

    Parameters:
        path (str): The path to the directory containing CSV, XLS, or XLSX files.

    Returns:
        pandas.DataFrame: A DataFrame with columns 'file_name', 'categorical_columns', and 'nunique'.
                          Each row represents a file in the path and provides information about the
                          number of unique values in each categorical column found in that file.
    """

    if os.path.isdir(path):
        for (dirpath, dirnames, filenames) in os.walk(path):
            break
    else:
        filenames = [os.path.basename(path).split('/')[-1]]
    
    new_df = {'file_name': [],
              'categorical_columns': [],
              'nunique': [],
             }
    
    for file in filenames:
        try:
            df = read_data(path+'/'+file)
        except Exception as e:
            print(e, file)
            continue
        
        columns = []
        for col in df.columns:
            if is_string_dtype(df[col].dropna()):
                columns.append(col)
        
        if len(columns) == 0:
            print('No categorical columns found in the DataFrame', file)
            continue
        
        for col in columns:
            new_df['file_name'].append(file)
            new_df['categorical_columns'].append(col)
            new_df['nunique'].append(len(df[col].unique()))

    return pd.DataFrame(new_df)

def numerical_summary(path):
    """
    Generate a summary of numerical columns in CSV, XLS, or XLSX files located in the given path.

    Parameters:
        path (str): The path to the directory containing CSV, XLS, or XLSX files.

    Returns:
        pandas.DataFrame: A DataFrame with columns 'file_name', 'num_column', 'min', and 'max'.
                          Each row represents a file in the path and provides information about the
                          minimum and maximum values for each numerical column found in that file.
    """

    if os.path.isdir(path):
        for (dirpath, dirnames, filenames) in os.walk(path):
            break
    else:
        filenames = [os.path.basename(path).split('/')[-1]]
    
    new_df = {'file_name': [],
              'num_column': [],
              'min': [],
              'max': [],
             }
    
    for file in filenames:
        try:
            df = read_data(path+'/'+file)
        except Exception as e:
            print(e, file)
            continue
        
        columns = []
        for col in df.columns:
            if is_numeric_dtype(df[col].dropna()):
                columns.append(col)
        
        if len(columns) == 0:
            print('No numerical columns found in the DataFrame', file)
            continue
        
        for col in columns:
            new_df['file_name'].append(file)
            new_df['num_column'].append(col)
            new_df['min'].append(format(min(df[col].dropna()), ".2f"))
            new_df['max'].append(format(max(df[col].dropna()), ".2f"))

    return pd.DataFrame(new_df)


