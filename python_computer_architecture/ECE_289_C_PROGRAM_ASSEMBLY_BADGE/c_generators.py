import random
import sys
import string

# borrowed base from https://codereview.stackexchange.com/questions/49432/python-script-for-generating-random-c-code
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

# writes text to a stored outputString
# fetch the outputString later for outputting
class output:
    def __init__(self):
        self.clear()

    def clear(self):
        self.outputString = ''
        self.__lineStart = True
        self.lineCount = 0
        self.nestingLevel = 0

    def __write(self, str):
        self.outputString += str

    def line(self):
        self.__write('\n')
        self.__lineStart = True
        self.lineCount += 1

    def output(self, str):
        # start each line with tabs equal to nesting level
        if(self.__lineStart == True):
            for q in range(0, self.nestingLevel):
                self.__write('\t')
            self.__lineStart = False

        self.__write(str)

    def put_open_brace(self):
        self.output('{')
        self.line()
        self.inc_nesting()

    def put_close_brace(self):
        self.dec_nesting()
        self.output('}')
        self.line()

    def inc_nesting(self):
        self.nestingLevel += 1

    def dec_nesting(self):
        self.nestingLevel -= 1

class variables:
    def __init__(self, int_var_count, char_var_count, static_string_var_count, int_pointer_var_count, int_pointer_min_size, int_pointer_max_size, dynamic_string_var_count):
        if int_var_count > 26:
            raise Exception('Don\'t you think you\'re being a bit too aggressive?')
        self.int_var_count = int_var_count
        lowercase = list(string.ascii_lowercase)
        self.int_variables = lowercase[0:int_var_count]
        prefix = 'n'
        self.int_variables = [prefix + sub for sub in self.int_variables]

        if char_var_count > 26:
            raise Exception('Don\'t you think you\'re being a bit too aggressive?')
        self.char_var_count = char_var_count
        lowercase = list(string.ascii_lowercase)
        self.char_variables = lowercase[0:char_var_count]
        prefix = 'c'
        self.char_variables = [prefix + sub for sub in self.char_variables]

        if int_pointer_var_count > 26:
            raise Exception('Don\'t you think you\'re being a bit too aggressive?')
        self.int_pointer_var_count = int_pointer_var_count
        lowercase = list(string.ascii_lowercase)
        self.int_pointer_variables_names = lowercase[0:int_pointer_var_count]
        self.int_pointer_varaibles_allocation_size = random.sample(range(int_pointer_min_size, int_pointer_max_size), int_pointer_var_count)
        prefix = 'np'
        self.int_pointer_variables_names = [prefix + sub for sub in self.int_pointer_variables_names]

        if static_string_var_count > 26:
            raise Exception('Don\'t you think you\'re being a bit too aggressive?')
        self.static_string_var_count = static_string_var_count
        uppercase = list(string.ascii_uppercase)
        self.static_string_variables = uppercase[0:static_string_var_count]
        prefix = 'csp'
        self.static_string_variables = [prefix + sub for sub in self.static_string_variables]

        if dynamic_string_var_count > 26:
            raise Exception('Don\'t you think you\'re being a bit too aggressive?')
        self.dynamic_string_var_count = dynamic_string_var_count
        uppercase = list(string.ascii_uppercase)
        self.dynamic_string_variables_names = uppercase[0:dynamic_string_var_count]
        self.dynamic_string_varaibles_allocation_size = random.sample(range(5, 20), dynamic_string_var_count)
        prefix = 'cdp'
        self.dynamic_string_variables_names = [prefix + sub for sub in self.dynamic_string_variables_names]

    def rand_int_vars(self, count = 1):
        if count > self.int_var_count:
            raise Exception('Variables.Rand requested more variables than available')
        elif count == 1:
            return random.choice(self.int_variables)
        elif count > 1:
            return random.sample(self.int_variables, count)
        else:
            raise Exception('Variables.Rand invalid argument')

    def rand_char_vars(self, count = 1):
        if count > self.char_var_count:
            raise Exception('Variables.Rand requested more variables than available')
        elif count == 1:
            return random.choice(self.char_variables)
        elif count > 1:
            return random.sample(self.char_variables, count)
        else:
            raise Exception('Variables.Rand invalid argument')

    def rand_int_pointer_vars_count(self):
        return self.int_pointer_var_count

    def get_int_pointer_allocation_size(self, idx):
        if idx > self.int_pointer_var_count:
            raise Exception('Variables.Rand requested more variables than available')
        else:
            # returns index of choice
            return self.int_pointer_varaibles_allocation_size[idx]

    def get_int_pointer_name(self, idx):
        if idx > self.int_pointer_var_count:
            raise Exception('Variables.Rand requested more variables than available')
        else:
            # returns index of choice
            return self.int_pointer_variables_names[idx]

    def rand_static_string_variable(self, count = 1):
        if count > self.static_string_var_count:
            raise Exception('Variables.Rand requested more variables than available')
        elif count == 1:
            return random.choice(self.static_string_variables)
        elif count > 1:
            return random.sample(self.static_string_variables, count)
        else:
            raise Exception('Variables.Rand invalid argument')

    def rand_dynamic_string_vars_count(self):
        return self.dynamic_string_var_count

    def get_dynamic_string_allocation_size(self, idx):
        if idx > self.dynamic_string_var_count:
            raise Exception('Variables.Rand requested more variables than available')
        else:
            # returns index of choice
            return self.dynamic_string_varaibles_allocation_size[idx]

    def get_dynamic_string_name(self, idx):
        if idx > self.dynamic_string_var_count:
            raise Exception('Variables.Rand requested more variables than available')
        else:
            # returns index of choice
            return self.dynamic_string_variables_names[idx]

    def init_var_statements(self, out, int_size):
        if self.int_var_count >= 1:
            out.output('int ')
            vars = []
            for var in self.int_variables:
                vars.append('%s = %i' % (var, random.randint((-int_size), int_size)))
            out.output(', '.join(vars))
            out.output(';')
            out.line()

        if self.char_var_count >= 1:
            out.output('char ')
            vars = []
            for var in self.char_variables:
                vars.append('%s = \'%s\'' % (var, get_random_string(1)))
            out.output(', '.join(vars))
            out.output(';')
            out.line()

        if self.int_pointer_var_count >= 1:
            out.output('// pointers ')
            out.line()
            out.output('int ')
            vars = []
            for var in self.int_pointer_variables_names:
                vars.append('*%s' % (var))
            out.output(', '.join(vars))
            out.output(';')
            out.line()

        if self.static_string_var_count >= 1:
            out.output('// pointer to statically allocated string ')
            out.line()
            out.output('char ')
            vars = []
            for var in self.static_string_variables:
                vars.append('%s[6] = "%s"' % (var, get_random_string(5)))
            out.output(', '.join(vars))
            out.output(';')
            out.line()

        if self.dynamic_string_var_count >= 1:
            out.output('// pointer to be dynamically allocated strings ')
            out.line()
            out.output('char ')
            vars = []
            for var in self.dynamic_string_variables_names:
                vars.append('*%s' % (var))
            out.output(', '.join(vars))
            out.output(';')
            out.line()

class action_copy:
    def __init__(self, variables, output):
        self.variables = variables
        self.out = output
        self.labelCount = 0

class static_string_statements():
    ASSIGN = 1
    SWAP = 2

    def __init__(self, output, variables):
        self.out = output
        self.variables = variables

    def put_assignment_rand(self):
        statement_type = random.randint(1,2)
        self.put_assignment(statement_type)

    def put_assignment(self, statement_type):
        if(statement_type ==  static_string_statements.ASSIGN):
            letters = string.ascii_lowercase
            char = random.choice(letters);
            idx = random.randint(0,5)
            dest = self.variables.rand_static_string_variable(1)
            self.out.output(dest+'['+str(idx)+'] = \'' + char + '\';')
            self.out.line()
        elif(statement_type ==  static_string_statements.SWAP):
            dest, src = self.variables.rand_static_string_variable(2)
            idx1 = random.randint(0,5)
            idx2 = random.randint(0,5)
            self.out.output(dest+'['+str(idx1)+'] = ' + src + '['+str(idx2)+'];')
            self.out.line()
        else:
            raise Exception('statement type' + str(statement_type) + '=bad argument')

class int_statements_w_idx_var():
    ASSIGN = 1
    ADD = 2
    SUB = 3
    MOD = 4
    DIV = 5
    MULT = 6

    def __init__(self, output, variables):
        self.out = output
        self.variables = variables

    def put_assignment_rand(self,idx_variable):
        statement_type = random.randint(1,6)
        self.put_assignment(statement_type, idx_variable)

    def put_assignment(self, statement_type, idx_variable):
        dest, src = self.variables.rand_int_vars(2)
        if(statement_type ==  int_statements_w_idx_var.ASSIGN):
            self.out.output(dest + ' = ' + idx_variable + ';')
            self.out.line()
        elif(statement_type ==  int_statements_w_idx_var.ADD):
            self.out.output(dest + ' = ' + src + ' + ' + idx_variable + ';')
            self.out.line()
        elif(statement_type ==  int_statements_w_idx_var.SUB):
            self.out.output(dest + ' = ' + src + ' - ' + idx_variable + ';')
            self.out.line()
        elif(statement_type ==  int_statements_w_idx_var.MOD):
            self.out.output(dest + ' = ' + src + ' % ' + idx_variable + ';')
            self.out.line()
        elif(statement_type ==  int_statements_w_idx_var.DIV):
            self.out.output(dest + ' = ' + src + ' / ' + idx_variable + ';')
            self.out.line()
        elif(statement_type ==  int_statements_w_idx_var.MULT):
            self.out.output(dest + ' = ' + src + ' * ' + idx_variable + ';')
            self.out.line()
        else:
            raise Exception('statement type' + str(statement_type) + '=bad argument')

class char_statements():
    ASSIGN = 1
    ADD = 2
    MULT = 3
    ASSIGN_NEW_CHAR = 4

    def __init__(self, output, variables):
        self.out = output
        self.variables = variables

    def put_assignment_rand(self):
        statement_type = random.randint(1,4)
        self.put_assignment(statement_type)

    def put_assignment(self, statement_type):
        if(statement_type ==  char_statements.ASSIGN):
            dest, src = self.variables.rand_char_vars(2)
            self.out.output(dest + ' = ' + src + ';')
            self.out.line()
        elif(statement_type ==  char_statements.ADD):
            dest, src1, src2 = self.variables.rand_char_vars(3)
            self.out.output(dest + ' = ' + src1 + ' + ' + src2 + ';')
            self.out.line()
        elif(statement_type ==  char_statements.MULT):
            dest, src1, src2 = self.variables.rand_char_vars(3)
            self.out.output(dest + ' = ' + src1 + ' * ' + src2 + ';')
            self.out.line()
        elif(statement_type ==  char_statements.ASSIGN_NEW_CHAR):
            dest, src = self.variables.rand_char_vars(2)
            self.out.output(dest + ' = \'' + get_random_string(1) + '\';')
            self.out.line()

        else:
            raise Exception('statement type' + str(statement_type) + '=bad argument')

class int_statements():
    ASSIGN = 1
    ADD = 2
    SUB = 3
    MOD = 4
    DIV = 5
    MULT = 6

    def __init__(self, output, variables):
        self.out = output
        self.variables = variables

    def put_assignment_rand(self):
        statement_type = random.randint(1,6)
        self.put_assignment(statement_type)

    def put_assignment(self, statement_type):
        if(statement_type ==  int_statements.ASSIGN):
            dest, src = self.variables.rand_int_vars(2)
            self.out.output(dest + ' = ' + src + ';')
            self.out.line()
        elif(statement_type ==  int_statements.ADD):
            dest, src1, src2 = self.variables.rand_int_vars(3)
            self.out.output(dest + ' = ' + src1 + ' + ' + src2 + ';')
            self.out.line()
        elif(statement_type ==  int_statements.SUB):
            dest, src1, src2 = self.variables.rand_int_vars(3)
            self.out.output(dest + ' = ' + src1 + ' - ' + src2 + ';')
            self.out.line()
        elif(statement_type ==  int_statements.MOD):
            dest, src1, src2 = self.variables.rand_int_vars(3)
            self.out.output(dest + ' = ' + src1 + ' % ' + src2 + ';')
            self.out.line()
        elif(statement_type ==  int_statements.DIV):
            dest, src1, src2 = self.variables.rand_int_vars(3)
            self.out.output(dest + ' = ' + src1 + ' / ' + src2 + ';')
            self.out.line()
        elif(statement_type ==  int_statements.MULT):
            dest, src1, src2 = self.variables.rand_int_vars(3)
            self.out.output(dest + ' = ' + src1 + ' * ' + src2 + ';')
            self.out.line()
        else:
            raise Exception('statement type' + str(statement_type) + '=bad argument')

class int_pointer():
    def __init__(self, output, variables):
        self.out = output
        self.variables = variables

    def put_malloc(self):
        for i in range(self.variables.rand_int_pointer_vars_count()):
            assignment_pointer_size = self.variables.get_int_pointer_allocation_size(i)
            assignment_pointer_name = self.variables.get_int_pointer_name(i)
            self.out.output(assignment_pointer_name + ' = (int*)malloc(sizeof(int)*' + str(assignment_pointer_size) + ');')
            self.out.line()

    def init_all_int_pointers_incrementally(self):
        for_loop = for_loops(self.out, self.variables)
        for i in range(self.variables.rand_int_pointer_vars_count()):
            assignment_pointer_size = self.variables.get_int_pointer_allocation_size(i)
            assignment_pointer_name = self.variables.get_int_pointer_name(i)

            for_loop.put_for_int_variable_0_to_size(assignment_pointer_size, 'i')
            self.out.output(assignment_pointer_name + '[i] = i;')
            self.out.line()
            for_loop.put_for_end()
            self.out.line()

    def access_pointers_based_on_striations(self, simple_cache):
        for_loop = for_loops(self.out, self.variables)
        assignment_pointer_size = self.variables.get_int_pointer_allocation_size(0)
        assignment_pointer_name = self.variables.get_int_pointer_name(0)
        dest = self.variables.rand_int_vars(1)

        for_loop.put_for_int_variable_rand_to_size_with_inc_1to3(assignment_pointer_size, 'i', 0, 20, assignment_pointer_size - 20, assignment_pointer_size, 1, 3)
        if simple_cache == 0:
            mod1 = str(random.randrange(1,3,2))
            mod2 = str(random.randrange(2,4,2))
            self.out.output(dest+' += '+assignment_pointer_name + '[i % '+mod1+'] + '+assignment_pointer_name + '[i % '+mod2+'];')
        else:
            mod1 = str(random.randrange(1,7,2))
            mod2 = str(random.randrange(2,8,2))
            mod3 = str(random.randrange(1,10,1))
            self.out.output(dest+' += '+assignment_pointer_name + '[i % '+mod1+'] + '+assignment_pointer_name + '[i % '+mod3+'] + '+assignment_pointer_name + '[i % '+mod2+'];')
        self.out.line()
        for_loop.put_for_end()
        self.out.line()


class dynamic_string():
    def __init__(self, output, variables):
        self.out = output
        self.variables = variables

    def put_malloc(self):
        for i in range(self.variables.rand_dynamic_string_vars_count()):
            assignment_pointer_size = self.variables.get_dynamic_string_allocation_size(i)
            assignment_pointer_name = self.variables.get_dynamic_string_name(i)
            self.out.output(assignment_pointer_name + ' = (char*)malloc(sizeof(char)*' + str(assignment_pointer_size) + ');')
            self.out.line()

    def init_all_dynamic_strings_to_aaa_null_term(self):
        for_loop = for_loops(self.out, self.variables)
        for i in range(self.variables.rand_dynamic_string_vars_count()):
            assignment_pointer_size = self.variables.get_dynamic_string_allocation_size(i)
            assignment_pointer_name = self.variables.get_dynamic_string_name(i)

            for_loop.put_for_int_variable_0_to_size(assignment_pointer_size-1, 'i')
            self.out.output(assignment_pointer_name + '[i] = \''+random.choice(string.ascii_letters)+'\';')
            self.out.line()
            for_loop.put_for_end()
            self.out.output(assignment_pointer_name + '['+str(assignment_pointer_size-1)+'] = \'\\0\';')
            self.out.line()

class while_loops():
    def __init__(self, output, variables):
        self.out = output
        self.variables = variables

    def put_condition_idx_0_to_max(self, while_size, idx_already_defined):
        if not(idx_already_defined):
            self.out.output('int idx = 0;')
            self.out.line()
        self.out.output('while(')
        self.out.output('idx < ' + str(while_size) + ')')
        self.out.line()
        self.out.put_open_brace()

    def put_condition_idx_scanf(self, while_size, idx_already_defined):
        if not(idx_already_defined):
            self.out.output('int idx = 0;')
            self.out.line()
        self.out.output('scanf("%d", &idx);')
        self.out.line()
        self.out.output('while(')
        self.out.output('idx != ' + str(while_size) + ')')
        self.out.line()
        self.out.put_open_brace()
        self.out.output('scanf("%d", &idx);')
        self.out.line()

    def put_loop_end_idx_increment(self):
        self.out.output('idx ++;')
        self.out.line()
        self.out.put_close_brace()

    def put_loop_end(self):
        self.out.put_close_brace()

    def put_while_loop_with_idx(self, idx_already_defined):
        self.put_condition_idx_0_to_max(random.randint(1,10), idx_already_defined)
        int_statements_w_idx_var(self.out, self.variables).put_assignment_rand("idx")
        self.put_loop_end_idx_increment()

    def put_while_loop_with_scanf_idx(self, idx_already_defined):
        self.put_condition_idx_scanf(random.randint(1,10), idx_already_defined)
        int_statements_w_idx_var(self.out, self.variables).put_assignment_rand("idx")
        self.put_loop_end()

class for_loops():
    def __init__(self, output, variables):
        self.out = output
        self.variables = variables

    def put_for_random_w_statement(self,idx_declared):
        if not(idx_declared):
            self.out.output('int i;')
            self.out.line()
        for_size = random.randint(1,10)
        self.out.output('for(int i = 0; i < '+ str(for_size) +'; i++)')
        self.out.line()
        self.out.put_open_brace()

    def put_for_int_variable_0_to_size(self, for_size, variable):
        self.out.output('for(int '+variable+' = 0; '+variable+' < '+ str(for_size) +'; '+variable+'++)')
        self.out.line()
        self.out.put_open_brace()

    def put_for_int_variable_rand_to_size_with_inc_1to3(self, for_size, variable, init_min, init_max, end_min, end_max, inc_min, inc_max):
        for_init = str(random.randint(init_min,init_max))
        for_size_to_go = str(random.randint(end_min,end_max))
        index_inc = str(random.randint(inc_min,inc_max))
        self.out.output('for(int '+variable+' = '+for_init+'; '+variable+' < '+ str(for_size_to_go) +'; '+variable+'= '+variable+' + '+index_inc+')')
        self.out.line()
        self.out.put_open_brace()

    def put_for_end(self):
        self.out.put_close_brace()

    def put_for_loop(self, idx_declared):
        self.put_for_random_w_statement(idx_declared)
        int_statements_w_idx_var(self.out, self.variables).put_assignment_rand("i")
        self.put_for_end()

class if_statements():
    def __init__(self, output, variables):
        self.out = output
        self.variables = variables

    def put_if_conditional(self):
        first, second = self.variables.rand_int_vars(2)
        self.out.output('if(')
        cond_type = random.randint(1,6)
        if (cond_type == 1):
            self.out.output(first + ' == ' + second)
        elif (cond_type == 2):
            self.out.output(first + ' < ' + second)
        elif (cond_type == 3):
            self.out.output(first + ' > ' + second)
        elif (cond_type == 4):
            self.out.output(first + ' <= ' + second)
        elif (cond_type == 5):
            self.out.output(first + ' >= ' + second)
        elif (cond_type == 6):
            self.out.output(first + ' != ' + second)
        self.out.output(')')
        self.out.line()
        self.out.put_open_brace()

    def put_else(self):
        self.out.output('else')
        self.out.line()
        self.out.put_open_brace()

    def put_if_else_with_rand_statements(self):
        self.put_if_conditional()
        int_statements(self.out, self.variables).put_assignment_rand()
        self.out.put_close_brace()
        self.put_else()
        int_statements(self.out, self.variables).put_assignment_rand()
        self.out.put_close_brace()

class function_generator:
    total_func_counter = 0 # how many functions

    def __init__(self, num_int_variables, num_char_variables, num_static_string_variables, num_int_pointer_vars, int_pointers_min, int_pointers_max, num_dynamic_string_vars):
        self.funcNum = function_generator.total_func_counter
        function_generator.total_func_counter += 1

        self.variables = variables(num_int_variables, num_char_variables, num_static_string_variables, num_int_pointer_vars, int_pointers_min, int_pointers_max, num_dynamic_string_vars) # number of variables to define
        self.out = output()
        self.name = 'Simple_Vars' + str(self.funcNum)

        self.action = action_copy(self.variables, self.out)

        # include libraries
        self.out.output('#include <stdio.h>')
        self.out.line()
        self.out.output('#include <stdlib.h>')
        self.out.line()
        self.out.output('#include <string.h>')
        self.out.line()
        self.out.line()

    def function_header_int(self):
        self.out.output('int ' + self.name + '()')
        self.out.line()
        self.out.output('{')
        self.out.line()
        self.out.inc_nesting()

    def function_footer_return_int(self):
        retval = self.variables.rand_int_vars()
        self.out.output('return ' + retval + ';')
        self.out.line()
        self.out.dec_nesting()
        self.out.output('}')
        self.out.line()

    def function_header_void_name(self, name):
        self.out.output('void ' + name + '()')
        self.out.line()
        self.out.output('{')
        self.out.line()
        self.out.inc_nesting()

    def function_footer_no_return(self):
        self.out.dec_nesting()
        self.out.output('}')
        self.out.line()

    def function_main_declare(self):
        # make a main so compiles
        self.out.line()
        self.out.output('void main()')
        self.out.line()
        self.out.output('{')
        self.out.line()
        self.out.inc_nesting()

    def function_call_in_main(self, function_name):
        self.out.output(function_name+'();')
        self.out.line()

    def function_body(self):
        # int functionname()
        # {
        self.function_header()

        # int a = 1, b = 2, etc
        # char A[6] = "asdas", B[6] = "testo",
        self.variables.init_var_statements(self.out, 10)
        self.out.line()

        # mallocs
        self.int_pointer = int_pointer(self.out, self.variables)
        self.int_pointer.put_malloc()
        self.out.line()
        self.dynamic_string = dynamic_string(self.out, self.variables)
        self.dynamic_string.put_malloc()
        self.out.line()

        # [function body]

        for i in range(5):
            int_statements(self.out, self.variables).put_assignment_rand()
        self.out.line()
        for i in range(5):
            static_string_statements(self.out, self.variables).put_assignment_rand()
        self.out.line()

        for i in range(5):
            if_statements(self.out, self.variables).put_if_else_with_rand_statements()
        self.out.line()

        while_loops(self.out, self.variables).put_while_loop_with_idx(False)
        self.out.line()
        for_loops(self.out, self.variables).put_for_loop(False)
        self.out.line()

        self.int_pointer.init_all_int_pointers_incrementally()
        self.out.line()
        self.dynamic_string.init_all_dynamic_strings_to_aaa_null_term()
        self.out.line()

        # }
        self.function_footer_return_int()

    def function_c_and_assembly_statements(self):
        # int functionname()
        # {
        function_name = 'c_and_assembly_statements';
        self.function_header_void_name(function_name)

        # int a = 1, b = 2, etc
        # char A[6] = "asdas", B[6] = "testo",
        self.variables.init_var_statements(self.out, 10)
        self.out.line()

        self.out.output('// these are integer C statements')
        self.out.line()
        for i in range(5):
            int_statements(self.out, self.variables).put_assignment_rand()
        self.out.line()
        self.out.line()

        self.out.output('// these are char C statements where an array of chars is a string')
        self.out.line()
        for i in range(5):
            char_statements(self.out, self.variables).put_assignment_rand()
        self.out.line()

        # }
        self.function_footer_no_return()

        # make a main so compiles
        self.function_main_declare()
        self.function_call_in_main(function_name)
        self.function_footer_no_return()

    def function_if_else_w_rand_statements(self):
        # int functionname()
        # {
        function_name = 'c_and_assembly_if_else';
        self.function_header_void_name(function_name)

        # int a = 1, b = 2, etc
        # char A[6] = "asdas", B[6] = "testo",
        self.variables.init_var_statements(self.out, 10)
        self.out.line()

        for i in range(3):
            if_statements(self.out, self.variables).put_if_else_with_rand_statements()
            self.out.line()

        self.function_footer_no_return()

        # make a main so compiles
        self.function_main_declare()
        self.function_call_in_main(function_name)
        self.function_footer_no_return()

    def function_while_scanf(self):
        # int functionname()
        # {
        function_name = 'c_and_assembly_while_loop';
        self.function_header_void_name(function_name)

        # int a = 1, b = 2, etc
        # char A[6] = "asdas", B[6] = "testo",
        self.variables.init_var_statements(self.out, 10)
        self.out.line()

        while_loops(self.out, self.variables).put_while_loop_with_idx(False)
        self.out.line()
        while_loops(self.out, self.variables).put_while_loop_with_scanf_idx(True)
        self.out.line()

        self.function_footer_no_return()

        # make a main so compiles
        self.function_main_declare()
        self.function_call_in_main(function_name)
        self.function_footer_no_return()

    def function_for(self):
        # int functionname()
        # {
        function_name = 'c_and_assembly_for_loop';
        self.function_header_void_name(function_name)

        # int a = 1, b = 2, etc
        # char A[6] = "asdas", B[6] = "testo",
        self.variables.init_var_statements(self.out, 10)
        self.out.line()

        for_loops(self.out, self.variables).put_for_loop(False)
        self.out.line()
        for_loops(self.out, self.variables).put_for_loop(True)
        self.out.line()

        self.function_footer_no_return()

        # make a main so compiles
        self.function_main_declare()
        self.function_call_in_main(function_name)
        self.function_footer_no_return()

    def function_pointer_examples(self):
        # int functionname()
        # {
        function_name = 'c_and_assembly_for_pointer_example';
        self.function_header_void_name(function_name)

        # int a = 1, b = 2, etc
        # char A[6] = "asdas", B[6] = "testo",
        self.variables.init_var_statements(self.out, 10)
        self.out.line()

        # mallocs
        self.int_pointer = int_pointer(self.out, self.variables)
        self.int_pointer.put_malloc()
        self.out.line()
        self.dynamic_string = dynamic_string(self.out, self.variables)
        self.dynamic_string.put_malloc()
        self.out.line()

        self.out.output('// integer pointers')
        self.out.line()
        self.int_pointer.init_all_int_pointers_incrementally()
        self.out.line()

        # these are static arrays of characters/strings
        self.out.output('// static arrays of characters/strings')
        self.out.line()
        for i in range(5):
            static_string_statements(self.out, self.variables).put_assignment_rand()
        self.out.line()

        self.out.output('// character dynamic pointers')
        self.out.line()
        self.dynamic_string.init_all_dynamic_strings_to_aaa_null_term()
        self.out.line()

        self.function_footer_no_return()

        # make a main so compiles
        self.function_main_declare()
        self.function_call_in_main(function_name)
        self.function_footer_no_return()

    def function_cache_class(self):
        # int functionname()
        # {
        function_name = 'c_cache_for_class';
        self.function_header_void_name(function_name)

        # int a = 1, b = 2, etc
        # char A[6] = "asdas", B[6] = "testo",
        self.variables.init_var_statements(self.out, 10)
        self.out.line()

        # mallocs
        self.int_pointer = int_pointer(self.out, self.variables)
        self.int_pointer.put_malloc()
        self.out.line()

        # pointer int initialize
        self.out.output('// init integer pointers')
        self.out.line()
        self.int_pointer.init_all_int_pointers_incrementally()
        self.out.line()

        # now access the integer array
        self.out.output('// integer pointers')
        self.out.line()
        self.int_pointer.access_pointers_based_on_striations(0)
        self.out.line()

        self.function_footer_no_return()

        # make a main so compiles
        self.function_main_declare()
        self.function_call_in_main(function_name)
        self.function_footer_no_return()

    def function_cache_badge(self):
        # int functionname()
        # {
        self.out.output(' // Assume\n \
// - 2-way set associative cache\n \
// - cache size = 4\n \
// - cache hits take 1 cycle\n \
// - cache miss takes 10 cycles\n \
// - all other instructions 1 cycle\n \
\n \
// Report number of cycles for an\n \
// - architecture with a cache (including hits and misses)\n \
// - architecture with no cache (slower, in theory)\n')
        self.out.line()
        function_name = 'c_cache_for_badge';
        self.function_header_void_name(function_name)

        # int a = 1, b = 2, etc
        # char A[6] = "asdas", B[6] = "testo",
        self.variables.init_var_statements(self.out, 10)
        self.out.line()

        # mallocs
        self.int_pointer = int_pointer(self.out, self.variables)
        self.int_pointer.put_malloc()
        self.out.line()

        # pointer int initialize
        self.out.output('// init integer pointers')
        self.out.line()
        self.int_pointer.init_all_int_pointers_incrementally()
        self.out.line()

        # now access the integer array
        self.out.output('// integer pointers')
        self.out.line()
        self.int_pointer.access_pointers_based_on_striations(1)
        self.out.line()

        self.function_footer_no_return()

        # make a main so compiles
        self.function_main_declare()
        self.function_call_in_main(function_name)
        self.function_footer_no_return()

    def function_pipeline_badge(self):
        # int functionname()
        # {
        string_list = []
        string_list.append('a[i] = c + d;\n\t\te = a[i] + 2;')
        string_list.append('a[i] = 7;\n\t\tb = c + d;\n\t\te = a[i] + a[i+1];')
        string_list.append('a[i] = 7;\n\t\ta[i+1] = 8;\n\t\tc = a[i] + a[i+1];')
        string_list.append('a[i+1] = 9;\n\t\ta[i] = 7;\n\t\tc = a[i+1]+a[i]')
        string_list.append('c = a[i] + a[i+1];\n\t\ta[i] = c;')

        self.out.output('// Report number of cycles for an\n \
// - architecture with a 4 stage pipeline and calculate stalls\n \
// - architecture with no pipeline takes 4 cycles per instruction\n')
        self.out.line()
        function_name = 'c_pipeline_for_badge';
        self.function_header_void_name(function_name)

        # int a = 1, b = 2, etc
        # char A[6] = "asdas", B[6] = "testo",
        self.variables.init_var_statements(self.out, 10)
        self.out.line()

        # mallocs
        self.int_pointer = int_pointer(self.out, self.variables)
        self.int_pointer.put_malloc()
        self.out.line()

        # pointer int initialize
        self.out.output('// init integer pointers')
        self.out.line()
        self.int_pointer.init_all_int_pointers_incrementally()
        self.out.line()

        # now access the integer array
        self.out.output('// integer pointers')
        self.out.line()
        for_loop = for_loops(self.out, self.variables)
        assignment_pointer_size = self.variables.get_int_pointer_allocation_size(0)
        assignment_pointer_name = self.variables.get_int_pointer_name(0)
        dest = self.variables.rand_int_vars(1)

        for_loop.put_for_int_variable_rand_to_size_with_inc_1to3(assignment_pointer_size, 'i', 0, 20, assignment_pointer_size - 20, assignment_pointer_size, 1, 3)
        mod1 = str(random.randrange(1,7,2))
        mod2 = str(random.randrange(2,8,2))
        mod3 = str(random.randrange(1,10,1))
        str_out = string_list[random.randint(0,4)].replace("a", assignment_pointer_name)
        str_out = str_out.replace("b", self.variables.int_variables[0])
        str_out = str_out.replace("c", self.variables.int_variables[1])
        str_out = str_out.replace("d", self.variables.int_variables[2])
        str_out = str_out.replace("e", self.variables.int_variables[3])

        self.out.output(str_out)
        self.out.line()
        for_loop.put_for_end()
        self.out.line()

        self.function_footer_no_return()

        # make a main so compiles
        self.function_main_declare()
        self.function_call_in_main(function_name)
        self.function_footer_no_return()

    def function_for_optimize(self):
        # int functionname()
        # {
        function_name = 'c_and_assembly_for_optimize';
        self.function_header_void_name(function_name)

        # int a = 1, b = 2, etc
        # char A[6] = "asdas", B[6] = "testo",
        self.variables.init_var_statements(self.out, 10)
        self.out.line()

        self.out.output('// loop fully unrolled and constant folding')
        self.out.line()
        for_loops(self.out, self.variables).put_for_loop(False)
        self.out.line()

        self.function_footer_no_return()

        # make a main so compiles
        self.function_main_declare()
        self.function_call_in_main(function_name)
        self.function_footer_no_return()

    def function_call_function(self):

        self.out.output('int bar(int a, int b)')
        self.out.line()
        self.out.output('{')
        self.out.line()
        self.out.output('\treturn (a + b * b);');
        self.out.line()
        self.out.output('}')
        self.out.line()
        self.out.line()
        # int functionname()
        # {
        function_name = 'foo';
        self.function_header_void_name(function_name)

        # int a = 1, b = 2, etc
        # char A[6] = "asdas", B[6] = "testo",
        self.variables.init_var_statements(self.out, 10)
        self.out.line()

        self.out.output('// call function')
        self.out.line()
        v1, v2, v3 = self.variables.rand_int_vars(3)
        self.out.output(v3+' = bar ('+v1+', '+v2+');')
        self.out.line()

        self.function_footer_no_return()

        # make a main so compiles
        self.function_main_declare()
        self.function_call_in_main(function_name)
        self.function_footer_no_return()


    def output_string(self):
        return self.out.outputString

def PrintLongFunction(file_to_print_to, num_int_variables, num_char_variables, num_static_string_variables, num_int_pointer_vars, num_dynamic_string_vars):
    func = function_generator(num_int_variables,num_char_variables,num_static_string_variables,num_int_pointer_vars, num_dynamic_string_vars)
    func.function_body()
    file_to_print_to.write(func.output_string())

def print_c_statements_to_file(file_to_print_to):
    func = function_generator(5,5,0,0,0,0,0)
    func.function_c_and_assembly_statements()
    file_to_print_to.write(func.output_string())

def print_c_if_else_to_file(file_to_print_to):
    func = function_generator(3,3,0,0,0,0,0)
    func.function_if_else_w_rand_statements()
    file_to_print_to.write(func.output_string())

def print_c_while_loop_with_scanf_to_exit_file(file_to_print_to):
    func = function_generator(3,3,0,0,0,0,0)
    func.function_while_scanf()
    file_to_print_to.write(func.output_string())

def print_c_for_loop_file(file_to_print_to):
    func = function_generator(3,3,0,0,0,0,0)
    func.function_for()
    file_to_print_to.write(func.output_string())

def print_c_pointer_basic_funcionality_file(file_to_print_to):
    func = function_generator(0,0,3,3,5,20,3)
    func.function_pointer_examples()
    file_to_print_to.write(func.output_string())

def print_cache_generator_for_class(file_to_print_to):
    func = function_generator(3,0,0,1,60,80,0)
    func.function_cache_class()
    file_to_print_to.write(func.output_string())

def print_cache_generator_for_badge(file_to_print_to):
    func = function_generator(3,0,0,1,80,100,0)
    func.function_cache_badge()
    file_to_print_to.write(func.output_string())

def print_pipeline_generator_for_badge(file_to_print_to):
    func = function_generator(6,0,0,1,80,100,0)
    func.function_pipeline_badge()
    file_to_print_to.write(func.output_string())

def print_c_optimization_for_class(file_to_print_to):
    func = function_generator(3,3,3,0,0,0,0)
    func.function_for_optimize()
    file_to_print_to.write(func.output_string())

def print_c_function_call(file_to_print_to):
    func = function_generator(10,0,0,0,0,0,0)
    func.function_call_function()
    file_to_print_to.write(func.output_string())

#if __name__ == "__main__":
#    f = open("test.c", "w")
#    PrintLongFunction(f, 5, 6, 3, 2)

