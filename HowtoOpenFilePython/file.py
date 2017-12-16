#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
from __future__ import print_function
import os, sys

class File():

	#
	# Constructor
	#
	def __init__(self):
		self.file_lines = []
		self.__file_input_name = ""
		self.__complete_content = ""
		self.__file_input_stdin = None

		# Read STDIN and the contents of the file
		self.parse_stdin()

		if self.__file_input_name is not "" or self.__file_input_stdin is not None:
			self.read_content_of_file()
		else:
			exit("Something went wrong parsing your input file.  Exiting...")

		if len(self.file_lines) == 0:
			exit("Nothing was read in to memory from the file.  Exiting...")

	#
	# Parse STDIN if any was presented when the program was run
	#
	def parse_stdin(self):
		# Use sys.argv or sys.stdin to get the file input from the command line
	    if len(sys.argv) > 1 and sys.argv[1] is not None:
	        # Recognize that sys.argv has a file argument in it
	        self.__file_input_name = sys.argv[1]
	    elif not sys.stdin.isatty():
	        # isatty() makes sure stdin has data http://man7.org/linux/man-pages/man3/isatty.3.html
	        # Recognize that there is a file object in sys.stdin
	        self.__file_input_stdin = sys.stdin
	    else:
	        # Display the error to the console
	        print("OOPs! There was an issue locating your input file")
	        exit("Please provide a valid filename or file as a CLI argument")

	#
	# The the contents of the file that was presented
	#
	def read_content_of_file(self):
        # -------- Attempt to open the file and read contents --------

        # Open file, read contents into a list to be parsed
		try:
            # Open the file and read the contents into a
			if self.__file_input_stdin is None:
				with open(self.__file_input_name, 'r') as file_obj:
					self.__complete_content = file_obj.read()
			else:
				self.__complete_content = self.__file_input_stdin.read()

			# Explode or split the string contents to a list
			self.file_lines = self.__complete_content.split("\n")

		except ValueError:
			# Write the raised error
			error_raised = "Error loading file: " + str(sys.exc_info()[0])
			# Display the error to the console
			print(error_raised)
			exit("This program needs an input file to continue. Exiting...")




