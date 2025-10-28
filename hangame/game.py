import hangame.words
def init_state(secret :str  , max_tries :int) -> dict:
    display = []
    for i in range(len(words)):
        display.append(i)
    {
        "secret": words,
        "display":list[str] ,
        "guessed": set[str] ,
        "wrong_guesses": int ,
        "max_tries": int
    }




#def validate_guess(ch:str ,guessed:set[str]) -> tuple[bool , str]:
    if ch in word:
        print("sacsasful")


