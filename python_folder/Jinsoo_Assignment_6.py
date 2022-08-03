# Python Assignment 6

"""
    1.) Updating a CSV file
    You are given a CSV file called exam_results.csv which contains three
    exam results for 4 students each. The first line contains the names
    of the students. The next three lines contain the results. Commas (,)
    separate each piece of data from each other while the new line denotes
    a new row of data.

    Write a function that takes in this file, adds "Total" and "Average"
    to the top line and then for each of the other lines place the
    sum/total of all the numbers in that row and beside that place the
    average of the numbers of that row. These values should be floats.
    Make sure to do this in the same file
    exam_results.csv so that you overwrite the file.

    The function restore_exam_results() is placed underneath to allow you
    to rebuild the file if you make mistakes.

    The original data looks like:

Mark, Bobby, Susan, Mary
60, 77, 96, 81
95, 79, 60, 54
88, 81, 69, 84

    The final data should look like:

Mark, Bobby, Susan, Mary, Total, Average
60, 77, 96, 81, 314.0, 78.5
95, 79, 60, 54, 288.0, 72.0
88, 81, 69, 84, 322.0, 80.5
"""
print("\nQ 1.")

# Open a file with r+ mode

with open('exam_results.csv', mode='r+', encoding='utf-8') as f1:

    # Get a list of all sentences in the file.
    # Change the data type of each element(sentence) in the list to a list. (splited by ', ')

    all_text_li = f1.read().split('\n')
    all_text_multi_li = list(map(lambda el: el.split(', '), all_text_li))

    # Add two elements to the first list in the multi-list
    # and change the data type of the list to string. (joined by ', ')

    all_text_multi_li[0].extend(['Total', 'Average'])
    all_text_multi_li[0] = ', '.join(all_text_multi_li[0])

    # Change the data type of all the elements(scores of all students) of
    # the rest lists(all subjects) in the multi-list to int.                (1)
    # Find the sum and average of each subject.                             (2)
    # Add the sum and average to the end of each list.                      (3)
    # Change the data type of each list to string
    # and change the data for that element in the multi-list to the string. (4)

    for line_num in range(1, len(all_text_multi_li)):

        # (1)
        crr_sentence_li = list(map(int, all_text_multi_li[line_num]))

        # (2)
        total_score = float(sum(crr_sentence_li))
        average_score = float(sum(crr_sentence_li)/len(crr_sentence_li))

        # (3)
        crr_sentence_li.extend([total_score, average_score])

        # (4)
        all_text_multi_li[line_num] = ', '.join(map(str, crr_sentence_li))

    # Change the data type of all_text_multi_li to string.(joined by '/n')

    result_data = '\n'.join(all_text_multi_li)

    # Move the mouse point to the beginning of the file.
    # Overwrite the content of the file with result data.

    f1.seek(0)
    f1.write(result_data)

# Print out an alert when the file change is complete.

print('The content of exam_results has been changed.')


def restore_exam_results():
    print('exam_results HAS BEEN RESTORED TO ORIGINAL!')
    print('IF YOU DONT WANT THIS TO HAPPEN COMMENT OUT')
    print('restore_exam_results()')
    with open('exam_results.csv', mode='w', encoding='utf-8') as f_restore:
        f_restore.write("""Mark, Bobby, Susan, Mary
60, 77, 96, 81
95, 79, 60, 54
88, 81, 69, 84""")


######################
# restore_exam_results()
######################


"""
	2.) Create a class called GameCharacter. This class should take
    in 3 object attributes.

    name - a string which should be assigned a value by the user at creation
    health - an int which should be fixed to 10
    lives - an int which should be fixed to 3

    The class should have 1 method which is given below called
    describe_character(). This doesn't take in any parameters
    and simply prints out all of the objects attributes and their values.
    Make sure your class has this method

    def describe_character(self):
        print(self.__dict__)

    The class needs 3 other methods which you will need to create:

    take_damage(damage)
    which takes in a parameter which represents the
    number of damage the character has taken. This will be an int. When
    called the method should print
    "CharacterName" took X damage" where X is the number of damage.
    Then the damage amount should be removed from the object's health
    attribute. Then call describe_character() to display the object's
    current stats and finally the method should check to see if the
    object has any health left. If it has 0 or less health then the
    method should call the lose_life() method.

    lose_life()
    should print
    "CharacterName lost a life" and then decrement the lives attribute
    by 1. Then call describe_character() to display the object's
    current stats. If the number of lives has reduced to 0 or less,
    print "CharacterName has died!". If not then restore the character's
    health back to it's full value which is 10.

    drink_potion()
    should print
    "CharacterName restored health to full" and then set the health
    attribute to it's original max value of 10. Then call
    describe_character() to display the object's current stats.

    Applying all these together you should have created an object
    representing a videogame character that we can perform actions
    on and track the vital points of information related to the
    character.

    If I was to create a new object from this class and perform
    the following methods on it like so:

mario = GameCharacter('Mario')

mario.take_damage(4)
mario.take_damage(7)
mario.take_damage(5)
mario.drink_potion()
mario.take_damage(11)
mario.take_damage(15)

    I should see the following output in Command Prompt
Mario took 4 damage.
{'name': 'Mario', 'health': 6, 'lives': 3}
Mario took 7 damage.
{'name': 'Mario', 'health': 0, 'lives': 3}
Mario lost a life.
{'name': 'Mario', 'health': 0, 'lives': 2}
Mario took 5 damage.
{'name': 'Mario', 'health': 5, 'lives': 2}
Mario restored health.
{'name': 'Mario', 'health': 10, 'lives': 2}
Mario took 11 damage.
{'name': 'Mario', 'health': 0, 'lives': 2}
Mario lost a life.
{'name': 'Mario', 'health': 0, 'lives': 1}
Mario took 15 damage.
{'name': 'Mario', 'health': 0, 'lives': 1}
Mario lost a life.
{'name': 'Mario', 'health': 0, 'lives': 0}
This character has died

    Take note that the health value never dips below 0 despite the
    level of damage the character takes. This needs to
    be programmed into your class.

    Also take note that if I continue calling methods on the
    object after it has died, that is ok. No need to write code to
    prevent this
"""

print("\nQ 2.")

# Create a new class


class GameCharacter:

    # Use the __init__ function to take in 3 object attributes
    # 'name' should be assigned a value by the user at creation
    # 'health' and 'lives' are fixed to 10 and 3

    def __init__(self, name):

        self.name = name
        self.health = 10
        self.lives = 3

# Create a method which simply prints out
# all of the objects attribute and their values.

    def describe_character(self):

        print(self.__dict__)

# Create a method which takes in a parameter which represents
# the number of damage the character has taken.

# (1) Print how much damage the character took.

# (2) Remove the damage amount from the health attribute.
#     If its value is negative, value to 0.

# (3) Call the describe_character() method
#     to display the character's current stats.

# (4) Call the loss_life() method only if the character's current health is 0.

    def take_damage(self, damage):

        print(f"{self.name} took {damage} damage")  # (1)
        self.health -= damage if self.health >= damage else self.health  # (2)
        self.describe_character()  # (3)
        self.lose_life() if self.health == 0 else ...  # (4)

# Create a method

# (1) Print out 'The character lost a life'.

# (2) Decrement the lives attribute by 1.

# (3) Call the describe_character() function to display the character's current stats.

# (4) print out 'The character has died!' if the number of lives has reduced to 0 or less.
#     If not, restore the character's health back to 10(full value).

    def lose_life(self):

        print(f"{self.name} lost a life")  # (1)
        self.lives -= 1  # (2)
        self.describe_character()  # (3)

        if self.lives <= 0:  # (4)
            print(f"{self.name} has died!")
        else:
            self.health = 10

# Create a method
# (1) Print out 'The character restored health to full'.

# (2) Set the health attribute to it's original max value of 10

# (3) Call the describe_character() function to display the character's current stats.

    def drink_potion(self):

        print(f"{self.name} restored health to full")
        self.health = 10
        self.describe_character()


# Test code

mario = GameCharacter('Mario')

mario.take_damage(4)
mario.take_damage(7)
mario.take_damage(5)
mario.drink_potion()
mario.take_damage(11)
mario.take_damage(15)
