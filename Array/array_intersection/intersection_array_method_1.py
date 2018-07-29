"""Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""


def array_intersection(list1, list2): 
	"""
	:params list1: 
	:params list2: 
	"""
	list3 = []

	for num in list1:
		if num in list2: 
			list3.append(num)
	return list3

	
def main():
	nums1 = [1,2,2,1]
	nums2 = [2,2]
	intersection = array_intersection(nums1, nums2)
	print intersection


if __name__ == "__main__": main()