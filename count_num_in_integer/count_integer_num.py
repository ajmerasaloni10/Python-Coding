


def get_count_int(number):
	count = 0
	if number == 0:
		return 1
	while number > 0:
		number = number / 10
		count = count + 1
	return count 

number1 = 1234567
number2 = -12334
number3 = 1
number4 = 0
print get_count_int(number1)
print get_count_int(abs(number2))
print get_count_int(abs(number3))
print get_count_int(abs(number4))
