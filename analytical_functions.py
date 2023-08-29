import statsmodels.api as sma

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