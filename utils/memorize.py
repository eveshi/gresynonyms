import json
import os
import random

path = os.path.dirname(os.path.realpath(__file__))

with open(path + '/../db/explainations.json') as explainations:
    explainations_dict = json.load(explainations)

def print_one_word(word_index):
    print(list(explainations_dict.keys())[word_index] + ": \n" + ",".join(list(explainations_dict.values())[word_index]))

def print_list(start_point):
    end_point = start_point + 10
    if end_point > len(explainations_dict):
        end_point = len(explainations_dict)

    while start_point < end_point:
        print_one_word(start_point)
        go_to_next = input("Type enter to continue. Type '-ex' to quit.")
        if go_to_next == '-ex':
            start_point = end_point
            return False
        else:
            start_point += 1

    if_continue = input('Continue to next list? y/N')
    return if_continue

def random_memorize():
    total_chinese_words = len(explainations_dict)
    random_word_index = random.randrange(total_chinese_words)
    print_one_word(random_word_index)

def list_memorize():
    memory = open(path + '/../db/memorize.txt', 'r+')
    if memory.read() == "":
        start_point = 0
    else:
        start_point = int(memory.read())
    
    if_continue = 'y'
    while if_continue == 'y':
        if_continue = print_list(start_point)
        if if_continue != False:
            start_point += 10
    
    memory.write(str(start_point))

def main():
    choice = input("pls choose the mode: \n-r: random word \n-l: memorize a list\n-ex: return to main menu\n")
    if choice == "-r":
        random_memorize()
    elif choice == "-l":
        list_memorize()
    else:
        choice = input("pls type a command")
    
