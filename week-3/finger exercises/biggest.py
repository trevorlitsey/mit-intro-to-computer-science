"""finger exercise"""


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    lengths = map(lambda x: len(x), aDict.values())
    print(lengths)
    largest = max(lengths)
    print(largest)
    for key in aDict.keys():
        if len(aDict[key]) == largest:
            return key
    return None
