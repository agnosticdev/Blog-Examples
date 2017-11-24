#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Import needed stdlib and other dependencies
#
from __future__ import print_function
import os, sys, time, subprocess, shutil, datetime


# Iterate through files in this directory and remove all old .o files
for file_item in os.listdir('.'):
	if file_item[-2:] == '.o':
		print("Found .o file: " + file_item)
		os.remove(file_item)

# Iterate through files in this directory and compile all .c files to .o files
for file_item in os.listdir('.'):
	if file_item[-2:] == '.c':
		print("Found .c file: " + file_item)

		compile_command = "gcc -c " + file_item + " -o " + file_item[:(len(file_item) -2)] + ".o"
		os.system(compile_command)


# Iterate through files in this directory and capture them in a list
object_files = []
for file_item in os.listdir('.'):
	if file_item[-2:] == '.o':
		object_files.append(file_item)

# Iterate through files in this directory and link them together to form a binary
final_command = "gcc "
for object_file in object_files:
	final_command += object_file + " "


final_command += " -o main"

# Build the binary
os.system(final_command)


# Executes the binary
print("PROGRAM OUT: ")
os.system("./main")

