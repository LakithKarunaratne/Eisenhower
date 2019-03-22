"""
This file contains all functions that needs to be inculded in the main file
Assume as a header file for python, for easy code readability
"""
import time


def gencode():
    return


def getTime():
    """ 
    %d/%m/%Y %I:%M%p # current time standard format

    Sample output:
    > 22/03/2019 12:51PM
    """
    return time.strftime("%d/%m/%Y %I:%M%p")


print(getTime())
