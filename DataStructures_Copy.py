
#Lists:
>>> colours1 = ["red", "green"]
>>> colours2 = colours1
>>> print(colours1)                   #['red', 'green']
>>> print(colours2)                   # ['red', 'green']
>>> print(id(colours1),id(colours2))  #43444416 43444416
>>> colours2 = ["rouge", "vert"]
>>> print(colours1)                   #['red', 'green']
>>> print(colours2)                   #['rouge', 'vert']
>>> print(id(colours1),id(colours2))  #43444416 43444200

#Dictionaries:

#Shallow Copy: By "shallow copying" it means the content of the dictionary is not copied by value, but just creating a new reference.
>>> a = {1: [1,2,3]}
>>> b = a.copy()
>>> a, b                              #({1: [1, 2, 3]}, {1: [1, 2, 3]})
>>> a[1].append(4)
>>> a, b                              #({1: [1, 2, 3, 4]}, {1: [1, 2, 3, 4]})

#Deep Copy: A deep copy will copy all contents by value
>>> c = copy.deepcopy(a)
>>> a, c                              #({1: [1, 2, 3, 4]}, {1: [1, 2, 3, 4]})
>>> a[1].append(5)
>>> a, c                              #({1: [1, 2, 3, 4, 5]}, {1: [1, 2, 3, 4]})

#Shallow copying, a and b will become two isolated objects, but their contents still share the same reference. 
#Deep copying, a and b's structure and content become completely isolated.
