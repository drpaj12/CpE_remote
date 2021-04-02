import sys
import os
import subprocess
import random
import operator

def concat_bit_sequence_of_size(size, sequence):
    """ Concat random bits of size to sequence
    """
    print("Start:size "+sequence+":"+str(size))
    for i in range(1, random.randrange(size)+2):
        sequence += "," + str(random.randrange(2))
    #print("End "+sequence)

    return sequence

def create_sequence():
    """ Question 1 - 
    """
    
    # first 4 bits
    rand_valA = random.randrange(2)
    rand_valB = random.randrange(2)
    rand_valC = random.randrange(2)
    rand_valD = random.randrange(2)
    sequence1 = str(rand_valA)+","+str(rand_valB)+","+str(rand_valC)+","+str(rand_valD);

    rand_num = random.randrange(2)
    if rand_num == 0:
        # A!B
        rand_valB = (rand_valB + 1) % 2
        sequence2 = str(rand_valA)+","+str(rand_valB)
        sequence2 = concat_bit_sequence_of_size(random.randrange(2)+1, sequence2)
    else:
        # AB!C
        rand_valC = (rand_valC + 1) % 2
        sequence2 = str(rand_valA)+","+str(rand_valB)+","+str(rand_valC)
        sequence2 = concat_bit_sequence_of_size(1, sequence2)

    return sequence1, sequence2
