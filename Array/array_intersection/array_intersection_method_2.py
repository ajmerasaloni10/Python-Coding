
# assumption1: all elements are integer
# assumption2: all elements in both the arrays are unique 
# assumption3: if any of the list is empty return NONE 


import logging
import sys,pdb
LOGGER = logging.getLogger(__name__)

def get_dictionary(list1):
	pdb.Pdb(stdout=sys.__stdout__).set_trace()
	list1_dict = {}
	for num in list1: 
		try:
			if not list1_dict[num]:
				list1_dict[num] = True
		except: 
			LOGGER.debug("elemnt already present in the list1_dict")
	return list1_dict


def get_intersection(nums1, nums2):
	pdb.Pdb(stdout=sys.__stdout__).set_trace()
	nums3 = []
	if len(nums1) == 0 or len(nums2) == 0:
		return False


	list1_dict = get_dictionary(nums1)
	for num in nums2:
		try:
			if list1_dict[num]:
				nums3.append(num)

		except KeyError:
			LOGGER.debug("element does not exist in list1_dict {}".format(num))

	return nums3



def main():
	nums1 = [1, 2, 3, 4]
	nums2 = [1, 2]

	nums3 = get_intersection(nums1, nums2)
	print nums3

if __name__ == "__main__" : main()