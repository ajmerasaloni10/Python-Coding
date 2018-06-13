# Asumptions: 

# if length of array is empty return none
# if lenght of array is one return array 


# Complexity : 


def left_rotate(given_array, n):
	""" Left rotate each element 

	given_array: input array 
	n : number of times rotation will take place
	"""

	count = 1
	arr_len = len(given_array)

	if arr_len == 0: 
		return None

	while count <= n:
		temp = given_array[0]
		for i in range(arr_len-1):
			given_array[i] = given_array[ i + 1 ] 

		given_array[arr_len-1] = temp
		count = count + 1 

	return given_array


def main():
	given_array = []
	print left_rotate(given_array, 1) 


if __name__ == "__main__": main()