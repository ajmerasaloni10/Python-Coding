# objective : How to Print duplicate characters from String which has only one repating character?

"""ASSUMPTION 
1. String has only one repeating character. 
2. other data strcuture is allowed to use. 
"""
""" EDGE CASESE: 

1. case sensitivity - no 
2. Empty String 
3. one chacter in a string. 
4. no repeating character in a  string. 
"""

def get_repeating_character(given_string):
	""" find the repeating characer from the give_string

	:param given_string: a string for which repating characer has to be found.
	"""
	if len(given_string)<2:
		return 
	repeat_char = {}

	for char in given_string:
		char = char.lower()
		try:
			if repeat_char[char]: 
				return "{0} is a repating character in the string {1}".format(char, given_string)
				break
		except KeyError:
			repeat_char[char] = 1 

	return 'no rpeating character in the string'

given_string1 = 'java'    #expected a 
given_string2 = ''				
given_string3 = 'a'
given_string4 = 'Prany godha '  #expected a
given_string5 = 'PlazZa'

print get_repeating_character(given_string1)
print get_repeating_character(given_string2)
print get_repeating_character(given_string3)
print get_repeating_character(given_string4)
print get_repeating_character(given_string5)