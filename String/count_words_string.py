# count words in a string 

'''
#assumptions : 
1. if string is empty return null 
'''

def get_count_string(given_string):
	count = 0

	if given_string == '':
		return 	'null'
	
	for word in given_string.split():
		count = count +1 

	return count

given_string1 = 'My name is   Saloni'
given_string2 = 'saloni'
given_string3 = ''

print get_count_string(given_string1)
print get_count_string(given_string2)
print get_count_string(given_string3)
