import operator
# Python Collections

"""
	1.) Below, commented out, are 4 collections. A list, tuple, set and 
	dictionary. They are created with errors. Uncomment the code, fix the 
	errors and print each one along with its type e.g. type(myList).
"""
print("\nQ 1.")

my_list = ["list", "tuple", "set", "dictionary"]
my_tuple = ("cannot", "change", "a", "tuple")
my_set = {"no", "duplicates", "allowed", "here"}
my_dict = {"string": "word", "number": 1, "boolean": True}

print(my_list, type(my_list))
print(my_tuple, type(my_tuple))
print(my_set, type(my_set))
print(my_dict, type(my_dict))


"""
	2.) Below is a list called colours. Add 2 new colours to the list and
	remove the first colour from it using code. Then print the entire list and after,
	print the the following "There are X colours in my list" where X is
	the number of elements in your list.
"""
print("\nQ 2.")

colours = ["red", "green", "brown", "white"]

colours.append('grey')
colours.append('black')
del(colours[0])
print(colours,f'There are {len(colours)} colours in my list')


"""
	3.) Create a tuple called car_brands with 5 strings in it representing
	different car companies. In separate print(), print out:
	- the first element in your tuple
	- the third and fourth element in your tuple
	- the last element in your tuple
	- the first, third and fifth element in your tuple
"""
print("\nQ 3.")

car_brands = ('Toyota','Honda','Chevrolet','Ford','Jeep')
print (car_brands[0])
print(car_brands[2:4])
print(car_brands[len(car_brands)-1])
for i in range(len(car_brands)):
	if not i%2 :
		print(car_brands[i])

"""
	4.) Create a list and store 3 country names inside it as strings.
	Ask the user using an input to add a new country into the list. If
	the country name doesn't appear in the list, add it in. If it already
	is in the list then insert it in with all the letters capitalized. 
	Print out your list at the end to see the effect,
"""
print("\nQ 4.")
countries = ["Korea","Japan","Canada"]
new_country = input("countriy: ")
if new_country in countries :
	countries.append(new_country.upper())
else :
	countries.append(new_country)
print(countries)

"""
	5.) Below you will find a large list containing numerous numbers. 
	Write code to check and see if the number 13 is present in 
	it. If it is, remove it from the list. Print how many items
	are in this list. Then cast the list to a set to remove any duplicate
	items that may be present. Then print the new number of items in
	the list now that all duplicates have been removed.
"""
print("\nQ 5.")

huge_list = [54, 22, 111, 5, 22, 22, 67, 6, 99, 99, 20, 67, 90,
			123, 110, 4, 18, 19, 111, 77, 6, 54, 81, 80, 13, 38]
if 13 in huge_list:
	huge_list.remove(13)
print(len(huge_list))
print(len(list(set(huge_list))))


"""
	6.) Remove all duplicates from the names list below and then
	print each name in alphabetical order separated by the following
	characters " -- "
"""
print("\nQ 6.")

names = ["james", "mark", "mary", "paul", "mark", "aaron", "mary", "mark"]


names = sorted(list(set(names)))
for i in names:
	print(i)
"""
	7.) Create a colletion variable that holds the names of 4 of your
	friends paired with their phone number. Decide between a list,
	tuple, set or dictionary to create this. Then, using one of your 
	friend's names, print their name along side their number
"""
print("\nQ 7.")

collection = {'Jinsoo':'236-668-8845','Yu':'236-838-3733', 'mark':'234-234-3443'}
print(collection.keys())
for i in range(len(collection)):
	print(f'{list(collection.keys())[i]} : {list(collection.values())[i]}')

"""
	8.) Below is a dictionary containing some of the richest people in 
	the world along side their net worth. They are randomly ordered. 
	Write code to print out the following: "X is the richest person with
	$YYY. Z is the poorest person with $WWW" where YYY and WWW is the
	number of dollars they have.
"""
print("\nQ 8.")

worlds_richest = {
	"Bernard Arnault": 196000000000, 
	"Bill Gates":      137900000000, 
	"Elon Musk":       278700000000, 
	"Jeff Bezos":      200500000000,
	"Larry Ellison":   127100000000, 
	"Larry Page":      124700000000
}
sorted_worlds_richest = sorted(worlds_richest.items(),key=operator.itemgetter(1))
print(sorted_worlds_richest[0])
print(f'{sorted_worlds_richest[len(worlds_richest)-1][0]} is the richest person with' +
f'${sorted_worlds_richest[len(worlds_richest)-1][1]}. {sorted_worlds_richest[0][0]}'+ 
f'is the poorest person with ${sorted_worlds_richest[0][1]}.')
