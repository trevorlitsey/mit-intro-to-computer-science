def isUnique(aDict, value):
    hasBeenSeen = False
    valueIsUnqiue = True
    for key in aDict:
        if aDict[key] == value:
            if hasBeenSeen:
                valueIsUnqiue = False
                break
            else:
                hasBeenSeen = True
    return valueIsUnqiue


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    if type(aDict) is not dict:
        return []

    values = list(aDict.values())
    keys = []
    for value in values:
        if isUnique(aDict, value) == True:
            for key in aDict:
                if aDict[key] == value:
                    keys.append(key)
    keys.sort()
    return keys
