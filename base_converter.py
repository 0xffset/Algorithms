#!/usr/bin/env python
from Stack import *


"""Questions: What is the value of 25 expressed as an octal number? ❓       #31
			  What is the value of 256 expressed as a hexidecimal number? ❓ #100
			  What is the value of 26 expressed in base 26? ❓"""            # 10


def base_converter(dec_number, base):
	digits = "0123456789ABCDEF"
	call_stack = Stack()
	while dec_number > 0:
		rem = dec_number % base
		call_stack.push(rem)
		dec_number = dec_number // base
	
	asnwer = ""
	while not call_stack.is_emptly():
		asnwer = asnwer + digits[call_stack.pop()]
	return asnwer

print(base_converter(25, 25))

