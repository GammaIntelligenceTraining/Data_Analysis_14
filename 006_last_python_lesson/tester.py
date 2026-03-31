# while True:
#     print('I can\'t stop')

# counter = 0
# while counter < 20:
#     print(counter)
#     counter += 1

# while True:

#     user_choice = input('1. Say hello\n' \
#                         '2. Skip\n' \
#                         '3. Exit\n' \
#                         '-> ')
    
#     if user_choice == '1':
#         print('Hello!')
#     elif user_choice == '2':
#         continue
#     elif user_choice == '3':
#         break
#     else:
#         print('Choice is out of range')
#     print('*********************************')

# exit()
# print('Good bye!')

# for letter in 'python':
#     if letter in 'yo':
#         continue
#     else:
#         print(letter)
#     print('step')

# user_choice = 0

# if user_choice == '1':
#     pass
# elif user_choice == '2':
#     pass
# elif user_choice == '3':
#     pass


# try:
#     square_width = float(input('Enter square width: '))
#     if square_width == 0:
#         raise UserWarning
#     # square_width / 0
# except ValueError:
#     print('Value entered was not numeric')
# except ZeroDivisionError:
#     print('You can\'t divide by 0')
# except UserWarning:
#     print('Width of a square should be positive number')
# else:
#     print(square_width ** 2, 'area')
# finally:
#     print('Done')

# numbers = [4, 7, 3, 8, 9, 23, 15, 3, 85, 32, 945, 123, 153]

# numbers.sort()

# def sort_key(point):
#     return point[0] + point[1]


# points = [(5, 8), (9, 1), (4, 7), (1, 2), (6, 3), (2, 5)]

# points.sort(key=lambda point: point[1])

# print(points)


# no_params = lambda: print('Hello world!')

# no_params()

# one_param = lambda x: x ** 2

# print(one_param(5))

# more_params = lambda a, b, c=0: a + b + c

# print(more_params(10, 20, 30))
# print(more_params(10, 20))


# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']

# zipped = zip(list1, list2, range(10))

# print(zipped)

# enum = list(enumerate(list2, 100))

# print(enum)

# zipped2 = list(zip(zipped, 'abc'))
# print(zipped2)


# numbers = [1, 4, 6, 9, 3, 23, 52, 85, 301, 41, 45, 32]


# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False


# evens = list(filter(is_even, numbers))

# print(evens)


# odds = list(filter(lambda num: num % 2 != 0, numbers))

# print(odds)

# evens = list(filter(lambda num: True if num % 2 == 0 else False, numbers))
# print(evens)


# x = 0

# print('YES' if x > 0 else 'NO')

# name = 'Jack'

# x = name or 'stranger'

# print(x)

# from pprint import pp

# mapped = list(map(lambda num: num ** 2, numbers))
# print(mapped)

# mapped = list(map(lambda num: {
#     'number': num,
#     'square': num ** 2,
#     'cube': num ** 3,
# }, numbers))

# pp(mapped)


# people = [
#     {
#         'name': 'Jack',
#         'surname': 'Smith',
#         'email': 'asddas@dasdas.das',
#         'age': 18
#     },
#     {
#         'name': 'Mary',
#         'surname': 'Smith',
#         'email': 'aasddas@dasdas.das',
#         'age': 20
#     },
#     {
#         'name': 'Sarah',
#         'surname': 'Gold',
#         'email': 'vvvvvvv@dasdas.das',
#         'age': 21
#     },
# ]

# ages = list(map(lambda person: person['age'], people))
# print(ages)

# complex_map = list(map(lambda person: {
#     f'{person['name']} {person['surname']}': {
#         'email': person['email'],
#         'age': person['age'],
#     }
# }, people))

# from pprint import pp
# pp(complex_map)


# x = list(map(lambda num: True, numbers))
# print(x)

numbers = [1, 2, 3, 4, 5, 6]

squares = [num ** 2 for num in numbers]

print(squares)

evens = [num for num in numbers if num % 2 == 0]
print(evens)

labels = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print(labels)

pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)

def square(num):
    return num ** 2

squares2 = [square(num) for num in numbers]
print(squares2)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
summed = [x + y for x, y in zip(l1, l2)]
print(summed)

squares_dict = {num: num ** 2 for num in numbers}
print(squares_dict)

numbers = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4]
unique_squares = {num ** 2 for num in numbers}
print(unique_squares)
