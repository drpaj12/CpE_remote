import sys
import os
import subprocess
import random
import operator
import csv
# from files connected to
from c_generators import *
# for documents
from docx import Document
# EMAIL STUFF
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from email.message import EmailMessage

#--------------------
def send_email(username, directory):
    # sends the email attachment
    msg = EmailMessage()
    sender = '' # sender email - add yours here
    receiver = username+'@miamioh.edu' # note that this was originally designed for Miami and you should use your own here
    cc = "" # a cc if you want it
    receivers = [cc] + [receiver]
    password = "" # password you've setup with your email - not your password to the account, but an email setup
    msg['From'] = sender
    msg['To'] = receiver
    msg['Cc'] = cc
    msg['Subject'] = "ECE 289 - C Code Packet for course"
    msg.set_content("ECE 289 Attached C files")
    filename=''+directory+''+username+'_c_assembly_for_loop.c'
    msg.add_attachment(open(filename, "r").read(), filename=directory+''+username+'_c_assembly_for_loop.c')
    filename=''+directory+''+username+'_c_assembly_if_statement.c'
    msg.add_attachment(open(filename, "r").read(), filename=directory+''+username+'_c_assembly_if_statement.c')
    filename=''+directory+''+username+'_c_assembly_pointers.c'
    msg.add_attachment(open(filename, "r").read(), filename=directory+''+username+'_c_assembly_pointers.c')
    filename=''+directory+''+username+'_c_assembly_variables_and_statements.c'
    msg.add_attachment(open(filename, "r").read(), filename=directory+''+username+'_c_assembly_variables_and_statements.c')
    filename=''+directory+''+username+'_c_assembly_while_loop.c'
    msg.add_attachment(open(filename, "r").read(), filename=directory+''+username+'_c_assembly_while_loop.c')
    filename=''+directory+''+username+'_c_cache_benchmark_for_badge.c'
    msg.add_attachment(open(filename, "r").read(), filename=directory+''+username+'_c_cache_benchmark_for_badge.c')
    filename=''+directory+''+username+'_c_cache_example.c'
    msg.add_attachment(open(filename, "r").read(), filename=directory+''+username+'_c_cache_example.c')
    filename=''+directory+''+username+'_c_compiler_optimize.c'
    msg.add_attachment(open(filename, "r").read(), filename=directory+''+username+'_c_compiler_optimize.c')
    filename=''+directory+''+username+'_c_assembly_function_call.c'
    msg.add_attachment(open(filename, "r").read(), filename=directory+''+username+'_c_assembly_function_call.c')
    filename=''+directory+''+username+'_c_pipeline_benchmark_for_badge.c'
    msg.add_attachment(open(filename, "r").read(), filename=directory+''+username+'_c_pipeline_benchmark_for_badge.c')

    # app password - created on gmail account
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(sender, password)

    # actual send
    print("sender:"+sender)
    print("receivers:")
    print(*receivers)
    #print("message="+msg.as_string())
    smtpObj.send_message(msg)

    smtpObj.quit()

#--------------------

# 0_script 1_list_of_student_usernames 2_directory_to_store_files
# SAMPLE: create_code_for_ece289.py student_list.csv GENERATED_FILES
print ("Number of arguments: %d" %  len(sys.argv))
print ("Argument List: %s" % str(sys.argv))

directory_out = sys.argv[2]
code = 0
# read through the file and run them 
with open(sys.argv[1]) as f:
    reader = csv.reader(f)
    for student_name, subject_line, body, attach in reader:
        print("Student Name: %s" % student_name)
        print("Subject Line: %s" % subject_line)
        print("Body: %s" % body)
        print("Attachment: %s" % attach)

        # create code for first sample
        c_file = open(sys.argv[2] + '/' + student_name + '_c_assembly_variables_and_statements.c', "w")
        print_c_statements_to_file(c_file)
        c_file.close()

        # create code for if
        c_file = open(sys.argv[2] + '/' + student_name + '_c_assembly_if_statement.c', "w")
        print_c_if_else_to_file(c_file)
        c_file.close()

        # create for while with and user input exit
        c_file = open(sys.argv[2] + '/' + student_name + '_c_assembly_while_loop.c', "w")
        print_c_while_loop_with_scanf_to_exit_file(c_file)
        c_file.close()

        # create "for loop"
        c_file = open(sys.argv[2] + '/' + student_name + '_c_assembly_for_loop.c', "w")
        print_c_for_loop_file(c_file)
        c_file.close()

        # create pointers
        c_file = open(sys.argv[2] + '/' + student_name + '_c_assembly_pointers.c', "w")
        print_c_pointer_basic_funcionality_file(c_file)
        c_file.close()

        # create cache_access for class
        c_file = open(sys.argv[2] + '/' + student_name + '_c_cache_example.c', "w")
        print_cache_generator_for_class(c_file)
        c_file.close()

        # create cache_access for badge
        c_file = open(sys.argv[2] + '/' + student_name + '_c_cache_benchmark_for_badge.c', "w")
        print_cache_generator_for_badge(c_file)
        c_file.close()

        # create cache_access for badge
        c_file = open(sys.argv[2] + '/' + student_name + '_c_pipeline_benchmark_for_badge.c', "w")
        print_pipeline_generator_for_badge(c_file)
        c_file.close()

        # create cache_access for badge
        c_file = open(sys.argv[2] + '/' + student_name + '_c_compiler_optimize.c', "w")
        print_c_optimization_for_class(c_file)
        c_file.close()

        # create simple function call 
        c_file = open(sys.argv[2] + '/' + student_name + '_c_assembly_function_call.c', "w")
        print_c_function_call(c_file)
        c_file.close()

        # send the email
        send_email(student_name, sys.argv[2])

        # update the code
        code = code + 1
 
f.close()

