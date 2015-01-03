#Sort a List Alphabetically
my_list = ['mango', 'apple', 'pear', 'orange']
my_list.sort()
for item in my_list:
	print item
"""
Outputs:
	apple
	mango
	orange
	pear
"""

#Return a Copy of a List, Sorted Alphabetically
my_list = ['mango', 'apple', 'pear', 'orange']
my_sorted_list = sorted(my_list)
for item in my_sorted_list:
	print item
"""
Outputs:
	apple
	mango
	orange
	pear
"""

#Sort a List in Reverse Alphabetical Order
my_list = ['mango', 'apple', 'pear', 'orange']
my_list.sort(reverse=True)
for item in my_list:
	print item
"""
Outputs:
	pear
	orange
	mango
	apple
"""

#Return a Copy of a List Sorted in Reverse Alphabetical Order
my_list = ['mango', 'apple', 'pear', 'orange']
my_sorted_list = sorted(my_list, reverse=True)
for item in my_list:
	print item
"""
Outputs:
	pear
	orange
	mango
	apple
"""

#Sort a List by a Child List's (or Tuple's) Value
import operator
my_list = [
	['z', '3'],
	['a', '2'],
	['g', '4']
]
my_list.sort(key=operator.itemgetter(0))
for item in my_list:
	print item
"""
Outputs:
	['a', '2']
	['g', '4']
	['z', '3']
"""

#Sort a List by a Child List's (or Tuple's) Value in Reverse
import operator
my_list = [
	['z', '3'],
	['a', '2'],
	['g', '4']
]
my_list.sort(reverse=True, key=operator.itemgetter(0))
for item in my_list:
	print item
"""
Outputs:
	['a', '2']
	['g', '4']
	['z', '3']
"""

