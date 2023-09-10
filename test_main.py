"""
Start Test
"""

from main import readhead
from main import meanfunction
from main import medianfunction
from main import summary

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

if __name__ == "__main__":
    test_readfeatures()
    