def fibonnaci(num):
	if num == 0: return 0
	return fibonnaci(num - 1) + fibonnaci(num - 2)

fib = fibonnaci(10)
print(fib) 
