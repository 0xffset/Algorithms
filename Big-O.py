
#!/usr/bin/env python
#Question: Given the following code fragment, what is its Big-O running time? ❓
"""
1. O(n)
2. O(n**2) ✔️
3. O(log n)
4. O(n**3)

"""
""" Review  📝
	We have one for insede in that other(nested for loops). So that means
	for each loop in the first for loop, we'll have the range of n.
"""
def question(n):
	test = 0 # Initial value 
	for i in range(n): # run for the range n. e.g is n=5, the loop will run 1,2,3,4,5 
		for j in range(n):
			print(i, '', j)
			test = test + i *j
	return test
