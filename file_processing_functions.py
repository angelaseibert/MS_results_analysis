import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import warnings

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

def normal_data(data_to_norm, filter_by_temp, what_temp, filter_by_co2, what_co2, cols_norm_name, file_outpath, csv_name):
    """
    Normalize a dataframe using the MinMaxScaler function from sklearn. Each group of LAI values is normalized by plot or the unique treatment conditions.
    
    Parameters
    ----------------
    data_to_norm:
        the dataframe full of the data to normalize
    type:
        pandas dataframe
    filter_by_temp:
        the name of the temperature column, you could also go by a different column name if you wanted to normalize by something else
    type:
        string, ex: 'temp'
    what_temp: 
        the category of the data that it should be filtered by
    type: 
        string or number, ex: '0' or 0, just depends on the original df
    filter_by_co2:
        the name of the co2 treatment column
    type: 
        string
    what_co2:
        the category of the data in the co2 treatment column 
    type:
        string, ex: 'elevated' or 'ambient'
    cols_norm_name: 
        the column name that contains the data you want to normalize
    type:
        string, ex 'LAI'
    file_outpath:
        filepath to output the csv file
    type:
        string containing a file path
    csv_name:
        name of the csv file you want to call the results 
    type:
        string with the extension .csv
    Returns
    ----------------
    csv file containing LAI data normalized by plot or treatment group 
    """
    filtered_1 = filter_df(data_to_norm, filter_by_temp, what_temp, exclude = False)
    temp_df = filter_df(filtered_1, filter_by_co2, what_co2, exclude = False)
    cols_to_norm = [cols_norm_name]
    temp_df[cols_to_norm] = MinMaxScaler().fit_transform(temp_df[cols_to_norm])
    warnings.filterwarnings('ignore')
    return temp_df.to_csv(file_outpath + csv_name, index = False)

def normal_data_CO2(data_to_norm, filter_by_co2, what_co2, cols_norm_name, file_outpath, csv_name):
    """
    Normalize a dataframe using the MinMaxScaler function from sklearn. Each group of LAI values is normalized by plot or the unique treatment conditions.
    
    Parameters
    ----------------
    data_to_norm:
        the dataframe full of the data to normalize
    type:
        pandas dataframe
    filter_by_co2:
        the name of the co2 treatment column
    type: 
        string
    what_co2:
        the category of the data in the co2 treatment column 
    type:
        string, ex: 'elevated' or 'ambient'
    cols_norm_name: 
        the column name that contains the data you want to normalize
    type:
        string, ex 'LAI'
    file_outpath:
        filepath to output the csv file
    type:
        string containing a file path
    csv_name:
        name of the csv file you want to call the results 
    type:
        string with the extension .csv
    Returns
    ----------------
    csv file containing LAI data normalized by plot or treatment group 
    """
    temp_df = filter_df(data_to_norm, filter_by_co2, what_co2, exclude = False)
    cols_to_norm = [cols_norm_name]
    temp_df[cols_to_norm] = MinMaxScaler().fit_transform(temp_df[cols_to_norm])
    warnings.filterwarnings('ignore')
    return temp_df.to_csv(file_outpath + csv_name, index = False)