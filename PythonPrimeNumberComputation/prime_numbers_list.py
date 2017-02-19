#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Support:
#  This program supports Python 2.7 -> Python 3.5
#  This program was design to run on a *nix system
#  This program was tested with a virtualenv for 2.7 and 3.5
#
# Overview:
#  The purpose of this program is to write a program that display prime
#  numbers from 1 to 100
#
import os, sys

# Find a prime number
def is_prime(num):
	i = 0
	for e in range(1, (num + 1)):
		if num % e == 0:
			i += 1

		if i > 2:
			return False

	return True

	

# Main definition 
def main():
	primes = []
	for i in range(1, 100):
		# Add some common filters to reduce time complexity
		if i > 2 and i % 2 == 0:
			continue
		if i > 3 and i % 3 == 0:
			continue
		if i > 5 and i % 5 == 0:
			continue
		if i > 7 and i % 7 == 0:
			continue
		if i % 9 == 0:
			continue

		# If we have made is it this far, by the laws of multiples
		# we know that we do not have to go through the expensive
		# routine of checking if the number is prime or not
		# As the iterator grows the time complexity of checking if the number
		# is prime or not grows with it.
		primes.append(i)

		# Uncomment here to use the is_prime method
		#if is_prime(i):
		#	primes.append(i)


	# Display prime numbers
	for i in primes:
		print("Prime: " + str(i))
	exit("Goodbye!")



# Execute the main function
if __name__ == '__main__':
    main()
