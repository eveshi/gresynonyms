import re
import json
import os

path = os.path.dirname(os.path.realpath(__file__))

with open(path + '/../db/words.json') as words:
    words_dict = words_dict = json.load(words)
with open(path + '/../db/explainations.json') as explainations:
    explainations_dict = json.load(explainations)

def search():
    query_word = input('Search: ')
    if re.search('^[a-zA-Z0-9$@$!%*?&#^-_. +]+$', query_word) is not None:
        #search in eng
        search_location = words_dict
    elif re.search('', query_word):
        #search in chi
        search_location = explainations_dict

    if query_word in words_dict:
        print(query_word + ': ' + ','.join(search_location[query_word]))
    else:
        print('no results')
    

