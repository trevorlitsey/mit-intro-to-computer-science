def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    longest = None
    if len(s1) >= len(s2):
        longest = len(s1)
    else:
        longest = len(s2)

    newStr = []
    for i in range(longest):
        if i < len(s1):
            newStr.append(s1[i])
        if i < len(s2):
            newStr.append(s2[i])

    return ''.join(newStr)
