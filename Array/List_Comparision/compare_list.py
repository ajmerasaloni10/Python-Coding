#Objective : To compare two give list 

# assumptions : 
"""
1. if both the list or one of the list is empty, return 'cant compare empty list'
"""


def get_dict(itemlist):
	list_dict = {}
	
	for item in itemlist: 
		try: 
			if list_dict[item]:
				list_dict[item] += 1 
		except: 
			list_dict[item] = 1 

	return list_dict

def comapre_list(list_1, list_2):
	list_1_dict = get_dict(list_1)
	list_2_dict = get_dict(list_2)
	
	if len(list_1)!= len(list_2):
		return False

	else:

		for key in list_1_dict:

			try: 
				if list_2_dict[key]:
					if list_1_dict[key] != list_2_dict[key]: 
						return False
			except: 
				return False

		return True

def main():
	list_1 = ['a', 'b', 'c', 'd', 'c', 'd', 'a', 'b', 1, 2, 4 ,2]
 	list_2 = ['a', 'b', 'c', 'd', 'c', 'd', 'a', 'b', 1, 2, 4, 6]
 	result = comapre_list(list_1, list_2)
 	print result

if __name__ == "__main__": 
	main()