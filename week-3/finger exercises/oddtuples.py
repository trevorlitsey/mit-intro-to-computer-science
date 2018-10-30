def odd_tuples(aTup=()):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    bTup = ()
    for num in range(0, len(aTup), 2):
        bTup = bTup + (aTup[num],)
    return bTup
