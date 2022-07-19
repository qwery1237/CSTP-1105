# Python Variables
import math
import os
import re
"""
	1.) Create three string variables called myName, parentName1 
	and parentName2 and assign them values. Then in a single sentence 
	print out "My name is X. My parents' names are Y and Z"
"""
print("\nQ 1.")

my_name = 'Jinsoo Son'
parent_name1 = 'Sungmin Son'
parent_name2 = 'Heeyoung Kim'
print(f'My name is {my_name}. My parents\' names are {parent_name1} and {parent_name2}')

"""
	2.) Create a string variable called petName and give it a string value. 
	Create an integer and call it petAge and assign it a value. Print the
	sentence "X is my pet and they are Y years old". Make sure to cast the
	petAge variable as a string before outputting the sentence.
"""
print("\nQ 2.")

pet_name = 'paul'
pet_age = 3
print(f'{pet_name} is my pet and they are {pet_age} years old')

"""
	3.) Four strings are provided below representing files. They have file 
	extensions such as .txt, .html and .js at the end. Print out each file name 
	without the file extension. Only remove the file extension from the end
"""
print("\nQ 3.")
s1 = "homework.txt"
s2 = "assignment2.html"
s3 = "main.js"
s4 = "js.mainjs.js"
print (os.path.splitext(s1)[0])
print (os.path.splitext(s2)[0])
print (os.path.splitext(s3)[0])
print (os.path.splitext(s4)[0])


"""
	4.) Four strings are provided below. Update each one of the strings by
	removing all numbers that appear inside them and uppercase the first
	letter. Then in a single sentence print out each new string separated
	by commas e.g. Apple, Orange, Lemon, Tea
"""
print("\nQ 4.")
f1 = "ap12ple"
f2 = "oran454ge"
f3 = "9lem5on5"
f4 = "t12ea"
f1 = re.sub(r'[0-9]+', '',f1).capitalize()
f2 = re.sub(r'[0-9]+', '',f2).capitalize()
f3 = re.sub(r'[0-9]+', '',f3).capitalize()
f4 = re.sub(r'[0-9]+', '',f4).capitalize()
print(f'{f1}, {f2}, {f3}, {f4}')

"""
	5.) Ask the user to type in their name using input(). Then replace
	all occurences of the letter "a" with "x", and print the following
	"Welcome Nxme! Your name is Y letters long." where Nxme is their 
	inputted converted name and Y is the number of characters in the name. 
	Note that the first letter is capitalized, all subsequent letters are 
	lowercase and all "a"s are replaced with "x".
"""
print("\nQ 5.")
user_name = input("What is your name? ")
user_name = user_name.replace('a','x').lower().capitalize()
name_length = len(user_name.replace(' ',''))
print(user_name,name_length)



"""
	6.) Create an integer called age and another called year and assign them 
	the values of your age and the current year. Then print a single
	sentence that says "My age is X and I was born in the year YYYY" where
	YYYY is year - age.
"""
print("\nQ 6.")
age = 25
year = 2022
print(f'My age is {age} and I was born in the year {year - age}')



"""
	7.) Do the exact same as above except this time ask the user to input their
	age and the current year
"""
print("\nQ 7.")
user_age = int(input("your age : "))
crr_year = int(input('current year : '))
print(f'My age is {user_age} and I was born in the year {crr_year - user_age}')



"""
	8.) There are two variables below representing a temperature in Celsius
	and one in Fahrenheit. Write code that converts the temperatures to the
	opposite scale and print 2 sentences reading "X degrees Celsius is Y degrees 
	Fahrenheit" and vice versa for the other one.
"""
print("\nQ 8.")
tempFahrenheit = 32
tempCelsius = 25
f_to_c = (tempFahrenheit -32) /1.8
c_to_f = (tempCelsius * 1.8) + 32
print(f'{tempCelsius} degrees Celsius is {c_to_f} degrees Fahrenheit')
print(f'{tempFahrenheit} degrees Fahrenheit is {f_to_c} degrees Celsius')


"""
	9.) Calculate the area of a circle that has a radius of 45.5cm. Use
	the correct and accurate value of a pi. Display this result like 
	"6503.882cm^2". Note the area is rounded to three decimal places
"""
print("\nQ 9.")
radius = 45.5
circle_area = round((radius**2) *math.pi,3) 
print(f'{circle_area}cm^2')