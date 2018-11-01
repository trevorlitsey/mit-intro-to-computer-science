from hangman import isWordGuessed, getGuessedWord, getAvailableLetters


def test_is_word_guessed():
    assert(isWordGuessed('tomato', ['t', 'o', 'x']) == False)
    assert(isWordGuessed('tomato', ['t', 'o', 'm', 'a']) == True)


def test_get_guessed_word():
    assert(getGuessedWord('tomato', ['t', 'o', 'x']) == 't o _ _ t o')
    assert(getGuessedWord('tomato', ['t', 'x']) == 't _ _ _ t _')


def test_get_available_letters():
    assert(getAvailableLetters(['a', 'b', 'z'])
           == 'cdefghijklmnopqrstuvwxy')
