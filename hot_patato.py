from Queue import *
import random
def hot_patato(name_list, num):
	sim_queue = Queue()
	for name in name_list:
		ran_num = random.randrange(0, len(name_list))
		sim_queue.enqueue(name_list[ran_num])
	while sim_queue.size() > 1 and not sim_queue.is_empty():
		for x in range(num):
			sim_queue.enqueue(sim_queue.dequeue())

		sim_queue.dequeue()
	return sim_queue.dequeue()
 