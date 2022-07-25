import book
# Python Assignment 4
#
# NOTE - RENAME ASSIGNMENT FILE yourname_Assignment_4.py
# DON'T FORGET THE UNDERSCORES _ IN YOUR FILE NAME
# Hand up only this file and not a folder nor the book.py file
"""
    1.) A file called book.py is included in this folder. It contains
    a string variable called paragraphs. Write code to do the following:
    - Import the book file as a module into this file

    In a single message print the following:
    - "There are X sentences in book."
    - "There are Y words in book."
      Note that hyphenated words e.g. "backward-compatible" count 
      as a single word and names, numbers and years count as
      words as well.
    - The last sentence from paragraph but replace all occurences
      of the word "and" with "&".
"""

print("\nQ 1.")
# Import book.py(at the top of the file)
# Count the number of sentences in the paragraph
num_of_sentences = len(book.paragraphs.split('. '))
# Count the number of words in the paragraph
num_of_words = len(book.paragraphs.split(' '))
# Replace all occurences of the word 'and' with '&'
replaced_paragraph = book.paragraphs.replace('and', '&')
# Get each sentence in the paragraph as an element in a list
paragraph_sentences_list = replaced_paragraph.split('. ')
# Get the last sentece in the list
last_sentence = paragraph_sentences_list[len(paragraph_sentences_list)-1]
# Print the number of sentences in the paragraph, the number of words in the paragraph, and the last sentence.
print(f"""
There are {num_of_sentences} sentences in book.
There are {num_of_words} words in book.
{last_sentence}
""")


"""
	2.) Tax Collector

	Write code that will ask the user, using an input, what their 
    monthly gross income is. If the user doesn't type in a number 
    print "ERROR not a number" and do not proceed with 
    the calculation.

    - If the user earns less than 500 dollars, the tax 
    taken is 0 and they are in the low tax bracket. Only for these 
    people should you do the following. Ask the user how many 
    children they have. For each child that they have, give them 
    10 dollars in child benefits. If the user does not type in a 
    number they get 0 dollars in child benefits.

    - If the user earns 500 dollars or more but less than  
    700 they are in the medium tax bracket. Tax taken 
    here should be 15% of any sum that is over 500.

    - If the user earns 700 dollars or more they are in the high 
    tax bracket. Tax taken here should be 15% of the sum that is 
    over 500 but less than 700 and 25% of everything over 700.

    The final result should show in a single print the user's 
    gross income, the tax bracket (low, medium or high), total 
    tax, child benefits and net income (gross + child benefits - 
    tax).

    Gross Salary = 400, Bracket = Low,    Tax = 0,     Child Benefits = 20, Net Income = 420, this user has 2 kids
    Gross Salary = 620, Bracket = Medium, Tax = 18,    Child Benefits = 0,  Net Income = 602
    Gross Salary = 905, Bracket = High,   Tax = 81.25, Child Benefits = 0,  Net Income = 823.75
"""

print("\nQ 2.")
# Ask user's gross salary
gross_salary = input('Gross Salary : ')
# Convert the type of user input to float.
# If an error occurs, print 'ERROR not a number'.
# If the gross salary is negative, print 'Salary can not be negative'.
# Except for the previous cases, proceed with the tax calculation and print the result.
# The result includes information about gross salary, tax bracket, tax, child benefits(defalut = 0), and net income.
# Only if the user is a low bracket, ask the number of children and calculate child benefits.
# If user input is not valid, change the value to 0.
# and add information about the number of children to the end of the message.
try:
    gross_salary = round(float(gross_salary), 2)

    if gross_salary < 0:
        print('Salary can not be negative')
    else:
        bracket = ''
        tax = 0
        child_benefit = 0
        num_of_children = ''

        if gross_salary < 500:
            bracket = "Low"
            num_of_children = input("How many children do you have? ")
            num_of_children = int(
                num_of_children) if num_of_children.isnumeric() else 0
            child_benefit = num_of_children*10
        elif gross_salary < 700:
            bracket = "Medium"
            tax = (gross_salary - 500) * 0.15
        else:
            bracket = "High"
            tax = (700 - 500.01) * 0.15 + (gross_salary - 700) * 0.25
        tax = round(tax, 2)
        net_income = round(gross_salary + child_benefit - tax, 2)
        message = f'Gross Salary = {gross_salary}, Bracket = {bracket},Tax = {tax},' +\
                  f'     Child Benefits = {child_benefit}, Net Income = {net_income} '

        if type(num_of_children) is int:
            if num_of_children > 1:
                message = message + f', this user has {num_of_children} kids'
            else:
                message = message + f', this user has {num_of_children} kid'

        print(message)
except:
    print('ERROR not a number')
