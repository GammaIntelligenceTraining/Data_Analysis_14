# def say_hello(name):
#     print(f'Hello {name}')


# # say_hello('Jack')
# # say_hello('Max')
# # say_hello('Bob')
# # say_hello('Mary')
# # say_hello('Sarah')

# print(say_hello('Bob'))


# def square(number):
#     return number ** 2


# x = square(25)
# print(x)

# def long_name(name):
#     if not name:
#         return None
#     if len(name) > 5:
#         return True
#     return False

# print(long_name('Jessica'))


# def largest_of_two(num1, num2):
#     if type(num1) not in [int, float] or type(num2) not in [int, float]:
#         raise TypeError
#     if num1 > num2:
#         print(num1, 'is greater')
#     elif num2 > num1:
#         print(num2, 'is greater')
#     else:
#         print(num1, 'is equal to', num2)


# largest_of_two(10, 10)
# largest_of_two(23.3, 12.2)
# largest_of_two('hello', 'world')


# def is_even(number: int) -> bool:
#     if number % 2 == 0:
#         return True
#     return False


# print(is_even(103))


# def tester(a, b, c=0):
#     print(a, b, c)

# tester(10, 20, 30)

# def args_kwargs(*numbers, a, b=0):
#     result = 0
#     for num in numbers:
#         result += num
#     print(result)
#     print('a', a, 'b', b)

# args_kwargs(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, a=10)

# def keywordargs(**kwargs):
#     print(kwargs)

# keywordargs(a=10, b=20, x=300, y=1000)

# a = 1
# b = 2
# c = 3

# def tester():
#     a = 10
#     b = 20
#     print('inside function', a, b, c)

# tester()
# print('outside function', a, b, c)



# def letter_counter(list_of_strings: list) -> None:
#     counter = 0

#     for text in list_of_strings:
#         counter += len(text)
#     return counter

# counter = 0
# strings = ['Hello', 'world', 'people', 'planet', 'sunshine']

# counter = letter_counter(strings)


# print(counter)

# def outer_func(id_code):

#     def inner_func():
#         try:
#             int(id_code)
#             if len(id_code) != 11:
#                 raise UserWarning
#         except:
#             return False
#         else:
#             return True
    
#     if inner_func():
#         print("All good")
#         print(id_code)
#     else:
#         print("Code error")


# outer_func('38803160272')

# def say_hello():
#     print('Hello world')


# def logger(func):
#     print('Starting')
#     func()
#     print('Finishing')


# logger(say_hello)


# def square_area(a, b):
#     return a * b


# def print_area():
#     print(f'Rectangle area is {square_area(20, 10)}mm2')

# print_area()

# import my_funcs

# my_funcs.say_hello('Roman')
# print(my_funcs.PI)

# mf = 0
# print(mf)
# import my_funcs as mf

# mf.say_good_bye()
# print(mf)

# PI = 123
# print(PI)

# from my_funcs import PI as P, say_hello as sh

# print(P)
# sh('Hello')


# PI = 10

# print(PI)

# from my_funcs import *

x = 100
from my_funcs import PI
print(PI)