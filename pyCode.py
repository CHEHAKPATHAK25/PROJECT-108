#THIS IS THE PROJECT CODE
#import modules
import numpy as np
#Here, "np" is an ALIAS = alternate name[in Python]
import pandas as pd
import plotly.figure_factory as ff

#read the csv file using pandas module
dataFrame = pd.read_csv("csvData.csv")

#creating the distribution plot graph figure using ff(plotly.figure_factory)
distribution_plot_graph_figure = ff.create_distplot(["Avg Rating"].tolist(), ["Avergae Rating of mMobiles"])
distribution_plot_graph_figure.show()