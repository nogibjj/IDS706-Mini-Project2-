"""
Start mainfunction
"""

import pandas as pd

def readhead():
    """
    Main Function to read columns of given dataframe
    """
    data = pd.read_csv("camera.csv")
    return data.head()