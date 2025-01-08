#-------------------- Python Variables

# In programming, a variable is a container (storage area) to hold data. For example,

# number = 10
# Here, number is a variable storing the value 10.

# variable cannot start with number
# no special char only underscore
# minimum length 
# meaningfull



# ------------Changing the Value of a Variable in Python
# site_name = 'programiz.pro'
# print(site_name)                                  o/p = programiz.pro

# # assigning a new value to site_name
# site_name = 'apple.com'

# print(site_name)                                      output = apple.com




              # DATA TYPES--------

# NUMERIC____
#  int = 22,-46756, 3, 46576867
# float = 4565.768, 5.7
# complex =10+aj, 6j

# SEQUENCE
# list = ["dd", "maths", "sci"]  ___mutable
# tuple = ("abs", 2, 3.14, "hello")    _____ immutable

# set = {"me", 4, 6}     duplicates are not allowed---------mutable
# frozenset = frozenset({2,5,8,7}) ---------immutable

# bytes
# bytearray
# range = range(1,20)


# MAPPING 
# dict{"NAME" : "shreya", "branch" : "IT", "AGE" : 23}

# BOOLEAN
# bool = true, false



# ----------------data types--------------

# mutable =      list ,dict, set, bytearray
# immutable =    int, float, complex, str, tuple, bool, frozenset, bytes


#literals = literals are the fixed values (raw values) used to represent data directly
#string literals, collection literals, numeric literals, boolean literals



# a = 10
# b = 10
# print (a + b)
# # print (a*b)
# print (a-b)
# # print (a/b)
#  a=10
# >>> a
# 10
# # >>> b=10
# # >>> b
# 10
# >>> a+b
# 20
# >>> a*b
# 100
# >>> a/b
# 1.0
# >>> a= a
# >>> type(a)
# <class 'int'>
# >>> a = 10
# >>> type(a)
# <class 'int'>
# a = 10
# print(type(a))
# >>> a = 10+2j
# >>> type(a)
# <class 'complex'>
# >>> type(a)
# <class 'complex'>
# >>> a= 237.56
# >>> a= 237.56
# >>> type(a)
# <class 'float'>
# >>> a= ["a", "dd", "3465"]
# >>> type(a)
# <class 'list'>
# >>> a = 'h'
# >>> type(a)
# <class 'str'>
# >>>   A = true
#   File "<stdin>", line 1
#     A = true
# IndentationError: unexpected indent
# >>> type(a)
# <class 'str'>
# >>> a= true
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'true' is not defined. Did you mean: 'True'?
# >>> a = true
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'true' is not defined. Did you mean: 'True'?
# >>> a = True
# >>> type(a)
# <class 'bool'>
# >>> a = [10, "10", "aaa"]
# >>> type(a)
# <class 'list'>
# >>> a = ["shreya", "anjali", 'renu']
# >>> type(a)
# <class 'list'>
# >>> a = ("a", "aa", "master")
# >>> type(a)
# <class 'tuple'>
# >>> a = {1, 2, "parrot"}
# >>> type(a)
# <class 'set'>
# >>> a = frozenset({parrot, peacock})
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'parrot' is not defined
# >>> type(a)
# <class 'set'>
# >>> a = {"name" : "shree", "branch" : "it", "clg" : "prmit&r"}
# >>> type(a)
# <class 'dict'>
# >>> a = none
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'none' is not defined. Did you mean: 'None'?
# >>> range(1,20)
# range(1, 20)
# >>> a = range(1,20)
# >>> type(a)
# <class 'range'>
# >>>

# a = 10
# print(type(a))
# print(float(a))
