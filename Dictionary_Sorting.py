#Sorting a dictionary by key
my_dict = {
	'z': 'q',
	'b': 'r',
	'y': 'a'
}
for key in sorted(my_dict):
	print key, ':', my_dict[key]
"""
Outputs:
	b : r
	y : a
	z : q
"""

#Sort a Dictionary by Value
import operator
my_dict = {
	'z': 'q',
	'b': 'r',
	'y': 'a'
}
for key, value in sorted(my_dict.iteritems(), key=operator.itemgetter(1)):
	print key, ':', value
"""
Outputs:
	y : a
	z : q
	b : r
"""

#Sort a Dictionary by a Child List's Value
my_dict = {
	'q': [6, 'a'],
	'z': [18, 't'],
	'a': [3, 'r']
}
for key, value in sorted(my_dict.iteritems(), key=lambda kvt: kvt[1][0]):
	print key, ':', value
"""
Outputs:
	a : [3, 'r']
	q : [6, 'a']
	z : [18, 't']
"""

#Sort a Dictionary by a Child Dictionary's Value
my_dict = {
	'q': {'age': 32},
	'z': {'age': 54},
	'a': {'age': 96}
}
for key, value in sorted(my_dict.iteritems(), key=lambda kvt: kvt[1]['age']):
	print key, ':', value
"""
Outputs:
	q : {'age': 32}
	z : {'age': 54}
	a : {'age': 96}
"""

