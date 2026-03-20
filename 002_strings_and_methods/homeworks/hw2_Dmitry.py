# Write a code to return "Hero" from given string
example_string1 = "Hello bro"
result1 = example_string1.replace("llo b", "")
print(result1)


# Write a code to return "Jack is my name"
example_string2 = "jack Is My NAME"
result2 = example_string2.lower().capitalize()
print(result2)


# Write a code to return "Get rid of junk please"
example_string3 = "%-*Get rid of *junk* please*-L%*"
result3 = example_string3.strip("%*-L")
result3 = result3.replace("*", "")
print(result3)

# Write a code to return "Hello my name is Jack"
example_string4 = "hello my name is jack"
result4 = example_string4[:-4].capitalize() + example_string4[-4:].capitalize()
print(result4)  # Hello my name is Jack


# Count all occurrences of “Estonia” in a given string ignoring the case.
example_string5 = "Welcome to estonia. Estonia is awesome, isn't it? I moved to ESTONIA 5 years ago."
count_estonia = example_string5.lower().count("estonia")
print(count_estonia)


# Write a code to return f-string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"
result5 = f"{var2.capitalize()}, {var3.lower()} {var1.capitalize()}"
print(result5)


# Write a code to return byte_string text value (try utf-8 and utf-16)
byte_string = b"\316\273"
print(byte_string.decode("utf-8"))
print(byte_string.decode("utf-16"))