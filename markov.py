from random import choice
import random


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path, 'r') as f:
        all_words = f.read()
    
    return all_words
    #return all_words


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    text_string_list = text_string.split()

    length = len(text_string_list) - 2
    for i in range(length):
        key_1 = text_string_list[i]
        key_2 = text_string_list[i+1]
        value = text_string_list[i+2]
        key_tuple = key_1, key_2 

        if key_tuple not in chains:
            chains[key_tuple] = [value]
        else:
            chains[key_tuple].append(value)
 
    return chains

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # TODO: check to see if the key exists before adding it to the text file
    
    text = ""

    rand_key = random.choice(chains.keys())
    list_of_keys = chains.keys()
    count = 0
    length = len(chains.keys()) - 2 # we have 22 keys
    while count < range(length):
        first, second = rand_key
        next_word = random.choice(chains[rand_key])
        text = text + " " + first + " " + second + " " + next_word 
        rand_key = (second, next_word)

        count += 1

        if count >= length: 
            break

    print text
        
input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
