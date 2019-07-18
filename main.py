# 4 modes
# - search for synonyms
# - do comments 
# - easy game: synonym quiz
# - quick memorize: random words memorize

# scripts
# -s
# -q
# -rw [username]
# -i
# --help


from utils import save_words, search, memorize

def main():
    mode = input('Welcome to Gresynonyms, pls type your commands:\n-s: search for words or explainations\n-i: input new words pair\n')
    if mode == '-s':
        search.search()
    elif mode == '-q':
        memorize.main()
#     elif '--rw' in mode:
    elif mode == '-i':
        input_continue = "y"
        while input_continue != "N":
            save_words.input_pairs()
            input_continue = input("continue input? y/N: ")
    elif mode == '--help':
        print('-s search /n -q quiz /n --rw random word /n -w write new pairs')
    else:
        print('invalid inpt, pls ')

main()