from random import sample
from os import system
from time import sleep
import codecs
from cv2 import waitKey
from msvcrt import getch

with codecs.open('dane', 'r', 'utf-8') as file:
    siema = list(file)

questions = []
answers = []

for i, line in enumerate(siema):
    if i % 2 == 0:
        questions.append(line[0:len(line) - 1 - 1])
    else:
        answers.append(line[0:len(line) - 1 - 1])


def shuffled_range(n):
    return sample(range(n), n)

system('color')

for i in shuffled_range(len(questions)):
    system('cls')
    print('\033[37m' + '>', questions[i])
    print()

    presented_answers = shuffled_range(len(answers))
    presented_answers.remove(i)
    presented_answers = sample(presented_answers, len(presented_answers))[0:3]
    presented_answers.append(i)
    presented_answers = sample(presented_answers, len(presented_answers))

    keys = ['h', 'j', 'k', 'l']
    for j in range(len(presented_answers)):
        print('\033[37m' + keys[j], '\033[37m' + answers[presented_answers[j]])
        print()

    answer = getch()
    answer_dict = {b'h' : 0,
                   b'j' : 1,
                   b'k' : 2,
                   b'l' : 3 } 
    answer = answer_dict[answer]

    system('cls')
    print('\033[37m' + '>', questions[i])
    print()
    for j in range(len(presented_answers)):
        color_line = None
        if presented_answers[answer] == i:
            color_line = '\033[35m'
        else:
            color_line = '\033[31m'

        if answer != j:
            color_line = '\033[37m'
        
            if presented_answers[answer] != i and presented_answers[j] == i:
                color_line = '\033[35m'


        print('\033[37m' + keys[j], color_line + answers[presented_answers[j]])
        print()


    getch()

