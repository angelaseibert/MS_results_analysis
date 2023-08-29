import matplotlib.pyplot as plt
import seaborn as sns

def LAInormal_timeseries (normal_df, legend_title, y_title, line_palette, what_style):
    """
    Generate timeseries figure grouping data by their temperature treatments
    
    Parameters
    ----------------
    normal_df: 
        the normalized dataframe
        type: pandas dataframe
    legend_title:
        title of the legend
        type: string
    y_title:
        title of the y axis
        type: string
    line_palette:
        colors you want the lines to be
        type: string listing color codes
    what_style:
        linestyle you want (ex. dashed or dotted)
        type: string, look up linestyle matplotlib
    Returns
    ----------------
    multiline figure showing change in LAI under each treatment condition over time
    """
    plt.figure(dpi= 1200, figsize = (10,6))
    LAI_normtimeseries = sns.lineplot(data=normal_df, x="year", y= 'LAI', 
                                      hue_order = ['0','2.25','4.5','6.75','9','control'], hue = 'temp', linestyle = what_style, 
                                      palette = line_palette)
    plt.ylabel(y_title, fontsize = 14);
    plt.xlabel("Year", fontsize = 14);
    legend = plt.legend(title = legend_title, loc='best')
    
    styleofline = what_style
    for lines in legend.get_lines():
        lines.set_linestyle(styleofline)
        
    plt.plot()
    plt.ylim(0, 1)
    return LAI_normtimeseries