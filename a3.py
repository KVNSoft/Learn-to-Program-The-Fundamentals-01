def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    """

    return word in wordlist


def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    """

    return "".join(board[row_index])


def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    """
    return "".join(x[column_index] for x in board)


def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    """

    for column_index01 in range(len(board[0])):
        if word in make_str_from_column(board, column_index01):
            return True

    return False


def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    """

    return board_contains_word_in_row(board, word) or board_contains_word_in_column(board, word)


def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16

    >>> word_score('DRUDG')
    5
    """
    
    len1 =  len(word)

    return (3<=len1<=6)*len1 + (7<=len1<=9)*2*len1 + (len1>=10)*3*len1


def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """
    
    player_info[1] += word_score(word)
    #print(player_info)
    return


def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    
    num_words = 0
    for var01 in words:
        if board_contains_word(board, var01):
            num_words += 1
    
    return num_words


def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """

    """
    my_list01 = list()

    for var01 in words_file:
        for var02 in var01:
            my_list01.append(var02.rstrip('\n'))

    return my_list01  """

    my_list01 = list()
   
    for var01 in words_file:
        my_char01 =""

        for var02 in var01:
            my_char01 += (var02 != "\n") * var02 

        my_list01.append(my_char01)

    return my_list01



def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """

    """
    my_list01 = list()

    for var01 in board_file:
            my_list02 = [x for x in var01.rstrip('\n')]

    if len(my_list02) > 0:
            my_list01.append(my_list02)


    return my_list01

    """

    my_list01 = list()
         
    for var01 in board_file:
        my_list02 = list()

        for var02 in var01:
            if var02 != '\n':
                my_list02.append(var02)

        if len(my_list02) > 0:
            my_list01.append(my_list02)

    return my_list01

