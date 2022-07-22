# Python MultiLists

multi_lists = [
	['A', 'B', 'C'],
	['D', 'E', 'F'],
	['G', 'H', 'I', 'J'],
]

"""
	1.) In separate prints, print out the A, D, E, I and J
	from multi_lists. Use the [][] system to access these values.
"""
print("\nQ 1.")

print(multi_lists[0][0])
print(multi_lists[1][0])
print(multi_lists[1][1])
print(multi_lists[2][2])
print(multi_lists[2][3])

"""
	2.) Count the number of items that appear in the entire
	multi_lists. Print the sentence "There are X items 
	in multi_lists"
"""
print("\nQ 2.")

num_of_total_els = 0
for li in multi_lists:
	for el in li:
		num_of_total_els += 1
print(num_of_total_els)
"""
	3.) Store the three tuples below in a list to create
	a multi dimensional collection variable. The loop through
	every item in this multidimensional collection and print 
	each one out. You will need to create a nested for loop.
"""
print("\nQ 3.")
li_of_tuple =[]
tuple_a = ('one', 'two', 'three')
tuple_b = ('four', 'five', 'six')
tuple_c = ('seven', 'eight', 'nine')
li_of_tuple.extend([tuple_a,tuple_b,tuple_c])
for tp in li_of_tuple:
	for el in tp:
		print(el)

"""
	4.) Below is a multi dimensional list containing dictionaries.
	Loop through each one and print both the key and the value
	in each dictionary like so Key ~~ Value. When you encounter the 
	value "STOP"  stop printing anything else from the collection
	and exit out of all the loops
"""
print("\nQ 4.")

multi_dict = [
	{'BC': 'Vancouver', 'Ontario': 'Toronto', 'Alberta': 'Calgary'},
	{'Washington': 'Seattle', 'Oregon': 'STOP', 'Florida': 'Miami'},
	{'UK': 'London', 'Ireland': 'Dublin', 'France': 'Paris'}
]
for cities in multi_dict:
	for city in cities:
		if cities[city] == 'STOP':
			break
	else:
		continue
	break

	

print("This print shows you have gotten to the end")

