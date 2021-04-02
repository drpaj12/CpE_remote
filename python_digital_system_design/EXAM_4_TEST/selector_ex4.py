import sys
import os
import subprocess
import random
import operator

def pick_mem_params():
    """ Concat random bits of size to sequence
    """
    
    # first 4 bits
    word_size = random.randrange(7)
    word_size = word_size * 4 + 12
    
    number_of_words = random.randrange(3)
    if number_of_words == 0:
        number_of_words = 32
    elif number_of_words == 1:
        number_of_words = 64
    elif number_of_words == 2:
        number_of_words = 128
    else:
        print("Problem")

    return word_size, number_of_words
