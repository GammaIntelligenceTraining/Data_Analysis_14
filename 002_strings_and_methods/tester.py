# string_sample = "Hello world world"
#                 #0123456789.....
#                         #-5-4-3-2-1
# string_sample2 = "first letteR is lowErcase"
# string_sample3 = "  !!  **     extra whitespace string    **  !!     "
# german_sample = "der Fluß"


# # [START:END:STEP]
# # print(string_sample[-1])
# # print(string_sample[2:12])
# # print(string_sample[-6:])
# # print(string_sample[:6])
# # print(string_sample[::-1])

# # string_sample = string_sample[::-1]

# # print(len(string_sample))

# # print(string_sample.upper())

# # print(german_sample.lower())
# # print(german_sample.casefold())

# # print(string_sample2.title())
# # print(string_sample2.capitalize())

# # print(string_sample3.strip(' !*'))
# # print(string_sample3.rstrip())
# # print(string_sample3.lstrip())

# # print(string_sample.replace('world', 'planet', 1))
# # print(string_sample.replace('Hello', ''))

# # print(string_sample.count('world', 7))
# # print(string_sample.find('world', 7))

# # print(string_sample[17])

# # print('Hello', 123, False, sep='***', end='!')
# # print('Hello world!', True)

# # print('Hello\nworld')

# # print('\\that\'s')

# # print(r'\thats')


# # print('hello'[2:5].upper().replace('L', 'p')[0].find('p') / 200)

# # salary = 2000
# # name = 'John'
# # string_template = '{0}s salary is {1}$'

# # print(string_template.format(name, salary))

# product = 'computer'
# price = 1000

# string_template = 'This {product} costs {price:.2f}$'

# print(string_template.format(product=product, price=price))

# # Formated string used in Python 2
# x = 12231.3456789
# y = 131.1314
# print('The value of x is %.4f' % x)
# print('The value of y is %.2f' % y)

# emp_name = 'John'
# emp_age = 30
# emp_salary = 1500

# emp_string = 'Hi, my name is %(name)s! I am %(age)s old. My salary is %(salary).2f' % {'name': emp_name, 'salary': emp_salary, 'age': emp_age}
# print(emp_string)

# name = 'Jack'
# salary = 1000

# formatted_string = f'{name.upper()}s salary is {salary + salary * 1.2:.2f}$'
# print(formatted_string)

# byte_sting = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
# print(byte_sting.decode('utf-8'))

print('hello'.center(20, '*'))

print('hello'.endswith('ll'))
print('hello'.startswith('0'))

print("hello 123".isalnum())
print('123.123'.isdecimal())

print('hello'.rjust(20, '*'))
print('23'.zfill(10))