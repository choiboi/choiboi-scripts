#!/usr/bin/python

# 
# This script is meant to rename all the files in the given directory by adding
# a provided prefix and end with a number that will increase sequentially.
# 

import os
from os import path

def ask_for_input(question):
    response = ""
    while response == "":
        response = raw_input(question)

    return response

def verify_provided_inputs(from_dir, to_dir, filename_prefix, starting_sequence, seq_num_digits):

    if not path.isdir(from_dir):
        print "Directory {} does not exist.".format(from_dir)
        return False

    if not path.isdir(to_dir):
        print "Directory {} does not exist.".format(to_dir)
        return False
    
    try:
        int(starting_sequence)
    except ValueError:
        print "Starting sequence number must be an Integer."
        return False

    try:
        seq_num_digits = int(seq_num_digits)
        if seq_num_digits < 1 or seq_num_digits > 10:
            print "Number digits for the sequence number must be an Integer must be between 1 to 10."
    except ValueError:
        print "Number digits for the sequence number must be an Integer."
        return False

    return True

if __name__ == '__main__':
    from_dir = ask_for_input("Enter directory that you want to rename the files.\n")
    to_dir = ask_for_input("Enter directory where you want to move the files to.\n")
    filename_prefix = ask_for_input("Specify new filename prefix.\n")
    starting_sequence = ask_for_input("Specify starting sequence number.\n")
    seq_num_digits = ask_for_input("Number of digits for the sequence number between (1 to 10).\n")

    isResponsesValid = verify_provided_inputs(from_dir, to_dir, filename_prefix, starting_sequence, seq_num_digits)
