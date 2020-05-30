import math

def pascal_triangle(cant):
	for i in range(0, cant):
		for j in range(0, i+1):
			print(binomial_coefficiente(i, j), "", end="")
		print()

def binomial_coefficiente(a,b):
	numerator = math.factorial(a)
	denumerador = math.factorial(b) * math.factorial(a - b)
	return numerator // denumerador
pascal_triangle(5)