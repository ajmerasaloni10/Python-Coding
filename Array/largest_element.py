

def get_largest(elements):

	largest = elements[0] 
	smallest = element[1]
	for element in elements: 
		if element > largest:
			largest = element
		

	return largest
`
elements = [1, 3 ,5 ,7, 2 ,4]
print get_largest(elements)