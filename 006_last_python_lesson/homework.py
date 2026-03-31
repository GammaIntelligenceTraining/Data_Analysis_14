# Part 1: Refactoring with map()
# The map() function applies a transformation to every item in a list.
# Task: Convert the following for loop into a single line using map() and a lambda.

# Standard Loop version
prices = [10.0, 25.5, 40.0, 100.0]
discounted_prices = []

for p in prices:
    discounted_prices.append(p * 0.9) # 10% discount

# TODO: Your map implementation below
# discounted_prices = list(map(...))



# Part 2: Data Cleaning with filter()
# The filter() function keeps only the items that return True based on a specific condition.

# Task: We have a list of usernames. Some are too short (less than 5 characters). Filter them out.

usernames = ["admin", "joe", "skywalker", "ace", "python_pro", "em"]

# TODO: Use filter() to keep only names with length >= 5
# valid_users =


# Part 3: The "Grand Finale" (Map + Filter)
# Scenario: You have a list of temperatures in Celsius.
# Filter out any temperatures that are below freezing (0°C).
# Map the remaining "warm" temperatures to Fahrenheit using the formula:
#    F = (C x 9/5) + 32.



