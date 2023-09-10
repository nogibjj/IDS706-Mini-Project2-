"""
Start mainfunction
"""

import pandas as pd

data = pd.read_csv("camera.csv")

def readhead():
    """
    Main Function to read columns of given dataframe
    """
    return data.head()

def meanfunction():
    """
    Mean funtion to calculate mean of columns with numerical data
    """
    return data[['Max resolution', 'Low resolution']].mean()

def medianfunction():
    """
    Median function to calculate median of coumns with numerical data
    """
    return data[['Effective pixels', 'Storage included']].median()

def summary():
    """
    EDA with Pandas describe function to get mean, median, and standard deviation
    """
    return data['Price'].describe()

def makeplot():
    """
    Display time-series plot for EDA
    """
    return data.plot()
    