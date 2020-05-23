
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

#Question 2: Given the following code fragment, what is its Big-O running time? ❓

""" Review  📝
	In this case, whe have two for loops that does not have nesteding. 
	However, are running in the same index position. I think that it's lineal time complexity algorithm.   

"""

def question_2(n):
	test = 0
	for i in range(n):
		test = test +1
	for j in range(n):
		test = test -1
	print(i, '',j)

"""
1. O(n) ✔️
2. O(n**2) 
3. O(log n)
4. O(n**3)

"""


#Question 3: Given the following code fragment, what is its Big-O running time? ❓

""" Review  📝
	Here we have while loop. First, i  is iqual to n and while i are greater that 0
	i will be floor devided of 2. In addiction, does not exists a correlation between k and i.   
"""

def question_3(n):
	i = n
	while i > 0:
		k = 2 + 2
		i = i // 2	
		print(i)
question_3(100)
"""
1. O(n) ✔️
2. O(n**2) 
3. O(log n)
4. O(n**3)

"""