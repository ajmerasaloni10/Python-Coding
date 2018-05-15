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
	repeat_char = {}
	for char in given_string:
		char = char.lower()
		try:
			if repeat_char[char]: 
				return "{0} is a repating character in the string {1}".format(char, given_string)
				break
		except KeyError:
			repeat_char[char] = 1 

	return "no rpeating character in the string {0}".format(given_string)

given_string1 = 'java'    #expected a 
given_string2 = ''		  #empty string		
given_string3 = 'a'	      # one character in a string
given_string4 = 'Prany godha '  #expected a
given_string5 = 'PlazZa'		# case sensitivity
given_string6 = 'saloni' # demonstrates no repeating characer in the string 

print get_repeating_character(given_string1)
print get_repeating_character(given_string2)
print get_repeating_character(given_string3)
print get_repeating_character(given_string4)
print get_repeating_character(given_string5)
print get_repeating_character(given_string6)


"""Complexity
    Time Complexity: O(n)
    Space Complexity: O(n)
"""
