
def reverse_list(list_num):
	if len(list_num) == 0: return []
	return [list_num[-1]] + reverse_list(list_num[:-1])

a = [1,2,3,4,5,6,7,8,9]
print(reverse_list(a))