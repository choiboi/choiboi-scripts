# 
# This script is meant to rename all the files in the given directory by adding
# a provided prefix and end with a number that will increase sequentially.
# 


def ask_for_input(question):
    
    response = ""
    while response != "":
        response = raw_input(question)

if __name__ == '__main__':
    fromDir = ask_for_input("Entry directory that you want to rename the files.")
    toDir = ask_for_input("Enter directory where you want to move the files to.")
    filenamePrefix = ask_for_input("Specify new filename prefix.")
    startingSequenceNum = ask_for_input("Specify starting sequence number.")
    seqNumDigits = ask_for_input("How digits for the sequence number.")
    
    raw_input()