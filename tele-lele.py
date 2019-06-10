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
correct_answer = []
correct_answer_count = 0

for i, line in enumerate(siema):
    j = i % 6
    if j == 0:
        questions.append(line[0:len(line) - 1 - 1])
        answers.append([])
    elif j > 0 and j <= 4:
        answers[int(i / 6)].append(line[1:len(line) - 1 - 1])
    else:
        correct_answer.append(int(line[1:len(line) - 1]))        


def shuffled_range(n):
    return sample(range(n), n)

system('color')

for x, i in enumerate(shuffled_range(len(questions))):
    system('cls')
    print('\033[37m' + str(x + 1), '/', len(questions), '|', '>', '[', questions[i], ']')
    print()

    presented_answers = shuffled_range(len(answers[i]))
    presented_answers.remove(correct_answer[i])
    presented_answers = sample(presented_answers, len(presented_answers))
    presented_answers.append(correct_answer[i])
    presented_answers = sample(presented_answers, len(presented_answers))

    keys = ['h', 'j', 'k', 'l']
    for j in range(len(presented_answers)):
        print('\033[37m' + keys[j], '\033[37m' + answers[i][presented_answers[j]])
        print()

    answer = getch()
    answer_dict = {b'h' : 0,
                   b'j' : 1,
                   b'k' : 2,
                   b'l' : 3 } 
    answer = answer_dict[answer]

    if presented_answers[answer] == correct_answer[i]:
        correct_answer_count = correct_answer_count + 1

    system('cls')
    print('\033[37m' + str(x + 1), '/', len(questions), '|', '>', '[', questions[i], ']')
    print()
    for j in range(len(presented_answers)):
        color_line = None
        if presented_answers[answer] == correct_answer[i]:
            color_line = '\033[32m'
        else:
            color_line = '\033[31m'

        if answer != j:
            color_line = '\033[37m'
        
            if presented_answers[answer] != correct_answer[i] and \
            presented_answers[j] == correct_answer[i]:
                color_line = '\033[32m'


        print('\033[37m' + keys[j], color_line + answers[i][presented_answers[j]])
        print()


    getch()

system('cls')
print('\033[37m' + 'Poprawność:', correct_answer_count / len(questions) * 100, '%')
getch()


