def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N < 10:
        return N
    else:
        return sumDigits(N // 10) + N % 10
