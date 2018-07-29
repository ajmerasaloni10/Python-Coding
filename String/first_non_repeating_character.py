#Objective How to program to print first non repeated character from String


"""corner cases
1. String is empty 


"""

def create_dict(given_string):
	count_dict = {}

	for char in given_string:
		try:
			if count_dict[char]:
				count_dict[char] += 1
		except KeyError: 
			count_dict[char] = 1
			
	return count_dict


def get_first_non_repeating_char(count_dict, given_string):
	if len(count_dict) == 0:
		print 'empty'

	#pdb.Pdb(stdout=sys.__stdout__).set_trace()
	for char in given_string:
		if count_dict[char] == 1 :
			print "{0} is the first non-repeating character in string {1}".format(char, given_string)
			break


given_strings = {
	'saloni',
	'anagha',
	'aaa',
	'a',
	''
}

for given_string in given_strings:

	count_dict = create_dict(given_string)
	print get_first_non_repeating_char(count_dict,given_string)

