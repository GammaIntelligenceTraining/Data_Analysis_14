# a = 5
# b = 10
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
# print(a == b)
# print(a != b)

# print(a < 8 < b)
# print(a < 8 and b > 8)
# print(a < 0 or b > 5)

# print("a" > "b")
# print(ord("a"))

# print("art" < "artist")

# print(not True)

# x = 'hello'
# if type(x) != str:
#     print('string')

# x = 0
# if not x:
#     print(x)

# print(not [])

# year = 1700

# print(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)

# print(1 in [1, 2, 3])
# print(1 in (1, 2, 3))
# print(1 in {1, 2, 3})
# print('12' in '123')

# x = None
# print(x is not None)


# name = input('Enter name: ')
# surname = input('Enter surname: ')

# if not name or not surname:
#     print('Name and Surname are a must')

# x = [1, 2, 3]
# y = x.copy()

# print(x == y)
# print(x is y)

# numbers = [-2, -1, 1, 2]
# print(any(numbers))
# print(all(numbers))

# age = 70

# if not age < 0:
#     if age < 12:
#         print('child')
#     elif age < 18:
#         print('teenager')
#     elif age < 65:
#         print('adult')
#     else:
#         print('senior')
# else:
#     print('Age must be positive number')


# numbers = [1, 2, 3, 4, 5]
# evens = []

# for num in numbers:
#     print(num)
#     if num % 2 == 0:
#         evens.append(num)

# print(evens)
# print('Good bye!')

# names = ['Jack', 'Sarah', 'Mary', 'Bob']

# for name in names:
#     print('Hello ' + name)

# people = [
#     ('Jack', 'Smith', 56),
#     ('Sarah', 'Gold', 30),
#     ('Simon', 'Green', 25),
# ]

# for name, surname, age in people:
#     print(f'{name} {surname} is {age} years old')

# name, surname, age = people[0]

# a, b, c = [1, 2, 3, 4]

# print(a, b, c)


# x = [1, 2, 3]
# print(*x)
# print(1, 2, 3)

# y = [10, 20, *x, 30]
# print(y)

# first, *rest, last = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(first)
# print(rest)
# print(last)
# x = [1, 2, 2, 2, 3, 3, 4, 5, 3]
# print(list(range(100, 200, 10)))

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# for index in range(len(x)):
#     print(x[index] * y[index])


# for num1 in range(10):  # 0-9   10 times
#     for num2 in range(10):    # 10 * 10 = 100
#         for num3 in range(10):  # 10 * 10 * 10 = 1000
#             print(num1, num2, num3)

# Для диапозона чисел от 0 до 100
# Если число делится на 3 без остатка -> число и 'FIZZ'
# Если число делится на 5 без остатка -> число и 'BUZZ'
# Если число делится на 3 и 5 без остатка -> число и 'FIZZBUZZ'

# for num in range(101):
#     if num % 3 == 0 and num % 5 == 0:
#         print(num, 'FIZZBUZZ')
#     elif num % 3 == 0:
#         print(num, 'FIZZ')
#     elif num % 5 == 0:
#         print(num, 'BUZZ')


# empty = {}
# empty = dict()

# print(type(empty))  # dict()

# student = {
#     "name": "Jack",
#     "info": {
#         "languages": ["English", "Estonian", "Finnish"],
#         "eye_color": "blue",
#     },
#     10: 'int key',
#     (1, 2): (1, 2, 3, 4, 5, 6)
# }

# print(student["info"]['languages'][1])

# print(student[(1, 2)][2])


# my_car = {
#     "make": "VW",
#     "mileage": 100000,
# }

# my_car["make"] = "BMW"
# my_car["color"] = "red"
# print(my_car)

# print(my_car.get('make'))

# x = my_car.get("model", '')
# y = x.count('s')
# print(y)

student = {
    'name': 'Jack',
    'surname': 'Smith',
    'avg_grade': 4.5,
}

# student.update({'name': 'Bob', 'phone': '555-555-5555'})
student.update(name='Bob', phone='555-555-5555')
print(student)

# deleted = student.pop('name')
# print(student)
# print(deleted)

# del student['name']

# print(student)

print(student.keys())
print(student.values())
print(student.items())


for key, value in student.items():
    print(key, value)

