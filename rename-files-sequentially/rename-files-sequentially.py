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


def verify_provided_inputs(source_dir, dest_dir, filename_prefix, starting_sequence, seq_num_digits):

    if not path.isdir(source_dir):
        print "Source directory {} does not exist.".format(source_dir)
        return False

    if not path.isdir(dest_dir):
        print "Destination directory {} does not exist.".format(dest_dir)
        return False
    
    try:
        starting_sequence = int(starting_sequence)
        if starting_sequence < 0:
            print "Starting sequence number must be greater than 0."
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


def rename_and_move_file(source_dir, dest_dir, filename_prefix, starting_sequence, seq_num_digits):

    for filename in sorted(os.listdir(source_dir)):
        file_extension = get_file_extension(filename)
        source_file = source_dir + filename
        destination_file = dest_dir + filename_prefix + get_sequence_value(starting_sequence, seq_num_digits) + "." + file_extension
        starting_sequence += 1
        os.rename(source_file, destination_file)


def get_file_extension(filename):
    return filename.split(".")[-1]


def get_sequence_value(sequence, num_of_seq_digits):
    seq_str = str(sequence)

    while len(seq_str) < num_of_seq_digits:
        seq_str = "0" + seq_str

    return seq_str


if __name__ == '__main__':
    source_dir = ask_for_input("Enter source directory.\n")
    dest_dir = ask_for_input("Enter destination directory.\n")
    filename_prefix = ask_for_input("Specify new filename prefix.\n")
    starting_sequence = ask_for_input("Specify starting sequence number.\n")
    seq_num_digits = ask_for_input("Number of digits for the sequence number between (1 to 10).\n")

    print "--------------------------------------------------------"
    isResponsesValid = verify_provided_inputs(source_dir, dest_dir, filename_prefix, starting_sequence, seq_num_digits)
    if isResponsesValid:
        print "Input verification...PASSED"
        print "--------------------------------------------------------\n"

        starting_sequence = int(starting_sequence)
        seq_num_digits = int(seq_num_digits)
        if not source_dir.endswith("/"):
            source_dir += "/"
        if not dest_dir.endswith("/"):
            dest_dir += "/"


        print "--------------------------------------------------------"
        print "Renaming and moving files..."
        rename_and_move_file(source_dir, dest_dir, filename_prefix, starting_sequence, seq_num_digits)
        print "Rename and move files...COMPLETE"
        print "--------------------------------------------------------\n"

    else:
        print "Input verification...FAILED"
        print "--------------------------------------------------------\n"
