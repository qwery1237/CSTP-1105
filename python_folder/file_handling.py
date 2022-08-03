# Python File Handling


"""
	1.) Open and read the file q1_text.txt. Print out the entire
	contents of the file.
"""
from distutils.command.build_scripts import first_line_re


print("\nQ 1.")

with open("q1_text.txt", mode ="r", encoding="utf-8") as f1:
	all_text = f1.read()

print(all_text)
"""
	2.) Open and read the file q2_text.txt. Print out only the
	first and last line in this file.
"""
print("\nQ 2.")

with open("q2_text.txt" , mode="r", encoding="utf-8") as f2:
	first_line_f2 = f2.readline().rstrip()
	last_line_f2 = f2.readlines()[-1].rstrip()
print(first_line_f2, last_line_f2)

"""
	3.) Open up file q3_text.txt and at the end of it write a
	new line "- From <your name here>". Make sure not to delete 
	any of the text inside of it.
"""
print("\nQ 3.")

# Write Code here
with open("q3_text.txt", mode="a", encoding="utf-8") as f3:
	f3.write('\n- From Jinsoo Son')


def restore_q3():
	print('Q3. HAS BEEN RESTORED')
	with open('q3_text.txt', mode='w', encoding='utf-8') as f3:
		f3.write("""Dear Santa,
This year I would like a bike
because my last one was stolen
on Granville Island!""")

# Call restore_q3() if you accidentally delete the file
restore_q3()
#############



"""
	4.) Open up file q4_text.txt and print the averageW of all
	the numbers that appear in the file. The numbers are all 
	separated by a single space " " each
"""
print("\nQ 4.")
with open("q4_text.txt" , mode="r" , encoding='utf-8') as f4:
	all_text_f4 = f4.read()
num_list = all_text_f4.split(' ')
num_list = list(map(int,num_list))
num_average = round(sum(num_list)/len(num_list),2)
print(num_average)

"""
	5.) Create a new file called q5_answer.txt and write
	2 lines in it reading "I made this with Python" and
	"A new file gets created if no file in the directory
	has the same name as it!". After this is created, print
	the line "q5_answer is made"
"""
print("\nQ 5.")
with open('q5_answer.txt',mode='w',encoding='utf-8') as f5:
	f5.write('I made this with Python\n')
	f5.write('A new file gets created if no file in the directory has the same name as it!')
print('q5_answer is made')


"""
    6.) q6_tsv.tsv is a tab separated values file. It
    contains words separated by tabs \t on a single line. 
    Count how many words there are in the file and print it. 
    Also, to the end of the file add the following "there are
    X words in this file".

"""
print("\nQ 6.")

with open('q6_tsv.tsv', mode='a+', encoding='utf-8') as f6:
	f6.seek(0)
	all_words_f6 = f6.read().split('\t')
	word_num = len(all_words_f6)
	f6.seek(2)
	f6.write(f"\nThere are {word_num} words in this file")

def restore_q6():
	print('Q6 HAS BEEN RESTORED')
	with open('q6_tsv.tsv', mode='w', encoding='utf-8') as f6:
		f6.write('cat\tbat\that\tmat\tfat\tchat')

# Call restore_q6() if you accidentally delete the file
restore_q6()
#############



"""
	7.) Print how many times the word "Canada" appears in 
	the q7_text.txt file. Replace all appearances of the word 
	Canada in the file with the word "CENSORED". You must 
	overwrite the file when doing this.
"""
print("\nQ 7.")
with open('q7_text.txt',mode='r+',encoding='utf-8') as f7:
	all_content_f7 = f7.read()
	word_num = all_content_f7.count('Canada')
	content_replaced = all_content_f7.replace('Canada','CENSORED')
	f7.seek(0)
	f7.write(content_replaced)
	print(word_num)
def restore_q7():
	print('Q7 HAS BEEN RESTORED')
	with open('q7_text.txt', mode='w', encoding='utf-8') as f7:
		f7.write("""Canada is a country in North America. 
Canada's capital is Ottawa, and its three largest 
metropolitan areas are Toronto, Montreal, and Vancouver.
Indigenous peoples have continuously inhabited what is 
now Canada for thousands of years.
In 1867, with the union of three British North American 
colonies through Confederation, Canada was formed as a 
federal dominion of four provinces.""")

# Call restore_q7() if you accidentally delete the file
# restore_q7()
#############


