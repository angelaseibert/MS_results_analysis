# Seibert MS 2021 - 2023 results functions 

import os
import pandas as pd
import statsmodels.api as sma
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.preprocessing import MinMaxScaler


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
    
def box_plots(box_data, box_palette):
    """
    Plot boxplots of LAI data
    
    Parameters
    ----------------
    box_data:
        the dataframe to generate a boxplot with
    box_palette:
        the palette you would like to use to color the boxes
        type: series of color code strings
    Returns
    ----------------
    box plot of the LAI over time, grouped by carbon dioxide
    """
    plt.figure(dpi= 1200)
    LAI_plot = sns.boxplot(data=box_data, x="year", y= 'LAI', hue = 'carbon dioxide', palette = box_palette)
    plt.xlabel("Years", fontsize = 14)
    plt.ylabel("LAI (m${}^2$/m${}^2$)", fontsize = 14)
    sns.move_legend(LAI_plot, "best")
    return LAI_plot
    
def kde_plots(kde_data):
    """
    Plot kernel density functions on top of each other
    
    Parameters
    ----------------
    kde_data:
        the dataframe to generate the distributions
    Returns
    ----------------
    kernel density functions showing the distributions of LAI 
    """
    plt.figure(dpi= 1200)
    df_LAIall_ec = kde_data[kde_data['carbon dioxide'] == 'elevated']
    df_LAIall_ac = kde_data[kde_data['carbon dioxide'] == 'ambient']
    df_LAIall_control = kde_data[kde_data['carbon dioxide'] == 'control']
    
    kde_ec_plot = sns.kdeplot(data=df_LAIall_ec['LAI'], color = '#ff7f00', fill = True, label = 'Elevated CO${}_2$ & Elevated Temp')
    kde_ac_plot = sns.kdeplot(data=df_LAIall_ac['LAI'], color = '#377eb8', fill = True, label = 'Ambient CO${}_2$ & Elevated Temp')
    kde_c_plot = sns.kdeplot(data=df_LAIall_control['LAI'], color = '#984ea3', fill = True, label = 'Control')

    plt.xlabel("LAI (m${}^2$/m${}^2$)", fontsize = 14)
    plt.ylabel("Frequency", fontsize = 14)
    plt.legend()
    
    print('Elevated CO2:', (df_LAIall_ec['LAI']).describe()) 
    print('Ambient CO2:', (df_LAIall_ac['LAI']).describe()) 
    print('Control:', (df_LAIall_control['LAI']).describe())
    
    return plt

def LAI_hist_plot(hist_data):
    """
    Plot histogram of all LAI values
    
    Parameters
    ----------------
    hist_data:
        the dataframe to generate the distributions
    Returns
    ----------------
    histogram showing the distribution of LAI 
    """
    plt.figure(dpi = 1200)
    LAI_histogram = sns.histplot(data=hist_data['LAI'], binwidth=0.2, kde=True, stat = 'probability', color = '#e41a1c', label = 'Plot LAI')
    plt.xlabel("LAI (m${}^2$/m${}^2$)", fontsize = 14)
    plt.ylabel("Frequency", fontsize = 14)
    plt.legend()
    
    print((hist_data['LAI']).describe());
    
    return LAI_histogram

def LAI_lineplot(line_data, line_palette):
    """
    Plot line plot of LAI data
    
    Parameters
    ----------------
    line_data:
        the dataframe to generate the line plots
    type:
        pandas dataframe
    line_palette:
        the palette you would like to use to color the lines
    type:
        string of color codes
    Returns
    ----------------
    LAI line plot
    """
    plt.figure(dpi= 1200, figsize = (10,6))
    LAI_species_lineplot = sns.lineplot(data=line_data, x="year", y= 'LAI', hue = 'species', 
                                        style = 'carbon dioxide', palette = line_palette, marker = 'o', err_style = 'bars', markersize= 8)
    plt.xlabel("Years", fontsize = 14)
    plt.ylabel("LAI (m${}^2$/m${}^2$)", fontsize = 14)
    sns.move_legend(LAI_species_lineplot, "best")
    return LAI_species_lineplot

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

def LAInormal_timeseries (normal_df, legend_title, line_palette):
    plt.figure(dpi= 1200, figsize = (10,6))
    LAI_normtimeseries = sns.lineplot(data=normal_df, x="year", y= 'LAI', 
                                      hue_order = ['0','2.25','4.5','6.75','9','control'], hue = 'temp', palette = line_palette)
    plt.ylabel("Normalized Leaf Area Index (m${}^2$/m${}^2$)", fontsize = 14);
    plt.xlabel("Year", fontsize = 14);
    plt.legend(title= legend_title, loc='best')
    plt.plot()
    plt.ylim(0, 1)
    return LAI_normtimeseries



