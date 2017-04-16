#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
from functools import partial

class Employee():

	def __init__(self):
		self.__employee_name = ""
		self.__employee_number = -1

	def set_employee_name(self, name):
		if len(name) > 0:
			self.__employee_name = name
			return True
		else:
			return False

	def get_employee_name(self):
		return self.__employee_name

	def set_employee_number(self, number):
		if self.validate_numeric(number):
			self.__employee_number = number
			return True
		else:
			return False

	def get_employee_number(self):
		return self.__employee_number

	def validate_numeric(self, num):
		if len(num) == 0:
			return False
		try:
			x = int(num)
			if x < 1:
				return False
			return True
		except ValueError:
			return False


def main():
	employee = Employee()
	instructions = [
		"Please enter an employee name: ",
		"Please enter an employee number: "
	]
	func_references = {
		0: partial(employee.set_employee_name),
		1: partial(employee.set_employee_number)
	}
	index = 0

	# Process user input
	while index < len(instructions):
		# Support for Python 3
		if sys.version_info.major > 2:
			# Value comes off standard output as a string
			input_value = input(instructions[index])
			flag = func_references[index](input_value)
			if flag:
				index += 1
			else:
				print("Not a valid input, please try again.")
				print("------------Starting Over-----------------")
		# Support for Python 2
		else:
			# Value comes off standard output as a string
			input_value = raw_input(instructions[index])
			flag = func_references[index](input_value)
			if flag:
				index += 1
			else:
				print("Not a valid input, please try again.")
				print("------------Starting Over-----------------")

	print("------------ Employee ---------------")
	print("Employee name: " + employee.get_employee_name())
	print("Employee number: " + employee.get_employee_number())
	exit("Goodbye!")


# Execute the main function
if __name__ == '__main__':
    main()
