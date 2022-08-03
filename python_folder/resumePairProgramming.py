# Python File Handling
from datetime import date
"""
Write code that will take the resume.txt file and replace
all words surrounded by angle brackets <> with values 
to yourselves. This new resume you create should be outputted
to a new file called new-resume.txt

<USERNAME> and <JOBTITLE> values can be hardcoded 
<CURRENTYEAR> should be the current year and needs to programmed
	so that in 2022 it will read 2022 without you changing it
<YEARS> should be programatically generated so that in 2 years
	time it update to account for you being more experienced

At the end of the file I want to see a list of programming 
languages on new lines with a leading hyphen like so
- JavaScript
- Python
These languages should be inputted by asking the user for input.
Keep asking the user to add languages until they type the
word "STOP" at which point the program should end and produce
the new file
"""


with open('resume.txt', mode='r', encoding='utf-8') as f:
	all_content = f.read()

current_year = date.today().year
written_year = 2022
job_experience = 2 + (current_year - written_year)
programming_languages =''

while True:
	language = f"\n- {input('What programming language do you use? ')}"
	if language != "\n- STOP":
		programming_languages += language
	else:
		break

all_content = all_content.replace('<USERNAME>','Joy')
all_content = all_content.replace('<JOBTITLE>','HelpDesk')
all_content = all_content.replace('<CURRENTYEAR>',str(current_year))
all_content = all_content.replace('<YEARS>',str(job_experience))
all_content += programming_languages

with open('new-resume.txt', mode='w', encoding='utf-8') as f2:
	f2.write(all_content)


print('Done')

# In case you accidentally modify the original file
# call this function to restore it to its former self
def restore_resume():
	with open('resume.txt', mode='w', encoding='utf-8') as f:
		f.write("""<USERNAME> Resume <CURRENTYEAR>
<JOBTITLE>
=====================================================

I am an enthusiastic and hard-working programmer that 
has recently graduated from the VCC Computer Systems
Technology diploma program. I have <YEARS> years experience 
writing code.

Programming Languages""")

########################
# Call this function
# to restore resume.txt
# to original form
# ######################
# restore_resume()
