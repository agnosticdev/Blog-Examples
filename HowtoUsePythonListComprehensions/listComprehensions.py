#!/usr/bin/env python
# -*- coding: utf-8 -*-


# List comprehension take's the form of 
# [ (output) (for loop(s)) (condition)]


def print_list(list_arg, label):
	for n in list_arg:
		print(label + ": " +str(n))

##################### Example One #####################

# Example One
# Example one square's a list of numbers by hand

print("------------------By Hand------------------")

l = [4, 5, 6, 7, 8]
squared_list = []
for n in l:
	squared_list.append(n*n)

print_list(squared_list, "Squared Number")

print("-----------List Comprehension--------------")

# Square a list of numbers using a list comprehension
squared_list = [n * n for n in l]
print_list(squared_list, "Squared Number")

# Takes the form
# [(output) (for loop)]
# Squared Number: 16
# Squared Number: 25
# Squared Number: 36
# Squared Number: 49
# Squared Number: 64

##################### Example Two #####################

# Example Two
# Create a matrix/NumPy array by hand
# Example two includes a double for loop that creates a 2d array/list
dx = [3, 4, 5, 9]
dy = [5, 3, 2, 1]
output_matrix = []

for dx_n in dx:
	dx_row = []
	for dy_n in dy:
		dx_row.append(dx_n * dy_n)
	output_matrix.append(dx_row)

print("------------------By Hand------------------")
print(output_matrix)

print("-----------List Comprehension--------------")
output = []
output = [[dx_n * dy_n for dy_n in dy] for dx_n in dx]

print(output)

# Takes the form
# [ [(output) (for columns] | for rows )]
# [[15, 9, 6, 3], [20, 12, 8, 4], [25, 15, 10, 5], [45, 27, 18, 9]]

#################### Example Three ####################

# Example Three
# Create a list of even numbers using a list comprehension that contains a conditional

print("------------------By Hand------------------")

l = [3, 4, 5, 6, 8, 9, 11, 12, 13, 14, 15]
even_list = []
for num in l:
	if num % 2 == 0:
		even_list.append(num)

print_list(even_list, "Even Number")

print("-----------List Comprehension--------------")
even = []
even = [num for num in l if num % 2 == 0]
print_list(even, "Even Number")





