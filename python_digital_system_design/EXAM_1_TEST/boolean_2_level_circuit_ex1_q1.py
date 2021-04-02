import sys
import os
import subprocess
import random
import operator

OPERATIONS_3 = [
    ('&',  operator.and_),
    ('|',  operator.or_),
    ('^',  operator.xor),
]
OPERATIONS_2 = [
    ('&',  operator.and_),
    ('|',  operator.or_),
    ('^',  operator.xor),
]
OPERATIONS_1 = [
    ('~',  operator.not_),
]

def random_3_gate_terminal(binary_operations, str_in1, str_in2, str_in3):
    """Generate a 2 input gate"""
    op_sym, op_func = random.choice(binary_operations)
    gate_format = '{} {} {} {} {}'.format(str_in1, op_sym, str_in2, op_sym, str_in3)
    gate_tupple = (op_sym, op_func)
    return gate_format, gate_tupple

def random_2_gate_print(binary_operations, variable_list, num_variables):
    """Generate a 2 input gate"""
    op_sym, op_func = random.choice(binary_operations)
    n1 = random.randint(0, num_variables-1)
    n2 = random.randint(0, num_variables-1)
    while n1 == n2:
        n2 = random.randint(0, num_variables-1)
    gate_format = '({} {} {})'.format(variable_list[n1], op_sym, variable_list[n2])
    gate_tupple = (op_sym, op_func, n1, n2)
    return gate_format, gate_tupple

def random_3_gate_print(binary_operations, variable_list, num_variables):
    """Generate a 3 input gate"""
    op_sym, op_func = random.choice(binary_operations)
    n1 = random.randint(0, num_variables-1)
    n2 = random.randint(0, num_variables-1)
    n3 = random.randint(0, num_variables-1)
    while n1 == n2:
        n2 = random.randint(0, num_variables-1)
    while n2 == n3 or n1 == n3:
        n3 = random.randint(0, num_variables-1)
    gate_format = '({} {} {} {} {})'.format(variable_list[n1], op_sym, variable_list[n2], op_sym, variable_list[n3])
    gate_tupple = (op_sym, op_func, n1, n2, n3)
    return gate_format, gate_tupple

def random_4_gate_print(binary_operations, variable_list, num_variables):
    """Generate a 4 input gate"""
    op_sym, op_func = random.choice(binary_operations)
    n1 = random.randint(0, num_variables-1)
    n2 = random.randint(0, num_variables-1)
    n3 = random.randint(0, num_variables-1)
    n4 = random.randint(0, num_variables-1)
    while n1 == n2:
        n2 = random.randint(0, num_variables-1)
    while n2 == n3 or n1 == n3:
        n3 = random.randint(0, num_variables-1)
    while n3 == n4 or n2 == n4 or n1 == n4:
        n4 = random.randint(0, num_variables-1)
    gate_format = '({} {} {} {} {} {} {})'.format(variable_list[n1], op_sym, variable_list[n2], op_sym, variable_list[n3], op_sym, variable_list[n4])
    gate_tupple = (op_sym, op_func, n1, n2, n3, n4)
    return gate_format, gate_tupple

def get_val(var, in0, in1, in2, in3, in4):
    """ Gets the value of a variable as an int {0,1} for simulation """
    if var == 0:
        return in0
    elif var == 1:
        return in1
    elif var == 2:
        return in2
    elif var == 3:
        return in3
    elif var == 4:
        return in4
    elif var == 5:
        return not(in0)
    elif var == 6:
        return not(in1)
    elif var == 7:
        return not(in2)
    elif var == 8:
        return not(in3)
    elif var == 9:
        return not(in4)
    else:
        print("ERROR %s" % var)
        return 0

def eval_gate_first_stage(size, gate_tupple, in0, in1, in2, in3, in4):
    """Calculate the binary result"""
    operation = gate_tupple[1]
    for i in range(size-1):
        if i == 0:
            val1 = get_val(gate_tupple[2], in0, in1, in2, in3, in4)
            val2 = get_val(gate_tupple[i+3], in0, in1, in2, in3, in4)
            result = operation(val1, val2) 
        else:
            val2 = get_val(gate_tupple[i+3], in0, in1, in2, in3, in4)
            result = operation(result, val2) 

    return result

def eval_gate_second_stage(gate_tupple, in0, in1, in2):
    """Calculate the binary result"""
    operation = gate_tupple[1]
    result = operation(in0, in1) 
    result = operation(result, in2) 
    return result

def create_two_equations(directory_out, student_name):
    """ Create the two equations, make a answer file, and return the strings """
    variable_list = ['a','b','c','d','e','!a','!b','!c','!d','!e']
    
    # Question 1 - Build a 2 level circuit verilog equations
    rand_num = random.randrange(3)
    if rand_num == 0:
        gate1_out, gate1_val = random_2_gate_print(OPERATIONS_2, variable_list, 10)
        gate1_size = 2
    elif rand_num == 1:
        gate1_out, gate1_val = random_3_gate_print(OPERATIONS_2, variable_list, 10)
        gate1_size = 3
    else:
        gate1_out, gate1_val = random_4_gate_print(OPERATIONS_2, variable_list, 10)
        gate1_size = 4
    
    rand_num = random.randrange(3)
    if rand_num == 0:
        gate2_out, gate2_val = random_2_gate_print(OPERATIONS_2, variable_list, 10)
        gate2_size = 2
    elif rand_num == 1:
        gate2_out, gate2_val = random_3_gate_print(OPERATIONS_2, variable_list, 10)
        gate2_size = 3
    else:
        gate2_out, gate2_val = random_4_gate_print(OPERATIONS_2, variable_list, 10)
        gate2_size = 4
    
    rand_num = random.randrange(3)
    if rand_num == 0:
        gate3_out, gate3_val = random_2_gate_print(OPERATIONS_2, variable_list, 10)
        gate3_size = 2
    elif rand_num == 1:
        gate3_out, gate3_val = random_3_gate_print(OPERATIONS_2, variable_list, 10)
        gate3_size = 3
    else:
        gate3_out, gate3_val = random_4_gate_print(OPERATIONS_2, variable_list, 10)
        gate3_size = 4
    
    o1_final_gate_out, o1_final_gate_val = random_3_gate_terminal(OPERATIONS_3, gate1_out, gate2_out, gate3_out)
    #print("GATE: o1 = %s" % o1_final_gate_out)
     
    rand_num = random.randrange(2)
    if rand_num == 0:
        o2_final_gate_out, o2_final_gate_val = random_3_gate_print(OPERATIONS_2, variable_list, 10)
        o2_final_gate_size = 3
    else:
        o2_final_gate_out, o2_final_gate_val = random_4_gate_print(OPERATIONS_2, variable_list, 10)
        o2_final_gate_size = 4
    #print("GATE: o2 = %s" % o2_final_gate_out)
    
    # create the answers
    answer_file = open(directory_out+'/'+student_name+'_answers_exam1_q1.txt', 'w')
    answer_file.write("Question 1 = Truth Table\n")
    answer_file.write("a b c d e o1 o2\n")
    for a in range(2):
        for b in range(2):
            for c in range(2):
                 for d in range(2):
                    for e in range(2):
                        gate1_result = eval_gate_first_stage(gate1_size, gate1_val, a, b, c, d, e);
                        gate2_result = eval_gate_first_stage(gate2_size, gate2_val, a, b, c, d, e);
                        gate3_result = eval_gate_first_stage(gate3_size, gate3_val, a, b, c, d, e);
                        o1 = eval_gate_second_stage(o1_final_gate_val, gate1_result, gate2_result, gate3_result);
                        o2 = eval_gate_first_stage(o2_final_gate_size, o2_final_gate_val, a, b, c, d, e);
                        answer_file.write("%d %d %d %d %d  %d  %d\n" % (a, b , c, d, e, o1, o2))
    
    # close answer file
    answer_file.close()
    
    return o1_final_gate_out, o2_final_gate_out
