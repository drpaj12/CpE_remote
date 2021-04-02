import sys
import os
import subprocess
import random
import operator

def create_equation():
    """ Question 1 - Build a circuit of A ?1 B ?2 C ?3 D where ?1 = {+ or -}, ?2 = {^ or ~^}, ?3 = {- or + invert of 2} and A, B, C, or D 'pick one' is two's comp based on <, >, >=, <=  """
    
    rand_num = random.randrange(2)
    if rand_num == 0:
        # ADD   
        op1 = "+"
        op2 = "-"
    else:
        # SUB
        op1 = "-"
        op2 = "+"
    
    rand_num = random.randrange(2)
    if rand_num == 0:
        # XOR
        op3 = "^"
    else:
        # XNOR
        op3 = "~^"
    
    rand_num = random.randrange(4)
    if rand_num == 0:
        # <
        comp = "<"
    elif rand_num == 1:
        # >
        comp = ">"
    elif rand_num == 2:
        # >=
        comp = ">="
    else:
        # <=
        comp = "<="
 
    Astring = "A"
    Bstring = "B"
    Cstring = "C"
    Dstring = "D"
    rand_num = random.randrange(4)
    if rand_num == 0:
        # A
        where = "A's value is defined as: if (B " + comp + " C) A=A else A=-A"
    elif rand_num == 1:
        # B
        where = "B's value is defined as: if (A " + comp + " C) B=B else B=-B"
    elif rand_num == 2:
        # C
        where = "C's value is defined as: if (A " + comp + " B) C=C else C=-C"
    else:
        # D
        where = "D's value is defined as: if (A " + comp + " B) D=D else D=-D"

    equation = "(((" + Astring + " " + op1 + " " + Bstring + ") " + op3 + " " + Cstring + ") " + op2 + " " + Dstring + ")\n where " + where

    A_val = random.randrange(9) - 5
    while A_val == 0 :
        A_val = random.randrange(9) - 5
    B_val = random.randrange(9) - 5
    while B_val == 0 :
        B_val = random.randrange(9) - 5
    C_val = random.randrange(9) - 5
    while C_val == 0 :
        C_val = random.randrange(9) - 5
    D_val = random.randrange(9) - 5
    while D_val == 0 :
        D_val = random.randrange(9) - 5

    values = "A = "+str(A_val)+"; B = "+str(B_val)+"; C = "+str(C_val)+"; D = "+str(D_val)
    
    return equation, values
