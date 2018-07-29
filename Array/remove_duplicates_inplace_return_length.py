
numbers = [1, 2, 2, 3, 4, 4, 5, 6]

start = 0 
end = 1 
length  = len(numbers)

while end < length: 
	if numbers[start] != numbers[end]:
		start = start + 1
		if start != end:
			numbers[start] = numbers[end]
		end = end + 1 

	else: 
		end = end +1 

print numbers








