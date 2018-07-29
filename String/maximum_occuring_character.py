# Assumptions : 
"""
1. if the given string is empty return null 
2. if the given string has only one char return the char itself 
"""



def get_most_repeating_char(given_string):
	""" returns the most repeating character 
	@param: given_string: input string 
	"""
	count_dict = {}
	for char in given_string: 

		if len(given_string) ==0:
			return 'None'

		try: 
			if count_dict[char]: 
				count_dict[char] += 1

		except KeyError: 
			count_dict[char] = 1

	sorted_dict = sorted(count_dict.items(), reverse=False)
	return sorted_dict[0][0]


def main(): 
	given_string = 's'
	print get_most_repeating_char(given_string)


if __name__ == "__main__": main()