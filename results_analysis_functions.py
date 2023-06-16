# results functions 

import os
import pandas as pd
import statsmodels.api as sma
import matplotlib.pyplot as plt
import seaborn as sns

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
    if exclude:
        df_filtered = df_unfiltered[df_unfiltered[column_name] != column_name_type]
    else:
        df_filtered = df_unfiltered[df_unfiltered[column_name] == column_name_type]
    return df_filtered

def filter_df(dataframe, column_name, column_name_type, exclude = False):
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
    plt.figure(dpi= 1200, figsize = (10,6))
    LAI_species_lineplot = sns.lineplot(data=line_data, x="year", y= 'LAI', hue = 'species', 
                                        style = 'carbon dioxide', palette = line_palette, marker = 'o', err_style = 'bars', markersize= 8)
    plt.xlabel("Years", fontsize = 14)
    plt.ylabel("LAI (m${}^2$/m${}^2$)", fontsize = 14)
    sns.move_legend(LAI_species_lineplot, "best")
    return LAI_species_lineplot

#FIGURES USING TEMPERATURES NEED TO BE FIXED
 

