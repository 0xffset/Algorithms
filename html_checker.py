from Stack import *

def html_checker(html):
	
	rem_stack = Stack()
	
	list_arr =  html.split()

	letters = "abcdefghijklmnñopqrstuvwxyz"
	numbers = "0123456798"
	
	for x in  list_arr:
		if x == "<html>":
			rem_stack.push(x)
		elif x == "<head>":
			rem_stack.push(x)
		elif x == "<title>":
			rem_stack.push(x)
		elif x == "<body>":
			rem_stack.push(x)
		elif x == "</body>":
			rem_stack.push(x)
		elif x == "</title>":
			rem_stack.push(x)
		elif x == "</head>":
			rem_stack.push(x)
		elif x == "</html>":
			rem_stack.push(x)

	return is_valid_html(rem_stack.get_list())

def is_valid_html(list_lebels):
	for i in range(len(list_lebels)):
		if "<html>" in list_lebels and "</html>" in list_lebels and "<body>" in list_lebels and "</body>" in list_lebels and "<head>" in list_lebels and "</head>" in list_lebels and "<title>" in list_lebels and "</title>" in list_lebels:
			print("The HTML is valid.")
			return True
		else:
			print("The html does not valid.")
			return False

html = "<html> <head> <title> Page Title </title> </head> <body> <h1> My First Heading </h1> <p> My first paragraph. </p> </body> </html>"
print(html_checker(html))

	