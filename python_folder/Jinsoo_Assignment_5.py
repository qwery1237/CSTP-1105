import assignment5ModuleContainingVariables as my_vars
# Python Assignment 5
#
# NOTE - RENAME ASSIGNMENT FILE yourname_Assignment_5.py
# DON'T FORGET THE UNDERSCORES _ IN YOUR FILE NAME
# Hand up only this file and not a folder nor the accompanying module file
# assignment5ModuleContainingVariables.py

"""
    1.) Making a Tuple of Numbers
    Write a function called

    divisible_numbers()

    that takes in two number parameters. The first parameter
    represents the start number and the second represents the end number.
    The first parameter will always be smaller than the second parameter
    so there is no need to check or constrain this.
    This function should RETURN a tuple of all the numbers between these
    numbers (including the start and end numbers themselves if applicable)
    that are divisible by either the number 3, 5 or 7. That means if I divide
    the number by either 3 or by 5 or by 7 it shouldn't leave a remainder.
    The modulo operator % will come in handy here https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python
    as will using casting to transform a collection of one type into another.

    EXAMPLE
    ParameterA = 2,  ParameterB = 14, Result = (3, 5, 6, 7, 9, 10, 12, 14)
    ParameterA = -5, ParameterB = 5 , Result = (-5, -3, 0, 3, 5)
"""
print("\nQ 1.")

# Function 1
# 1. Create an empty list
# 2. Check if each number between start_num and end_num is divisible by either the number 3, 5 or 7
# 3. If the number is divisible by any of the 3 numbers, append the number to the list
# 4. Convert the data type of the list to a tuple and return it.


def divisible_numbers(start_num, end_num):

    new_li = []

    while end_num >= start_num:
        new_li.append(
            start_num) if not (start_num % 3 and start_num % 5 and start_num % 7) else ...
        start_num += 1

    return tuple(new_li)


# 2 test results

test_result1 = divisible_numbers(2, 14)
test_result2 = divisible_numbers(-5, 5)

# print the results

print(test_result1)
print(test_result2)

"""
	2.) Returning True of False
    Write a function called

    no_hyphen_only_lower()

    that takes in a string as a parameter. This function
    should RETURN a boolean True if the string contains only lowercase letters
    and does not contain a hyphen "-".
    It should return False if there are any uppercase letters present or if
    there are any hyphens "-" present.
    EXAMPLE
    Parameter = "james",     Result = True
    Parameter = "Mark",      Result = False
    Parameter = "ann-marie", Result = False

    Use this function to count the number of items in the question_two_multi_list
    variable that is stored in the accompanying module that contain only lowercase
    letters without any hyphens. Each list item is a single word or single hyphenated word.

    Finally PRINT a sentence that reads "There are X lowercase no-hyphen words
    in the list" where X is the counted number.

    EXAMPLE
    test_list = [
        ["bakery", "Lions", "ice-cream", "caT", "sunday", "marKET"],
        ["drive-through", "Inspired", "haze"]
    ]
    Result = "There are 3 lowercase no-hyphen words in the list"

"""
print("\nQ 2.")

# Function 1
# Check if a parameter has no hyphen and no uppercase letter.
# Return the boolean value ( True if the string is a lowercase no-hyphen word)


def no_hyphen_only_lower(str1):

    return str1.islower() if not '-' in str1 else False


lower_letters_num = 0

# Access to each word in multi-list
# Count the number of words which are lowercase no-hyphen words
# To check whether it is a lowercase no-hyphen word or not, call function 1.

for li in my_vars.question_two_multi_list:
    for word in li:
        lower_letters_num += 1 if no_hyphen_only_lower(word) else 0

# Create a message and print it
result2 = f'There are {lower_letters_num} lowercase no-hyphen words in the list'
print(result2)

"""
    3.) Dictionary of Counted Words
    Write a function called

    most_used_words()

    that takes in a string as a parameter and returns a dictionary containing
    any word that appears more than 4 times in the string. The
    word should be in lowercase and appear as the the dictionary key
    and its value should be
    an integer representing the amount of times it appears. The
    order these words appear in the dictionary does not matter.
    The casing of the word should not matter either e.g. cat is
    the same as CAT and should be counted together.

    Use this function to return a dictionary on the snippet
    of text from the 1840 Canadian Act of Union which is
    stored in the accompanying module.

    EXAMPLE
    Parameter = "Cat story. The cat in the cat ville, had the sister cat, who's name was the cat-like name called Cat. All the cats loved being a cat.",
    Result = {'cat': 6, 'the': 5}

    NOTE in the code above, "cat-like" was not considered "cat" neither
         was "cats" because of the "s" at the end.

"""
print("\nQ 3.")

# Function
# 1. Create an empty dictionary
# 2. Remove symbols exept ' ' and '-' from the string
# 3. Get words as a list ( split the string by ' ')
# 4. Count the number of each word without repetition and add it in the dictionary (dict[word] = the number of word)
# 5. Return the dictionary


def most_used_words(str1):

    words_num_dict = {}  # 1

    filtered_str = ''.join(filter(  # 2
        lambda letter: str.isalnum(letter) or letter == '-' or letter == ' ', str1)).lower()

    words_in_sentence = filtered_str.split(' ')  # 3

    for word in set(words_in_sentence):  # 4
        words_num_dict[word] = words_in_sentence.count(word)

    return words_num_dict  # 5


# Run the function and get a result and print

result3 = most_used_words(my_vars.the_union_act_1840)
print(result3)
