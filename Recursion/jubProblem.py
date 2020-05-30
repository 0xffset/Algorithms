
from collections import defaultdict

is_visited = defaultdict(lambda: False)
jub_1 = 4
jub_2 = 3
water_end = 2

def jub(w_jub_1, w_jub_2):
	if (w_jub_1 == water_end and w_jub_2 == 0) or (w_jub_2 == water_end and w_jub_1 == 0):
		print(w_jub_1, w_jub_2)
		return True

	if (is_visited[(w_jub_1, w_jub_2)]) == False:
 		print(w_jub_1, w_jub_2)

 		is_visited[(w_jub_1, w_jub_2)] == True

 		return (jub(0, w_jub_2) or jub(w_jub_1, 0) or jub(jub_1, w_jub_2) or 
 				jub(w_jub_1, jub_2) or jub(w_jub_1 + min(w_jub_2, (jub_1 + w_jub_1)), 
 				w_jub_2 - min(w_jub_2, (jub_1 - w_jub_1))) or jub(w_jub_1 + min(w_jub_1, (jub_2 + w_jub_2)), 
 				w_jub_2 - min(w_jub_1, (jub_2 - w_jub_2)))) 
 	 else:
 	 	return True

jub(0,0)

	
