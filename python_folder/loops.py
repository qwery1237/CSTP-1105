# Python Loops

"""
	1.) Below is a tuple, list and dictionary. Write a simple for loop
	for each one, that prints off each value in each of them
"""
print("\nQ 1.")

my_list = ["list1", "list2"]
my_tuple = ("tuple1", "tuple2")
my_dict = {"A": "word", "B": 1, "C": 3}
for el in my_list:
	print(el)
for el in my_tuple:
	print(el)
for el in my_dict:
	print(f'{el} : {my_dict[el]}')


"""
	2.) Loop through this string and for each character print out
	"x is a letter in y" where x is the letter and y is the contents
	of the string
"""
print("\nQ 2.")

my_string = "abcd"
for letter in my_string:
	print(f'{letter} is a letter in {my_string}')


"""
	3.) Loop through this string and using a single print(), print
	out the string but have all vowels capitalized. You'll need to
	create a new empty string and add each letter. If the letter is
	a vowel use .upper() to uppercase it
"""
print("\nQ 3.")

my_other_string = "abcdefghijklmnopqrstuvwxyz"

message = ''
for letter in my_other_string:
	if letter in 'aeiou':
		message = message + letter.capitalize()
	else :
		message = message + letter
print(message)
"""
	4.) Write a for loop that prints the numbers from 0 to 5
"""
print("\nQ 4.")
for num in range(0,6):
	print(num)


"""
	5.) Write a for loop that prints the numbers from 5 to 20
	in increments of 3. That is to print 5 8 11 14 17 20. Make
	sure to print this all off in a single print()
"""
print("\nQ 5.")
message2 = ''
for num in range(0,6):
	message2 = message2 + f'{5+num*3} '
print(message2)

"""
	6.) Create a new list that contains only the planet strings
	from planet_list that have 5 characters or less. Print out
	that list at the end.
"""
print("\nQ 6.")

planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
new_planet_list = []
for planet in planet_list:
	if len(planet) <= 5 :
		new_planet_list.append(planet)
print(new_planet_list)


"""
	7.) Write code that removes all items from the list that are
	'N'. Decide on what loop is best to use in thie situation. Also
	count how many times 'N' appears in the list. Finally print the
	new list and print "X number of Ns were removed from the list"
"""
print("\nQ 7.")

list_to_remove_items = ['N', 'A', 'B', 'N', 'N', 'M', 'B', 'W', 'A', 'N', 'L', 'S', 'H', 'D', 'N', 'N', 'P']
num_of_n = 0
while 'N' in list_to_remove_items :
	num_of_n += 1
	list_to_remove_items.remove('N')
print(list_to_remove_items)
print(f'{num_of_n} numver of Ns were removed from the list')
"""
	8.) Write code that asks the user to input a number. If they
	don't input a number, keep asking them to do it until they
	do. When they do, print the sentence "Half of your number is X"
	where X is half of the number.
	Use a while loop. Use try...except to test if input is an integer
"""
print("\nQ 8.")

num_user_input = input('Enter a number : ')
while not num_user_input.isnumeric() :
	num_user_input = input('Please put a number : ')

print(f'Half of your number is {int(num_user_input)/2}')
 
