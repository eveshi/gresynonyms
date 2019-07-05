# 4 modes
# - search for synonyms
# - do comments
# - easy game: synonym quiz
# - quick memorize: random words memorize

from utils import save_words

def main():
    input_continue = "y"
    while input_continue != "N":
        save_words.input_pairs()
        input_continue = input("continue input? y/N: ")

main()