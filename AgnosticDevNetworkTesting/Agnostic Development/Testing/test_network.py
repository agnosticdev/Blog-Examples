#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Usage:
#  $ ./test_network.py urls
#  $ ./test_network.py < urls
#
# Import needed stdlib and other dependencies
#
from __future__ import print_function
import os, sys, time, subprocess

def cutOutNextOccurrenceOfString(std, needle, endKeyWord):
    v = std.find(needle)
    if v != -1:
        rtn_str = ""
        let = (v + 1000)
        while v < len:
            char = std[v]
            if char is endKeyWord[0]:
                next_char = endKeyWord[1]
                next_next_char = endKeyWord[2]
                next_std = std[(v+1)]
                next_next_std = std[(v+2)]
                # Consider a three char match good enough
                if next_std is next_char and next_next_std is next_next_char:
                    break
            rtn_str += char
            v += 1
        std = std[v:]
        return (1, std, rtn_str)
    else:
        return (-1, std, "")

# Main function
def main():
    # Create some local variables
    file_input_name = ""  # Input name for the file being passed in by the command line
    complete_content = "" # The string contents of the file
    file_lines = [] # A list of lines that the complete_content will be exploded to
    file_input_stdin = None # File from stdin, i.e., < input.txt
    
    print("----------------- Starting Program -----------------")
    # ---------------- Parse the command line input ----------------
    
    # Use sys.argv or sys.stdin to get the file input from the command line
    if len(sys.argv) > 1 and sys.argv[1] is not None:
        # Recognize that sys.argv has a file argument in it
        file_input_name = sys.argv[1]
    elif not sys.stdin.isatty():
        # isatty() makes sure stdin has data http://man7.org/linux/man-pages/man3/isatty.3.html
        # Recognize that there is a file object in sys.stdin
        file_input_stdin = sys.stdin
    else:
        # Write the raised error
        error_raised = "OOPs! It seems that there was an issue locating your input file"
        # Display the error to the console
        print(error_raised)
        exit("Please provide a valid filename or file as a command line input argument")
    
    
    # Check whether the file_input_name from sys.argv is actually a valid file
    if file_input_stdin is None:
        if not os.path.isfile(file_input_name):
            # Write the raised error
            # Display the error to the console
            print("OOPs! It seems there was an issue locating your filename")
            exit("Please provide a valid filename")

        # ---------------- Attempt to open the file ----------------

        # Open file, read contents into a list to be parsed
        try:
            # Open the file and read the contents into a
            if file_input_stdin is None:
                with open(file_input_name, 'r') as file:
                    complete_content = file.read()
            else:
                complete_content = file_input_stdin.read()

            # Explode or split the string contents to a list
            file_lines = complete_content.split("\n")

        except ValueError:
            # Write the raised error
            error_raised = "Unexpected error loading file: " + str(sys.exc_info()[0])
            # Display the error to the console
            print(error_raised)
            exit("This program needs an input file to continue. Exiting...")

        # ---------------- Parse the file ----------------
        urls = ""
        i = 0
        url_list = []
        log = ""

        for url in file_lines:
            i += 1
            print(url)
            urls += url + ","

            if i % 2 == 0:
                if urls.endswith(","):
                    urls = urls[:-1]

                test_command = "xcodebuild \
                                -project '../Agnostic Development.xcodeproj' \
                                -scheme AgnosticDevelopmentLatencyTest \
                                -destination 'platform=iOS,name=Matts iPhone 7+' \
                                URL_ARGS=" + urls +" \
                                clean test"

                print("Working...")
                stdout_response = subprocess.check_output(test_command,stderr=subprocess.STDOUT,shell=True)
                flag = 1
                while flag is 1:
                    tuple = cutOutNextOccurrenceOfString(stdout_response, "SUCCESS", "|DONE|")
                    flag = tuple[0]
                    stdout_response = tuple[1]
                    log += tuple[2] + "\n"

                urls = ""
        print(log)
        print("----------------- Ending Program -----------------")
        exit()
    else:
        # Write the raised error
        error_raised = "OOPs! It seems that there was an issue locating your input file"

# Execute the main function
if __name__ == '__main__':
    main()
