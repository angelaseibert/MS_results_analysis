# results functions 

import os
import pandas as pd
import statsmodels.api as sma
boxplot_palette = ['#ff7f00','#377eb8','#984ea3']

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

def load_and_filter(results_path, column_name, column_name_type):
    """
    Perform an ordinary least squares regression analysis on data
    
    Parameters
    ----------------
    reg_data: 
        the data to be used with the regression
        type: variable containing a file path read as a csv
    ind_var_name:
        name of the independent variable column 
        type: column of the dataframe as dataframe.column
    dep_var_name:
        name of the dependent variable column
        type: column of the dataframe as dataframe.column
    Returns
    ----------------
    summary of the regression results
    """
    df_unfiltered = pd.read_csv(results_path)
    df_filtered = df_unfiltered[df_unfiltered[column_name] == column_name_type]
    return df_filtered

def regression_analysis(reg_data, ind_var_name, dep_var_name):
    """
    Perform an ordinary least squares regression analysis on data
    
    Parameters
    ----------------
    reg_data: 
        the data to be used with the regression
        type: variable containing a file path read as a csv
    ind_var_name:
        name of the independent variable column 
        type: column of the dataframe as dataframe.column
    dep_var_name:
        name of the dependent variable column
        type: column of the dataframe as dataframe.column
    Returns
    ----------------
    summary of the regression results
    """
    ind_variable = ind_var_name
    dep_variable = dep_var_name
    constant = sma.add_constant(ind_variable)
    _1 = sma.OLS(dep_variable, constant)
    _2 = _1.fit()
    
    return print(_2.summary())
    
def box_plots()


