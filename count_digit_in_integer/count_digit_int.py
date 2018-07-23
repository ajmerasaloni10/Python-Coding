# problem : count digits in a integer. 

## assumptions 
'''
1. if an integer is 0 return 1 
2. if an integer is empty return null
'''

def get_count_int(number):
	count = 0

	if number == 0:  
		return 1

	if number < 1: # handles negative number
		number = abs(number)

	while number > 0:
		number = number / 10
		count = count + 1
	return count 

number1 = 1234567
number2 = -12334
number3 = 1
number4 = 0
number5 =10000

print get_count_int(number1)
print get_count_int(number2)
print get_count_int(number3)
print get_count_int(number4)
print get_count_int(number5)