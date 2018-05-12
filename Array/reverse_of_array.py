
def reverse_array(array):
	"""
	to reverse the given character array
	:param array: given array to be reversed 
	:param start: starting pointer
	:param end: ending pointer
	"""
    start = 0
    end = len(array)-1
	for char in array:
		temp = array[start]  # store the start element in the temp  variable 
		array[start] = array[end]   # end element replaced to start 
		array[end] = temp  # temp element to end position 
		start = start + 1
		end = end -1 
		if start > end: 
			return array


array = ['a', 'b', 'c', 'd']
print reverse_array(array)
