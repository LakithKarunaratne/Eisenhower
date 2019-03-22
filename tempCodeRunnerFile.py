
import time

import hashlib


def gencode(taskName):
    """
    this generates a unique code for a given value
    """
    now = getTime()
    string = taskName + now
    result = hashlib.md5(string.encode()) 
    result = result.hexdigest()
    return result

print(gencode("hihihi"))
