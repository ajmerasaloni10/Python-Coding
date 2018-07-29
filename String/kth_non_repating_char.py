import sys,pdb

def k_non_repeating_char(given_string, k):
	"""

	"""

	count_dict = {}
	count = 0

	if len(given_string) == 0:
		return None
	for char in given_string: 
		try: 
			if count_dict[char]:
				count_dict[char] += 1

		except: 
			count_dict[char] = 1

	for char in given_string: 
		if count_dict[char] == 1:
			count += 1
			if count == k:
				return char
	return None


def main(): 
	given_string = 'abcabcabcxyzdfghk'
	print k_non_repeating_char(given_string, 7)


if __name__ == "__main__": main()