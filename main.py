"""
Start mainfunction
"""

import pandas as pd
import matplotlib.pyplot as plt

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
    print(data['Price'].describe())

def seeplot():
    """
    Displays plot with Pandas plot function 
    """
    plt.scatter(data['Weight (inc. batteries)'], data['Storage included'], label="data")
    plt.legend(loc="best")
    plt.title("weight vs storage graph")
    plt.xlabel("weight")
    plt.ylabel("storage")
    plt.show()
    