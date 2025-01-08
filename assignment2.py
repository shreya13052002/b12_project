# <<<<<<<<<<<<<<<<<<<<<<<<<    positional arguments      >>>>>>>>>>>>>>>>>>>>>>>>>>>

# 

# def greet(name):
#     print("shreya", "john")                    shreya john

# greet("name")



# 2. Adding two numbers
# def add(a,b):
#     print(a + b)                                  30

# add(10, 20)


# 3. Multiplying two numbers
# def multiply(a,b,c):
#     print(a*b*c)                                   24

# multiply(2,3,4)


# 4. Subtracting two numbers
# def subtract(a,b,c):
#     print(a-b-c)                                   30

# subtract(80,40,10)


# # 5. Displaying user details
# def user_details(name,age):
#     print(f"name : {name}, age : {age}")          # name : shreya, age : 23

# user_details("shreya", "23")

# def user_details(name,age):
#     print(f"name : {name},\n age : {age}")          # name : shreya,
#                                                     # age : 23

# user_details("shreya", "23")

# def user_details(name,age):
#     print(f"name of user: {name}, age of user: {age}")      name of user: shreya, age of user:  25 

# user_details("shreya"," 25")






# 6. Area of a rectangle
# def area(length,width):
#     print(length*width)                                66

# area(2,33)


# # 7. Dividing two numbers
# def division(a,b):
#     print(a/b)                                      4.0

# division(20,5)


# # 8. Full name
# def full_name(first,last):
#     print(f" first name is: {first} , last name is: {last}")     first name is: shreya , last name is: mahalle

# full_name("shreya" , "mahalle")


# 9. describing a Pet 
# def pet_description(name,age):
#     print(f"pet name is : {name}, pet age is: {age}")                    pet name is : buddy, pet age is: 4

# pet_description("buddy", 4)

# 10. checking if number is positive
# def check_positive(number):
#     if number > 0:
#         print("Positive")                          #Positive
#     else:
#         print("Not Positive")

# check_positive(3)


# def check_positive(number):
#     if number > 0:
#         print("Positive")                          #Not Positive
#     else:
#         print("Not Positive")

# check_positive(0)


# 11. Finding the maximum of three numbers
# def max_number(a,b,c):
#     print(max(a,b,c))                          545

# max_number(545,57,76)


# # 12. Printing a message
# def print_message(message):
#     print(message)                                  hello, i am fine

# print_message("hello, i am fine")

# 13. 15. Checking if a number is odd
# def odd_number(number):
#     if number % 2 != 0:
#         print("number is odd")                            number is odd
#     else:
#         print("number is even")

# odd_number(65)


# 14.  Converting minutes to seconds
# def convert_min_to_sec(minutes):
#     print(minutes*60)                                 180

# convert_min_to_sec(3)


# 15. convert temperature in kelvin
# def celsius_to_kelvin(celsius):
#     print(celsius + 273.15)                               298.15

# celsius_to_kelvin(25)

# ------------------------------------------------------------------------------------------------------------------------


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   keyword arguments >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def func(a=10, b=20, c=30, d=40):       coz' it is default value
#     print(a,b,c,d)                      30 20 40 10

# func(30,20,40,10)                          and it is actual value of a,b,c,d


# def func(a=10, b=20, c=30, d=40):      # coz' it is default value
#     print(a,b,c,d)                      #25,50,30,40

# func(a=25,b=50)                                  # it is keyword arg#


# # 1. Greeting a user
# def greet(name,greeting):
#     print(f"{greeting}, {name}")                hello,good morning, shreya

# greet(name="shreya", greeting="hello,good morning")


# # 2. adding two numbers
# def add(a=10,b=20):
#     print(a+b)                8

# add(a=5,b=3)


# 3. Displaying user details
# def user_details(name="shreya",age="23"):
#     print(f"name: {name}, age :{age}")                  name: shreya, age :22

# user_details(name="shreya",age = "22")


# 4. Area of a rectangle
# def area(length=22,width=11):
#     print(length*width)                     # 10

# area(length=5,width=2)

# def area(length=22,width=11):
#     print(length*width)                     # 242

# area(length=22,width=11)


# # 5. Full name
# def full_name(firstname="shreya", lastname="mahalle"):
#     print(f" {firstname},{lastname}")               #  shru,mahalle

# full_name(firstname="shru", lastname="mahalle")


# 6. Describing a pet
# def description(name="moti",animal="dog"):
#     print(f"{name} {animal}")                 #  moti dog

# description(name="moti",animal="dog")

# def description(name,animal):
#     print(f"{name} {animal}")                 #  moti dog

# description(name="moti",animal="dog")



# 8. Checking divisibility
# def check_divisibility(a,b):
#     if a % b == 0:
#         print("divisible")                        divisible
#     else:
#         print("not divisible")

# check_divisibility(a = 15, b = 3)



# # 9. Printing favorite hobby
# def fav_hobby(name="shreya", hobby="travelling"):
#     print(f"{name},{hobby}")                         name=john,hobby=travelling

# fav_hobby("name=john","hobby=travelling")


# 10. Calculating speed
# def speed(distance,time):
#     print(distance/time)       50.0

# speed(distance=100,time=2)


# 11. Checking if a number is positive or negative
# def check_number(number):
#     if number >= 0:
#         print("positive")                   positive
#     else:
#          print("positive") 

# check_number(number = 6676767)


# 12. Finding the maximum of three numbers
# a = int(input("enter a number: "))
# b = int(input("enter a number: "))
# c = int(input("enter a number: "))

# def max_number(a,b,c):
#     print(max(a,b,c))                      #30

# max_number(a=10,b=20,c=30)


# 13. cube of number
# def cube(number):
#     print(number**3)                64

# cube(4)

# 14. finding square root 
# def square_root(number):
#     print(number ** 0.5)                       4.0

# square_root(number=16)



# 15. Converting hours to minutes
# def hours_to_min(hours):
#     print(hours*60)                     120

# hours_to_min(2)


# ---------------------------------------------------------------------------------------------------------------------------



# <<<<<<<<<<<<<<<<<<<<<<<<<<     default argument    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

#1. def greet(name="Guest"):
#     print(f"Hello, {name}!")             #Hello, mehmaan!

# greet(name="mehmaan")


# def greet(name="Guest"):
#     print(f"Hello, {name}!")             #Hello, Guest!

# greet()

# def func(a,b,c):
#     print(a,b,c)                       # 10 20 30

# func(10,20,30)

# def func(a,b,c=100):
#     print(a,b,c)                       # 10 20 100

# func(10,20)

# def func(a,b,c=100):
#     print(a,b,c)                       # 10 20 30

# func(10,20,30)


# 3.  Adding two numbers
# def add(a,b=30):
#     print(a+b)                            # 40

# add(10)

# def add(a=0,b=0):
#     print(a+b)                            # 0

# add()



# 4. Calculating the area of a rectangle
# def area(length=10,width=20):
#     print(length*width)                               30

# area(5,6)


# # 5. Displaying a student's grade
# def student_grade(name,marks):
#     print(f"name: {name},marks: maths{marks}, science{marks}")         name: shreya,marks: maths20, science20

# student_grade(name="shreya",marks= 20)


# 6. Printing a welcome message
# def print_msg(msg="python is fun"):
#     print(msg)                           #python is fun

# print_msg()


# def print_msg(msg="python is fun"):
#     print(msg)                           #hello,python

# print_msg("hello,python")


# 7. Calculating the power of a number
# def power_of_no(num):
#     print(num**2)                            25

# power_of_no(5)


# 8. Multiplying numbers
# def multiply(a=1,b=3,c=2):
#     print(a*b*c)              #6

# multiply()

# def multiply(a=1,b=3,c=2):
#     print(a*b*c)              #16

# multiply(a=4,b= 2)

#9. Calculating the square of a number
# def square(num=6):
#     print(num**2)                      36

# square()


# 10. 
# def func(base=5,exponent=3):
#         print(base**exponent)         125

# func()

# 11. Displaying a price with product
# def display(product="mobile", price=440000):
#     print(f"{product}, {price}")                laptop, 440000   

# display(product="laptop")



# #12. Checking if a person is an adult
# def check(age=18):
#     if age < 18:
#         print("teenager")
#     else:
#         print("adult")                         # adult

# check()
    
# def check(age=18):
#     if age < 18:
#         print("teenager")
#     else:
#         print("adult")                         # teenager

# check(age = 17)


#13. 
# def odd_or_even(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")                       #   odd

# odd_or_even(num=55)

# def odd_or_even(num=23):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")                       #   even

# odd_or_even(num=44)

#14.Printing a default list
# def default_lst(lst=[10,20,30]):
#     print(lst)                               # [1, 2, 3]

# default_lst([1,2,3])


# def default_lst(lst=[10,20,30]):
#     print(lst)                               # [10, 20, 30]

# default_lst()



#15.  Repeating a string

# def repeat_string(string="Python", times=3):
#     print(string * times )                     #  shreyashreyashreya

# repeat_string("shreya")



# def repeat_string(string="Python", times=3):
#     print(string * times )                     #  PythonPythonPython

# repeat_string()

#16. reverse a str
# def reversed_str(str="python"):
#     print(str[::-1])                          #  nohtyp

# reversed_str()

# def reversed_str(str="python", times=3):
#     print(str[::-1]*times, str.expandtabs==4)                          #  nohtypnohtypnohtyp False

# reversed_str()

# def reversed_str(str="python", times=3):
#     print(str[::-1]*times)                          #  nohtypnohtypnohtyp 

# reversed_str()



# ------------------------------------------------------------------------------------------------------------




# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   variable length arguments   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def func(a,b,c,*args):
#     print("positional argument: ", a,b,c)                     positional argument:  10 20 30
#     print("variable length argument: ",*args)                 variable length argument:  40 50 python

# func(10,20,30,40,50,"python")


# 1. Summing numbers using *args
# def sum_number(*args):
#     print(sum(args))                            14

# sum_number(2,3,4,5)


# 2. Finding the maximum number
# def maximum_number(*args):
#     print(max(args))                               5453

# maximum_number(22,435,5453,76,32)


# # 3. Joining strings
# def concatenation(*args):
#     print(" ".join(args))                             python is language

# concatenation("python", "is", "language")


# 4. Printing all arguments
# def print_arguments(*args):
#     for arg in args:
#         print(arg,end=" ")                                 1 Python 3.14 True 

# print_arguments(1, "Python", 3.14, True)

# 5. Finding the length of arguments
# def count_arguments(*args):
#     print(len(args))                                      5

# count_arguments(1, 2, 3, "Python", True)


# 6.  Checking even numbers
# def even_or_odd(*args):
#     for num in args:
#         if num % 2 == 0:
#             print(f"even: {num}",end=" ")                      #odd: 3 even: 4 odd: 7 even: 10 
#         else:
#             print(f"odd: {num}",end=" ")

# even_or_odd(3, 4, 7, 10)


# # 7.display students score
# def student_grades(name,*score):
#     print(f"name: {name}, score: {score}")                     name: shyam, score: (98, 78, 88, 79, 99)

# student_grades("shyam", 98,78,88,79,99)


# 8. Concatenating numbers
# def concatenate_number(*args):
#     print(" ".join(map(str, args)))                     1 2 3 4

# concatenate_number(1,2,3,4)



# 10. Checking divisibility
# def check_divisibility(*args):
#     for num in args:
#         if args % 5 == 0:
#             print(f"{num} is divisible")
#         else:
#             print(f"{num} is not divisible")

# check_divisibility(22,435,556,768,76)

# output =
# 22 is not divisible
# 435 is divisible
# 556 is not divisible
# 768 is not divisible
# 76 is not divisible


# 11. Displaying shopping list
# def display_lst(*args):
#     print("shopping list: ")
#     for arg in args:
#         print(arg)

# display_lst("apple","comb","table", "cover")

# shopping list: 
# ['apple', 'comb', 'table', 'cover']

# def display_lst(*args):
#     # print("shopping list: ")
#     # for arg in args:
#         print(args, end=" ")                    ('apple', 'comb', 'table', 'cover') 

# display_lst("apple","comb","table", "cover")

# def display_lst(*args):
#     print("shopping list: ")
#     for arg in args:
#         print(arg, end=" ")

# display_lst("apple","comb","table", "cover")

# shopping list: 
# apple comb table cover


# # 12. Sorting arguments
# def sorted_arguments(*args):
#     print(sorted(args))                                 [2, 3, 5, 6, 8, 9, 11]

# sorted_arguments(5,6, 3, 2 ,8, 9,11)


# # 13. Finding unique values
# def unique_arg(*args):
#     print(set(args))                                       {1, 2, 3, 4, 5, 6}

# unique_arg(1,1,1,3,4,2,3,3,4,2,5,6)


# 15. Printing names with greetings
# def greet(*names):
#     for name in names:
#         print(f"hello, {name}")

# greet("alice", "shreya")

# ello, alice
# hello, shreya

# 16. Checking positive numbers
# def check_numbers(*args):
#     for num in args:
#         if num >= 0:
#             print(f"{num} is positive")
#         else:
#             print(f"{num} is negative")

# check_numbers(-56,0,676,-5,32)

# 0 is positive
# 676 is positive
# -5 is negative
# 32 is positive

# 17. Sorting arguments in reverse
# def sort_reverse(*args):
#     print(sorted(args, reverse=True))                 [4, 3, 2, 1]

# sort_reverse(3, 1, 4, 2)

#finding minimum value
# def find_min(*args):
#     print(min(args))                               2

# find_min(5, 8, 2, 10, 3)


# ----------------------------------------------------------------------------------------------------------------------------




# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   variable length keyword argument   >>>>>>>>>>>>>>>>>>>>>>>>
 

# def func(a,b,c,**kwargs):                  #-------# variable length    ----- minimum value = 0      maximum value = no limit
#     print("positional arg:- ",a,b,c)                         #    positional arg:-  10 20 30
#     print("variable length keyword:- ", kwargs)   # it gives result in dict   #variable length keyword:- {'d': 40, 'e': 50, 'f': 60, 'g': 80}

# func(a=10,b=20,c=30, d=40,e=50,f=60,g=80)

#  1. Displaying user information
# def user_information(**kwargs):
#     print(kwargs)               {'name': 'shreya', 'age': 22, 'education': 'be', 'branch': 'it'}

# user_information(name="shreya", age=22, education="be", branch="it")


# 2. Book details
# def details(**kwargs):
#     print(kwargs)                {'name': 'quants', 'author': 'r.s.agrawal'}

# details(name="quants", author="r.s.agrawal")


# # 3. storing grades
# def grades(**kwargs):
#     print(kwargs)                    {'science': 89, 'maths': 79}

# grades(science=89,maths = 79)


# # 4. Employee record
# def emp_record(**kwargs):
#     print(kwargs)                {'firstname': 'shreya', 'lastname': 'mahalle', 'id': 101, 'role': 'developer'}

# emp_record(firstname="shreya", lastname="mahalle",id=101, role="developer")


# # 5. Generating an address
# def add(**kwargs):
#     print(kwargs)              {'colony': 'kohinoor colony', 'city': 'karanja', 'district': 'washim'}

# add(colony="kohinoor colony", city="karanja", district="washim")



#sum numberas
# def sum_numbers(**kwargs):
#     print(sum(kwargs.values()))            #60

# sum_numbers(a=10,b=20,c=30)


# # 8. Flexible function
# def flexbile(**kwargs):
#     print(kwargs)                   {'name': 'shreya', 'add': 'karanja lad', 'cont_no': '9356835542'}

# flexbile(name="shreya", add="karanja lad", cont_no="9356835542")


# 9. Merging dictionaries
# def merge_dict(**kwargs):
#     print(kwargs)                       {'a': 10, 'b': 20, 'c': 30}

# merge_dict(a=10,b=20,c=30)


# # 11. Displaying product details
# def product_details(**kwargs):
#     print(kwargs)                           {'name': 'laptop', 'price': '65697'}

# product_details(name="laptop", price="65697")


# 12. Creating a profile
# def create_profile(**kwargs):
#     print(kwargs)              {'username': 'shreya', 'age': 22, 'password': 'shreya123', 'email': 'shreyamahalle@gmail.com'}

# create_profile(username="shreya", age=22, password="shreya123", email="shreyamahalle@gmail.com")



# # 14. 15. Storing configuration
# def config_settings(**kwargs):
#     print(kwargs)                {'theme': 'dark', 'font_size': 14, 'language': 'EN'}

# config_settings(theme="dark", font_size=14, language="EN")


# 16. Summing numeric arguments
# def sum_numbers(**kwargs):
#     print(sum(kwargs.values()))            60

# sum_numbers(a=10,b=20,c=30)


# 17. Listing favorite movies
# def favorite_movies(**kwargs):
#     # for person, movie in kwargs.items():
#         print(kwargs)             {'John': 'Inception', 'Alice': 'Titanic', 'Mary': 'Avengers'}

# favorite_movies(John="Inception", Alice="Titanic", Mary="Avengers")


# 18. Sorting dictionary values
# def sorted_values(**kwargs):
#     print(sorted(kwargs.values()))                [10, 40, 50, 70, 90]

# sorted_values(a=10,b=70,c=50,d=40, e=90)


# 19. reversed 
# def sorted_values(**kwargs):
#      print(sorted(kwargs.values(),reverse=True))              #  [90, 70, 50, 40, 10]

# sorted_values(a=10,b=70,c=50,d=40, e=90)



# ---------------------------------------------------------------------------------------------------


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<,,,,, lambda function >>>>>>>>>>>>>>>>>>>>>>>>>>>>>.


# square = lambda x:x ** 2
# print(square(5))                            25


# How do you define a lambda function that adds two numbers and returns their sum?
# add = lambda x,y: x + y
# print(add(10,20))                              30


# Write a lambda function to check whether a number is even or odd. What will be the output for lambda(7)?
# check_even = lambda x: "even" if x % 2 == 0 else "odd"
# print(check_even(7))                                    odd


# Create a lambda function to concatenate two strings. What will be the output for lambda("Hello, ", "World!")?
# concat = lambda s1, s2: s1 + s2
# print(concat("Hello, ", "World!"))                         Hello, World!


# How do you use a lambda function to find the larger of two numbers?
# larger_num = lambda num1,num2: num1 if num1 > num2 else num2
# print(larger_num(10,20))                                      20

# Write a lambda function to reverse a string. What will be the output of lambda("Python")?
# reverse = lambda str1: str1[::-1]
# print(reverse("python"))                              nohtyp


# What will the following code output?
# from functools import reduce
# nums = [1, 2, 3, 4]
# sum_nums = reduce(lambda x, y: x + y, nums)
# print(sum_nums)                                           10


# Use filter() and a lambda function to find all even numbers in a list. What will the output be for [1, 2, 3, 4, 5, 6]?

# lst1 = [1, 2, 3, 4, 5, 6]
# find_even =list(filter(lambda x: x % 2 == 0, lst1))
# print(find_even)                                             [2, 4, 6]

# lst1 = [10,20,30,44,545,78,33,7]
# odd = list(filter(lambda x: x % 2 != 0,lst1))
# print(odd)                                                    [545, 33, 7]


# How do you use a lambda function to double each number in a list using map()?
# lst1 = [10,20,30,40]
# double = list(map(lambda x:x**2,lst1))
# print(double)                                    [100, 400, 900, 1600]


# Write a lambda function to sort a list of names by their lengths. What will be the output for ["Alice", "Bob", "Charlie"]
# lst1 = ["Alice", "Bob", "Charlie"]
# sort_list = sorted(lst1, key=lambda x: len(x))
# print(sort_list)                                      ['Bob', 'Alice', 'Charlie']


# # Cube of a Number
# cube = lambda x: x**3
# print(cube(3))                         27


# Define a lambda function to increment a number by 10. What will lambda(25) output?
# increment = lambda x: x+10
# print(increment(10))                     20


# Use a lambda function with map() to find the lengths of strings in a list. What will be the output for ["apple", "banana", "cherry"]
# lst1 = ["apple", "banana", "cherry"]
# find_length = list(map(lambda x: len(x),lst1))
# print(find_length)                                    [5, 6, 6]


# How do you multiply all elements of a list using reduce() with a lambda function?
# lst1 = [1,2,3,4,5]
# from functools import reduce
# multiply = reduce(lambda x,y:x*y,lst1)
# print(multiply)                                         120


# Write a lambda function to capitalize the first letter of a string. What will be the output for lambda("hello")
# capitalize = lambda s: s.capitalize()
# print(capitalize("hello"))                          Hello


# lower = lambda s: s.lower()
# print(lower("HELLO"))                                   hello


# # find square_root
# square_root = lambda x: x ** 0.5
# print(square_root(16))                                     4.0


# Convert Celsius to Fahrenheit
# celsius_to_fahrenheit = lambda c: (c * 9/5)+32
# print(celsius_to_fahrenheit(0))                                32.0


# # Find Remainder
# remainder = lambda x,y: x % y 
# print(remainder(10,6))                                     4


# # 13. Sum of Three Numbers
# sum_numbers = lambda x,y,z:x+y+z
# print(sum_numbers(2,3,4))                                       9


# # 12. Check Palindrome
# check_palindrome = lambda s:s == s[::-1]
# print(check_palindrome("python"))                                 False


# check_palindrome = lambda s:s == s[::-1]
# print(check_palindrome("madam"))                                       True



# ------------------------------------------------------------------------------------------------------------------------------------