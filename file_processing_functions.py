import os
import pandas as pd

def stack_its(file_path, final_csv_name):
    """
    Create a dataframe of all model iterations for LAI data only
    
    Parameters
    ----------------
    file_path: 
        the file path where you stored the model iteration results
        type: string
    final_csv_name:
        name of what you want to name the final file
        type: string
    
    Returns
    ----------------
    csv of all LAI data from model iterations
    """ 
    file_list = os.listdir(file_path)
    
    df_list = []

    for file in file_list:
        df_LAI_fp = pd.read_csv(file_path + file)
        df_list.append(df_LAI_fp)
    final_df = pd.concat(df_list, ignore_index = True)
    return final_df.to_csv(file_path + final_csv_name, index = False)

def load_and_filter(results_path, column_name, column_name_type, exclude = False):
    """
    load and filter a csv (to filter a dataframe, see filter_df function below)
    
    Parameters
    ----------------
    results_path: 
        where the csv is located
        type: string location
    column_name: 
        name of the column which the data will be filtered by
        type: column label as a string, ex: species or year
    column_name_type:
        category of the column which the data will be filtered by
        type: column label category, ex: larch or 2015 
    exclude:
        determines whether to exclude the designated data type or filter by it
        type: boolean phrase, True or False
    Returns
    ----------------
    filtered dataframe from a csv file
    """
    df_unfiltered = pd.read_csv(results_path)
    if exclude:
        df_filtered = df_unfiltered[df_unfiltered[column_name] != column_name_type]
    else:
        df_filtered = df_unfiltered[df_unfiltered[column_name] == column_name_type]
    return df_filtered

def filter_df(dataframe, column_name, column_name_type, exclude = False):
    """
    filter a dataframe
    
    Parameters
    ----------------
    dataframe: 
        the dataframe
        type: pandas dataframe
    column_name: 
        name of the column which the data will be filtered by
        type: column label as a string, ex: species or year
    column_name_type:
        category of the column which the data will be filtered by
        type: column label category, ex: larch or 2015 
    exclude:
        determines whether to exclude the designated data type or filter by it
        type: boolean phrase, True or False, default is False
    Returns
    ----------------
    filtered dataframe from a pandas dataframe
    """
    if exclude:
        df_filtered = dataframe[dataframe[column_name] != column_name_type]
    else:
        df_filtered = dataframe[dataframe[column_name] == column_name_type]
    return df_filtered

def readfiles(filepath, unique_id):
    """
    read in csv files with a unique part of their name
    
    Parameters
    ----------------
    filepath: 
        the filepath to the files of interest
        type: string
    unique_id: 
        part of the file names that is unique, useful if you need subset of csv files from folder
        type: string
    Returns
    ----------------
    list of dataframes
    """
    # unique_id will be either eco2 or aco2
    # filepath = filepath containing the files of interest
    
    file_list = os.listdir(filepath)
    print(file_list)
    dataframes_list_var = []
    
    for file in file_list:
        if unique_id in file:
            final_file_path = os.path.join(filepath, file)
            dataframe = pd.read_csv(final_file_path)
            dataframes_list_var.append(dataframe)
    return dataframes_list_var