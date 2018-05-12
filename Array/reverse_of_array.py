
def reverse_array(array):
	"""
	to reverse the given character array
	:param array: given array to be reversed 
	:param start: starting pointer
	:param end: ending pointer
	"""
	array_length = len(array)
	if array_length < 2 : # if array length is 0 or 1, return array
		return array
    
	start = 0
	end = array_length - 1
	for char in array:
		temp = array[start]  # store the start element in the temp  variable 
		array[start] = array[end]   # end element replaced to start 
		array[end] = temp  # temp element to end position 
		start =+1
		end =-1 
		if start > end: 
			return array


array = [1,2,3]
print reverse_array(array)


"""
    corner casese:
    1.what if array is empty?
    2.what if array has only one element
"""
