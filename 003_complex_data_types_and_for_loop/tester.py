# # empty = []  # list()
# # empty = list()

# # print(type(empty))
# # print(bool(empty))

# # filled_list = [123, 12.032, False, None, [1, 2, [10, 20, [100, 200, 300]], 4, 5], 'hello world', 'hello world', 'hello world']

# # print(filled_list[0:5:2])
# # print(len(filled_list))

# # print(filled_list[4][2][2][1])

# # print(filled_list[5])

# courses = ["History", "Math", "English", "Physics", "Programming", "123", "art"]

# # courses[1] = "Chemistry"

# # print(courses)

# # courses.append('Art')
# # courses.extend(['Art', 'Chemistry'])
# # print(courses[4])
# # courses.insert(2, 'Art')
# # print(courses[4])

# # courses.remove('Math')
# # # deleted = courses.pop(0)

# # print(courses)
# # print(deleted)

# # print(courses[::-1])
# # courses.reverse()
# # courses.sort(reverse=True)
# # print(courses)

# # print(min(courses))
# # print(max(courses))
# # print(sum([1, 2, 3, 4, 5]))

# # print(courses.index('Math'))
# # print(courses.count('Math'))

# # courses_string = '***'.join(courses)

# # print('Hello people of planet Earth'.split())
# # print(courses_string.split("***"))

# # print(list("Hello people"))

# # print([1, 2, 3] + [4, 5, 6])

# # a = 5
# # b = a
# # a += 10

# # print('A', a, 'B', b)

# # a = 'Hello'
# # b = a
# # a += 'world'

# # print('A', a, 'B', b)


# # a = [1, 2, 3]
# # b = a.copy()
# # a += [4, 5]
# # b += [6, 7]

# # print('A', a, 'B', b)


# # a = [1, 2, 3]
# # print(id(a))
# # b = a.copy()
# # a.append(5)
# # print(id(a))
# # print(id(a))
# # b.append(10)

# # print(a)
# # print(b)


# empty = ()
# empty = tuple()

# print(type(empty))


# one_element = (123, 23, 12, 45)
# print(type(one_element))

# print((1, 2, 3) + (4, 5, 6))


# one_element = list(one_element)
# one_element.append(33)
# one_element = tuple(one_element)
# print(one_element)

# empty = set()
# print(type(empty))

# courses = {'Physics', 'Math', 'History', 'Art', 'Programming', 'Art', 'Art', 'Art'}

# print(courses)

# print(list(set([1, 1, 1, 2, 2, 2, 3, 3, 3])))

# set1 = {'Math', 'Art', 'Chemistry', 'History'}
# set2 = {'Math', 'History', 'English', 'Physics'}

# print(set1.intersection(set2))
# set1.intersection_update(set2)
# print(set1)

# print(set1.difference(set2))
# print(set2.difference(set1))

# print(set1.symmetric_difference(set2))

# print(set1 & set2)

# print(set1.union(set2))


# set1 = {'Math', 'Art', 'Chemistry', 'History'}
# mini_set = {'Math', 'Art'}

# print(set1.issuperset(mini_set))
# print(mini_set.issubset(set1))

# x = -12

# if x > 0:
#     print('X is greater than 0')
# elif x < 0:
#     print('X is less than 0')
# else:
#     print('X is 0')


# x = 1000

# if x > 0 and x < 100:
#     print('One')
# if x > 10:
#     print('Two')
# if x > 100:
#     print('Three')


isikukood = "38803160272"

if len(isikukood) == 11:
    print('OK')
else:
    if len(isikukood) < 11:
        print('Code is too short')
    else:
        print('Code is too long')