from random import choice
import random
import sys 


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

    length = len(text_string_list) - 2  #setting the range 
    for i in range(length): 
        key_1 = text_string_list[i] #setting the first element of our tuple
        key_2 = text_string_list[i+1] #setting the second element of our tuple 
        value = text_string_list[i+2] #setting the value of our tuple 
        key_tuple = key_1, key_2 

        if key_tuple not in chains:
            chains[key_tuple] = [value] #adding key and value to the dictionary 
        else:
            chains[key_tuple].append(value) #appending the value to our list of values for each key. 
    print chains
    print "\n"
    return chains

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # TODO: the last word in our string does not print i.e. "sam I" instead of "sam i am"
    # welp
    
    text = ""
    text_list = []
    rand_key = random.choice(chains.keys()) #generating a random key from dictionary 
    while rand_key in chains: 
        first, second = rand_key #unpack random key from above
        next_word = random.choice(chains[rand_key]) #binding next word to random word in list associated with random index
        rand_key = (second, next_word) #binding rand key to a tuple - second word from random index, next word from list
        text_list.append(next_word)

    text = ' '.join(text_list)
    print text
        
input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text


