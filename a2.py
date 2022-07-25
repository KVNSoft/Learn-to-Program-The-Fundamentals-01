def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1


def is_valid_sequence(dna01):
    """ (str) -> bool

    Return True if and only if the DNA sequence  dna01 is valid 
    (that is, it contains no characters other than ["A", "C", "G", "T"])

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGGCK')
    False

    """
    DNA_LIST01 = ["A", "C", "G", "T"]

    for var01 in dna01:
        if var01 not in DNA_LIST01:
            return False
    
    return True


def insert_sequence(dna1, dna2, index01):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence dna2 into the first DNA sequence dna1 at the given index index01. 
    (You can assume that the index is valid.)

    >>> insert_sequence('CCGG', "AT", 2)
    "CCATGG"
    >>> insert_sequence('ATATCCGG', "CCCGGG", 5)
    "ATATCCCCGGGCGG"
    >>> insert_sequence('CCGG', "AT", 0)
    "ATCCGG"

    """

    return dna1[:index01] + dna2 + dna1[index01:]


def get_complement(dna01):
    """ (str) -> str

    The first parameter is a nucleotide dna01. Return the nucleotide's complement

    >>> get_complement('A')
    "T"
    >>> get_complement("T")
    "A"
    
    """

    MY_DICT01 = {"A" : "T", "C" : "G", "G" : "C", "T" : "A"}

    return MY_DICT01[dna01]


def get_complementary_sequence(dna01):
    """ (str) -> str

    The parameter is a DNA sequence dna01. Return the DNA sequence that is complementary to the given DNA sequence.
    >>> get_complementary_sequence('ATATCCGG')
    "TATAGGCC"
    >>> get_complementary_sequence("TATAGGCC")
    "ATATCCGG"
    
    """

    MY_DICT01 = {"A" : "T", "C" : "G", "G" : "C", "T" : "A"}
    my_compl01 = ""

    for var01 in dna01:
        my_compl01 +=  MY_DICT01[var01]

    return my_compl01

