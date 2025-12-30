#!/usr/bin/python

#
# If you have two sets of folders with the same file naming sequence (regardless of file type). Then you
# go through the one folder and delete some files. This script will delete those files in the other set
# of files.
#
# This script assumes that it has similar prefix filename sequence. Ignores file extension types. 
#

import os
from os import path

DS_STORE_FILETYPE = '.DS_Store'


def ask_for_input(question):
    response = ""
    while response == "":
        response = raw_input(question)

    return response


def verify_directory_exists(source_dir, dest_dir):
    if not path.isdir(source_dir):
        print "Source directory {} does not exist.".format(source_dir)
        return False

    if not path.isdir(dest_dir):
        print "Destination directory {} does not exist.".format(dest_dir)
        return False
    
    return True


def get_file_list(dir):
    file_list = sorted(os.listdir(dir))

    # Filter out .DS_Store files.
    for file in file_list:
        if file.find(DS_STORE_FILETYPE) > -1:
            file_list.remove(file)

    return file_list


def get_list_of_files_to_delete(src_list, dest_list):
    # Ensure there are files in both src dir and dest dir.
    if len(dest_list) <= 0 and len(src_list) <= 0:
        return []
    
    # Get the file extension of both dest dir and src dir.
    src_file_ext = src_list[0].split(".")[-1]
    dest_file_ext = dest_list[0].split(".")[-1]
    files_to_delete = []

    # For each file in dest list, swap file extension with src extension
    # and if the file is not in src dir, then add into list to be deleted.
    for dest_file in dest_list:
        filename = dest_file.replace(dest_file_ext, src_file_ext)
        if filename not in src_list:
            files_to_delete.append(dest_file)

    return files_to_delete


def delete_files(dest_dir, files_to_delete):
    dest_dir = dest_dir + "/" if not dest_dir.endswith("/") else dest_dir
    count = 0

    for file in files_to_delete:
        filepath = dest_dir + file
        if os.path.exists(filepath):
            os.remove(filepath)
            print "Deleted %s" % (file)
            count += 1
        else:
            print "File does not exist, ignored %s" % (file)

    return count


if __name__ == '__main__':
    source_dir = ask_for_input("Main directory:\n").strip()
    dest_dir = ask_for_input("Directory to mimic main directory:\n").strip()

    print "\n--------------------------------------------------------"
    validation_result = verify_directory_exists(source_dir, dest_dir)
    if validation_result:
        print "Input verification...PASSED"
        print "--------------------------------------------------------"

        print "Checking files..."
        source_file_list = get_file_list(source_dir)
        dest_file_list = get_file_list(dest_dir)
        files_to_delete = get_list_of_files_to_delete(source_file_list, dest_file_list)
        print "DONE"
        print "--------------------------------------------------------"

        print "Deleting files in %s" % (dest_dir)
        deleted_count = delete_files(dest_dir, files_to_delete)
        print "Deleting files...COMPLETE"
        print "Deleted %s files." % (deleted_count)
        print "--------------------------------------------------------\n"
    else:
        print "Input verification...FAILED"
        print "--------------------------------------------------------\n"

