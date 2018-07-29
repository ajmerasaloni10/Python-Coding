
def get_intersection(list1, list2): 
	return list(set(list1) & set(list2))


def main():
	list1 = [1, 2, 3, 5, 5 ,5, 5, 6, 7]
	list2 = [3, 6, 6, 7, 8, 5, 5, 5]
	print get_intersection(list1, list2)


if __name__ == "__main__": main()

	