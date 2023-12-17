#!/usr/bin/env python3

'''
Write a function print_fibonacci() that prints a list of the fibonacci sequence
up to the length provided in the function's parameters.
'''
def print_fibonacci(length):

	fib_seq = []
	if length > 0:
		fib_seq.append(0)
	if length >= 2:
		fib_seq.append(1)
		for i in range(2, length):
			fib_seq.append(fib_seq[-1] + fib_seq[-2])

	print(fib_seq)

