#a super simple attempt at an script to show random questions
import random

#for now questions are saved on a txt file, one question per line
inputFilePath = './file/questions.txt'

#read the file and load it to a list
file = open(inputFilePath)
filelines = file.readlines()
#using the length of the list to feed the RNG
qlen = len(filelines)

menu_options = ">> Press 1 then ENTER to get a question, or press ENTER to exit: "

option = input(f"\n===\nHi! I'm a simple question roulette script :)\n===\n\n\n{menu_options}")

while option:
    try:
        option = int(option)
        while option < 2:
            #check if the list is stil populated, if not end the script
            if qlen > 0:
                random_index = random.randint(0,qlen-1)
                #delete the question already rolled so it doesn't come out again
                question = filelines.pop(random_index)
                #reset the length used to feed the RNG
                qlen = len(filelines)
                print(f"\nHere's your question:\n===\n{question}===\n\n")
                option = input(menu_options)
                if not option:
                    break
                option = int(option)
            else:
                print("There are no more questions. Bye!")
                break
        break
    except Exception as e:
        print("Invalid value")
        option = input(menu_options)
