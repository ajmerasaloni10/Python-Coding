
import sys,pdb

def get_second_largest(elements):
	largest = None
	second_largest = None

	for element in elements:
		if largest is None:
			largest = element
		
		elif element > largest:
			second_largest = largest
			largest = element

		elif second_largest is None: 
			second_largest = element

		elif element> second_largest:
			second_largest = element

	print largest
	print second_largest


elements = [1, 2, 3, 4, 5]
get_second_largest(elements)