import pandas as pd
import tqdm
import os
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
from .reader import read_data


def data_summary(path):
    """
    Description:
        Generate a summary of each CSV, XLS, or XLSX file in the specified path.

    Parameters:
        path (str): The directory path containing CSV, XLS, or XLSX files.

    Returns:
        pandas.DataFrame: A data frame with the following columns:
            - 'file_name': The name of the file (including the extension).
            - 'nb_rows': The number of rows in the file.
            - 'nb_columns': The number of columns in the file.
            - 'prop_null%': The proportion of null values in the file.

    Note:
        - Supported file formats: CSV, XLS, and XLSX.
        - The function will skip files with unsupported formats.
        - The 'prop_null' column represents the proportion of missing (null) values
          in the data, calculated as the number of missing values divided by the total
          number of elements in the file.
    
    Example:
        >>> path = '/path/to/files/'
        >>> summary_df = data_summary(path)
        >>> print(summary_df)
            file_name  nb_rows  nb_columns  prop_null%
        0  data_file.csv      100           5   0.023400
        1  data_file.xlsx      80           6   0.041250
        2  data_sheet.xls      50           4   0.005000
    """
    
    if os.path.isdir(path):
        for (dirpath, dirnames, filenames) in os.walk(path):
            break
    else:
        filenames = [os.path.basename(path).split('/')[-1]]

    new_df = {'file_name': [],
              'nb_rows': [],
              'nb_columns': [],
              'prop_null%': []
             }

    for file in tqdm.tqdm(filenames):
        try:
            df = read_data(path+'/'+file)
        except Exception as e:
            print(e, file)
            continue
        
        new_df['file_name'].append(file)
        new_df['nb_rows'].append(df.shape[0])
        new_df['nb_columns'].append(df.shape[1])
        new_df['prop_null%'].append(("{:.2f}".format(((1 - (df.count().agg("sum") / (new_df['nb_rows'][-1] * new_df['nb_columns'][-1])))) * 100)))

    return pd.DataFrame(new_df)

def categorical_summary(path):
    """
    Description
        Generate a summary of categorical columns in CSV, XLS, or XLSX files located in the given path.

    Parameters:
        path (str): The path to the directory containing CSV, XLS, or XLSX files.

    Returns:
        pandas.DataFrame: A DataFrame with columns 'file_name', 'categorical_columns', 'nunique' and 'prop_null%'.
                          Each row represents a file in the path and provides information about the
                          number of unique values in each categorical column found in that file.
    
    Example:
        >>> path = '/path/to/files/'
        >>> summary_df = categorical_summary(path)
        >>> print(summary_df)

            file_name        categorical_column  nunique  prop_null%
        0  data_file.csv        Category           10      0.020000
        1  data_file.csv        Gender             2       0.000000
        2  data_file.xlsx       Location           20      0.002500
        3  data_sheet.xls       Department         8       0.000000
        4  data_sheet.xls       City               15      0.010000
    """

    if os.path.isdir(path):
        for (dirpath, dirnames, filenames) in os.walk(path):
            break
    else:
        filenames = [os.path.basename(path).split('/')[-1]]
    
    new_df = {'file_name': [],
              'categorical_columns': [],
              'nunique': [],
              'prop_null%': []
             }
    
    for file in tqdm.tqdm(filenames):
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
            new_df['prop_null%'].append(("{:.2f}".format(((1 - (df[col].count() / (df.shape[0])))) * 100)))


    return pd.DataFrame(new_df)

def numerical_summary(path):
    """
    Description
        Generate a summary of numerical columns in CSV, XLS, or XLSX files located in the given path.

    Parameters:
        path (str): The path to the directory containing CSV, XLS, or XLSX files.

    Returns:
        pandas.DataFrame: A DataFrame with columns 'file_name', 'num_column', 'mean', 'std', 'min', '25%',
                          '50%', '75%' and 'max'.
                          Each row represents a file in the path and provides information about the
                          minimum and maximum values for each numerical column found in that file.
    
    Example:
        >>> path = '/path/to/files/'
        >>> summary_df = numerical_summary(path)
        >>> print(summary_df)

            file_name       num_column   mean    std   min   25%   50%   75%   max
        0  data_file.csv      Column1    10.50   5.00    5  7.25  10.5  13.75   16
        1  data_file.csv      Column2    25.00   7.00   15  20.0  25.0  30.00   35
        2  data_file.xlsx     Column1    18.75   2.50   16  17.5  18.5  19.75   22
        3  data_sheet.xls     Column3    42.00  10.00   30  35.0  42.0  49.00   55
    """

    if os.path.isdir(path):
        for (dirpath, dirnames, filenames) in os.walk(path):
            break
    else:
        filenames = [os.path.basename(path).split('/')[-1]]
    
    new_df = {'file_name': [],
              'num_column': [],
              'mean': [],
              'std': [],
              'min': [],
              '25%': [],
              '50%': [],
              '75%': [],
              'max': [],
             }
    
    for file in tqdm.tqdm(filenames):
        try:
            df = read_data(path+'/'+file)
            describe = df.describe()
        except Exception as e:
            print(e, file)
            continue
        
        columns = []
        for col in df.columns:
            filter_values = df[col].dropna()
            if is_numeric_dtype(filter_values) and len(filter_values)>0:
                columns.append(col)
        
        if len(columns) == 0:
            print('No numerical columns found in the DataFrame', file)
            continue
        
        for col in columns:
            new_df['file_name'].append(file)
            new_df['num_column'].append(col)
            new_df['mean'].append(describe[col]['mean'])
            new_df['std'].append(describe[col]['std'])
            new_df['min'].append(describe[col]['min'])
            new_df['25%'].append(describe[col]['25%'])
            new_df['50%'].append(describe[col]['50%'])
            new_df['75%'].append(describe[col]['75%'])
            new_df['max'].append(describe[col]['max'])

    return pd.DataFrame(new_df)

