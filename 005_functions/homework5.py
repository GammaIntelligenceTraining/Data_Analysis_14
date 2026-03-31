# Write a function that accepts a list of numbers as an argument
# And returns list with squares for each number
# Input: list of numbers
# Output: list of numbers

def squares(list_of_nums: list) -> list:
    result = []
    for num in list_of_nums:
        result.append(num ** 2)
    return result

print(squares([1, 2, 3, 4, 5, 6, 7, 8]))



# Write a function that accepts a list of numbers
# And returns a tuple with two numbers, amount of odd and even numbers
# Example: input -> [1, 2, 3, 4, 5] output (3, 2)
# Where 3 is amount of Odds and 2 is amount of evens

def count_odds_and_evens(list_of_numbers: list) -> tuple:
    odds, evens = 0, 0

    for num in list_of_numbers:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    
    return odds, evens


print(count_odds_and_evens([1, 2, 3, 4, 5, 6, 7]))

# Write a function that accepts a list of numbers
# and returns largest number

def largest_number(list_of_numbers: list) -> int:
    max_count = 0
    for num in list_of_numbers:
        if num > max_count:
            max_count = num
    return max_count


print(largest_number([1, 2, 3, 4, 5, 6, 7, 8]))



# Write a function that accepts a start number and end number
# Create a FizzBuzz for given range
# (If number divided by 3 has no remainder, print number + FIZZ
# If number divided by 5 has no remainder, print number + BUZZ
# If number divided by 5 and 3 has no remainder, print number + FIZZBUZZ)
def fizzbuzz(start, end):

    for num in range(start, end + 1):
        if num % 5 == 0 and num % 3 == 0:
            print(num, 'FIZZBUZZ')
        elif num % 5 == 0:
            print(num, 'BUZZ')
        elif num % 3 == 0:
            print(num, 'FIZZ')


fizzbuzz(100, 200)