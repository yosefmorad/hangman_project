from random import randrange

def choose_secret_word (words:list[str])-> str:
    word = words[ randrange (0 ,len(words)-1)]

    return word