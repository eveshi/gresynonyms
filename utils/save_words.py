import json
import os

path = os.path.dirname(os.path.realpath(__file__))

with open(path + '/../db/words.json') as words:
    words_dict = words_dict = json.load(words)
with open(path + '/../db/explainations.json') as explainations:
    explainations_dict = json.load(explainations)

def input_pairs():
    explainations_input = input("the explaination is: ")
    words_input = input("words(use comma and space between words): ")

    words_list = words_input.split(", ")

    for word in words_list:
        if (word in words_dict) and (explainations_input not in words_dict[word]):
            words_dict[word] = list(set([explainations_input] + words_dict[word]))
        elif (word in words_dict) and (explainations_input in words_dict[word]):
            print("duplicate inputs")
        else:
            words_dict[word] = [explainations_input]

    if explainations_input in explainations_dict:
        explainations_dict[explainations_input] = list(set(words_list + explainations_dict[explainations_input]))
    else:
        explainations_dict[explainations_input] = words_list

    with open(path + '/../db/words.json', 'w') as words:
        json.dump(words_dict, words, indent=2, ensure_ascii=False)
    with open(path + '/../db/explainations.json', 'w') as explainations:
        json.dump(explainations_dict, explainations, indent=2, ensure_ascii=False)

    print("save successfully")

    
