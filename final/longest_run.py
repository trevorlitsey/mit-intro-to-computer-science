def longestRun(L):
    """
    L is a non-empty list

    Returns the length of the longest run of 
    monotonically increasing numbers occurring in L
    """
    longest = 1
    for i in range(len(L) - 1):
        j = i + 1
        while j <= len(L) - 1 and L[j] >= L[j-1]:
            j += 1
        if j - i > longest:
            longest = j - i

    return longest
