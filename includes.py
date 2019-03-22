"""
This file contains all functions that needs to be inculded in the main file
Assume as a header file for python, for easy code readability
"""
import time

import hashlib


def gencode(taskName):
    """
    this generates a unique code for a given value
    taskName : Name of the 
    """
    now = getTime() # get the current time stamp
    string = taskName + now # concatenate with taskName
    result = hashlib.md5(string.encode()) # encode to md5
    result = result.hexdigest() # get hash digest
    return result # return value



def getTime():
    """ 
    %d/%m/%Y %I:%M%p # current time standard format

    Sample output:
    > 22/03/2019 12:51PM
    """
    return time.strftime("%d/%m/%Y %I:%M%p")

if __name__ == "__main__":
    print(getTime())
    print(gencode("hihihi"))
    pass