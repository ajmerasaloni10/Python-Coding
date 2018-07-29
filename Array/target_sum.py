
def get_dict(given_array):
	index = 0
	for integer in given_array:
		index_dict[integer] = index
		index =+ 1
	return index_dict

def get_index(index_dict, target_sum):
	for key in index_dict: 
		expected_compliment = abs(target_sum - key) # assuming positive integers

		try:
			if index_dict[expected_compliment]:
				print '{0} {1}'.format(index_dict[key],index_dict[expected_compliment])
				break
		except KeyError as e:
			print "{0} not in dictionary".format(key)


index_dict = {}
given_array = [2,7,11,15] 
target_sum = 9
index_dict = get_dict(given_array)
get_index(index_dict, target_sum)
