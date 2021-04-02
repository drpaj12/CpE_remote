import sys
import os
import random

def random_3_ints(size):
    """Create three random numbers in range that aren't equal """
    n1 = random.randint(0, size)
    n2 = random.randint(0, size)
    n3 = random.randint(0, size)
    while n1 == n2:
        n2 = random.randint(0, size)
    while n2 == n3 or n1 == n3:
        n3 = random.randint(0, size)

    if n2 < n1 and n2 < n3:
        temp = n1
        n1 = n2
        n2 = temp
    elif n3 < n1:
        temp = n1
        n1 = n3
        n3 = temp

    if n3 < n2:
        temp = n2
        n2 = n3
        n3 = temp

    return n1, n2, n3

def random_3_term():
    """Create two random 5 tupples with 1, 0, and 3x's """
    n1, n2, n3 = random_3_ints(4)

    term_0 = [0,0,0,0,0]

    for i in range(5):
        if i == n1 or i == n2 or i == n3:
            term_0[i] = 2
        else:
            term_0[i] = random.randint(0, 1)

    return term_0

def random_2_term():
    """Create two random 5 tupples with 1, 0, and 2x's """
    n1, n2, n3 = random_3_ints(4)

    term_0 = [0,0,0,0,0]

    for i in range(5):
        if i == n1 or i == n2:
            term_0[i] = 2
        else:
            term_0[i] = random.randint(0, 1)

    return term_0

def random_1_term():
    """Create two random 5 tupples with 1, 0, and 1x's """
    n1, n2, n3 = random_3_ints(4)

    term_0 = [0,0,0,0,0]

    for i in range(5):
        if i == n1:
            term_0[i] = 2
        else:
            term_0[i] = random.randint(0, 1)

    return term_0

def write_out_term(term, file_handle):
    for i in range(5):
        if term[i] == 0:
            file_handle.write ('0')
        elif term[i] == 1:
            file_handle.write ('1')
        else:
            file_handle.write ('X')
    file_handle.write ('\n')

def create_kmap_question(directory_out, student_name):
    """ Create the equation, make a answer file, and return the string of minterms in form-> (m0, m1, ...) """
    variable_list = ['a','b','c','d','e','!a','!b','!c','!d','!e']

    final_terms = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    vals_3_0 = [0,0,0,0,0,0,0,0]
    vals_3_1 = [0,0,0,0,0,0,0,0]
    vals_2_0 = [0,0,0,0]
    vals_2_1 = [0,0,0,0]
    vals_1_0 = [0,0]
    vals_1_1 = [0,0]

    # create the terms
    term_3_0 = random_3_term()
    term_3_1 = random_3_term()
    term_2_0 = random_2_term()
    term_2_1 = random_2_term()
    term_1_0 = random_1_term()
    term_1_1 = random_1_term()

    answer_file = open(directory_out+'/'+student_name+'_answers_exam1_q2.txt', 'w')
    answer_file.write("Question 2 = Original Terms\n")
    write_out_term(term_3_0, answer_file)
    write_out_term(term_3_1, answer_file)
    write_out_term(term_2_0, answer_file)
    write_out_term(term_2_1, answer_file)
    write_out_term(term_1_0, answer_file)
    write_out_term(term_1_1, answer_file)
    # close answer file
    answer_file.close()

    x_found = 1
    for i in range(5):
        if term_3_0[i] == 1: # binary 1
            for j in range(8):
                vals_3_0[j] = vals_3_0[j] + 2**(4-i)
        elif term_3_0[i] == 2: # x
            if x_found == 1:
                """ Do the first 4 """
                for j in range(4):
                    vals_3_0[j] = vals_3_0[j] + 2**(4-i)
            if x_found == 2:
                """ Do 2 at a time """
                for j in range(2):
                    vals_3_0[j] = vals_3_0[j] + 2**(4-i)
                    vals_3_0[j+4] = vals_3_0[j+4] + 2**(4-i)
            if x_found == 3:
                """ Do alternating """
                for j in range(4):
                    vals_3_0[j*2] = vals_3_0[j*2] + 2**(4-i)
            x_found = x_found + 1
    for i in range(8):
        final_terms[vals_3_0[i]] = 1
    #print(*vals_3_0)

    x_found = 1
    for i in range(5):
        if term_3_1[i] == 1: # binary 1
            for j in range(8):
                vals_3_1[j] = vals_3_1[j] + 2**(4-i)
        elif term_3_1[i] == 2: # x
            if x_found == 1:
                for j in range(4):
                    vals_3_1[j] = vals_3_1[j] + 2**(4-i)
            if x_found == 2:
                for j in range(2):
                    vals_3_1[j] = vals_3_1[j] + 2**(4-i)
                    vals_3_1[j+4] = vals_3_1[j+4] + 2**(4-i)
            if x_found == 3:
                for j in range(4):
                    vals_3_1[j*2] = vals_3_1[j*2] + 2**(4-i)
            x_found = x_found + 1
    for i in range(8):
        final_terms[vals_3_1[i]] = 1
    #print(*vals_3_1)
                  
    x_found = 1
    for i in range(5):
        if term_2_0[i] == 1: # binary 1
            for j in range(4):
                vals_2_0[j] = vals_2_0[j] + 2**(4-i)
        elif term_2_0[i] == 2: # x
            if x_found == 1:
                for j in range(2):
                    vals_2_0[j] = vals_2_0[j] + 2**(4-i)
            if x_found == 2:
                vals_2_0[0] = vals_2_0[0] + 2**(4-i)
                vals_2_0[2] = vals_2_0[2] + 2**(4-i)
            x_found = x_found + 1
    for i in range(4):
        final_terms[vals_2_0[i]] = 1
    #print(*vals_2_0)
                  
    x_found = 1
    for i in range(5):
        if term_2_1[i] == 1: # binary 1
            for j in range(4):
                vals_2_1[j] = vals_2_1[j] + 2**(4-i)
        elif term_2_1[i] == 2: # x
            if x_found == 1:
                for j in range(2):
                    vals_2_1[j] = vals_2_1[j] + 2**(4-i)
            if x_found == 2:
                vals_2_1[0] = vals_2_1[0] + 2**(4-i)
                vals_2_1[2] = vals_2_1[2] + 2**(4-i)
            x_found = x_found + 1
    for i in range(4):
        final_terms[vals_2_1[i]] = 1
    #print(*vals_2_1)

    for i in range(5):
        if term_1_0[i] == 1: # binary 1
            for j in range(2):
                vals_1_0[j] = vals_1_0[j] + 2**(4-i)
        elif term_1_0[i] == 2: # x
            vals_1_0[0] = vals_1_0[0] + 2**(4-i)
    for i in range(2):
        final_terms[vals_1_0[i]] = 1
    #print(*vals_1_0)
    for i in range(4):
        if term_1_1[i] == 1: # binary 1
            for j in range(2):
                vals_1_1[j] = vals_1_1[j] + 2**(4-i)
        elif term_1_1[i] == 2: # x
            vals_1_1[0] = vals_1_1[0] + 2**(4-i)
    for i in range(2):
        final_terms[vals_1_1[i]] = 1
    #print(*vals_1_1)

    one_coma = 0
    q2_sum = 'f(a,b,c,d,e)=Σ('
    for i in range(32):
        if final_terms[i] == 1:
            if one_coma == 0:
                q2_sum = q2_sum + 'm'+str(i)
                one_coma = 1
            else:
                q2_sum = q2_sum + ', m'+str(i)
    q2_sum = q2_sum + ')'

    return q2_sum
