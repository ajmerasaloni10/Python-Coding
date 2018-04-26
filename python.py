# print the duplicate character from a string 


string = 'abcab'

count = { } #creates a dictionary with name count 

for char in string:
	if char not in count.keys():
		count[char] = 1
	else:
		count[char] = count[char] + 1

for key in count:
	if count[key]>1:
		print key, count[key]



	


