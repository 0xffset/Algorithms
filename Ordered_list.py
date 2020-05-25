class Node: 
	def __init__(self, data):
		self.data = data
		self.next = None

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_data(self, new_data):
		self.data = new_data

	def set_next(self, new_next):
		self.next = new_next

	def len_nodes(self):
		return len(self.data)
	

class OrdernerList: 
	def __init__(self):
		self.head = Node

	def search(self, item):
		current = self.head

		found = False
		stop = False
		while current != None and not found and not stop:
			if current.get_data() == item:
				found = True
			else:
				if current.get_data() > item:
					stop = True
				else:
					current = current.get_next()
		return found

	def add(self, item):
		current = self.head
		previous = None
		stop = False

		while current != None and not stop:
			if current.get_data() > item:
				stop =  True
			else:
				previous = current
				current = current.get_next()

		temp = Node(item)
		if previous == None:
			temp.set_next(self.head)
			self.head = temp
			# print(self.head.get_data())
		else:
			temp.set_next(current)
			previous.set_next(temp)

	def __str___(self):
		return str(self.head.get_data())

	def slice_list(self, start, end):
		list_numbers = list(self.head.get_data())
		return list_numbers[start : end]

o = OrdernerList()
print(o.add(5))


