"""
Start Test
"""

from main import readhead
from main import meanfunction
from main import medianfunction
from main import summary
from main import makeplot

def test_readfeatures():
    """
    Test defined readhead function
    """
    output = readhead()
    print(output)

def test_mean():
    """
    Test defined meanfunction
    """
    output = meanfunction()
    print(output)

def test_median():
    """
    Test defined median function
    """
    output = medianfunction()
    print(output)

def test_summary():
    """
    Test defined summary (or describe) function
    """
    output = summary()
    print(output)

def test_plot():
    """
    Test defined makeplot function regarding data visualization
    """
    output = makeplot()
    print(output)

if __name__ == "__main__":
    test_readfeatures()
    test_mean()
    test_median()
    test_summary()
    test_plot()
