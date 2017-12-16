#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $ python main.py text_file.txt
# $ ./ main.py text_file.txt
# $ ./main.py < text_file.txt
# $ ./main.py
#
from __future__ import print_function
from file import File
import os, sys


# Main function
def main():

	# If there is a file expected from STDIN, create the file object
	# and the file object will attempt to read the contents of STDIN
	# in the constructor.
	file = File()
 
	for line in file.file_lines:
		print("Line for file: " + line)


	'''
	log_file = 'logs/log'
	complete_content = ''
	content_list = []
	try:
		with open(log_file, 'r') as file_obj:
			complete_content = file_obj.read()

	except ValueError:
		# Write the raised error
		error_raised = "Error loading file: " + str(sys.exc_info()[0])
		# Display the error to the console
		print(error_raised)
		exit("This program needs an input file to continue. Exiting...")

	# Explode or split the string contents to a list
	content_list = complete_content.split("\n")

	for line in content_list:
		print("Line for file: " + line)

	'''
	
	exit("Exiting...")

# Execution of the main function
if __name__ == "__main__":
	main()