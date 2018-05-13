#Problem: Implement an algorithm to determine if a string has all unique characters.

"""constraints : 
1.  Can we assume string is ASCII?  yes
2. 	Can we assume this is case sensitive ? no
3. can we use additional data structures  ? yes
4. can we assume this fits in memory ? yes
"""
def _is_unique_string(given_string):
	""" To detrmine if a given string has unqiue character or not
	
	:param given_string: 
	"""

	unique_char_count = {}
	if given_string == '':
		return 'String is empty'

	for char in given_string:

		if char in unique_char_count.keys():
			return False
		else: 
			unique_char_count[char] = 1

	return True

given_strings = {
	'',
	'saloni',
	'aaaaaa',
	'abcabc',
	'a'
}

for given_string in given_strings:
	print "{0} is {1}".format(given_string, _is_unique_string(given_string))
