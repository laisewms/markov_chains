"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open('green-eggs.txt') # open
    text= file.read() # read
    file.close() # close

    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = text_string.split()
    
    words.append(None)
    
    for i in range(len(words)-2): # range loop, -2 to prevent index error
        key = (words[i], words[i+1]) # modify the loop so that you're putting the words at i and i+1 in a tuple, and these use that tuple as a key in your dictionary
        value = words[i + 2]

        if key not in chains: 
            chains[key] = []

        chains[key].append(value)
    # your code goes here

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    
    key = choice(list(chains.keys())) # randomly selecting one of our keys
    words = [key[0], key[1]] # setting variable words to list of key at index 0 and key at index 1
    word = choice(chains[key]) # setting word to a random selection of values that 

    while word is not None:
        key = (key[1], word) # new key starts with second word, pull in variable word
        words.append(word) # append new randomly selected word to that list
        word = choice(chains[key]) # resetting variable word to a new randomly selected item

    return ' '.join(words)



 


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
