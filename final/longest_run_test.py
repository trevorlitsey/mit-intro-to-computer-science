from longest_run import longestRun


def testLaceStrings():
    assert(longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 2]) == 5)
    assert(longestRun([1, 1, 1, 1, 1]) == 5)
    assert(longestRun([-10, -5, 0, 5, 10]) == 5)
    assert(longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 2]) == 5)
    assert(longestRun([1, 0, 0, 0, 4, 5, 1, 2, 9, 4, -1, 0]) == 5)
